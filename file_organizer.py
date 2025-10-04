# file_organizer.py

import os
import shutil
import sys
from collections import defaultdict

# --- Configuration ---
# A dictionary mapping file extensions (lowercase) to their target folder names.
FILE_TYPE_MAP = {
    # Documents
    'pdf': 'PDFs',
    'docx': 'Documents',
    'doc': 'Documents',
    'txt': 'Documents',
    'rtf': 'Documents',
    'odt': 'Documents',
    
    # Images
    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'gif': 'Images',
    'bmp': 'Images',
    'tiff': 'Images',

    # Compressed/Archives
    'zip': 'Archives',
    'rar': 'Archives',
    '7z': 'Archives',

    # Executables/Scripts
    'exe': 'Programs',
    'py': 'Scripts',
    'sh': 'Scripts',
    
    # Audio/Video
    'mp3': 'Media',
    'wav': 'Media',
    'mp4': 'Media',
    'mov': 'Media',
    'avi': 'Media',
}

# The default folder for files not matching any extension in FILE_TYPE_MAP
OTHER_FOLDER = 'Others'

def get_destination_folder(file_extension):
    """
    Determines the correct destination folder name based on the file extension.
    If the extension is not in the map, returns the 'Others' folder name.
    """
    # Remove leading dot and convert to lowercase for consistent lookup
    extension = file_extension.lstrip('.').lower()
    return FILE_TYPE_MAP.get(extension, OTHER_FOLDER)

def rename_if_exists(destination_path):
    """
    Handles file name conflicts by appending '_copy' before the extension.
    If 'file.txt' exists, it returns 'file_copy.txt'.
    If 'file_copy.txt' exists, it returns 'file_copy_copy.txt', and so on.
    """
    if not os.path.exists(destination_path):
        return destination_path
    
    base, ext = os.path.splitext(destination_path)
    counter = 1
    new_path = f"{base}_copy{ext}"

    # Simple approach to append '_copy' until a unique name is found
    while os.path.exists(new_path):
        new_path = f"{base}_{'copy' * (counter + 1)}{ext}"
        counter += 1
        # This while loop ensures no collisions, though in a production env, 
        # a more robust naming scheme (like appending a timestamp) might be used.
        base = new_path.rsplit(ext, 1)[0] # Reset base for the next iteration
        new_path = f"{base}_copy{ext}"

    return new_path

def organize_files(target_directory):
    """
    Main function to iterate over files in the directory and move them.
    
    :param target_directory: The path to the folder to organize.
    """
    print(f"--- Starting file organization in: {target_directory} ---\n")
    
    # Ensure the target directory exists
    if not os.path.isdir(target_directory):
        print(f"Error: Directory not found: {target_directory}")
        return

    # Count of files moved for summary
    files_moved = 0
    
    # Use os.scandir for better performance iterating directories
    with os.scandir(target_directory) as entries:
        for entry in entries:
            # Skip directories, symbolic links, and the script itself
            if entry.is_file() and entry.name != os.path.basename(__file__):
                
                source_path = entry.path
                
                # Get the file extension
                _, extension = os.path.splitext(entry.name)
                
                # Determine the destination folder
                folder_name = get_destination_folder(extension)
                destination_folder_path = os.path.join(target_directory, folder_name)
                
                # 1. Create the destination folder if it doesn't exist
                try:
                    os.makedirs(destination_folder_path, exist_ok=True)
                except OSError as e:
                    print(f"Error creating directory {folder_name}: {e}")
                    continue # Skip this file if folder creation fails

                # Define the final path for the file
                destination_file_path = os.path.join(destination_folder_path, entry.name)
                
                # 2. Handle file existence conflict (rename if destination exists)
                final_destination_path = rename_if_exists(destination_file_path)

                # 3. Move the file
                try:
                    shutil.move(source_path, final_destination_path)
                    
                    # 4. Log the move operation
                    relative_source = os.path.basename(source_path)
                    relative_dest = os.path.join(folder_name, os.path.basename(final_destination_path))
                    print(f"Moved: {relative_source} -> {relative_dest}")
                    
                    files_moved += 1
                    
                except Exception as e:
                    print(f"Error moving {entry.name}: {e}")

    print(f"\n--- Organization Complete: {files_moved} files moved. ---")


if __name__ == "__main__":
    # The script expects the directory path as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python file_organizer.py <path_to_folder>")
        print("Example: python file_organizer.py ./MyDownloads")
        sys.exit(1)
    
    # Get the directory from the command-line arguments and normalize the path
    target_dir = os.path.abspath(sys.argv[1])
    organize_files(target_dir)
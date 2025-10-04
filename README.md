# 📂 File Organizer Python Script

A simple, yet powerful Python script to automatically organize files within a specified directory into subfolders based on their file type (e.g., Images, PDFs, Documents).

This project demonstrates practical file system manipulation using the built-in `os` and `shutil` libraries, incorporating best practices like error handling and conflict resolution.

## ✨ Features

- **Type-Based Sorting:** Moves files into predefined category folders (`PDFs`, `Images`, `Documents`, `Archives`, etc.).
- **Automatic Folder Creation:** Creates destination folders on the fly if they don't already exist.
- **Conflict Resolution:** Safely handles file name collisions by automatically renaming files (e.g., `report.pdf` becomes `report_copy.pdf`).
- **Detailed Logging:** Prints a log message for every file moved, providing a clear overview of the script's actions.
- **Extensible Configuration:** Easily customizable file-type-to-folder mapping in the `FILE_TYPE_MAP` dictionary.

## 🚀 How to Run the Script

### Prerequisites

You need **Python 3.x** installed on your system. No external libraries are required beyond Python's standard distribution (`os`, `shutil`, `sys`).

### Execution

1.  **Save the Script:** Save the code above as a file named `file_organizer.py`.
2.  **Open Terminal/Command Prompt:** Navigate to the location where you saved the script.
3.  **Run with Target Directory:** Execute the script by passing the path to the folder you wish to organize as a command-line argument.

    ```bash
    # Example: Organizing a 'Downloads' folder located in your current directory
    python file_organizer.py ./Downloads
    
    # Example: Organizing a folder using an absolute path
    python file_organizer.py /Users/username/Desktop/UnsortedFiles
    ```

### Example Output

--- Starting file organization in: /path/to/Downloads ---

Moved: vacation_photo.jpg -> Images/vacation_photo.jpg
Moved: research_paper.pdf -> PDFs/research_paper.pdf
Moved: notes.txt -> Documents/notes.txt
Moved: existing_file.png -> Images/existing_file_copy.png

--- Organization Complete: 4 files moved. ---

.
├── file_organizer.py  # The core Python script
└── README.md          # This file

## 👨‍💻 Author

[Rohan Kumar / mrrohan0306-web]

Feel free to connect or contribute!
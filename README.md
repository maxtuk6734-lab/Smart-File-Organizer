# Smart File Organizer 📂

An automated Python utility designed to instantly organize messy directories by categorizing files into specific folders based on their extensions.

## Features
- **Smart Sorting:** Automatically sorts Images, Documents, Code, Media, and Archives.
- **Dynamic Structure:** Creates necessary folder structures on the fly if they don't exist.
- **Safe Handling:** Unrecognized file formats are safely moved to an 'Other' directory.
- **Time-Saving:** Automates routine administrative tasks to keep the local environment clean.

## Tech Stack
- Python 3.x
- `os`, `shutil` (Core system libraries)

## How to Use
1. Drop the `sorter.py` script into the directory you want to organize (or specify the `target_dir` in the code).
2. Run the script via terminal: 
   ```bash
   python sorter.py

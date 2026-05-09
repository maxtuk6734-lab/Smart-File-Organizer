import os
import shutil

def organize_folder(folder_path):
    # Dictionary mapping category names to file extensions
    extensions_map = {
        "Images": ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        "Documents": ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.csv'],
        "Code": ['.py', '.c', '.cpp', '.html', '.css', '.js', '.json'],
        "Media": ['.mp4', '.mp3', '.wav', '.avi'],
        "Archives": ['.zip', '.rar', '.7z', '.tar']
    }

    print(f"[*] Starting to organize the folder: {folder_path}...")

    # Check if the specified directory exists
    if not os.path.exists(folder_path):
        print("[!] Error: The specified folder does not exist. Please check the path.")
        return

    # Iterate over all items in the directory
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories, we only want to sort files
        if os.path.isdir(file_path):
            continue

        # Extract the file extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        moved = False
        # Check which category the file belongs to
        for folder_name, exts in extensions_map.items():
            if extension in exts:
                category_path = os.path.join(folder_path, folder_name)
                
                # Create the category folder if it doesn't exist
                if not os.path.exists(category_path):
                    os.makedirs(category_path)

                # Move the file to its corresponding category folder
                new_path = os.path.join(category_path, filename)
                shutil.move(file_path, new_path)
                print(f"[+] Moved: {filename} -> {folder_name}/")
                moved = True
                break
        
        # If the file extension is unknown, move it to the 'Other' folder
        if not moved and extension:
            other_path = os.path.join(folder_path, "Other")
            if not os.path.exists(other_path):
                os.makedirs(other_path)
            shutil.move(file_path, os.path.join(other_path, filename))
            print(f"[~] Unknown format: {filename} -> Other/")

    print("[*] Folder organization successfully completed!")

# SPECIFY THE TARGET FOLDER HERE
# Creating a test directory next to the script for safety
target_dir = "test_folder" 

# Setup for first-time run
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    print(f"[*] Created an empty folder '{target_dir}'. Drop some files there and run the script again!")
else:
    organize_folder(target_dir)
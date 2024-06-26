import os
import shutil
from CheckFiles import *
from tkinter import messagebox, filedialog
from FoldersList import *


def main():
    messagebox.showinfo(
        "Directory selection",
        "A window dialog will open, please choose the folder you want to organize"
    )
    input_path = filedialog.askdirectory()
    if not input_path:
        messagebox.showerror("Error",
                             "You didn't select a directory.")
        return

    source_dir = input_path
    predefined_folders = [os.path.basename(folder) for folder in [
        downloaded_images_folder,
        downloaded_compressed_files_folder,
        downloaded_music_folder,
        downloaded_videos_folder,
        downloaded_documents_folder,
        downloaded_design_files_folder,
        downloaded_programming_files_folder,
        downloaded_font_files_folder,
        downloaded_executable_files_folder
    ]]

    try:
        with os.scandir(source_dir.strip()) as entries:
            for entry in entries:
                if os.path.isfile(entry):
                    try:
                        check_for_image_files(entry, source_dir)
                        check_for_compressed_files(entry, source_dir)
                        check_for_music_files(entry, source_dir)
                        check_for_video_files(entry, source_dir)
                        check_for_document_files(entry, source_dir)
                        check_for_design_files(entry, source_dir)
                        check_for_programming_files(entry, source_dir)
                        check_for_font_files(entry, source_dir)
                        check_for_executable_files(entry, source_dir)
                    except (PermissionError, OSError) as e:
                        messagebox.showerror(
                            "Error", f"There was an error moving the file: {entry.name}\n{str(e)}")
                elif os.path.isdir(entry):
                    if entry.name not in predefined_folders:
                        other_folder = os.path.join(
                            source_dir, "Other Folders")
                        if not os.path.exists(other_folder):
                            os.makedirs(other_folder)

                        if entry.path != other_folder:
                            new_name = entry.name
                            counter = 1
                            while os.path.exists(os.path.join(other_folder, new_name)):
                                new_name = f"{entry.name} ({counter})"
                                counter += 1

                            new_path = os.path.join(other_folder, new_name)
                            try:
                                shutil.move(entry.path, new_path)
                            except (PermissionError, OSError) as e:
                                messagebox.showerror(
                                    "Error", f"There was an error moving the folder: {entry.name}\n{str(e)}")
    except PermissionError:
        messagebox.showerror(
            "Error", "You don't have permission to access the selected directory.")
    except Exception as e:
        messagebox.showerror(
            "Error", f"An unexpected error occurred: {str(e)}")
    else:
        messagebox.showinfo("Process completed",
                            "Files and folders moved correctly!")


if __name__ == "__main__":
    main()

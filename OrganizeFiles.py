import os
import FoldersList
from CheckFiles import check_for_compressed_files, check_for_design_files, check_for_document_files, check_for_executable_files, check_for_font_files, check_for_image_files, check_for_music_files, check_for_programming_files, check_for_video_files
from tkinter import messagebox


def main():
    input_path = input("Enter the path of the directory you wanna organize: ")
    FoldersList.source_dir = input_path
    with os.scandir(FoldersList.source_dir) as entries:
        for entry in entries:
            if os.path.isfile(entry):
                check_for_image_files(entry)
                check_for_compressed_files(entry)
                check_for_music_files(entry)
                check_for_video_files(entry)
                check_for_document_files(entry)
                check_for_design_files(entry)
                check_for_programming_files(entry)
                check_for_font_files(entry)
                check_for_executable_files(entry)
    # Add tkinter message
    messagebox.showinfo("Process completed", "Files moved correctly")


if __name__ == "__main__":
    main()
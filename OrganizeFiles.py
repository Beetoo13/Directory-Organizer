import os
from CheckFiles import *
from tkinter import messagebox, filedialog


def main():
    messagebox.showinfo(
        "Directory selection",
        "A window dialog will open, please choose the folder you want to organize"
    )
    input_path = filedialog.askdirectory()
    if not input_path:
        messagebox.showerror("Error",
                             "No se ha seleccionado ningún directorio.")
        return

    source_dir = input_path
    with os.scandir(source_dir.strip()) as entries:
        for entry in entries:
            if os.path.isfile(entry):
                check_for_image_files(entry, source_dir)
                check_for_compressed_files(entry, source_dir)
                check_for_music_files(entry, source_dir)
                check_for_video_files(entry, source_dir)
                check_for_document_files(entry, source_dir)
                check_for_design_files(entry, source_dir)
                check_for_programming_files(entry, source_dir)
                check_for_font_files(entry, source_dir)
                check_for_executable_files(entry, source_dir)

    # # Add tkinter message
    messagebox.showinfo("Process completed", "Files moved correctly!")


if __name__ == "__main__":
    main()
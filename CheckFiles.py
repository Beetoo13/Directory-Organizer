from genericpath import isfile
import os
import shutil
from FoldersList import source_dir, downloaded_compressed_files_folder, downloaded_design_files_folder, downloaded_documents_folder, downloaded_executable_files_folder, downloaded_font_files_folder, downloaded_images_folder, downloaded_music_folder, downloaded_programming_files_folder, downloaded_videos_folder
from FilesTypes import compressed_types, design_types, documents_types, executable_types, font_types, image_types, music_types, programming_types, video_types


def move_files(entry, move_path):
    if os.path.exists(move_path):
        shutil.move(source_dir + "\\" + entry.name,
                    move_path + "\\" + entry.name)
    else:
        os.makedirs(move_path)
        shutil.move(source_dir + "\\" + entry.name,
                    move_path + "\\" + entry.name)


def check_for_image_files(entry):
    for image_type in image_types:
        if entry.name.lower().endswith(image_type):
            move_files(entry, downloaded_images_folder)


def check_for_compressed_files(entry):
    for compressed_type in compressed_types:
        if entry.name.lower().endswith(compressed_type):
            move_files(entry, downloaded_compressed_files_folder)


def check_for_video_files(entry):
    for video_type in video_types:
        if entry.name.lower().endswith(video_type):
            move_files(entry, downloaded_videos_folder)


def check_for_music_files(entry):
    for music_type in music_types:
        if entry.name.lower().endswith(music_type):
            move_files(entry, downloaded_music_folder)


def check_for_document_files(entry):
    for document_type in documents_types:
        if entry.name.lower().endswith(document_type):
            move_files(entry, downloaded_documents_folder)


def check_for_design_files(entry):
    for design_type in design_types:
        if entry.name.lower().endswith(design_type):
            move_files(entry, downloaded_design_files_folder)


def check_for_programming_files(entry):
    for programming_type in programming_types:
        if entry.name.lower().endswith(programming_type):
            move_files(entry, downloaded_programming_files_folder)


def check_for_font_files(entry):
    for font_type in font_types:
        if entry.name.lower().endswith(font_type):
            move_files(entry, downloaded_font_files_folder)


def check_for_executable_files(entry):
    for executable_type in executable_types:
        if entry.name.lower().endswith(executable_type):
            move_files(entry, downloaded_executable_files_folder)

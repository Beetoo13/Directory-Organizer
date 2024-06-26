from genericpath import isfile
import os
import shutil
from FoldersList import *
from FilesTypes import *


def move_files(entry, source_dir, move_path):
    destination_folder = os.path.join(source_dir, move_path)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    base_name, extension = os.path.splitext(entry.name)

    new_name = entry.name
    counter = 1
    while os.path.exists(os.path.join(destination_folder, new_name)):
        new_name = f"{base_name} ({counter}){extension}"
        counter += 1

    new_path = os.path.join(destination_folder, new_name)
    os.rename(os.path.join(source_dir, entry.name), new_path)


def check_for_image_files(entry, source_dir):
    for image_type in image_types:
        if entry.name.lower().endswith(image_type):
            move_files(entry, source_dir, downloaded_images_folder)


def check_for_compressed_files(entry, source_dir):
    for compressed_type in compressed_types:
        if entry.name.lower().endswith(compressed_type):
            move_files(entry, source_dir, downloaded_compressed_files_folder)


def check_for_video_files(entry, source_dir):
    for video_type in video_types:
        if entry.name.lower().endswith(video_type):
            move_files(entry, source_dir, downloaded_videos_folder)


def check_for_music_files(entry, source_dir):
    for music_type in music_types:
        if entry.name.lower().endswith(music_type):
            move_files(entry, source_dir, downloaded_music_folder)


def check_for_document_files(entry, source_dir):
    for document_type in documents_types:
        if entry.name.lower().endswith(document_type):
            move_files(entry, source_dir, downloaded_documents_folder)


def check_for_design_files(entry, source_dir):
    for design_type in design_types:
        if entry.name.lower().endswith(design_type):
            move_files(entry, source_dir, downloaded_design_files_folder)


def check_for_programming_files(entry, source_dir):
    for programming_type in programming_types:
        if entry.name.lower().endswith(programming_type):
            move_files(entry, source_dir, downloaded_programming_files_folder)


def check_for_font_files(entry, source_dir):
    for font_type in font_types:
        if entry.name.lower().endswith(font_type):
            move_files(entry, source_dir, downloaded_font_files_folder)


def check_for_executable_files(entry, source_dir):
    for executable_type in executable_types:
        if entry.name.lower().endswith(executable_type):
            move_files(entry, source_dir, downloaded_executable_files_folder)

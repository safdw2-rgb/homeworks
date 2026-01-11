import shutil
import os
import re

images_type = ("jpeg", "png", "jpg","svg")
documents_type = ("doc", "docx", "txt","pdf", "xlsx", "pptx")
audio_type = ("mp3", "ogg", "wav", "amr")
video_type = ("avi", "mp4", "mov", "mkv")
archives_type = ("zip", "gz", "tar")

def normalize(path):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    CYRILLIC_SYMBOLS = list(CYRILLIC_SYMBOLS)
    TRANS = {}
        
    for cymbol, translation in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(cymbol)] = translation
        TRANS[ord(cymbol.upper())] = translation.upper()

    translated_name = ""
    
    for letter in path:
        translated_name += letter.translate(TRANS)
        
    translated_name = re.sub(r"[^A-Za-z0-9.]", "_", translated_name)

    return translated_name



def create_folders(source_path):
    folders_files_type = ["images", "documents", "audio", "video", "archives", "other"]
    for folder in folders_files_type:
        os.makedirs(f"{source_path}/results/{folder}", exist_ok=True)



def sort_files(folder_path:str, base_path):

    IMAGES_FOLDER = f"{base_path}/results/images/"
    DOCUMENTS_FOLDER = f"{base_path}/results/documents/"
    AUDIO_FOLDER = f"{base_path}/results/audio/"
    VIDEO_FOLDER = f"{base_path}/results/video/"
    ARCHIVES_FOLDER = f"{base_path}/results/archives/"
    OTHER_FOLDER = f"{base_path}/results/other/"

    for file in os.listdir(folder_path):
        source_path = os.path.join(folder_path, file)
        file = normalize(file)

        if file.endswith(images_type):
            destination_path = os.path.join(IMAGES_FOLDER, file)
            shutil.move(source_path, destination_path)
        elif file.endswith(documents_type):
            destination_path = os.path.join(DOCUMENTS_FOLDER, file)
            shutil.move(source_path, destination_path)
        elif file.endswith(audio_type):
            destination_path = os.path.join(AUDIO_FOLDER, file)
            shutil.move(source_path, destination_path)
        elif file.endswith(video_type):
            destination_path = os.path.join(VIDEO_FOLDER, file)
            shutil.move(source_path, destination_path)
        elif file.endswith(archives_type):
            destination_path = os.path.join(ARCHIVES_FOLDER, file)            
            shutil.unpack_archive(source_path, destination_path.removesuffix(".zip").removesuffix(".gz").removesuffix(".tar"))
            os.remove(source_path)
            
        elif os.path.isfile(source_path):
            shutil.move(source_path, OTHER_FOLDER)

        elif os.path.isdir(source_path) and "results" not in source_path:
            sort_files(source_path, base_path)
            os.rmdir(source_path)



def unpack_folder(destination_path):
    folder_path = f"{destination_path}/results"
    for file in os.listdir(folder_path):
        source_item = os.path.join(folder_path, file)
        destination_item = os.path.join(destination_path, file)
        shutil.move(source_item, destination_item)

    os.rmdir(folder_path)    



def main(start_folder_path):
    create_folders(start_folder_path)
    sort_files(start_folder_path, start_folder_path)
    unpack_folder(start_folder_path)


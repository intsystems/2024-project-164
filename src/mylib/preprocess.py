import os
import glob

from PIL import Image
import numpy as np



def preprocess(dataset_path: str):
    base_path = dataset_path

    NUM_CHARS_FROM_ALPHABET_TO_TAKE = 14
    NUM_ALPHABETS = len(next(os.walk(base_path))[1])

    language_to_char_count_dict = {}

    images = [[] for _ in range(NUM_ALPHABETS)]
    grouped_images = [[[] for _ in range(NUM_CHARS_FROM_ALPHABET_TO_TAKE)] for _ in range(NUM_ALPHABETS)]

    alphabet_to_ext_index = {}
    ext_index_to_alphabet = {}

    character_to_ext_index = {}
    ext_index_to_character = {}

    for i, folder_path in enumerate(glob.glob(os.path.join(base_path, "*"))):
        language = folder_path.split('/')[-1]
        alphabet_to_ext_index[language] = i
        ext_index_to_alphabet[i] = language


        for j, folder_path_ in enumerate(glob.glob(os.path.join(folder_path, "*"))):
            if language_to_char_count_dict.get(language, 0) >= NUM_CHARS_FROM_ALPHABET_TO_TAKE:
                continue

            language_to_char_count_dict[language] = language_to_char_count_dict.get(language, 0) + 1

            character = folder_path_.split('/')[-1]
            character_to_ext_index[language] = character_to_ext_index.get(language, {})
            character_to_ext_index[language][character] = j
            ext_index_to_character[alphabet_to_ext_index[language]] = ext_index_to_character.get(alphabet_to_ext_index[language], {})
            ext_index_to_character[alphabet_to_ext_index[language]][j] = character


    language_to_char_count_dict = {}

    for folder_path in glob.glob(os.path.join(base_path, "*/*")):
        language = folder_path.split('/')[-2]
        character = folder_path.split('/')[-1]

        if language_to_char_count_dict.get(language, 0) >= NUM_CHARS_FROM_ALPHABET_TO_TAKE:
            continue

        language_to_char_count_dict[language] = language_to_char_count_dict.get(language, 0) + 1

        for full_file_path in glob.glob(os.path.join(folder_path, "*")):
            img = np.asarray(Image.open(full_file_path))
            images[alphabet_to_ext_index[language]].append(img)
            grouped_images[alphabet_to_ext_index[language]][character_to_ext_index[language][character]].append(img)

    return images
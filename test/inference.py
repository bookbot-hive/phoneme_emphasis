import os
import time
from text_processor import TextProcessor
from pkg_resources import resource_filename


def main():    
    model_dirs = {
        "en": "bookbot/roberta-base-emphasis-onnx-quantized",
        "sw": "",
        "id": ""
    }
    db_paths = {
        "en": resource_filename('text_processor', 'data/en_word_emphasis_lookup_mix_homographs.json'),
        "sw": "",
        "id": ""
    }
    
    cosmos_config = {
        "url": os.getenv("COSMOS_DB_URL"),
        "key": os.getenv("COSMOS_DB_KEY"),
        "database_name": "Bookbot"
    }

    # English
    model = TextProcessor(model_dirs["en"], db_paths["en"], language="en", use_cosmos=False, cosmos_config=cosmos_config, animation_tags_path="data.csv")
    
    # English Word input
    result = model.get_input_ids("<sound_scrolling_2> Hello [world]", phonemes=False, return_phonemes=True, push_oov_to_cosmos=True,  add_blank_token=True)
    print(f"Result: {result}")
    
    result = model.get_input_ids("Can you [lead] the <sound_part_showing_sound_1> conversation <smile>?", phonemes=False, return_phonemes=True, push_oov_to_cosmos=True, add_blank_token=True)
    print(f"Result: {result}")
    
    result = model.get_input_ids("I am 10 years old", phonemes=False, return_phonemes=True, push_oov_to_cosmos=True, add_blank_token=True)
    print(f"Result: {result}")
    
    # English Phoneme input
    phoneme = "hɛlˈoʊ mˈaɪ nˈeɪm ˈɪz"
    result = model.get_input_ids(phoneme, phonemes=True, return_phonemes=True, push_oov_to_cosmos=False, add_blank_token=True)
    print(f"Result: {result}")
    
    # Swahili Word input
    model = TextProcessor(model_dirs["sw"], db_paths["sw"], language="sw", use_cosmos=False, cosmos_config=cosmos_config, animation_tags_path="data.csv")
    result = model.get_input_ids("Jana <handRaiseHigh> nilitembelea mji wa [Nairobi]. 4525 Niliona majengo [marefu] na magari mengi <sound_part_showing_sound_1>.", phonemes=False, return_phonemes=True, push_oov_to_cosmos=False, add_blank_token=True)
    print(f"Result: {result}")
    
    # Indonesian Word input
    model = TextProcessor(model_dirs["id"], db_paths["id"], language="id", use_cosmos=False, cosmos_config=cosmos_config, animation_tags_path="data.csv")
    result = model.get_input_ids("<sound_scrolling_2> Halo <handRaiseHigh> nama saya Budi siapa [nama] kamu <sound_robotic_arm_2>?", phonemes=False, return_phonemes=True, push_oov_to_cosmos=False, add_blank_token=True)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
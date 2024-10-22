import os
from text_processor import TextProcessor

def main():    
    model_dirs = {
        "en": "bookbot/roberta-base-emphasis-onnx-quantized",
        "sw": "",
        "id": ""
    }
    db_paths = {
        "en": "/home/s44504/3b01c699-3670-469b-801f-13880b9cac56/Emphasizer/data/words_emphasis_lookup_mixed.json",
        "sw": "",
        "id": ""
    }
    
    cosmos_config = {
        "url": os.getenv("COSMOS_DB_URL"),
        "key": os.getenv("COSMOS_DB_KEY"),
        "database_name": "Bookbot"
    }

    # English
    model = TextProcessor(model_dirs["en"], db_paths["en"], language="en", use_cosmos=False, cosmos_config=cosmos_config)
    
    # English Word input
    result = model.get_input_ids("Hello! my name is \"ladida\"....!", phonemes=False, return_phonemes=True, add_blank_token=True)
    print(result)
    
    result = model.get_input_ids("Sure, I'd be happy to help you with your \"homework.\"", phonemes=False, return_phonemes=True, add_blank_token=True)
    print(result)
    
    result = model.get_input_ids("The capital of France is \"Paris.\"", phonemes=False, return_phonemes=True, add_blank_token=True)
    print(result)

    # English Phoneme input
    phoneme = "hɛlˈoʊ mˈaɪ nˈeɪm ˈɪz"
    result = model.get_input_ids(phoneme, phonemes=True, return_phonemes=True, add_blank_token=True)
    print(result)
    
    # Swahili Word input
    model = TextProcessor(model_dirs["sw"], db_paths["sw"], language="sw", use_cosmos=False, cosmos_config=cosmos_config)
    result = model.get_input_ids("Jana nilitembelea mji wa \"Nairobi\". Niliona majengo \"marefu\" na magari mengi.", phonemes=False, return_phonemes=True, add_blank_token=True)
    print(result)
    
    # Indonesian Word input
    model = TextProcessor(model_dirs["id"], db_paths["id"], language="id", use_cosmos=False, cosmos_config=cosmos_config)
    result = model.get_input_ids("Halo nama saya Budi. Siapa \"nama\" kamu?", phonemes=False, return_phonemes=True, add_blank_token=True)
    print(result)

if __name__ == "__main__":
    main()
from pathlib import Path
import ctranslate2
import sentencepiece as spm

def load_models(cur_dir):
    model_warehouse = cur_dir/ "models" 
    models = dict()

    for model_dir in model_warehouse.iterdir():
        model_name = model_dir.name
        tgt_vocab_model = model_dir / "tgt.model"
        src_vocab_model = model_dir / "src.model"

        src_tokenizer = spm.SentencePieceProcessor()
        src_tokenizer.load(str(src_vocab_model))
        
        tgt_tokenizer = spm.SentencePieceProcessor()
        tgt_tokenizer.load(str(tgt_vocab_model))

        translator = ctranslate2.Translator(str(model_dir)) 

        model_dict = {"src_tokenizer" : src_tokenizer, "tgt_tokenizer" : tgt_tokenizer, "translator" : translator }

        models[model_name] = model_dict 

    return models
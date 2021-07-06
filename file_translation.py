import argparse
from tools.model_utils import load_models
from pathlib import Path
from functools import partial

import logging

logging.basicConfig(level=logging.INFO, filename="test.log", 
format= "%(asctime)s:%(levelname)s - %(message)s")


cur_dir = Path.cwd()
models = load_models(cur_dir)

def translate_file(args):
    
    src = args.src_lang
    tgt = args.tgt_lang
    tgt_file = args.tgt_file
    src_file = args.src_file
    max_batch_size = args.max_batch_size

    model_name = f"{src}-{tgt}"
    model_dict = models[model_name]

    src_tokenizer = model_dict["src_tokenizer"]
    tgt_tokenizer = model_dict["tgt_tokenizer"]
    translator = model_dict["translator"]

    stats = translator.translate_file(
        source_path = src_file,
        output_path = tgt_file,
        max_batch_size = max_batch_size,
        batch_type = "tokens",
        source_tokenize_fn = partial(src_tokenizer.encode,out_type = "str" ),
        target_tokenize_fn = partial(tgt_tokenizer.encode,out_type = "str" ),
        target_detokenize_fn = tgt_tokenizer.decode
        )

    num_tokens, num_examples, num_seconds = stats[0], stats[1], stats[2]/1000
     
    logging.info(f"Total number of generated target tokens - {num_tokens}")
    logging.info(f"Total number of translated examples - {num_examples}")
    logging.info(f"Time taken in seconds - {round(num_seconds , 2)}")
    logging.info(f"Time taken per example - {round(num_seconds/num_examples, 3)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("src_file", help = "Path to the file containg source sentences")
    parser.add_argument("tgt_file", help = "Path to the file where translated sentences are written")
    #parser.add_argument("src_lang", help = "Source language")
    parser.add_argument("src_lang", help = "Source language", type=str, choices=["te", "hi"])
    parser.add_argument("tgt_lang", help = "Target language")
    parser.add_argument("--max_batch_size", help = "Maximum number of tokens in a batch" , default=4096, type=int )
    args = parser.parse_args()

    translate_file(args)

    
    ## stats is an object with the following properties:
# * num_tokens: the number of generated target tokens
# * num_examples: the number of translated examples
# * total_time_in_ms: the total translation time in milliseconds


# python file_translation.py telugu_sample.txt tmp.txt te en


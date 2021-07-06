def translate_batch(inputs, model_dict):
    src_sent = inputs['data']

    n_best =  1 if "n_best" not in inputs else inputs["n_best"]
    beam_size = n_best if n_best > 1 else 2

    src_tokenizer = model_dict["src_tokenizer"]
    tgt_tokenizer = model_dict["tgt_tokenizer"]
    translator = model_dict["translator"]

    src_tokens = src_tokenizer.encode(src_sent, out_type = "str")
    tgt_tokens_pred = translator.translate_batch(src_tokens,beam_size = beam_size, num_hypotheses = n_best)
    tgt_sents = detokenize_sents(tgt_tokens_pred,tgt_tokenizer)
    return tgt_sents


def detokenize_sents(tokens, tokenizer):
    detokenized_sents = [[tokenizer.decode(choice["tokens"]) for choice in example] for example in tokens] 
    return detokenized_sents
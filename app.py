from os import error
from pathlib import Path

from flask import Flask,request, jsonify
from tools.model_utils import load_models
from tools.translation_utils import translate_batch

import time

cur_dir = Path.cwd()
app = Flask(__name__)

STATUS_OK = "ok"
STATUS_ERROR = "error"

models = load_models(cur_dir)

@app.route("/")
def index():
    return "Hello World!!"

@app.route("/translate", methods = ["POST"])
def translate():
    start = time.time()

    # Parsing the input
    try:   
        inputs = request.get_json()
    except Exception as e:
        out = {'status': STATUS_ERROR,'error': str(e)}
        return out,400

    # Loading the correct model
    try:
        #Dont use pop, just get them form dict
        src = inputs.pop("src")
        tgt = inputs.pop("tgt")
        model_name = f"{src}-{tgt}"
        model_dict = models[model_name]

    except Exception as e:
        out = {'status': STATUS_ERROR,'error': str(e)}
        return out,422
        #Send error not serving this pair of languages

    #Translating the sentences    
    try:   
        tgt_sents = translate_batch(inputs, model_dict)
        end = time.time()
        out = {"result": tgt_sents, "time_taken": round(end - start, 3), "status": STATUS_OK}
        return jsonify(out)

    except Exception as e:
        out = {'status': STATUS_ERROR,'error': str(e)}
        return out,400
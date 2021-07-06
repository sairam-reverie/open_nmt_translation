import requests
from pprint import pprint

url = "http://127.0.0.1:5000/translate"

def request_translate(translation_data):
    response = requests.post(url = url, json=translation_data)
    if response.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    else:
        return response.json() 

if __name__ == "__main__":
    request1 = {
    "data":[ "తెలుగు అనేది ద్రావిడ భాషల కుటుంబానికి చెందిన భాష. ", "భారతదేశంలో అత్యధికంగా మాతృభాషగా మాట్లాడే భాషలలో తెలుగు నాలుగో స్థానంలో ఉంది. "],
    "src": "te",
    "tgt": "en" 
    }

    request2 = {
    "data":[ "दिल्ली पुलिस की साइबर सेल ने ट्विटर के खिलाफ दर्ज की एफआईआर", " पूर्वजन्म के ये रहस्य यकीनन नहीं पता होंगे "],
    "src": "hi",
    "tgt": "en" ,
    "n_best" : 3
    }

    print("\n")
    pprint(request_translate(url, request1))
    print("\n ---------------------------------------------------------------------------  \n")
    pprint(request_translate(url, request2))

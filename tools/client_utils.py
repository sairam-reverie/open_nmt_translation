import time
import argparse

def convert_files_to_dicts(src_file, src, tgt):
    src_requests = []
    with open(src_file, encoding="utf-8") as file:
        for line in file:
            line = line.rstrip()
            request_data = {"data": line, "src":src , "tgt":tgt }
            src_requests.append(request_data)
    return src_requests


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("src_file", help = "Path to the file containg source sentences")
    parser.add_argument("src_lang", help = "Source language", type=str, choices=["te", "hi"])
    parser.add_argument("tgt_lang", help = "Target language")
    args = parser.parse_args()

    src = args.src_lang
    tgt = args.tgt_lang
    src_file = args.src_file

    start = time.time()
    src_requests = convert_files_to_dicts(src_file, src, tgt)
    end = time.time()
    time_taken = end - start
    print(time_taken)








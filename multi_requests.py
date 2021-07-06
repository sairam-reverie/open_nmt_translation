from client_script import request_translate
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from pprint import pprint
import time
import sys


url = "http://127.0.0.1:5000/translate"


src_file = "telugu_dev.txt"
tgt_file = "english_dev.txt"

def create_request_from_sent(src_sent, src = "te", tgt ="en", n_best = 1):
    return {"data":[src_sent ],"src": src,"tgt": tgt}

def create_multi_requests(n):
    return [create_request_from_sent(sent) for sent in src_lines[:n]]

def request_synchronous(all_requests):
    all_responses =  [request_translate(data) for data in all_requests]
    return all_responses

def request_multithread(all_requests):
    with ThreadPoolExecutor() as executor:
        all_responses = executor.map(request_translate, all_requests)
    return all_responses

def request_multiprocess(all_requests):
    with ProcessPoolExecutor() as executor:
        all_responses = executor.map(request_translate, all_requests)
    return all_responses


if __name__ == "__main__":

    with open(src_file, "r") as file:
        src_lines = [line.rstrip() for line in file]

    # with open(tgt_file, "r") as file:
    #     tgt_lines = [line.rstrip() for line in file]
    
    n = int(sys.argv[1])

    print("\n")
    all_requests = create_multi_requests(n)

    start = time.perf_counter()
    all_responses = request_synchronous(all_requests)
    finish = time.perf_counter()
    print(f'Finished SYNCHRONOUS in {round(finish-start, 2)} second(s)')

    start = time.perf_counter()
    all_responses = request_multithread(all_requests)
    finish = time.perf_counter()
    print(f'Finished MULTITHREAD in {round(finish-start, 2)} second(s)')

    start = time.perf_counter()
    all_responses = request_multiprocess(all_requests)
    finish = time.perf_counter()
    print(f'Finished MULTIPROCESS in {round(finish-start, 2)} second(s)')


    # all_responses = list(all_responses)
    # print("\n")
    # print(all_responses[0])
    # print("\n ---------------------------------------------------------------------------  \n")
    # print(all_responses[-1])


    # print("\n")
    # print(create_request_from_sent(src_lines[0]))
    # print("\n ---------------------------------------------------------------------------  \n")
    # print(create_request_from_sent(src_lines[1]))



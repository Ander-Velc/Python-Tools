#!/usr/bin/python3

import hashlib
import signal
import argparse
from concurrent.futures import ThreadPoolExecutor
import time
import threading
import itertools
import sys
from functools import partial

# --------------------------------
# Colors
# --------------------------------
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
end = "\033[0m"

# --------------------------------
# CTRL + C Function
# --------------------------------
def def_handler(sig, frame):
    print("\n[!] Interrupted (CTRL+C). Exiting...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# --------------------------------
# Loading Function
# --------------------------------
def start_loader(text=f"Cracking..."):
    stop_event = threading.Event()

    def loader():
        spinner = itertools.cycle(['|', '/', '-', '\\'])
        while not stop_event.is_set():
            sys.stdout.write(f"\r{text} {next(spinner)}")
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write("\r")  # limpiar línea

    thread = threading.Thread(target=loader)
    thread.daemon = True
    thread.start()
    return stop_event, thread

# --------------------------------
# Banner
# --------------------------------
def attack_banner(algorithm, threads):
    date = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nStarting attack... {red}( https://github.com/ander-velc ){end} at {blue}{date}{end}")
    print(f"Algorithm: {blue}{algorithm}{end}")
    print(f"Threads: {blue}{threads}{end}\n")

# --------------------------------
# Crack Function
# --------------------------------
def crack(password, hashes, algorithm):
    password = password.strip()
    if not password:
        return None

    hash_func = getattr(hashlib, algorithm)
    hash_cracked = hash_func(password.encode('utf-8')).hexdigest()

    if hash_cracked in hashes:
        return (hash_cracked, password)
    return None

# --------------------------------
# Main
# --------------------------------
def main():
    parser = argparse.ArgumentParser(description="Hash Cracker")
    parser.add_argument("--hashes", required=True, help="File with hashes")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file")
    parser.add_argument("-a", "--algorithm", required=True, help="Hash algorithm (md5, sha256, etc.)")
    parser.add_argument("-t", "--threads", type=int, default=4, help="Number of threads")
    args = parser.parse_args()

    algorithm = args.algorithm.lower()
    threads = args.threads
    if not hasattr(hashlib, algorithm):
        print(f"\n{red}[!] Unsupported algorithm: {algorithm}{end}")
        sys.exit(1)

    attack_banner(algorithm, threads)
    with open(args.hashes, 'r') as f:
        hashes = set(line.strip() for line in f if line.strip())

    found = set()
    worker = partial(crack, hashes=hashes, algorithm=algorithm)

    sdate = time.perf_counter()
    loader_event, loader_thread = start_loader()

    try:
        with open(args.wordlist, 'r', encoding='latin-1') as f:
            with ThreadPoolExecutor(max_workers=threads) as executor:
                for result in executor.map(worker, f):
                    if result:
                        hash_val, password = result
                        print(f"\n\t{green}Hash cracked{end} --> {red}{hash_val}{end}:{green}{password}{end}")
                        found.add(hash_val)

                        # Parada temprana
                        if len(found) == len(hashes):
                            break
    finally:
        loader_event.set()
        loader_thread.join()

    fdate = time.perf_counter()
    end_date = time.strftime("%Y-%m-%d %H:%M:%S")

    if not found:
        print(f"\n{red}[-] No hashes cracked{end}")

    print(f"\nFinished at {blue}{end_date}{end}")
    print(f"Time elapsed: {blue}{fdate - sdate:.4f} seconds{end}")


if __name__ == '__main__':
    main()


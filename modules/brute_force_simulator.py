# Brute Force Simulator (Ultra Fast & Educational)

import itertools
import string
import time

def run_brute_force_simulator():
    print("\n--- Brute Force Simulator (Educational Mode) ---")
    target = input("Enter a small demo password (max 3 characters recommended): ")

    print("\nChoose speed mode:")
    print("1. Ultra Fast (no delay, minimal output)")
    print("2. Visual Slow Mode")
    mode = input("Enter choice (1/2): ")

    if mode == "2":
        delay = 0.05
        show_each = True
    else:
        delay = 0
        show_each = False

    charset = string.ascii_lowercase + string.digits
    max_length = len(target)

    attempts = 0
    start_time = time.time()

    print("\nStarting brute force simulation...\n")

    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            guess = ''.join(combo)
            attempts += 1

            if show_each:
                print(f"Trying: {guess}", end="\r")
                time.sleep(delay)
            else:
                if attempts % 500 == 0:
                    print(f"Attempts so far: {attempts}", end="\r")

            if guess == target:
                end_time = time.time()
                duration = round(end_time - start_time, 4)

                print("\n\nPassword FOUND!")
                print(f"Password: {guess}")
                print(f"Total Attempts: {attempts}")
                print(f"Time Taken: {duration} seconds")

                return

    print("\nPassword not found within limits.")

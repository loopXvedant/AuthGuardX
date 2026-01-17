# Hash Type Identifier Module
# Beginner-friendly & Educational

def identify_hash(hash_value):
    length = len(hash_value)

    if hash_value.startswith("$1$"):
        return "MD5 (Linux shadow format)"
    elif hash_value.startswith("$5$"):
        return "SHA-256 (Linux shadow format)"
    elif hash_value.startswith("$6$"):
        return "SHA-512 (Linux shadow format)"

    if length == 32:
        return "MD5"
    elif length == 40:
        return "SHA-1"
    elif length == 64:
        return "SHA-256"
    elif length == 128:
        return "SHA-512"
    elif length == 32 and hash_value.isalnum():
        return "NTLM (possible)"
    else:
        return "Unknown or unsupported hash type"

def run_hash_identifier():
    print("\n--- Hash Type Identifier ---")
    print("Enter 'exit' to return to main menu.\n")

    while True:
        hash_input = input("Enter a hash: ")

        if hash_input.lower() == "exit":
            break

        hash_type = identify_hash(hash_input)

        print("\n--- Result ---")
        print(f"Hash: {hash_input}")
        print(f"Detected Type: {hash_type}")

        print("\nExplanation:")
        if "MD5" in hash_type:
            print("- MD5 is a fast but insecure hashing algorithm.")
        elif "SHA-1" in hash_type:
            print("- SHA-1 is deprecated and insecure.")
        elif "SHA-256" in hash_type:
            print("- SHA-256 is part of the SHA-2 family, widely used.")
        elif "SHA-512" in hash_type:
            print("- SHA-512 is very strong and secure.")
        elif "NTLM" in hash_type:
            print("- NTLM is used in Windows authentication.")
        else:
            print("- Could not confidently identify this hash.")

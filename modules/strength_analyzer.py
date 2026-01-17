# Password Strength Analyzer Module
# Beginner-friendly version with loop

import math
import re

def calculate_entropy(password):
    charset_size = 0

    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in "!@#$%^&*()-_=+[]{};:,.<>?/|" for c in password):
        charset_size += 32

    if charset_size == 0:
        return 0

    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)

def run_strength_analyzer():
    while True:
        print("\n--- Password Strength Analyzer ---")
        password = input("Enter a password to analyze (or type 'exit' to go back): ")

        if password.lower() == "exit":
            break

        length = len(password)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(c in "!@#$%^&*()-_=+[]{};:,.<>?/|" for c in password)

        score = 0
        suggestions = []

        if length >= 8:
            score += 1
        else:
            suggestions.append("Use at least 8 characters.")

        if has_upper:
            score += 1
        else:
            suggestions.append("Add uppercase letters.")

        if has_lower:
            score += 1
        else:
            suggestions.append("Add lowercase letters.")

        if has_digit:
            score += 1
        else:
            suggestions.append("Add numbers.")

        if has_symbol:
            score += 1
        else:
            suggestions.append("Add special symbols.")

        # Weak pattern detection
        if re.search(r"(123|abc|password|admin)", password.lower()):
            suggestions.append("Avoid common patterns like 123, abc, password.")
            score -= 1

        entropy = calculate_entropy(password)

        # Strength Rating
        if score <= 2:
            strength = "WEAK ❌"
        elif score == 3 or score == 4:
            strength = "MEDIUM ⚠️"
        else:
            strength = "STRONG ✅"

        print("\n--- Analysis Result ---")
        print(f"Password Length: {length}")
        print(f"Uppercase Present: {has_upper}")
        print(f"Lowercase Present: {has_lower}")
        print(f"Number Present: {has_digit}")
        print(f"Symbol Present: {has_symbol}")
        print(f"Entropy Score: {entropy}")
        print(f"Strength Rating: {strength}")

        if suggestions:
            print("\nSuggestions to improve:")
            for s in suggestions:
                print("- " + s)

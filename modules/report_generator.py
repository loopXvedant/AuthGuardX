# Auto Security Report Generator
# Beginner-friendly version

import datetime
import os

def run_report_generator():
    print("\n--- Auto Security Report Generator ---")

    project_name = "AuthGuardX – Password Security Audit Toolkit"
    author = input("Enter your name: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    print("\nAnswer a few questions to generate your report.\n")

    dict_result = input("Did dictionary generator work? (yes/no): ")
    strength_result = input("Did strength analyzer work? (yes/no): ")
    brute_result = input("Did brute force simulator work? (yes/no): ")
    hash_result = input("Did hash identifier work? (yes/no): ")

    filename = f"output/reports/AuthGuardX_Report_{date}.txt"
    os.makedirs("output/reports", exist_ok=True)

    with open(filename, "w") as f:
        f.write("====================================\n")
        f.write("      SECURITY AUDIT REPORT\n")
        f.write("====================================\n\n")

        f.write(f"Project Name: {project_name}\n")
        f.write(f"Author: {author}\n")
        f.write(f"Date: {date}\n\n")

        f.write("1. Introduction\n")
        f.write("This project demonstrates password attack simulations and security auditing.\n\n")

        f.write("2. Modules Implemented\n")
        f.write(f"- Dictionary Generator: {dict_result}\n")
        f.write(f"- Password Strength Analyzer: {strength_result}\n")
        f.write(f"- Brute Force Simulator: {brute_result}\n")
        f.write(f"- Hash Type Identifier: {hash_result}\n\n")

        f.write("3. Observations\n")
        f.write("Weak passwords are easily guessable.\n")
        f.write("Strong passwords have higher entropy and complexity.\n")
        f.write("Brute force attacks take time depending on complexity.\n\n")

        f.write("4. Conclusion\n")
        f.write("Strong password policies and secure hashing are essential.\n\n")

        f.write("5. Future Scope\n")
        f.write("- Add real-time monitoring\n")
        f.write("- Integrate with SIEM\n")
        f.write("- Add GUI\n")

    print("\nReport generated successfully!")
    print(f"Saved at: {filename}")

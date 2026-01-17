# 🔐 AuthGuardX  
### Password Cracking & Credential Security Audit Toolkit

AuthGuardX is a lightweight, educational cybersecurity toolkit designed to simulate common password-based attacks and analyze authentication security. It provides an ethical and controlled environment to understand how weak passwords can be exploited and how strong password policies can be enforced.

This project is intended **strictly for learning, demonstration, and academic purposes only**.

---

## 📌 Features

- Dictionary Generator
- Password Strength Analyzer
- Brute Force Simulator (Fast & Visual Mode)
- Hash Type Identifier (MD5, SHA1, SHA256, SHA512, Linux Shadow)
- Auto Security Report Generator
- Menu-driven CLI interface
- Ethical & safe simulations

---

## 🧠 Modules Explanation

### 1. Dictionary Generator
Creates custom password wordlists using:
- Case variations
- Numbers
- Symbols

---

### 2. Password Strength Analyzer
Checks:
- Length
- Uppercase/lowercase
- Digits
- Symbols
- Entropy
- Weak patterns
- Provides suggestions

---

### 3. Brute Force Simulator
Simulates brute-force attacks:
- Ultra-fast mode
- Visual slow mode
- Attempt counter
- Time calculation
- Educational simulation only

---

### 4. Hash Type Identifier
Detects:
- MD5
- SHA-1
- SHA-256
- SHA-512
- Linux shadow formats

---

### 5. Auto Report Generator
Creates a structured security report summarizing:
- Results
- Observations
- Conclusion
- Future scope

---

## 💻 System Requirements

| Requirement | Description |
|------------|------------|
Python | Python 3.x |
OS | Linux / Windows / macOS |
Terminal | Required |
Git (Optional) | For cloning |

---

## 📥 How to Download

### Method 1: Download ZIP (Beginner Friendly)

1. Go to:  
   👉 https://github.com/loopXvedant/AuthGuardX  
2. Click **Code**
3. Click **Download ZIP**
4. Extract the ZIP file
5. Open the extracted folder

---

### Method 2: Clone Using Git

If Git is installed:

```bash
git clone https://github.com/loopXvedant/AuthGuardX.git
cd AuthGuardX
```

---

## ▶️ How to Run (Step-by-Step)

### Step 1: Open Terminal

Navigate into the project folder:

```bash
cd AuthGuardX
```

---

### Step 2: Run the Tool

```bash
python3 main.py
```

If `python3` does not work, try:

```bash
python main.py
```

---

## 🧭 Menu Options Explained

After running, you will see:

```
1. Dictionary Generator
2. Password Strength Analyzer
3. Brute Force Simulator
4. Hash Type Identifier
5. Generate Security Report
6. Exit
```

---

### Option 1: Dictionary Generator
- Enter a base word
- Choose number variations
- Choose symbol variations
- A wordlist will be saved in:
  ```
  output/wordlists/
  ```

---

### Option 2: Password Strength Analyzer
- Enter any password
- Get strength, entropy, and suggestions
- Type `exit` to return to menu

---

### Option 3: Brute Force Simulator
- Enter a small password (example: `a1`, `ab`)
- Choose speed mode
- See attempts, time, and success

---

### Option 4: Hash Type Identifier
Paste a hash and it will detect:
- MD5
- SHA1
- SHA256
- SHA512
- Linux shadow

Type `exit` to go back.

---

### Option 5: Report Generator
- Enter confirmation values
- Automatically creates a report
- Saved in:
  ```
  output/reports/
  ```

---

## 📂 Folder Structure

```
AuthGuardX/
│
├── main.py
├── modules/
│   ├── dictionary_generator.py
│   ├── strength_analyzer.py
│   ├── brute_force_simulator.py
│   ├── hash_identifier.py
│   ├── report_generator.py
│
├── output/
│   ├── wordlists/
│   ├── reports/
│
├── screenshots/
├── disclaimer.txt
└── README.md
```

---

## ⚠️ Disclaimer

This project is strictly for **educational and ethical purposes**.

Do NOT use this tool on real systems without permission.  
The author is not responsible for misuse.

---

## 🎯 Learning Outcomes

- Understanding of password attacks
- Importance of strong passwords
- Brute-force simulation exposure
- Hash format knowledge
- Cybersecurity fundamentals

---

## 🔮 Future Enhancements

- GUI version
- Database logging
- Web-based version
- Advanced cracking simulations
- Dashboard visualization

---

## ⭐ Support

If you find this project useful, give it a ⭐ on GitHub!

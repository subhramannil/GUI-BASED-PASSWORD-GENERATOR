# GUI-BASED-PASSWORD-GENERATOR
It is a gui based password generator, which also save the passwords of various websites, username also. 
# 🔐 GUI Password Manager

A robust desktop application built with Python and Tkinter that generates strong, random passwords and securely saves credentials locally. This project demonstrates proficiency in GUI development, event handling, and file I/O operations.

## 📸 Dashboard
<img width="1023" height="790" alt="Screenshot 2026-02-16 224401" src="https://github.com/user-attachments/assets/639e75d2-2c25-4f85-bf73-03c2848fdbe6" />


## ✨ Key Features

### 1. **Secure Password Generation**
Generates cryptographically strong passwords combining uppercase letters, lowercase letters, numbers, and symbols. 

### 2. **Local Data Persistence**
Unlike cloud managers, this tool keeps your data on your own machine. Credentials are formatted and appended to a local text file (`all.txt`) for easy reading and retrieval.

> **How data is stored:**

> <img width="567" height="315" alt="Screenshot 2026-02-16 224524" src="https://github.com/user-attachments/assets/47560abb-5e31-4a87-81d1-18605cdece67" />

### 3. **Smart Validation & User Safety**
The application includes error handling to prevent users from saving incomplete data. It also features a "Check Again" confirmation dialog to ensure accuracy before writing to the file.

> **Input Validation in action:**
> <img width="1151" height="797" alt="Screenshot 2026-02-16 224411" src="https://github.com/user-attachments/assets/9a50d7e2-96ad-44f1-97a0-fc30f6c091bc" />


## 🛠️ Tech Stack

* **Language:** Python 3.x
* **GUI Framework:** Tkinter
* **Modules:** `random`, `messagebox` (standard libraries)

## 🚀 How to Run

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/your-username/password-manager.git](https://github.com/your-username/password-manager.git)
    ```
2.  **Navigate to the folder**
    ```bash
    cd password-manager
    ```
3.  **Run the application**
    ```bash
    python PASSWORD_MAKING.py
    ```

## 📂 Project Structure

```text
password-manager/
│
├── PASSWORD_MAKING.py   # Main source code
├── all.txt              # Stores the saved passwords
├── rlock2.png           # App logo asset
└── README.md            # Documentation

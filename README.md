🔐 Secret Notes App (Python & Tkinter)

This project is a simple desktop note application built with Python and Tkinter that allows users to encrypt and decrypt secret notes using a master password.

The main goal of this project is to practice:

GUI development with Tkinter

Basic cryptography concepts

Error handling and input validation

Clean function-based structure

🚀 Features

🖥️ Simple Tkinter-based user interface

🔑 Encrypt notes using SHA-256 + Fernet encryption

🔓 Decrypt notes with the correct master key

❌ Prevents app crashes with input validation

🛡️ Handles wrong passwords without revealing correctness

💾 Encrypted notes are saved to a local file

🧠 How Encryption Works (Simple Explanation)

User enters a master key (password)

The password is converted into a SHA-256 hash

The hash is encoded into a Fernet-compatible key

The secret text is encrypted using Fernet

Encrypted text is saved to a file

For decryption:

If the password is correct → original text is shown

If the password is wrong → random fake data is shown (no crash)

🛠️ Technologies Used

Python 3

Tkinter (GUI)

cryptography library (Fernet)

hashlib (SHA-256)

base64
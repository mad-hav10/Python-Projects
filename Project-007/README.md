# Caesar Cipher 🔐

Welcome to the **Caesar Cipher**! This program encrypts or decrypts messages using a simple substitution cipher where each letter is shifted by a fixed number of positions in the alphabet.

## 📝 Description

The **Caesar Cipher** program allows you to:
- **Encrypt** a text by shifting its letters forward in the alphabet.
- **Decrypt** a text by shifting its letters backward in the alphabet.

This is a fun and straightforward way to secure your messages or learn about basic cryptography concepts.

## 🚀 How It Works

The program:
1. Asks the user whether they want to **Encrypt** or **Decrypt** a message.
2. Prompts the user to input the text and the shift amount.
3. Shifts each letter of the text by the specified amount:
   - Wraps around the alphabet for letters near the end (e.g., `z` shifts to `a`).
   - Leaves non-alphabetic characters (like spaces or punctuation) unchanged.
4. Displays the encrypted or decrypted message.

### Example:
- **Input**: `text = "hello"`, `shift = 3`, `operation = "encrypt"`
- **Output**: `"khoor"`

## 🖥️ Code Overview

The program is implemented in Python with the following key components:

1. **Alphabet List**:
   - A list of lowercase letters used for indexing and wrapping shifts.
2. **EncodeOrDecode Function**:
   - Handles both encryption and decryption based on the user's choice.
   - Shifts letters and handles wrap-around using modular arithmetic.
3. **User Interaction**:
   - Continuously prompts the user for input until they choose to exit.

You can find the complete implementation in the `main.py` file.

## 📂 Folder Structure

- `main.py`: Contains the main code for the project.

## 💡 Features

- Encrypts and decrypts text using a Caesar Cipher.
- Supports any shift value, including large numbers and negative shifts.
- Preserves non-alphabetic characters in the text.

## 🌟 Future Enhancements

- Add uppercase letter support for mixed-case inputs.
- Implement a graphical interface for a more user-friendly experience.
- Include an option to auto-decrypt using frequency analysis.

## 📜 License

This project is open-source and licensed under the MIT License.

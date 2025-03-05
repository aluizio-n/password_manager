# Password Manager (Secure & Encrypted)

## 📌 About the Project
This is a **secure password manager** built in Python. It allows users to store and retrieve passwords securely using encryption. All stored passwords are fully encrypted to ensure data protection.

## 🚀 Features
- **Secure storage:** Passwords are encrypted using the `cryptography` library.
- **Master key encryption:** Users must provide a master password to encrypt and decrypt stored passwords.
- **Database storage:** Uses SQLite to store encrypted credentials.
- **Random password generator:** Automatically generates strong passwords.
- **.env file support:** Securely configures database settings.

## 🛠 Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/aluizio-n/password_manager.git
cd password_manager
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up the Environment Variables**
Create a `.env` file in the project root and add:
```
DB_PATH=passwords.db
```

## 📌 Usage

### **Run the Program**
```sh
python main.py
```

### **Options**
1️⃣ **Store a password**: Enter a website, username, and password (or generate one automatically).
2️⃣ **Retrieve stored passwords**: Enter your master password to decrypt stored credentials.

## 🔒 Security Considerations
- Your master password **must always be the same** to correctly encrypt/decrypt stored passwords.
- The database only contains **encrypted** passwords, making it unreadable without the correct key.
- Never share your `.env` file or database file with others.

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Feel free to submit issues and pull requests to improve the project!

---
🚀 **Happy password managing! Stay secure!** 🔐


# Password Manager (Encryption)

## Project Overview

Password Manager is a secure Python application that helps users store and manage passwords safely. The application encrypts passwords before storing them, ensuring that sensitive information remains protected.

## Features

- Add Password
- View Saved Passwords
- Search Password by Website
- Delete Password
- Password Encryption using Fernet
- Secure JSON Storage
- Menu-Driven Interface

## Technologies Used

- Python
- Cryptography Library (Fernet)
- JSON
- File Handling

## Project Structure

```text
Password_Manager/
│
├── main.py
├── generate_key.py
├── key.key
├── passwords.json
├── README.md
└── requirements.txt
```

## Installation

1. Clone the repository

```bash
git clone <repository_url>
```

2. Navigate to the project folder

```bash
cd Password_Manager
```

3. Install required package

```bash
pip install cryptography
```

## How to Run

Generate encryption key (only first time):

```bash
python generate_key.py
```

Run the application:

```bash
python main.py
```

## Menu Options

```text
1. Add Password
2. View Passwords
3. Search Password
4. Delete Password
5. Exit
```

## Security

- Passwords are encrypted before storage.
- Encryption is performed using Fernet symmetric encryption.
- Stored passwords cannot be read directly from the JSON file.

## Learning Outcomes

Through this project, I learned:

- Python Programming
- Functions and Modular Programming
- File Handling
- JSON Data Management
- Encryption and Decryption
- CRUD Operations
- Menu-Driven Application Development

## Author

Kirithikaa S

## Internship

## Intern Details
- Name: Kirithikaa S
- Intern ID: CITS2745

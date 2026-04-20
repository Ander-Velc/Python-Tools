# Python-Tools

I made this repo to upload python scripts that I made for practicing my programming skills, perhaps someone else is also learning and can help.

# portscan.py

This tool has helped me to better understand the relationship of the information packets transmitted between systems, I tried to copy the nmap style and features.
Is slow and simple but it works...

<img width="1044" height="432" alt="image" src="https://github.com/user-attachments/assets/4b0a265f-71dd-44b4-b9f2-ef4c729ab0ae" />

<img width="1406" height="444" alt="image" src="https://github.com/user-attachments/assets/ae1368b6-3d11-4c19-8e4b-38d3a75b0434" />

## ⚙️ Requirements
Python 3.8+
`scapy, argparse`

Install:
```
pip install scapy, argparse
```

# quickcypher
QuickCypher is a lightweight command-line tool written in Python that allows users to quickly encrypt and decrypt text using Fernet, a secure symmetric encryption scheme based on AES.

This tool has helped me to apply basic cryptographic knowledge to programming

Usage:

- Encrypt text
`python3 quickcypher.py --text "secret message"`

<img width="2252" height="208" alt="image" src="https://github.com/user-attachments/assets/0afcebea-2ae0-4a48-b574-d1ed77808fc5" />

- Decrypt text
`python3 quickcypher.py --decrypt "<encrypted_token>" --key "<encryption_key>"`

<img width="2282" height="174" alt="image" src="https://github.com/user-attachments/assets/9f0660c4-7349-405e-b8e4-f79b17109c8e" />

## ⚙️ Requirements
Python 3.8+
`cryptography` library

Install:
```
pip install cryptography
```

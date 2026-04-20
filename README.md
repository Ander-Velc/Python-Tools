# Python-Tools

I made this repo to upload python scripts that I made for practicing my programming skills, perhaps someone else is also learning and can help.

# portscan.py

This tool has helped me to better understand the relationship of the information packets transmitted between systems, I tried to copy the nmap style and features.
Is slow and simple but it works...

<img width="2310" height="624" alt="image" src="https://github.com/user-attachments/assets/5d81e109-73a8-4bc3-8776-8a1e033c4ea0" />

Scan:

<img width="2326" height="826" alt="image" src="https://github.com/user-attachments/assets/1cc90ef2-df04-48c7-b71b-45e2f4bad2d7" />


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

# Python-Tools

<img width="712" height="729" alt="image" src="https://github.com/user-attachments/assets/124e9d0a-0e0b-4289-91d2-f5d101ed8d53" />

## Purpose

I made this repo to upload python scripts that I made for practicing my programming skills, perhaps someone else is also learning and can help.

# taurush.py

 I've tried to make a fast hash cracker tool, it support most of the common hash algorithms and include threads. Be careful with RAM...

<img width="1119" height="433" alt="image" src="https://github.com/user-attachments/assets/24f8fa64-1ee8-4cd1-83df-4d8366f678f0" />

I've tried to use a 40.000 lines wordlist and this is the average speed:

sha256:

<img width="1916" height="776" alt="image" src="https://github.com/user-attachments/assets/c90da3b5-c1a9-47e0-b7ae-f243b8eb0d57" />

md5:

<img width="1916" height="775" alt="image" src="https://github.com/user-attachments/assets/3facd230-7019-4ca0-82c2-822c800b6d0a" />

## ⚙️ Requirements

Python 3.8+

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
pip3 install scapy
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
pip3 install cryptography
```

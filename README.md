# CipherShelter
> A command-line file encryption utility built with Python, implementing AES-128 symmetric encryption via Fernet and PBKDF2-HMAC-SHA256 key derivation.

## Overview

Ciphershelter is a python-based application which encrypts & decrypts files with a uniquely derived key. CipherShelter uses PBKDF2-HMAC-SHA256 to generate a cryptographically secure key with 640,000 iterations, inline with [NIST recommendations](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-132.pdf).

## Features

- AES-128 encryption via Fernet
- Key derivation via PBKDF2-HMAC-SHA256
- Uniquely generated salt for each encryption
- Enforces password strength (length, number, & special character)
- Secure password entry on terminal
- Clean, descriptive error messages

## Installation
 
**Requirements:** Python 3.10+
 
```bash
# Clone the repository
git clone https://github.com/DweanMachine/CipherShelter.git
cd CipherShelter
 
# Install in editable mode
pip install -e .
```
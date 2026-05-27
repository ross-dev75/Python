# Password Manager

## What it does

A Tkinter desktop app for storing and retrieving credentials. Entries are encrypted at rest; a master password is required at every launch. Includes a password generator, vault browser, and master password change flow.

## Key concepts

- PBKDF2-HMAC-SHA256 key derivation (600,000 iterations, OWASP 2023 recommendation)
- Fernet symmetric encryption for the vault file
- Atomic file writes (write to `.tmp`, then `os.replace`) to prevent corruption on crash
- 3-attempt lockout on wrong master password

## How it works

On first launch, a fresh 16-byte salt is generated, the master password is stretched into a 32-byte key via PBKDF2, and an empty vault is encrypted and saved as `data.enc`. On subsequent launches, the salt is read from the first 16 bytes of `data.enc` and the key is re-derived to decrypt the rest. All credential data lives only in memory after unlock; changes are re-encrypted and atomically written on each save.

## How to run

```
$ pip install cryptography pyperclip
$ python password_manager.py
```

`data.enc` is gitignored. Do not commit it.

# Password Tool

A simple encrypted password generator and manager, built in Python as a hands-on learning project.

## Features

- **Password Strength Checker** — Evaluates passwords across length and character variety, returning a score (0-100) and a human-readable label (Weak / Medium / Strong / Very Strong).
- **Customizable Password Generator** — Generate passwords with configurable length and character types (uppercase, digits, symbols).
- **Encrypted Storage** — Saved passwords are encrypted using Fernet (AES-128 in CBC mode with HMAC-SHA256) before being written to disk. The plaintext is never stored.
- **Interactive CLI Menu** — A simple terminal interface to access all features.

## Tech Stack

- Python 3.10+
- [`cryptography`](https://cryptography.io/) — Fernet symmetric encryption
- Standard library: `random`, `string`, `os`

## Installation

```bash
git clone https://github.com/judyahmadd/password-tool.git
cd password-tool
pip install cryptography
```

## Usage

```bash
python password_tool.py
```

You'll be presented with a menu:

```
=== Password Tool ===
1. Check password strength
2. Generate new password
3. List saved passwords
4. Quit
```



On first run, a `secret.key` file is generated. **Do not delete it** — it's required to decrypt any saved passwords. Saved passwords are stored encrypted in `passwords.txt`.

## Security Notes

⚠️ **This is a learning project, not a production password manager.**

- The encryption key is stored alongside the data in `secret.key`. In a production tool, the key would be derived from a master password using PBKDF2 or Argon2.
- Both `secret.key` and `passwords.txt` are listed in `.gitignore` and should **never** be committed to version control.
- For real password storage, use established tools like Bitwarden, 1Password, or KeePass.

## Roadmap

Possible future improvements:
- Master password with PBKDF2 key derivation
- Guarantee at least one character from each selected type in the generator
- JSON storage format with metadata (created_at, last_modified)
- CLI flags via `argparse` for non-interactive use
- Search/filter saved passwords by name

## Author

**Judy Ahmad**
- Website: [judyahmad.com](https://judyahmad.com)
- GitHub: [@judyahmadd](https://github.com/judyahmadd)
- X (Twitter): [@judyahmadd](https://x.com/judyahmadd)

## License

MIT
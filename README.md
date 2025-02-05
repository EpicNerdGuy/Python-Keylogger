# Keylogger Script

## Description
This is a simple keylogger script that logs keystrokes and periodically sends them via email. The script:
- Captures keystrokes using the `pynput` library.
- Logs the keystrokes into a file (`keylog.txt`).
- Sends the logged keystrokes via email every 8 hours using SMTP.

## Requirements
Before running the script, ensure you have the following installed:
- Python 3.x
- `pynput` (`pip install pynput`)
- `schedule` (`pip install schedule`)

## Configuration
1. Replace `your_email@gmail.com` with your sender email.
2. Replace `your_app_password` with an app password (if using Gmail, enable 2FA and generate an app password).
3. Replace `recipient_email@gmail.com` with the recipient's email.

## Usage
Run the script using:
```bash
python keylogger.py
```

The script will run in the background, logging keystrokes and sending logs via email.

## Disclaimer
This script is for educational purposes only. Unauthorized use of keylogging software is illegal and unethical. Use responsibly!


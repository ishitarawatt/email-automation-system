# ✉️ Email Automation System

> Send personalised bulk emails from a CSV list over SMTP, with logging and error handling built in.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SMTP](https://img.shields.io/badge/SMTP-EA4335?style=flat-square&logo=gmail&logoColor=white)

## Features

- 📇 Reads recipients from `contacts.csv`
- 🧩 Personalises each message per recipient
- 🔐 Secure SMTP authentication
- 🧾 Logs every send
- 🛡️ Error handling so one bad address doesn't stop the batch

## Project structure

```
email-automation-system/
├── email_sender.py    # main script
├── config.py          # SMTP settings
├── contacts.csv       # recipient list
└── requirements.txt
```

## Setup

```bash
git clone https://github.com/ishitarawatt/email-automation-system.git
cd email-automation-system
pip install -r requirements.txt
```

1. Put your SMTP details in `config.py`. Use an **app password**, never your real password, and don't commit it.
2. Fill in `contacts.csv` with your recipients.
3. Run:
   ```bash
   python email_sender.py
   ```

## Tech stack

Python · SMTP · CSV

## Responsible use

Only email people who have agreed to hear from you, and respect your provider's sending limits.

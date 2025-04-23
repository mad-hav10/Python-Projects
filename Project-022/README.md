# 💌 Wednesday Quote Emailer

Automatically send a motivational quote every Wednesday with this simple Python script. It's a great way to keep yourself or someone else inspired midweek!

## 📝 Description

This project checks the current day of the week and, if it’s Wednesday, sends a randomly selected quote from a `.txt` file via email using Gmail's SMTP server.

### How It Works:
1. Reads the current day using `datetime`.
2. If it’s Wednesday (weekday `2`), the script:
   - Picks a random quote from a text file.
   - Logs into Gmail using SMTP.
   - Sends the quote via email.

## 🖥️ Code Overview

### 1. **Main Script (`main.py`)**
   - **Key Features**:
     - Checks for Wednesday using `datetime`.
     - Reads quotes from `quotes.txt`.
     - Uses `random.choice()` to pick a quote.
     - Sends the quote via Gmail's SMTP service.

   - **Core Libraries Used**:
     - `datetime` for weekday detection.
     - `smtplib` for sending emails.
     - `random` for selecting a quote.
     - `pandas` is imported but not used in this version.

### 2. **Quotes File (`quotes.txt`)**
   - A plain text file with motivational quotes.
   - Each quote should be on a new line.

## 📂 Folder Structure

```
WednesdayQuoteEmailer/
├── main.py
├── quotes.txt
```

## ⚙️ Requirements

- Python 3.x
- An active Gmail account
- Less secure app access enabled (or use [App Passwords](https://support.google.com/accounts/answer/185833))

## 🌟 Features

- **Automated Emailing**: Sends quotes only on Wednesdays.
- **Random Quote Selection**: Ensures a different message each week.
- **Secure Login**: Uses `starttls()` for secure Gmail connection.

## 🔒 Security Note

If you're using Gmail with 2-Step Verification, you'll need to create and use an [App Password](https://myaccount.google.com/apppasswords) instead of your main account password.

## 💡 Future Enhancements

- Schedule script with a task scheduler or CRON job.
- Add multiple recipient support.
- Customize quote categories (inspirational, funny, etc.).
- Use HTML formatting for richer emails.

## 📜 License

This project is open-source and available under the MIT License.

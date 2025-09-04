
# 📧 Gmail Bulk Email Sender (Python + Selenium)

This project automates sending bulk emails using **Gmail** and **Selenium WebDriver**.  
It reads recipient email addresses from a CSV file and sends a predefined subject and message to each one.

---

## 🚀 Features
- Reads email addresses from a CSV file (`MAIL IDS.csv`)
- Automates Gmail's **Compose → To → Subject → Body → Send**
- Uses **an existing Chrome session** (so no need to log in every time)
- Adds delays to avoid Gmail rate-limit issues
- Simple and beginner-friendly

---

## 📂 Project Structure
```

gmail-bulk-sender/
│── main.py             # Main automation script
│── requirements.txt    # Python dependencies
│── README.md           # Documentation

````

---

## ⚙️ Setup Instructions

### 1️⃣ Install Requirements
Make sure you have Python 3 installed, then install the dependencies:
```bash
pip install -r requirements.txt
````

### 2️⃣ Start Chrome with Debugging Mode

You need to open Chrome in **remote debugging mode** so Selenium can attach:

```bash
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"
```

* This opens a new Chrome profile.
* Log in to **Gmail** inside that window.

### 3️⃣ Prepare Your CSV

Create a file named `MAIL IDS.csv` in the same folder with a column called `email`. Example:

```csv
email
test1@example.com
test2@example.com
test3@example.com
```

### 4️⃣ Run the Script

Once Gmail is logged in, run:

```bash
python main.py
```

---

## 🛑 Important Notes

* This script is **for educational purposes only**.
* Do **NOT** use for spam — it may get your Gmail account suspended.
* Add `MAIL IDS.csv` to your `.gitignore` so you don’t accidentally upload private data.

---

## 📌 Example Email Sent

* **To**: [recipient@example.com](mailto:recipient@example.com)
* **Subject**: Your subject here
* **Body**: your email here

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork this repo and improve the automation.

---

## 📜 License

This project is licensed under the MIT License — you’re free to use, modify, and share it.

```

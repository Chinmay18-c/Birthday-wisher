# Birthday Wisher

Automatically sends birthday emails to people listed in `birthdays.csv`.

## Features
- Reads birthdays from a CSV file.
- Picks a random letter template and personalizes it.
- Sends email using Gmail SMTP.

## Folder Structure

```
birthday_wisher/
├── letter_templates/
│   ├── letter_1.txt       # Example: "Happy Birthday [NAME]! Have a great day!"
│   ├── letter_2.txt       # Example: "Hey [NAME], wishing you an amazing birthday!"
│   └── letter_3.txt       # Example: "Dear [NAME], Happy Birthday and best wishes!"
├── birthdays.csv          # List of birthdays
├── birthday_wisher.py     # Main Python script
├── password.env           # NOT pushed to GitHub (contains email credentials)
├── requirements.txt       # Required Python packages
└── README.md
```

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Gmail credentials:
   ```
   MY_EMAIL=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```
   **Note:** Use a Gmail App Password, not your regular password.

4. Add birthdays to `birthdays.csv` in this format:
   ```
   name,email,month,day
   John Doe,john@example.com,9,6
   Jane Doe,jane@example.com,12,25
   ```

5. Add your letter templates in the `letter_templates` folder using `[NAME]` as a placeholder for the person's name.

6. Run the script:
   ```bash
   python birthday_wisher.py
   ```

## Security
- **Do NOT push `password.env`** to GitHub.
- Add sensitive files to `.gitignore`:
  ```
  password.env
  __pycache__/
  *.pyc
  ```

## Example Letter Templates

- `letter_1.txt`: `Happy Birthday [NAME]! Have a great day!`
- `letter_2.txt`: `Hey [NAME], wishing you an amazing birthday!`
- `letter_3.txt`: `Dear [NAME], Happy Birthday and best wishes!`

## Notes
- Make sure your CSV has valid email addresses.
- The script only sends emails if the birthday matches today's date.
- For security, never commit real passwords to GitHub.

'''
Email Filter and Cleaner
----------------------------------
This script iterates through a list of raw email inputs, cleans whitespaces 
and casing, and classifies them into Valid, Invalid, or Spam categories.
'''
# Raw email data
raw_emails = [
    "sarah.n2003@gmail.com ",
    "monireh.jabbari.20@gmail.com ",
    "invalid_email.com",
    "   Dani_Mohhammadi@yahoo.com",
    "SPAM_OFFER@marketing.com",
    "n2n2n2@outlook.com    ",
    "Bad_guyyyy@",
    "yeganeh_salehi24@gmail.com ",
    "admin@GMAIL.COM  ",
    "FREE_MONEY@marketing.com",
    "leila_Ahamdi@yahoo.com",
]

valid_emails = []
invalid_emails = []
spam_emails = []

# Process and categorize emails
for email in raw_emails:
    clean_emails = email.strip().lower()
    if "marketing" in clean_emails or "spam" in clean_emails:
        spam_emails.append(clean_emails)
    elif "@" not in clean_emails or "." not in clean_emails:
        invalid_emails.append(clean_emails)
    else:
        valid_emails.append(clean_emails)
       
# Print formatted results
print("Valid emails:")
for email in valid_emails:
    print(f"  - {email}")

print("Invalid emails:")
for email in invalid_emails:
    print(f"  - {email}")

print("Spam emails:")
for email in spam_emails:
    print(f"  - {email}")

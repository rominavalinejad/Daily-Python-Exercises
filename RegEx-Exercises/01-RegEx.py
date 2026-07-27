'''
Log Data Parsing and Extraction System
'''

raw_log_data = """
[2026-07-27 08:30:15] CRITICAL_LOG - System automated check executed by admin_test@dev-server.net.
User login attempt from IP 192.168.1.105 succeeded. Primary contact: 09123456789.
Secondary notification sent to user.alex.smith@company.org and devops.team123@sub.domain.co.ir.

[2026-07-27 09:12:44] WARNING_LOG - Unauthorized access attempt detected from IP 10.0.0.1.
Triggered alert to security_dept@company.org. Emergency contact number: 09351112233.
Backup admin phone: 09109998877. Incident date recorded as 1405/05/12.

[2026-07-27 11:45:00] INFO_LOG - System update scheduled for 2026/08/01.
Coordinator email: sarah_connor99@gmail.com. Backup server IP: 172.16.254.1.
Support line: 09190001122. For inquiries, email support-desk@tech-corp.io.
"""
import re

# Define RegEx Pattern
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
phone_pattern = r"\b09\d{9}\b"
id_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
date_pattern = r"\b(?:\d{4}[/-]\d{2}[/-]\d{2})\b"

# Extract Data
emails = re.findall(email_pattern, raw_log_data)
phones = re.findall(phone_pattern, raw_log_data)
ip_addresses = re.findall(id_pattern, raw_log_data)
dates = re.findall(date_pattern, raw_log_data)

# Clean and deduplicate results
unique_emails = list(set(emails))
unique_phones = list(set(phones))
unique_id = list(set(ip_addresses))
unique_dates = list(set(dates))

# Display Results
print("\n=== EXTRACTED DATA SUMMARY ===")
result = {
    "Emails": unique_emails,
    "Phone Numbers": unique_phones,
    "IP Addresses": unique_id,
    "Dates": unique_dates
}

for title, data_list in result.items():
    print(f"\n{title} ({len(data_list)}):")
    for item in data_list:
        print(item)

# 01-RegEx
## Challenge: Log Data Parsing and Extraction System

1. Define a multi-line raw log string containing mixed technical data such as IP addresses, email addresses, phone numbers, and dates.
2. Define RegEx patterns using raw strings for emails, 11-digit Iranian mobile numbers starting with '09', IPv4 addresses, and formatted dates.
3. Use the re.findall() method to parse and extract all matching instances for each data category from the raw string.
4. Clean and deduplicate the extracted lists and convert them back into lists.
5. Display a structured summary in the terminal showing the count and line-by-line formatted values for each data category.

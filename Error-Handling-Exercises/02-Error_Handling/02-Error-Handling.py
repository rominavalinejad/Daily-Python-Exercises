'''
Data Pipeline and Bad Row Quarantine.
'''
import csv

def validate_row(row: dict) -> None:
    ''''
    Validate a single user row from the CSV file.
    Raise:
        ValueError: If any validation rule fails.
    '''
    name = row.get("name", "").strip()
    age = row.get("age", "").strip()
    email = row.get("email", "").strip()

    # Valid name
    if not name:
        raise ValueError("Naming is missing or empty")

    try:
        age_num = int(age)
    except ValueError as err:
        raise ValueError("Age must be a valid integer") from err

    # Validate accepted numerical range
    if age_num <= 0 or age_num > 100:
        raise ValueError("Age must be between 0 and 100")

    # Valid basic email structure
    if "." not in email or "@" not in email:
        raise ValueError("Invalid email address")

def process_data(input_file: str) -> None:
    '''
    Read CVS, validate rows, and separates valid data from bad rows
    '''
    with open(input_file, mode="r", encoding="utf-8") as infile, \
        open("valid_users.csv", mode="w", newline="", encoding="utf-8") as outfile, \
        open("quarantine.log", mode="w", encoding="utf-8") as logfile:

        reader = csv.DictReader(infile)
        fieldnames = ["id", "name", "age", "email"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for line_num, row in enumerate(reader,start=2):
            try:
                validate_row(row)
                writer.writerow(row)
            except ValueError as e:
                logfile.write(f"[Line {line_num}] Error: {e}\n {row}\n")

def main():
    '''Mian execution entry-point.'''
    process_data("user_data.csv")

if __name__ == "__main__":
    main()

import csv
import secrets
import string

# Open the source file to read AND create a new file to save our output data
with open('new_hires.csv', mode='r', encoding='utf-8-sig') as infile, \
     open('processed_onboarding.csv', mode='w', newline='', encoding='utf-8') as outfile:
     
    csv_reader = csv.DictReader(infile)
    
    # Define columns for our new database file
    fieldnames = ['first_name', 'last_name', 'department', 'email', 'temporary_password', 'status']
    csv_writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    # Write headers to our output file
    csv_writer.writeheader()
    
    print("Processing pipeline active. Writing data directly to master database...")
    print("=========================================================================")
    
    for row in csv_reader:
        cleaned_row = {}
        for key, value in row.items():
            if key is not None and value is not None:
                cleaned_row[key.strip()] = value.strip()
        
        if 'first_name' not in cleaned_row or 'last_name' not in cleaned_row:
            continue
            
        first_name = cleaned_row['first_name']
        last_name = cleaned_row['last_name']
        department = cleaned_row['department']
        
        # 1. Generate standard email
        email = f"{first_name.lower()}.{last_name.lower()}@mockcompany.com"
        
        # 2. Generate secure temporary password
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(secrets.choice(alphabet) for _ in range(12))
        
        # 3. Write row out to our processed file
        csv_writer.writerow({
            'first_name': first_name,
            'last_name': last_name,
            'department': department,
            'email': email,
            'temporary_password': password,
            'status': 'ACCOUNT_CREATED'
        })
        
        print(f"Successfully processed database record for: {first_name} {last_name}")

print("\nPipeline complete! Please check your folder for 'processed_onboarding.csv'.")

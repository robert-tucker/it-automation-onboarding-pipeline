# Automated Employee Provisioning Pipeline

A defensive, enterprise-focused Python data pipeline designed to automate user account provisioning, data sanitization, and secure credential generation from raw corporate personnel records.

## 🚀 Core Features

- **Automated Email Generation:** Dynamically derives uniform corporate emails using standard naming conventions (`f.lastname@company.com`) converted automatically to lowercase.
- **Defensive Error Handling:** Features robust data sanitization loops that automatically strip accidental whitespaces, handle null parameters, and eliminate byte-order mark (BOM) file corruptions from text/CSV files to preserve system runtime.
- **Cryptographically Secure Credentials:** Utilizes Python's compliance-standard `secrets` library to generate randomized, 12-character high-entropy temporary passwords.
- **Structured Database Output:** Generates clean, downstream database logs (`processed_onboarding.csv`) flagged with an operational audit status (`ACCOUNT_CREATED`).

## 🛠️ Technical Stack

- **Language:** Python 3.12+
- **Libraries Used:** `csv`, `secrets`, `string`
- **Data Formats:** CSV, I/O dictionary streaming (`DictReader` / `DictWriter`)

## 📊 Pipeline Architecture

1. **Ingest:** Reads raw, un-sanitized CSV files directly from the local file system.
2. **Scrub:** Automatically isolates missing rows and strips hidden line formatting anomalies.
3. **Provision:** Generates secure credentials and matches identity patterns.
4. **Log:** Streams results to an administrator console and outputs a master deployment spreadsheet.

# Python Log Analyzer

Basic SOC-style log analysis tool written in Python.

## Features

- Reads authentication log file
- Detects failed login attempts
- Aggregates failures by IP address
- Identifies potential brute-force activity

## How It Works

The script scans an `auth.log` file line by line, extracts failed login attempts, and counts occurrences per source IP.

## Example Output
Total Failed Login Attempts: 7
192.168.1.50 -> 3
10.0.0.8 -> 4


## Technologies Used

- Python 3
- Basic file handling
- Dictionary aggregation logic

git add .
git commit -m "Add README"
git push


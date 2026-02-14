# Counter for total failed login attempts
failed_attempts = 0

# Dictionary to store failures per IP address
# Format: { "IP address": number_of_failures }
ip_failures = {}

# Open the log file in read mode
with open("auth.log", "r") as file:

    # Loop through the file one line at a time
    for line in file:

        # Check if the line contains a failed login attempt
        if "FAILED" in line:

            # Increase total failed attempts counter
            failed_attempts += 1

            # Split the line into parts (separated by spaces)
            parts = line.split()

            # The last item in the line is the IP address
            ip = parts[-1]

            # If we've seen this IP before, increase its count
            if ip in ip_failures:
                ip_failures[ip] += 1
            else:
                # If it's a new IP, start its count at 1
                ip_failures[ip] = 1

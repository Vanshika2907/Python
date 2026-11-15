
# To develop a log file analyzer using JSON to store log records and analyze different types of log messages.

import json

# Sample log records
logs = [
    {"level": "INFO", "message": "Program started"},
    {"level": "WARNING", "message": "Low memory"},
    {"level": "ERROR", "message": "File not found"},
    {"level": "INFO", "message": "User logged in"},
    {"level": "ERROR", "message": "Connection failed"},
    {"level": "WARNING", "message": "High CPU usage"}
]

# Store logs in JSON file
with open("logs.json", "w") as file:
    json.dump(logs, file, indent=4)

# Read logs from JSON file
with open("logs.json", "r") as file:
    data = json.load(file)

# Initialize counters
info = 0
warning = 0
error = 0

print("Log File Analysis")
print("-----------------")

# Analyze log records
for log in data:
    if log["level"] == "INFO":
        info += 1
    elif log["level"] == "WARNING":
        warning += 1
    elif log["level"] == "ERROR":
        error += 1

# Display summary
print("Total Logs:", len(data))
print("INFO Messages:", info)
print("WARNING Messages:", warning)
print("ERROR Messages:", error)

# Display error messages
print("\nError Messages:")

for log in data:
    if log["level"] == "ERROR":
        print(log["message"])


# To write a Python program to read a log file and display its contents.

# Create a sample log file
with open("logfile.txt", "w") as file:
    file.write("INFO: Program started\n")
    file.write("WARNING: Low memory\n")
    file.write("ERROR: File not found\n")
    file.write("INFO: Program ended\n")

# Read and display the log file
with open("logfile.txt", "r") as file:
    print("Contents of Log File:")
    for line in file:
        print(line.strip())

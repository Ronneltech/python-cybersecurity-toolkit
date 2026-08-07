# Ronneltech Ltd
# Python Cybersecurity Toolkit
# Tool: Security Log Analyzer

def analyze_logs(log_file):

    suspicious_keywords = [
        "failed",
        "error",
        "unauthorized",
        "attack",
        "warning"
    ]

    print("\nSecurity Log Analysis")
    print("---------------------")

    try:
        with open(log_file, "r") as file:

            lines = file.readlines()

            suspicious_events = 0

            for line in lines:

                for keyword in suspicious_keywords:

                    if keyword.lower() in line.lower():
                        print("Suspicious Event Found:")
                        print(line.strip())
                        print()

                        suspicious_events += 1
                        break

            print("---------------------")
            print(f"Total Suspicious Events: {suspicious_events}")


    except FileNotFoundError:

        print("Log file not found.")


if __name__ == "__main__":

    log_file = input("Enter log file path: ")

    analyze_logs(log_file)

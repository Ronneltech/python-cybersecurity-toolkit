# Ronneltech Ltd
# Python Cybersecurity Toolkit
# Tool: Security Report Generator

from datetime import datetime


def generate_report():

    print("\nRonneltech Ltd Security Report Generator")
    print("----------------------------------------")

    project = input("Enter project name: ")
    findings = input("Enter security findings: ")
    recommendations = input("Enter recommendations: ")

    report = f"""
Ronneltech Ltd
Cybersecurity Assessment Report

Date:
{datetime.now()}

Project:
{project}

Security Findings:
{findings}

Recommendations:
{recommendations}

Prepared By:
MAITLAN AJONG ASONG

Founder — Ronneltech Ltd
"""

    filename = "security_report.txt"

    with open(filename, "w") as file:
        file.write(report)

    print("\nReport generated successfully.")
    print(f"Saved as: {filename}")


if __name__ == "__main__":
    generate_report()

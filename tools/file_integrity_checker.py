# Ronneltech Ltd
# Python Cybersecurity Toolkit
# Tool: File Integrity Checker

import hashlib
import os


def calculate_hash(filename):
    sha256 = hashlib.sha256()

    try:
        with open(filename, "rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


def check_integrity(filename, original_hash):

    current_hash = calculate_hash(filename)

    print("\nFile Integrity Check")
    print("--------------------")

    if current_hash is None:
        print("File not found.")
        return

    print("Current Hash:")
    print(current_hash)

    if current_hash == original_hash:
        print("\nStatus: File integrity verified")
    else:
        print("\nStatus: WARNING - File has been modified")


if __name__ == "__main__":

    filename = input("Enter file path: ")

    print("\nCreating initial file hash...")
    
    original_hash = calculate_hash(filename)

    if original_hash:
        print("Original Hash:")
        print(original_hash)

        check_integrity(filename, original_hash)
    else:
        print("Unable to calculate file hash.")

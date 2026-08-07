# Ronneltech Ltd
# Python Cybersecurity Toolkit
# Tool: Network Port Scanner

import socket


def scan_ports(target, start_port, end_port):
    print(f"Scanning target: {target}")
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")

        sock.close()


if __name__ == "__main__":
    target = input("Enter target IP address: ")

    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    scan_ports(target, start_port, end_port)

from subprocess import check_output
import os           # carry out os operations
import subprocess   # run commands
import socket       # ports
import pyfiglet    # banner
from datetime import datetime
import argparse

# Assuming cvemitre is imported correctly from the cvem module
from modules.cvem import cvemitre

class PortScanner:
    def __init__(self):
        subprocess.run('clear', shell=True)
        ascii_banner = pyfiglet.figlet_format("Vuln Scanner")
        print("\033[0;31m" + ascii_banner + "\033[0;0m")

    @staticmethod
    def banner_grab(ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((ip, port))
            sock.send(b"HEAD / HTTP/1.1\r\n\r\n")
            banner = sock.recv(1024).decode("utf-8", errors="ignore").strip()
            return banner.split("\n")[0]
        except Exception as e:
            return ""

    def scan_ports(self, ip):
        open_ports = []
        for port in range(21, 30):
            banner = self.banner_grab(ip, port)
            if banner:
                open_ports.append((port, banner))
        return open_ports

    def main(self):
        parser = argparse.ArgumentParser("Extract Service and Version information")
        parser.add_argument("ip", type=str, help="Target IP address")
        args = parser.parse_args()
        target_ip = socket.gethostbyname(args.ip)  
        print(" ")
        print("-" * 50)
        print("Scanning Target : " + target_ip)
        print("Scanning started at : " + str(datetime.now()))
        print('-' * 50)
        
        # Instantiate PortScanner and call scan_ports method
        open_ports = self.scan_ports(target_ip)
        print("\n")
        if open_ports:
            for port, banner in open_ports:
                if banner == "HEAD / HTTP/1.1":
                    continue
                else:
                    print(f"\033[1;31m{port}" + "    " + f"\033[0;32m{banner}")
                    cv = cvemitre(banner)  # Instantiate cvemitre object with banner as argument
                    cv.getvuln()  # Call the getvuln() method
                    print()
        else:
            print("No open Ports found")

if __name__ == "__main__":
    scanner = PortScanner()
    scanner.main()

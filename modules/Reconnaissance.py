import requests
import socket



class  Reconnaissance:
    def __init__(self):
        self.target = input("Enter Target:")
    def reverse_dns(self):
        self.rdnsapi=f"https://api.hackertarget.com/reversedns/?q={self.target}"
        response = requests.get(self.rdnsapi)
        print(response.text)
        with open("result.txt",'w') as f:
            f.writelines("################################### Reverse DNS ###################################\n\n")
            f.writelines(response.text )
        f.close()

    def dnslookup(self):
        self.dnsapi=f"https://api.hackertarget.com/dnslookup/?q={self.target}"
        response = requests.get(self.dnsapi)
        print(response.text)
    def hostsearch(self):
        self.hostsearchapi=f"https://api.hackertarget.com/hostsearch/?q={self.target}"
        response = requests.get(self.hostsearchapi)
        print(response.text)
        with open("result.txt",'a') as f:
            f.writelines("\n\n################################### Host Search ###################################\n\n")
            f.writelines(response.text)
        f.close()
    def zonetransfer(self):
            self.hostsearchapi=f"https://api.hackertarget.com/zonetransfer/?q={self.target}"
            response = requests.get(self.hostsearchapi)
            print(response.text)
            with open("result.txt",'a') as f:
                f.writelines("\n\n################################### Zone Transfer ###################################\n\n")
                f.writelines(response.text)
            f.close()
    def reverselookupip(self):
            self.hostsearchapi=f"https://api.hackertarget.com/reverseiplookup/?q={self.target}"
            response = requests.get(self.hostsearchapi)
            print(response.text)
            with open("result.txt",'a') as f:
                f.writelines("\n\n################################### Reverse DNS Lookup ###################################\n\n")
                f.writelines(response.text)
            f.close()

if __name__ == "__main__":
    recon = Reconnaissance()
    recon.reverse_dns()
    # recon.hostsearch()
    recon.zonetransfer()
    recon.reverselookupip()

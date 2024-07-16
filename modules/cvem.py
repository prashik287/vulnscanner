import requests
import pandas as pd
from bs4 import BeautifulSoup
from colorama import Fore

# Get data from cve mitre


class cvemitre:
    def __init__(self,service):
        self.titles=[]
        self.datas=[]
        self.service = service
    def getvuln(self):
        try:
            result=requests.get(f"https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword={self.service}")
            # print(result.content)
            soup = BeautifulSoup(result.text,features="html.parser")
            table = soup.find("div",id="TableWithRules")
            # print(table)
            cekk = table.find_all("th")
            # print(cekk)
            epp = table.find_all("td")

            for i in cekk:
                title = i.text
                self.titles.append(title)
            # print(titles)
            for i, d in enumerate(epp):
                # Assuming d is an object with a 'text' attribute or method
                data = d.text  # Assuming d.text gives you the text content of d
                self.datas.append(data)
            print(Fore.RED+ self.datas[0]+" : "+ Fore.WHITE + self.datas[1])
        except IndexError as i:
            print("\n\nNo vulnerability Found")
            for i in self.datas:
                print(i)
            # # print(datas)
            # df = pd.DataFrame(columns=titles)
            # # lent = len(datas)
            # print(df)
        
                
            # with open("test.txt",'w') as f:
            #     f.write(str(datas))
            # print(df)
        except Warning as w :
            print(w)
        except Exception as e :
            print(e)



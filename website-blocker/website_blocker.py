import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path="C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.pudelek.pl"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day+1,16):
        print("pracuj")
        with open(hosts_path,'r+') as file:
            content=file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect +" "+ website + "\n")

    else:

        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0) # ustawiamy początek nadpisania na 0 linię
            for line in content:
                if not any(website in line for website in website_list): #szukamy website po kolei w hosts porównując website w website_list
                    file.write(line) #wypisujemy linie nie zawierające website
                file.truncate() #obcina wszystko poniżej

        print("fun fun fun")
    time.sleep(5)

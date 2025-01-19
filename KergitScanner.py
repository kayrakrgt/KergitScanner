import requests , colorama , json , os , socket , urllib3 , requests
from colorama import init ,  Fore

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


init()

banner = """


██╗  ██╗██████╗  ██████╗████████╗███████╗ ██████╗ █████╗ ███╗   ██╗
██║ ██╔╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝██╔══██╗████╗  ██║
█████╔╝ ██████╔╝██║  ███╗  ██║   ███████╗██║     ███████║██╔██╗ ██║
██╔═██╗ ██╔══██╗██║   ██║  ██║   ╚════██║██║     ██╔══██║██║╚██╗██║
██║  ██╗██║  ██║╚██████╔╝  ██║   ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                   


"""

print(Fore.GREEN + banner)

hostname = input("Host name giriniz>>>")
hostip = socket.gethostbyname(hostname)

with open("data.json","r")as dosya:
  veri = json.load(dosya)

for key, value in veri.items():
  try:
   port = int(key)
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   s.settimeout(5)
   s.connect((hostip,port))
   print(f"PORT = {key}"+"         "+"DURUM = AÇIK"+"         "+f" AD = {value}")
   s.close()
  except socket.error:
    print("port kapalı")




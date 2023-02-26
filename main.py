import cowsay
from urllib.request import urlopen

ip = str(urlopen("http://checkip.amazonaws.com/").read())

cope = True
while cope == True:
    print(cowsay.cow(ip))

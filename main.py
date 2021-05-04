import cryptocompare
import socket
import whois
import os
while True:
    print(" ** Which one Do you want?")
    print("\n ** 1.My IP     **")
    print(" ** 2.BTC Price **")
    print(" ** 3.Whois     **")
    print(" ** 0.Exit      **")
    men = int(input(" ))=>> "))
    if men == 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print(" ** Your ip :",s.getsockname()[0])
        s.close()
    elif men == 2:
        btc = cryptocompare.get_price('BTC',currency='USD')["BTC"]["USD"]
        print(" ** Price =",btc,"$")
    elif men == 3:
        print(" ** Enter the website :")
        site = input(" ))=>> ")
        w = whois.whois(site)
        print(w)
    elif men == 0:
        break;
    ose = input("\n\n\t** Enter a key to exit .")
    os.system("cls")


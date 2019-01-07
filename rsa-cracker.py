#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#                      PYTHON UTILITY FILE TO CRACK WEAK RSA KEYS
#                BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Load any required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import sys
import binascii
import os.path

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Create a main menu system.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

menu = {}
menu['(1)']="Encrypt Plaintext File."
menu['(2)']="Create Private.pem."
menu['(3)']="Decrypt File."
menu['(4)']="Crack RSA-Xml."
menu['(5)']="View Message."
menu['(6)']="Exit."

while True: 
    os.system("clear")

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Display a universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

    print " ____  ____    _       ____ ____      _    ____ _  _______ ____   "
    print "|  _ \/ ___|  / \     / ___|  _ \    / \  / ___| |/ / ____|  _ \  "
    print "| |_) \___ \ / _ \   | |   | |_) |  / _ \| |   | ' /|  _| | |_) | "
    print "|  _ < ___) / ___ \  | |___|  _ <  / ___ \ |___| . \| |___|  _ <  "
    print "|_| \_\____/_/   \_\  \____|_| \_\/_/   \_\____|_|\_\_____|_| \_\ "
    print "                                                                  "
    print "      BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)       "
    print "\n"

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Display the status of the system files and create any missing files.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

    print "Public RSA  (weak) [",
    if os.path.exists('./key.pub'):
        print "  key.pub   ]",
    else:
        os.system("echo -----BEGIN PUBLIC KEY----- > key.pub")
        os.system("echo MIIBHzANBgkqhkiG9w0BAQEFAAOCAQwAMIIBBwKBgQMwO3kPsUnaNAbUlaubn7ip >> key.pub")
        os.system("echo 4pNEXjvUOxjvLwUhtybr6Ng4undLtSQPCPf7ygoUKh1KYeqXMpTmhKjRos3xioTy >> key.pub")
        os.system("echo 23CZuOl3WIsLiRKSVYyqBc9d8rxjNMXuUIOiNO38ealcR4p44zfHI66INPuKmTG3 >> key.pub")
        os.system("echo RQP/6p5hv1PYcWmErEeDewKBgGEXxgRIsTlFGrW2C2JXoSvakMCWD60eAH0W2PpD >> key.pub")
        os.system("echo qlqqOFD8JA5UFK0roQkOjhLWSVu8c6DLpWJQQlXHPqP702qIg/gx2o0bm4EzrCEJ >> key.pub")
        os.system("echo 4gYo6Ax+U7q6TOWhQpiBHnC0ojE8kUoqMhfALpUaruTJ6zmj8IA1e1M6bMqVF8sr >> key.pub")
        os.system("echo lb/N >> key.pub")
        os.system("echo -----END PUBLIC KEY----- >> key.pub")
        print "  key.pub   ]",

    print "\tPlaintext  [",
    if os.path.exists('./text.txt'):
        print "text.txt ]"
    else:
        os.system("echo Too many secrets... > text.txt")
        print "text.txt ]"

    print "Private RSA (fake) [",
    if  os.path.exists('private.pem'):
        print "private.pem ]",
    else:
        print "            ]",

    print "\tCyphertext [",
    if os.path.exists('text.enc'):
        print "text.enc ]"
    else:
        print "         ]"    

    print "XML RSA (crafted)  [",
    if os.path.exists('rsa.xml'):
        print "  rsa.xml   ]",
    else:
        print "            ]",
 
    print "\tPlaintext  [",
    if os.path.exists('text.dec'):
        print "text.dec ]\n"
    else:
        print "         ]\n" 

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu controller.   
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

    options=menu.keys()
    options.sort()
    for entry in options: 
        print entry, menu[entry]
    selection=raw_input("\nPlease Select: ")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option selected - Encrypt text.txt, output to text.enc
# Modified: N/A
# -------------------------------------------------------------------------------------

    if selection =='1':
        os.system("openssl rsautl -encrypt -inkey key.pub -pubin -in text.txt -out text.enc")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option selected - Create private.pem from key.pub
# Modified: N/A
# -------------------------------------------------------------------------------------

    if selection =='2':
        os.system("python ./RsaCtfTool/RsaCtfTool.py --publickey key.pub --private > private.pem")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Menu option selected - Decrypt text.enc, output to decrypted.txt
# Modified: N/A
# -------------------------------------------------------------------------------------

    if selection =='3':
        os.system("openssl rsautl -decrypt -inkey private.pem -in text.enc -out text.dec")
#       os.system("python ./RsaCtfTool/RsaCtfTool.py --publickey key.pub --uncipherfile text.enc > text.dec")

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - Crack RSA XML via known required parameters.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

    if selection =='4':
        print "                           Required\n"
        print "<Message>...</Message>      [yes]\n"
        print "<RSAKeyValue>"
        print "   <Modulus></Modulus>      [no] "
        print "   <Exponent></Exponent>         "
        print "   <P>...</P>               [yes]" 
        print "   <Q>...</Q>               [yes]"
        print "   <DP>...</DP>             [yes]"
        print "   <DQ>...</DQ>             [yes]"
        print "   <InverseQ></InverseQ>    [calculated]" 
        print "   <D></D>                  [no] "
        print "</RSAKeyValue>"

        c = 62078086677416686867183857957350338314446280912673392448065026850212685326551183962056495964579782325302082054393933682265772802750887293602432512967994805549965020916953644635965916607925335639027579187435180607475963322465417758959002385451863122106487834784688029167720175128082066670945625067803812970871
        p = 7901324502264899236349230781143813838831920474669364339844939631481665770635584819958931021644265960578585153616742963330195946431321644921572803658406281
        q = 12802918451444044622583757703752066118180068668479378778928741088302355425977192996799623998720429594346778865275391307730988819243843851683079000293815051
        dp = 5540655028622021934429306287937775291955623308965208384582009857376053583575510784169616065113641391169613969813652523507421157045377898542386933198269451
        dq = 9066897320308834206952359399737747311983309062764178906269475847173966073567988170415839954996322314157438770225952491560052871464136163421892050057498651
        iq=0
        d=0

        iq = (1/q) % p
        m2 = pow(c, dq, q)

        message = binascii.unhexlify(format(m2, 'x')).decode()
        with open('text.dec', 'w') as the_file:
            the_file.write(message)

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Menu option selected - View Message.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '5': 
        if os.path.exists('./text.dec'):
            os.system("strings text.dec")
            raw_input("System Message    : Press any key to continue...")
        else:
            print "The message has not been decoded yet..."
            raw_input("System Message    : Press any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Menu option selected - Quit program.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '6': 
        break

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Catch all other entries.
# Modified: N/A
# -------------------------------------------------------------------------------------

    else:
        print ""

#Eof


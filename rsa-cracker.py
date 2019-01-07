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
import os.path
import binascii
import linecache
import re

testfile = 0

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
menu['(4)']="Crack RSA-xml."
menu['(5)']="View Message."
menu['(6)']="Clean Files and Exit."

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

    print "xml RSA (crafted)  [",
    if os.path.exists('rsa.xml'):
        print "  rsa.xml   ]",
    else:
        print "            ]",
 
    print "\tPlaintext  [",
    if ((os.path.exists('text.dec')) and testfile == 1):
        print "text.dec ]\n"
    elif ((os.path.exists('xml.dec')) and testfile == 2):
            print "xml.dec  ]\n"   
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
        testfile = 1

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Menu option selected - Crack RSA xml via known required parameters.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

    if selection =='4':
        c = open("rsa.enc", "r").readlines()[0].rstrip()
        p = open("rsa.xml", "r").readlines()[3].rstrip()
        q = open("rsa.xml", "r").readlines()[4].rstrip()
        dp = open("rsa.xml", "r").readlines()[5].rstrip()
        dq = open("rsa.xml", "r").readlines()[6].rstrip()

        c = int(c)
        p = re.search('<P>(.*)</P>', p)
        p = int(p.group(1))
        q = re.search('<Q>(.*)</Q>', q)
        q = int(q.group(1))
        dp = re.search('<DP>(.*)</DP>', dp)
        dp = int(dp.group(1))
        dq = re.search('<DQ>(.*)</DQ>', dq)
        dq = int(dq.group(1))
           
        iq = (1/q) % p
        m2 = pow(c, dq, q)

        message = binascii.unhexlify(format(m2, 'x')).decode()
        with open('xml.dec', 'w') as the_file:
            the_file.write(message)
        testfile = 2

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Menu option selected - View Message.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '5': 
        print ""
        if ((os.path.exists('text.dec')) and testfile == 1):
            os.system("strings text.dec")
        elif ((os.path.exists('xml.dec')) and testfile == 2):
            os.system("strings xml.dec")
        else:
            print "No cyphertext has been decrypted yet!!..."
        raw_input("Press any key to continue...")
        
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Menu option selected - Clean the system.
# Modified: N/A
# -------------------------------------------------------------------------------------

    elif selection == '6':
        if os.path.exists('text.txt'):
            os.remove('text.txt')
        if os.path.exists('text.enc'):
            os.remove('text.enc')
        if os.path.exists('text.dec'):
            os.remove('text.dec')
        if os.path.exists('xml.dec'):
            os.remove('xml.dec')
        if os.path.exists('key.pub'):
            os.remove('key.pub')
        if os.path.exists('private.pem'):
            os.remove('private.pem')
        testfile = 0
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


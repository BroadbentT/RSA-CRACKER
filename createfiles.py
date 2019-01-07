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

banner = "banner"
argvment = len(sys.argv)
if argvment >= 1:
    banner = sys.argv[1]

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Display a universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if banner == "nobanner":
    print "\n"
else:
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
# Details : Create the plaintext file and the weak .pub key file.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

os.system("echo Too many secrets... > text.txt")

with open('key.pub', 'w') as the_file:
    the_file.write("-----BEGIN PUBLIC KEY-----\n")
    the_file.write("MIIBHzANBgkqhkiG9w0BAQEFAAOCAQwAMIIBBwKBgQMwO3kPsUnaNAbUlaubn7ip\n")
    the_file.write("4pNEXjvUOxjvLwUhtybr6Ng4undLtSQPCPf7ygoUKh1KYeqXMpTmhKjRos3xioTy\n")
    the_file.write("23CZuOl3WIsLiRKSVYyqBc9d8rxjNMXuUIOiNO38ealcR4p44zfHI66INPuKmTG3\n")
    the_file.write("RQP/6p5hv1PYcWmErEeDewKBgGEXxgRIsTlFGrW2C2JXoSvakMCWD60eAH0W2PpD\n")
    the_file.write("qlqqOFD8JA5UFK0roQkOjhLWSVu8c6DLpWJQQlXHPqP702qIg/gx2o0bm4EzrCEJ\n")
    the_file.write("4gYo6Ax+U7q6TOWhQpiBHnC0ojE8kUoqMhfALpUaruTJ6zmj8IA1e1M6bMqVF8sr\n")
    the_file.write("lb/N\n")
    the_file.write("-----END PUBLIC KEY-----\n")

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0                                                                
# Details : Create the RSA xml file and its associated encrypted message.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

with open('rsa.xml', 'w') as the_file:
    the_file.write("<RSAKeyValue>\n")
    the_file.write("   <Modulus></Modulus>\n")
    the_file.write("   <Exponent></Exponent>\n")
    the_file.write("   <P>7901324502264899236349230781143813838831920474669364339844939631481665770635584819958931021644265960578585153616742963330195946431321644921572803658406281</P>\n")
    the_file.write("   <Q>12802918451444044622583757703752066118180068668479378778928741088302355425977192996799623998720429594346778865275391307730988819243843851683079000293815051</Q>\n")
    the_file.write("   <DP>5540655028622021934429306287937775291955623308965208384582009857376053583575510784169616065113641391169613969813652523507421157045377898542386933198269451</DP>\n")
    the_file.write("   <DQ>9066897320308834206952359399737747311983309062764178906269475847173966073567988170415839954996322314157438770225952491560052871464136163421892050057498651</DQ>\n")
    the_file.write("   <InverseQ></InverseQ>\n")
    the_file.write("   <D></D>\n")
    the_file.write("</RSAKeyValue>\n")

os.system("echo 62078086677416686867183857957350338314446280912673392448065026850212685326551183962056495964579782325302082054393933682265772802750887293602432512967994805549965020916953644635965916607925335639027579187435180607475963322465417758959002385451863122106487834784688029167720175128082066670945625067803812970871 > rsa.enc")

if banner != "nobanner":
    os.system("ls -I createfiles.py -I rsa-cracker.py -I RsaCtfTool")

#Eof


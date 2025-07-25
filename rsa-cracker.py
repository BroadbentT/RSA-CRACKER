#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#                      PYTHON UTILITY FILE TO CRACK WEAK RSA KEYS
#                BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 3.0                                                                
# Details : Load any required imports.
# Modified: N/A
# -------------------------------------------------------------------------------------

import os
import re
import sys
import os.path
import binascii
import linecache

from termcolor import colored

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 3.0
# Details : Ccheck required installation files used by this utility are present.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if len(sys.argv) < 2:
   blackHat = 0
else:
   blackHat = 1

if os.path.exists('createfiles.py'):
    pass
else:
    print("File createfiles.py is missing...")
    exit(True)
   
# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 3.0
# Details : Define system display colours.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------
   
colour0 = "red"	
colour1 = "grey"
colour2 = "cyan"
colour3 = "blue"
colour4 = "black"
colour5 = "white"
colour6 = "green"
colour7 = "yellow"
colour8 = "magenta"

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 3.0                                                                
# Details : Create function to display my universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

def header():
   os.system("clear")
   print(colored("\t\t\t\t\t\t\t ____  ____    _       ____ ____      _    ____ _  _______ ____   ", colour0))
   print(colored("\t\t\t\t\t\t\t|  _ \/ ___|  / \     / ___|  _ \    / \  / ___| |/ / ____|  _ \  ", colour0))
   print(colored("\t\t\t\t\t\t\t| |_) \___ \ / _ \   | |   | |_) |  / _ \| |   | ' /|  _| | |_) | ", colour0))
   print(colored("\t\t\t\t\t\t\t|  _ < ___) / ___ \  | |___|  _ <  / ___ \ |___| . \| |___|  _ <  ", colour0))
   print(colored("\t\t\t\t\t\t\t|_| \_\____/_/   \_\  \____|_| \_\/_/   \_\____|_|\_\_____|_| \_\ ", colour0))
   print(colored("\t\t\t\t\t\t\t                                                                  ", colour0))
   print(colored("\t\t\t\t\t\t\t      BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)     \n", colour7,attrs=['bold']))

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 3.0                                                                
# Details : Create function to display the status of the system files to the user.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

def system():
   print("Public RSA Key [", end=' ')
   if os.path.exists('./weak_rsa.pub'):
      print(colored("weak_rsa.pub", colour6), end=' ')
      print("]",end=' ')
   else:
      print("             ]", end=' ')

   print("\tCrafted RSA (.xml) [", end=' ')
   if os.path.exists('weak_rsa.xml'):
      print(colored("weak_rsa.xml", colour6), end=' ')
      print("]")
   else:
      print("             ]")
      
   print("Plaintext file [", end=' ')
   if os.path.exists('./plain1.txt'):
      print(colored("plain1.txt  ", colour6), end=' ')
      print("]", end=' ')
   else:
      print("             ]", end=' ')
      
   print("\tEncrypted text     [", end=' ')
   if os.path.exists('text1.enc'):
      print(colored("text1.enc   ", colour3), end=' ')
      print("]", end=' ')
   else:
      print("             ]", end=' ')       
      
   print("\t\tDecrypted text [", end=' ')
   if os.path.exists('text.dec'):
      print(colored("text.dec", colour2), end=' ')
      print("]")
   else:
      print("         ]")  
      
   print("Plaintext XML  [", end=' ')
   if os.path.exists('./plain2.txt'):
      print(colored("plain2.txt  ", colour6), end=' ')
      print("]", end=' ')
   else:
      print("             ]", end=' ')
      
   print("\tEncrypted text     [", end=' ')
   if os.path.exists('xml_rsa.enc'):
      print(colored("xml_rsa.enc ", colour3), end=' ')
      print("]", end=' ')
   else:
      print("             ]", end=' ')     

   print("\t\tDecrypted text [", end=' ')
   if os.path.exists('_xml.dec'):
      print(colored("_xml.dec", colour2), end=' ')   
      print("]")
   else:
      print("         ]") 
      
   print("Private RSA!!! [", end=' ')
   if  os.path.exists('private.pem'):
      print(colored("private.pem ", colour7,attrs=['blink']), end=' ')
      print("]\n")
   else:
      print("             ]\n") 

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 3.0
# Details : Create the main menu system.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

def menu():
   print("(01) Build required files.	(04) View weak RSA .pub file.	(07) Read RSA plaintext file.	(09) Encrypt plain1.txt.    (10) Decrypt text file.	(12) Read decrypted text.dec.")
   print("(02) Build fake PEM  file.	(05) View weak RSA .xml file.	(08) Read XML plaintext file.	                            (11) Crack .xml text file.	(13) Read decrypted _xml.dec.")
   print("(03) Clean files and exit.	(06) View fake RSA .pem file.")
   if blackHat == 1:
      print(colored("\nBLACK HAT >>>", colour7), end=' ')
      print("			(14) Load weak RSA .pub file.	(15) Load Encrypted textfile.")
   return

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 3.0
# Details : Main Controller.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

while True: 
   header()
   system()
   menu()
   selection=input("\nPlease Select: ")
   
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 3.0
# Details : Menu option selected - Run createfiles.py
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='1':
      os.system("python3 createfiles.py")
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 3.0
# Details : Menu option selected - Create private.pem from key.pub
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection =='2':
      if os.path.exists('./weak_rsa.pub'):
         print("\nUsing wiener attack - https://github.com/sourcekris/RsaCtfTool.")
         os.system("RsaCtfTool --publickey ./weak_rsa.pub --private --output private.pem # --attack wiener")
      else:
         print("\nWeak_rsa_key file has not been created yet...")
      input("\nPress any key to continue...")
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 3.0
# Details : Menu option selected - Clean up the system files.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '3':
      if os.path.exists('plain1.txt'):
         os.remove('plain1.txt')
      if os.path.exists('plain2.txt'):
         os.remove('plain2.txt')
      if os.path.exists('text1.enc'):
         os.remove('text1.enc')
      if os.path.exists('text.dec'):
         os.remove('text.dec')
      if os.path.exists('_xml.dec'):
         os.remove('_xml.dec')
      if os.path.exists('weak_rsa.pub'):
         os.remove('weak_rsa.pub')
      if os.path.exists('private.pem'):
         os.remove('private.pem')
      if os.path.exists('xml_rsa.enc'):
         os.remove('xml_rsa.enc')
      if os.path.exists('weak_rsa.xml'):
         os.remove('weak_rsa.xml')
      exit(True)
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 3.0
# Details : Menu option selected - View the weak RSA file.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '4': 
      print("")
      if os.path.exists('weak_rsa.pub'):
         os.system("cat weak_rsa.pub")
      else:
         print("File does not exist yet...")
      input("\nPress any key to continue...")
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 3.0
# Details : Menu option selected - View weak .xml file.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '5': 
      print("")
      if os.path.exists('weak_rsa.xml'):
         os.system("cat weak_rsa.xml")
      else:
         print("File does not exist yet.")
      input("\nPress any key to continue...")

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 3.0
# Details : Menu option selected - View newly created private.pem file.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '6': 
      print("")
      if os.path.exists('private.pem'):
         os.system("cat private.pem")
      else:
         print("File does not exist yet.")
      input("\nPress any key to continue...")
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 3.0
# Details : Menu option selected - Show plaintext file.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='7':
      print ("")
      if os.path.exists('./plain1.txt'):
         os.system("cat plain1.txt")
      else:
         print("\nPlaintext files have not been created yet...")
      input("\nPress any key to continue...")
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 3.0
# Details : Menu option selected - Show plaintext file.
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='8':
      print("")
      if os.path.exists('./plain2.txt'):
         os.system("cat plain2.txt")
      else:
         print("\nPlaintext files have not been created yet...")
      input("\nPress any key to continue...")
          
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 3.0
# Details : Menu option selected - Encrypt text.txt, output to text1.enc
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='9':
      if os.path.exists('plain1.txt'):
         os.system("openssl pkeyutl -encrypt -inkey weak_rsa.pub -pubin -in plain1.txt -out text1.enc")
         print("\nFile encrypted.")
      else:
         print("\nPlaintext file has not been created yet...")
      input("\nPress any key to continue...")
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 3.0
# Details : Menu option selected - Decrypt text1.enc, output to decrypted.txt
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection =='10':
      if os.path.exists('text1.enc'):
         if os.path.exists('private.pem'):
            os.system("openssl pkeyutl -decrypt -inkey private.pem -in text1.enc -out text.dec")
#           os.system("RsaCtfTool --publickey key.pub --uncipherfile text1.enc > text.dec")
            print("\nFile successfuly decrypted.")
         else:
            print("\nThe private.pem file has not been created yet.")         
      else:
         print("\nThe plaintext has not been encrypted yet.")
      input("\nPress any key to continue...")

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 3.0                                                                
# Details : Menu option selected - Crack RSA .xml file via known required parameters.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

   elif selection =='11':
      print("\nUsing chinese remainder theorem - https://kconrad.math.uconn.edu/blurbs/ugradnumthy/crt.pdf.")
    
      c = open("xml_rsa.enc", "r").readlines()[0].rstrip()
      p = open("weak_rsa.xml", "r").readlines()[3].rstrip()
      q = open("weak_rsa.xml", "r").readlines()[4].rstrip()
      dp = open("weak_rsa.xml", "r").readlines()[5].rstrip()
      dq = open("weak_rsa.xml", "r").readlines()[6].rstrip()

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
      with open('_xml.dec', 'w') as the_file:
         the_file.write(message)
      print("\nFile cracked.")
      input("\nPress any key to continue...")      

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 3.0
# Details : Menu option selected - View text.dec message.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '12': 
      print("")
      if os.path.exists('text.dec'):
         os.system("cat text.dec")
      else:
         print("No cyphertext has been decrypted yet!!...")
      input("\nPress any key to continue...")
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 3.0
# Details : Menu option selected - View _xml.dec message.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '13': 
      print("")
      if os.path.exists('_xml.dec'):
         os.system("cat _xml.dec")
      else:
         print("No cyphertext has been decrypted yet!!...")
      input("\n\nPress any key to continue...")
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 3.0
# Details : Menu option selected - Allocate file.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '14': 
      newFile = input("[+] Enter file name: ")
      if os.path.exists(newFile):
         os.system("cp " + newFile + " weak_rsa.pub")
         print("[*] File allocated...")
      else:
         print("[-] Sorry, I could not find that file in this directory...")
      input("\n\nPress any key to continue...")
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 3.0
# Details : Menu option selected - Allocate file.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '15': 
      newFile = input("[+] Enter file name: ")
      if os.path.exists(newFile):
         os.system("cp " + newFile + " text1.enc")
         print("[*] File allocated...")
      else:
         print("[-] Sorry, I could not find that file in this directory...")
      input("\n\nPress any key to continue...")
  
#Eof


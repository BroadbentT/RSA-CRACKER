#!/usr/bin/python
# coding:UTF-8

# -------------------------------------------------------------------------------------
#                      PYTHON UTILITY FILE TO CRACK WEAK RSA KEYS
#                BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)
# -------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
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
# Version : 1.0
# Details : Create the system files and check installation the used by this utility.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

if os.path.exists('createfiles.py'):
    os.system("python createfiles.py")
else:
    print("File createfiles.py is missing...")
    exit(True)

if os.path.exists('RsaCtfTool'):
   requiredfiles = 1
else:
   print("RsaCtfTool's is missing in this directory...")
   exit(True)
   
# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Define the system display colours.
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
# Version : 2.0                                                                
# Details : Create function to display my universal header.    
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

def header():
   os.system("clear")
   print(colored("\t\t ____  ____    _       ____ ____      _    ____ _  _______ ____   ", colour0))
   print(colored("\t\t|  _ \/ ___|  / \     / ___|  _ \    / \  / ___| |/ / ____|  _ \  ", colour0))
   print(colored("\t\t| |_) \___ \ / _ \   | |   | |_) |  / _ \| |   | ' /|  _| | |_) | ", colour0))
   print(colored("\t\t|  _ < ___) / ___ \  | |___|  _ <  / ___ \ |___| . \| |___|  _ <  ", colour0))
   print(colored("\t\t|_| \_\____/_/   \_\  \____|_| \_\/_/   \_\____|_|\_\_____|_| \_\ ", colour0))
   print(colored("\t\t                                                                  ", colour0))
   print(colored("\t\t      BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)     \n", colour7,attrs=['bold']))

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Create function to display the status of the system files to the user.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

def system():
   print("Public RSA Key [", end=' ')
   if os.path.exists('./weak_rsa_key.pub'):
      print(colored("weak_rsa_key.pub ]", colour6), end=' ')
   else:
      print("                 ]", end=' ')

   print("Crafted RSA (.xml) [", end=' ')
   if os.path.exists('weak_rsa.xml'):
      print(colored("weak_rsa.xml]", colour6))
   else:
      print("            ]")
      
   print("Plaintext file [", end=' ')
   if os.path.exists('./plain1.txt'):
      print(colored("plain1.txt       ]", colour6), end=' ')
   else:
      print("                 ]", end=' ')
      
   print("Encrypted text     [", end=' ')
   if os.path.exists('text.enc'):
      print(colored("text1.enc   ]", colour3), end=' ')
   else:
      print("            ]", end=' ')       
      
   print("Decrypted text [", end=' ')
   if os.path.exists('text.dec'):
      print(colored("text.dec ]", colour2))
   else:
      print("         ]")  
      
   print("Plaintext XML  [", end=' ')
   if os.path.exists('./plain2.txt'):
      print(colored("plain2.txt       ]", colour6), end=' ')
   else:
      print("                 ]", end=' ')
      
   print("Encrypted text     [", end=' ')
   if os.path.exists('xml_rsa.enc'):
      print(colored("xml_rsa.enc ]", colour3), end=' ')
   else:
      print("            ]", end=' ')     

   print("Decrypted text [", end=' ')
   if os.path.exists('xml.dec'):
      print(colored("xml.dec  ]", colour2))   
   else:
      print("         ]") 
      
   print("Private RSA!!! [", end=' ')
   if  os.path.exists('private.pem'):
      print(colored("private.pem      ]\n", colour7,attrs=['bold']))
   else:
      print("                 ]\n") 

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Create the main menu system.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

def menu():
   print('(01) Create required files.')
   print('(02) Read both plaintext files.')
   print('(03) Encrypt plaintext file.')
   print('(04) Create private.pem.')
   print('(05) Crack plaintext file.')
   print('(06) Crack RSA-xml file.')
   print('(07) View decrypted plaintext message.')
   print('(08) View decrypted xml text message.')
   print('(09) View weak RSA key file.')
   print('(10) View fake private pem file.')
   print('(11) Clean files and exit.')
   return

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
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
# Version : 1.0
# Details : Menu option selected - Run createfiles.py
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='1':
      os.system("python3 createfiles.py")
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option selected 
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='2':
      if os.path.exists('./plain1.txt'):
         print("\nPlaintext file: ", end =' ')
         os.system("strings plain1.txt")
         print("\nXMl Plaintext : ", end=' ')
         os.system("strings plain2.txt")
      else:
         print("\nPlaintext files have not been created yet...")
      input("\nPress any key to continue...")
          
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option selected - Encrypt text.txt, output to text.enc
# Modified: N/A
# -------------------------------------------------------------------------------------

   if selection =='3':
      if os.path.exists('plain1.txt'):
         os.system("openssl pkeyutl -encrypt -inkey weak_rsa_key.pub -pubin -in plain1.txt -out text.enc")
         print("\nFile encrypted.")
      else:
         print("\nPlaintext file has not been created yet...")
      input("\nPress any key to continue...")
          
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 1.0
# Details : Menu option selected - Create private.pem from key.pub
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection =='4':
      if os.path.exists('./weak_rsa_key.pub'):
         os.system("python3 ./RsaCtfTool/RsaCtfTool.py --publickey ./weak_rsa_key.pub --private --output private.pem --attack wiener")
      else:
         print("\nWeak_rsa_key file has not been created yet...")
      input("\nPress any key to continue...")
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Menu option selected - Decrypt text.enc, output to decrypted.txt
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection =='5':
      if os.path.exists('./private.pem'):
         os.system("openssl pkeyutl -decrypt -inkey private.pem -in text.enc -out text.dec")
         print("\nFile cracked.")
#     os.system("python ./RsaCtfTool/RsaCtfTool.py --publickey key.pub --uncipherfile text.enc > text.dec")
      else:
         print("\nPrivate file has not been created yet...")
      input("\nPress any key to continue...")

# -------------------------------------------------------------------------------------
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub
# Version : 2.0                                                                
# Details : Menu option selected - Crack RSA xml via known required parameters.
# Modified: N/A                                                               
# -------------------------------------------------------------------------------------

   elif selection =='6':
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
      with open('xml.dec', 'w') as the_file:
         the_file.write(message)
      print("\nFile cracked.")
      input("\nPress any key to continue...")      

# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Menu option selected - View Message.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '7': 
      print("")
      if os.path.exists('text.dec'):
         os.system("strings text.dec")
#      if os.path.exists('xml.dec'):
#         os.system("strings xml.dec")
      else:
         print("No cyphertext has been decrypted yet!!...")
      input("\nPress any key to continue...")
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Menu option selected - View Message.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '8': 
      print("")
#      if os.path.exists('text.dec'):
#         os.system("strings text.dec")
      if os.path.exists('xml.dec'):
         os.system("strings xml.dec")
      else:
         print("No cyphertext has been decrypted yet!!...")
      input("\nPress any key to continue...")
      
 # ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Menu option selected - View the weak RSA file.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '9': 
      print("")
      if os.path.exists('weak_rsa_key.pub'):
         os.system("strings weak_rsa_key.pub")
      else:
         print("File does not exist yet...")
      input("\nPress any key to continue...")
      
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Menu option selected - View newly created private.pem file.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '10': 
      print("")
      if os.path.exists('private.pem'):
         os.system("strings private.pem")
      else:
         print("File does not exist yet.")
      input("\nPress any key to continue...")
        
# ------------------------------------------------------------------------------------- 
# AUTHOR  : Terence Broadbent                                                    
# CONTRACT: GitHub                                                               
# Version : 1.0
# Details : Menu option selected - Clean up the system files.
# Modified: N/A
# -------------------------------------------------------------------------------------

   elif selection == '11':
      if os.path.exists('plain1.txt'):
         os.remove('plain1.txt')
      if os.path.exists('plain2.txt'):
         os.remove('plain2.txt')
      if os.path.exists('text.enc'):
         os.remove('text.enc')
      if os.path.exists('text.dec'):
         os.remove('text.dec')
      if os.path.exists('xml.dec'):
         os.remove('xml.dec')
      if os.path.exists('weak_rsa_key.pub'):
         os.remove('weak_rsa_key.pub')
      if os.path.exists('private.pem'):
         os.remove('private.pem')
      if os.path.exists('xml_rsa.enc'):
         os.remove('xml_rsa.enc')
      if os.path.exists('weak_rsa.xml'):
         os.remove('weak_rsa.xml')
      exit(True)

#Eof


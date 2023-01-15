# pwd.py
from getpass import getpass
from colorama import Fore,Back
import time
import pwinput as pin
import socket
import socketserver
import serial
import string
from int import is_prime
def password_one1():
    Pwd = getpass("passwrod generalter: ")
    print("You type generalti on password: ",Pwd)
def password_two2():
    Pwd_two=pin.pwinput('Tru: ')
    print(r"password_two")
#[password_one1] and [pasword_two2]
#password_one1
#pasword_two2
time.sleep(3)

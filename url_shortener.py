import pyshorteners
import pyfiglet
from os import system, name
from time import sleep
def sleep_function():
    sleep(5)
def long_line():
    print("   =====================================================================================")
def banner_for_url():
    long_line()
    ascii_banner = pyfiglet.figlet_format("      SHORT_URL")

    print(ascii_banner)
    print("                                      Aurthor---->Sajawal Khan Sadozai")
    long_line()
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
sleep_function()
clear()
def beauty_line():
    print("===============================")
def orignal_code():
    clear()
    print("LINK SHORTNER STARTS PLEASE WAIT.....")
    sleep_function()
    clear()
    banner_for_url()
    enter_link=str(input("Enter the link : "))
    short=pyshorteners.Shortener()
    a=short.tinyurl.short(enter_link)
    print()
    print()
    sleep_function()
    print("process complete...")
    sleep_function()
    print("Done...")
    sleep_function()
    print()
    print()
    print("Here is your short link")
    beauty_line()
    print(a)
    beauty_line()
orignal_code()
from random import choice
from constants import *
import constants

def main():
    print(constants.helper.Logo()) 
    print(constants.helper.Menu())
    choice = input("\nChoose an option: ")
    if choice == "1":
        pass
    if choice == "2":
        print("2")
    if choice == "3":
        constants.helper.makeConfig()
        main()
    if choice == "4":
        print("4")
    if choice == "5":
        print("5")
    if choice == "6":
        print("6")
    if choice == "7":
        print("7")
    if choice == "8":
        constants.helper.downloadData()
    if choice == "9":
        print("9")
    if choice == "10":
        exit()

if __name__ == '__main__':
    main()
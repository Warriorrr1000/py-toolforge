import Tools.password_generator as pg 
import Tools.word_counter as wc
import Tools.file_organizer as fg
import Tools.system_info as si
import Tools.text_formatter as tf
import sys

def main():
    while True:
        print("""
==== PYTHON TOOLKIT ====
1. Password Generator
2. Word Counter
3. File Organizer
4. System Info
5. Text Formatter
6. Exit
""")
        try:
            choice = int(input("Enter the number associated with following option: \n"))
            if choice == 1:
                print("Password Generator \n")
                pg.main()
            elif choice == 2:
                print("Word Counter \n")
                wc.main()
            elif choice == 3:
                print("File Organizer \n")
                fg.main()
            elif choice == 4:
                print("System Info \n")
                si.main()
            elif choice == 5:
                print("Text Formatter \n")
                tf.main()
            elif choice == 6:
                sys.exit("Thanks For Using.")
            else:
                print("Invalid Option. \n")
        except ValueError:
            print(f"Invalid input. Please enter a number.")
            
if __name__=="__main__":
    main()
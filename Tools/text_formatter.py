import spacy
import sys

nlp = spacy.load("en_core_web_sm")

def main():
    txt_1 = "------- Text Formatter -------"
    print(txt_1.center(80))
    txt_2 = """
    Uppercase - [1]
    Lowercase - [2]
    Remove Unwanted Spaces - [3]
    Properly Format - [4]
    Exit - [5]
    """
    print(txt_2)
    while True:
        try:
            user_choice = int(input("Enter the number associated with following options: "))
            if user_choice == 1:
                print(uppercase(inp()))
            elif user_choice == 2:
                print(lowercase(inp()))
            elif user_choice == 3:
                print(remove_ut_spaces(inp()))
            elif user_choice == 4:
                print(formattify(inp()))
            elif user_choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid Option.")
                
        except ValueError:
            print("The program expects an integer.")
    

def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()

def remove_ut_spaces(text): #Removes unwanted spaces.
    words = text.split()
    return " ".join(words)

def formattify(text): #Custom Function which do all of above to format the text.
    # Step 1: remove extra spaces
    text = " ".join(text.split())
    
    doc = nlp(text)
    words = text.split()

    # Step 2: capitalize proper nouns
    for token in doc:
        if token.pos_ == "PROPN" and token.is_alpha:
            for i in range(len(words)):
                if words[i].lower() == token.text.lower():
                    words[i] = words[i].title()

    # Step 3: capitalize first word
    if words:
        words[0] = words[0].capitalize()
        
    return " ".join(words)

def inp():
    return input("Enter the text: ").strip()

if __name__=="__main__":
    main()
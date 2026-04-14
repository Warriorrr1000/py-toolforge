def main():
    user_input = input("Enter the text: ").strip()
    print(f"Characters: {characters_count(user_input)}")
    print(f"Total Words: {word_count(user_input)}")

def characters_count(text):
    return len(text)

def word_count(text):
    words = text.split()
    return len(words)

if __name__=="__main__":
    main()
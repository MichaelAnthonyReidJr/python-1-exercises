from exercises import ex4

def main():
    sentence = input("Enter a sentence: ")  
    num_words = ex4.count_words(sentence)
    print(num_words)

if __name__ == "__main__":
    main()
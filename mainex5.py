from exercises import ex5

def main():
    sentence = "Test.  This is a test.  Testing."
    sentence2 = ex5.replace_period(sentence, "!")
    print(sentence2) 

if __name__ == "__main__":
    main()
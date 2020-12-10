import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("\nDid you mean '%s' instead" %get_close_matches(word, data.keys())[0],word,"?")
        decide = input("Press 'Y' for yes or 'N' for no: ").lower()
        while(decide != "n"):
            if decide == "y":
                return data[get_close_matches(word , data.keys())[0]]
            else:
                print("\nYou have entered wrong input!")
                decide = input("Please Press only 'Y' for yes or 'N' for No: ").lower()
        else:
            return("".join(["Sorry! there is no any word like '",word,"' in this Dictionary."]))



if __name__ == "__main__":
    print("\n-------------------------------DICTIONARY---------------------------------------")
    
    print("\nIt's a Dictionary. Do you want to search any word?")
    decide = input("Press 'Y' for yes or 'N' for no: ").lower()
    while(decide != 'n'):
        if(decide != 'y'):
            print("\nYou have entered wrong input!")
            decide = input("Please Press only 'Y' for yes or 'N' for No: ").lower()
            continue
        word = input("\nEnter the word you want to search: ")
        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)
        print("--------------------------------------------------------------------------------")
        print("\nWanna to search any other word again?")
        decide = input("Press 'Y' for yes or 'N' for no: ").lower()
    print("\nThanks for using me!")
    print("Have a Nice day!")
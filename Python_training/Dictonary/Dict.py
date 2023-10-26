import json
import difflib

data = json.load(open("data.json"))

# print (data["smog"])

# x="y"
#
# while x=="y":
#     x=input("enter Y to search the word-->")
#     if x=="n":
#         exit()
# word=input("enter the word-->")
# if word in data:
#     print(data[word])
# elif word.title() in data:
#     print(data[word.title()])
# else:
#     print("no word found")
def translate(y):
    # while True:
    # y=input("enter word or EXIT to quit")

    if y in data:
        return data[y]
    elif y.capitalize() in data:  # first letter capital.
        return data[y.capitalize()]
    elif y.upper() in data:  # uppercase
        return data[y.upper()]
    elif y.lower() in data:  # lowercase
        return data[y.lower()]
    elif len(difflib.get_close_matches(y, data.keys())) > 0:
        print("did you mean %s instead?" % difflib.get_close_matches(y, data.keys())[0])
        choice=input("press Y for yes and N for no")
        if choice == "y":
            return data[difflib.get_close_matches(y, data.keys())[0]]
        elif choice == "n":
            return ("no word found")
        else:
            return ("you have entered wrong input please enter y or n")
    else:
        print("no word found")
while True:
    y = input("enter a word or EXIT to quit")
    if y == "exit":
        exit()
    else:
        # print("Enter start to Begin")
        output = translate(y)

        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)

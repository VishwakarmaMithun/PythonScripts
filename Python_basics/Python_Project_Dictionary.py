import json
import difflib
from shutil import register_unpack_format
from unittest import result
data = json.load(open(r'C:\Training\Python Practice\Python Example\Python_Project_Dictionary\data.json'))
print(data["quiz"]);

def dictionary(word):
    word  = word.lower()
    if word in data:
        return data[word];
    elif word.title() in data:
        return data[word.title()];
    elif word.upper() in data:
        return data[word.upper()];
    elif len(difflib.get_close_matches(word,data.keys()))>0:
        print("did you mean %s  "%difflib.get_close_matches(word,data.keys())[0])
        tell =input("press y for yes  or n for no")
        if tell=="y":
            return difflib.get_close_matches(word,data.keys())[0];
        elif tell=='n':
            return("error in word")
        else:
            return("no word found")
    else:
        print('word not found')


word = input("Enter Word :")
result =dictionary(word)

if type(result)==list:
    for item in result:
        print(item)
else:
    print(result)
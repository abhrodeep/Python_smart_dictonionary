import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data=json.load(open("data.json"))

def find(w):
    wch=w.lower()
    if wch in data:
        return data[wch]    
    elif len(get_close_matches(wch,data.keys()))> 0:      #x!=[]
        x=get_close_matches(wch,data.keys())   #x=get_close_matches("rainn",data.keys())[0]
        ans = input("Did you mean %s? Y or N?" % x[0])
        ans=ans.lower()
        if ans=='y':
            return data[x[0]]
        elif ans=="n":
            return "Not found! Try something else"
        else:
            return "Couldn't understand input"    
    else:
        return "Not found! Try somthing else"


word = input("Enter the word: ")
out=find(word)
if type(out) == list :
    for item in out:
        print(item)
else :
    print(out)
from queue import Empty


programming_keyword  = {
        "bug":"a bug is a coding error in a computer program.",
        "function":"Any character used to specify a function of a piece of software or hardware"
        }

#Retriving items from dictionary

print(programming_keyword["bug"])

programming_keyword['loop']=  "action is done over and over"
#Adding new items to dictionary

print(programming_keyword)

#Emptying dictionary

empty_dictionary = {}

programming_keywory = {}

print("------------------------------")
print(programming_keyword)
print("------------------------------")
print("Loop through dictionary")

for key in programming_keyword:
        print(key)
        print(programming_keyword[key])
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    pass
   
    

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
file=pandas.read_csv("python/NATO-alphabet-start/nato_phonetic_alphabet.csv")

dictionary={row.letter:row.code for(index,row) in file.iterrows()}

game_is_on=True

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while game_is_on:
    word=input("Insert a Word: ")
    letters=list(word.upper())
    result=[value for (key,value) in dictionary.items() if key in letters ]
    print(result)
    


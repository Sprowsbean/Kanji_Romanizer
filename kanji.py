import json 
    
with open('JMdict.json', 'r',encoding='utf-8') as f:
    dictionary_data = json.load(f)

words = dictionary_data.get("words",[])

## this function takes in values or items of words list ,that have that specific id, after that it print kanji text, so we get to the current item
#item with specific id 
user_input = input("Initialize a kanji: ")

for values in words:
    kanji_list = values.get("kanji", [])
    
    
    if kanji_list and user_input == kanji_list[0]["text"]:
        
        first_step = values["sense"][0]
        second_step = first_step["gloss"][0]
        eng_meaning = second_step["text"]
        
        print("Eng meaning: {}, kana: {}".format(eng_meaning, values["kana"][0]["text"]))
        break
else:
    print("This word is not in the dictionary")

    #sense , gloss , lang eng text
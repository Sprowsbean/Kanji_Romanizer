#Import dictionary kanji to romanized readings and one that evaulate to english words


#Prompt user for kanji input

#put that prompt into a list of kanji characters if user input sentence

#THe input will be force be checked by kanji dictionary to see if it exist

#If it exist, then it will be converted to romanized reading + english meaning

#return user the romanized reading + english meaning

import xml.etree.ElementTree as ET

# 1️⃣ Parse the JMdict XML
tree = ET.parse("data/JMdict.xml")
root = tree.getroot()

# 2️⃣ Build dictionary: keb -> (reb, gloss)
kanji_dict = {}

# For demo purposes, limit to first 50 entries
count = 0
MAX_ENTRIES = 50

for entry in root.findall("entry"):
    if count >= MAX_ENTRIES:
        break

    # Extract first <keb> (kanji)
    k_ele = entry.find("k_ele")
    if k_ele is None:
        continue  # skip kana-only words
    keb_elem = k_ele.find("keb")
    if keb_elem is None:
        continue
    keb = keb_elem.text

    # Extract first <reb> (reading in kana)
    r_ele = entry.find("r_ele")
    if r_ele is None:
        continue
    reb_elem = r_ele.find("reb")
    if reb_elem is None:
        continue
    reb = reb_elem.text

    # Extract first <gloss> (English meaning)
    sense = entry.find("sense")
    if sense is None:
        continue
    gloss_elem = sense.find("gloss")
    if gloss_elem is None:
        continue
    gloss = gloss_elem.text

    # Add to dictionary
    kanji_dict[keb] = (reb, gloss)
    count += 1

# 3️⃣ Prompt user for kanji input
user_input = input("Enter kanji characters: ")

# 4️⃣ Lookup and return reading + meaning
if user_input in kanji_dict:
    reading, meaning = kanji_dict[user_input]
    print(f"Reading (kana): {reading}, Meaning: {meaning}")
else:
    print("Kanji not found in dictionary.")

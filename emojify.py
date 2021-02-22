import pyperclip, string, emoji

# this is super gay but it works
remap_dict = {
    "?": "\U00002753",
    "!": "\U00002757",
    "+": "\U00002795",
    "-": "\U00002796",
    "#": "#️⃣",
    "*":"*️⃣",
    "0": "0️",
    "1": "1️⃣",
    "2": "2️⃣",
    "3": "3️⃣",
    "4": "4️⃣",
    "5": "5️⃣",
    "6": "6️⃣",
    "7": "7️⃣",
    "8": "8️⃣",
    "9": "9️⃣",
}

result = ""
while True:
    _input = input("Enter a word to emojify: ")
    if _input == "":
        continue

    # region indicator emoji are meant to be placed together to create flags, 
    # but flags are for fags so like we don't want that shit here. 
    # to avoid this, we need to put spaces in between each character
    result = (" ".join(map(lambda y : str(y),_input))).lower()

    for x in range(0,len(_input)):
        if ord(_input[x]) in range(ord('a'), ord('z')):
            # cool unicode range magic
            result = result.replace(_input[x], chr(ord(_input[x]) + 0x1F185),1)
        elif _input[x] in remap_dict:
            result = result.replace(_input[x], remap_dict[_input[x]],1)
    
    #python don't like emoji so the only option is to send it to our clipboard directly
    pyperclip.copy(emoji.emojize(result))
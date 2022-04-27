intro = input("Introduce yourself :")
characterCount = 0
wordCount = 1
for ia in intro: 
    characterCount+= 1
    if(ia == " "):
        wordCount +=1
print(characterCount)
print("Character count : " + str(characterCount))     
print(wordCount)   
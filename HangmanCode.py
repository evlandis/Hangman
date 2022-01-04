wordList = []
wordLengthList = []
readFile=open("wordsFile.txt")

for line in readFile:
    line = line.rstrip("\n")
    wordList.append(line)
    wordLength=len(line)
    wordLengthList.append(wordLength)
readFile.close()
numberOfWords = int(len(wordLengthList))

def turnIntoString(listW): 
    var = "" 
    for letter in listW: 
        var += letter  
    return var 
chosenWord=wordList[0]
chosenWordLength=wordLengthList[0]
wordSplit=list(chosenWord)

win=False
while win==False:
    spaces = int(wordLengthList[0])*"_"
    numOfGuesses = int(input("How many guesses do you want? "))
    spacesAsList=list(spaces)
    j=0
    i=0
    rightAdd=0
    while i<(numOfGuesses+rightAdd):
        print(i)
        print(numOfGuesses+rightAdd)
        print("Please guess a letter for the word ("+str(numOfGuesses+rightAdd-i)+" guesses left):", spaces)
        inputGuess = input("Guess: ")
        for j in range(int(chosenWordLength)):
            if inputGuess==chosenWord[j]:
                rightAdd+=1
                spacesAsList[j]=inputGuess
                spaces = turnIntoString(spacesAsList)
            ogWord = turnIntoString(spacesAsList)
        if ogWord == chosenWord:
            print("You've guessed correctly") 
            win=True
            break
        i+=1
    if win==False: 
        print("0 guesses left, you lost")

'''
Ismael Villalobos
6-9-19
Lab Assignment 1
Professor Fuentes
TA-Dita Nath
Purpose:
'''

import time


#Takes a file name, creates a set of words from the given file, and returns the Set
def readFile():
    try:
        wordList = set(line.strip() for line in open(r'words_alpha.txt'))
        return wordList
    #Prints Error message if the file cannot be found
    except IOError:
        print("Error File Not Found")
        
#Finds all prefixes of the word inputted
def getPrefixes(string):
    prefix = set()
    
    #Creates prfixes by adding x characters from the length of the word
    for x in range(1, len(string)):
        #Adds the list of prefixes into the empty set
        prefix.add(string[:x])
    return prefix
        
def anagramFinder(remainingL, scrambledL, word, wordSet, anagramSet):
    
    #Base Case if there are not letters remaining
    if len(remainingL) == 0:
        
        #Adds the word to a set then compares itself with fileSet to see if the
        #word is an anagram and if it is it is then added to the anagramSet
        tempPre = {scrambledL}
        tempSet = set.intersection(tempPre, wordSet)
        if len(tempSet) > 0:
            anagramSet.add(scrambledL)
    
    #Otherwise it beings making premutations of the inputted word and checks if
    #they are within the fileSet
    else:
        for i in range(len(remainingL)):
            scramble_letter = remainingL[i]
            remaining_letters = remainingL[:i] + remainingL[i + 1:]
            anagramFinder(remaining_letters, (scrambledL + scramble_letter), word, wordSet, anagramSet)
            
def anagramFinder_2(remainingL, scrambledL, word, wordSet, anagramSet, prefixSet):
    
    #Base Case if there are not letters remaining
    if len(remainingL) == 0:
        
        #Adds the word to a set then compares itself with fileSet to see if the
        #word is an anagram and if it is it is then added to the anagramSet
        tempPre = {scrambledL}
        tempSet = set.intersection(tempPre, wordSet)
        if len(tempSet) > 0:
            anagramSet.add(scrambledL)
            
    #Otherwise it beings making premutations of the inputted word and checks if
    #they are within the fileSet
    else: 
        #First Optimization
        #Creates a new epmty set to hold letters already used
        duplicatedL = set()
        for i in range(len(remainingL)):
            scramble_letter = remainingL[i]
            remaining_letters = remainingL[:i] + remainingL[i + 1:]
            
            #Uses the set of prefixes to stop the recusrion if the partial word
            #is not found in the set
            if len(remainingL) > 1:
                if(not((scrambledL + scramble_letter) in prefixSet)):
                    continue
            
            #Checks the set duplicateL for duplicated Letters
            if scramble_letter in duplicatedL:
                continue
            
            #If letter has no been used yet and it is in the prefix set then it
            #is added to duplicatedL
            duplicatedL.add(scramble_letter)
            anagramFinder_2(remaining_letters, (scrambledL + scramble_letter), word, wordSet, anagramSet, prefixSet)



def permutationsPart1(wordSet):
    
    #Runs the program untill the user enters an empty string
    while True:
        word = input("Enter a word or empty string to finish: ").lower()
        
        #If an empty sting is entered the program prints a goodbye message and closes
        if word == '':
            print("Bye, Thanks for using this program!")
            break
        
        #If a word is not inputed then it will prompt the user that that there input
        #is invalid
        elif(not(word in wordSet)):
            print("Input invalid")
        else:
            
            #Sorts the inputted word alphabetically 
            sortedList = sorted(list(word))
            sortedWord = ''.join(sortedList)
            
            #Adds the word to the set of anagrams to start the set so the word 
            #is already in the list when we try and remove it
            anagramSet = {word}
            start = time.time()
            anagramFinder(sortedWord, '', word, wordSet, anagramSet)
            end = time.time()
            runTime = end-start
            anagramSet.remove(word)
            
            
            anagramList = sorted(list(anagramSet))
            print("The word",  word, "has the following", len(anagramSet), "anagrams")
            for anagram in anagramList:
                print(anagram)
            print("It took", "{:.6f}".format(runTime), "seconds to find the anagrams")
            print()

       
            
def permutationsNoDuplicates(wordSet):
    
    #Runs the program untill the user enters an empty string
    while True:
        word = input("Enter a word or empty string to finish: ")
        
        #If an empty sting is entered the program prints a goodbye message and closes
        if word == '':
            print("Bye, Thanks for using this program!")
            break
        
        #If a word is not inputed then it will prompt the user that that there input
        #is invalid
        elif(not(word in wordSet)):
            print("Input invalid")
        else:
            
            #Sorts the inputted word alphabetically
            sortedList = sorted(list(word))
            sortedWord = ''.join(sortedList)
            
            #Adds the word to the set of anagrams to start the set so the word 
            #is already in the list when we try and remove it
            anagramSet = {word}
            
            prefixSet = set()
            
            #Creats and Adds prefixes for all words in the fileSet
            #and adds them into the set prefixSet
            for setWord in wordSet:
                prefixSet.update(getPrefixes(setWord)) 
            
            start = time.time()
            anagramFinder_2(sortedWord, '', word, wordSet, anagramSet, prefixSet)
            end = time.time()
            runTime = end-start
            
            #removes the original word from the anagramSet
            anagramSet.remove(word)
                
            #Converts anagramSet to a list, sorts them alphabetically, and 
            #then prints them alphabetically
            anagramList = sorted(list(anagramSet))
            print("The word",  word, "has the following", len(anagramSet), "anagrams")
            for anagram in anagramList:
                print(anagram)
            print("It took","{:.6f}".format(runTime), "seconds to find the anagrams")
            print()

       



    
wordSet = set(line.strip() for line in open('words_alpha.txt'))

print("Finding Permutations")
permutationsPart1(wordSet)
print()
print("Finding Permutations without Duplicates")
permutationsNoDuplicates(wordSet)

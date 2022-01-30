import numpy as np
import csv
import matplotlib.pyplot as plt
letters = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
alphabet = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

def readCsv(filename):
    wordList = []
    with open(filename, mode ='r') as file:   
            
        # reading the CSV file
        csvFile = csv.DictReader(file)
    
        # displaying the contents of the CSV file
        for lines in csvFile:
            wordList.append(lines['word'])

    return wordList

def letterDist(words):
    lettersPlot = letters
    plot = np.zeros(26)
    for i in range(len(words)):
        w = words[i]
        for j in range(5):
            plotInd = alphabet[w[j]] - 1
            plot[plotInd] += 1

    # Sort letters by frequency
    sortArgs = np.argsort(plot)
    sortLetters = [lettersPlot[i] for i in sortArgs]
    sortPlot = [plot[i] for i in sortArgs]

    plt.figure()
    plt.bar(sortLetters, sortPlot)
    plt.show()

def letterDistbyPos(words, pos):
    lettersPlot = letters
    plot = np.zeros(26)
    for i in range(len(words)):
        w = words[i]
        plotInd = alphabet[w[pos]] - 1
        plot[plotInd] += 1

    # Sort letters by frequency
    sortArgs = np.argsort(plot)
    sortLetters = [lettersPlot[i] for i in sortArgs]
    sortPlot = [plot[i] for i in sortArgs]

    plt.figure()
    plt.bar(sortLetters, sortPlot)
    plt.show()

def removeLetter(words, l, v, p = None):
    removeInd = []
    for i in range(len(words)):
        w = words[i]
        # Remove words with letter l
        if v == 0:
            for j in range(5):
                if w[j] == l:
                    removeInd.append(i)
                    break

        # Keep words with letter l
        if v == 1:
            for j in range(5):
                if j == p and w[j] == l:
                    removeInd.append(i)
                    break
                if j == p:
                    continue
                if w[j] == l:
                    break    
                if j==4:
                    removeInd.append(i) 
                        
        # Keep words with letter l in position p
        if v == 2:
            for j in range(5):
                if j == p and w[j] != l:
                    removeInd.append(i)
                    break

    # Remove these indices    
    wordsOut = []
    for i in range(len(words)):
        if i not in removeInd:
            wordsOut.append(words[i])

    return wordsOut

def updateSol(words, wdlIn, wdlOut):
    for letInd in range(5):
        # print(wdlIn, wdlOut, letInd)
        words = removeLetter(words, wdlIn[letInd], wdlOut[letInd], letInd)
            
    return words


if __name__ == "__main__":
    guessList = readCsv('valid_guesses.csv')
    solList = readCsv('valid_solutions.csv')
    # letterDist(guessList)
    # letterDistbyPos(guessList, 1)
    wordIn = 'dzzzz'
    coloursOut = [1, 0, 0, 0, 0]
    wordsNew = updateSol(guessList, wordIn, coloursOut)
    print(wordsNew)
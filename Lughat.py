import os
import sys
from datetime import datetime

start=datetime.now()

#Function to populate a list with file contents
def list_populate(FILE_NAME):
    try:
        with open(FILE_NAME,'r',encoding='utf8') as set_file:
            lughatwords = [line.strip() for line in set_file.readlines()]
            #lughatwords = set(line.strip() for line in set_file.readlines())
    except ValueError as e:
           print(e)
    return lughatwords

#Function to Create a Dictionary with a list of words starting with a specific key(alphabet)
def wordList(LUGHAT,letter,key,dictAlfaaz={}):
    for word in LUGHAT:
        if word.startswith(letter):
            dictAlfaaz[key].append(word)
    return dictAlfaaz

def dictWordsListfunc(totWords,LUGHAT):

    #Creating Dictionary with Urdu Letters as Keys and words starting with that letter as a list
    dictWordsList = dict((k,list()) for k in urduLetters.keys())

    for key in urduLetters.keys():
        dictWordsList = wordList(LUGHAT,urduLetters[key],key,dictWordsList)
        #print("Words in {} are: {}".format(key, len(dictWordsList[key])))
        totWords +=len(dictWordsList[key])
    return dictWordsList,totWords

def file_writes(basedir,dictWordsList):
    totWords = 0
    fileNames = []
    print('********Function write_files**********')
    for key in urduLetters.keys():
        fileln = 0
        wordfile = key + "words.txt"
        FILE_WRITE = os.path.join(basedir,wordfile)
        with open(FILE_WRITE,'w',encoding='utf8') as fWrite:
             for y in dictWordsList[key]:
                 #print("{} words are : ".format(y))
                fWrite.write("{}\n".format(y))
                fileln += 1
        #print("Words in {} are : {}".format(wordfile,fileln))
        fileNames.append(wordfile)

def program_stats(totWords,LUGHAT):
    print("Total words in Dictionary are {}".format(totWords))
    print("Total words in LUGHAT are {}".format(len(LUGHAT)))
    print(datetime.now()-start)

urduLetters = {
"Alif":"ا","AlifMada":"آ", "Bay":"ب", "Pay":"پ", "Tay":"ت","Ttay":"ٹ","Say":"ث","Jeem":"ج",
"Chay":"چ","Hay":"ح","Khay":"خ","Daal":"د","Ddaal":"ڈ","Zaal":"ذ","Ray":"ر","Array":"ڑ","Zay":"ز","Yaal":"ژ",
"Seen":"س","Sheen":"ش","Swaad":"ص","Zwaad":"ض","Touay":"ط","Zouay":"ظ","Ain":"ع","Ghain":"غ","Fay":"ف",
"Kaaf":"ک","Qaaf":"ق","Gaaf":"گ","Laam":"ل","Meem":"م","Noon":"ن","Wow":"و","Hai":"ہ","Hamza":"ء","ChotiYay":"ی","BariYay":"ے"
}

totWords = 0
basedir = r'C:\Test\Data'
FILE_NAME = os.path.join(basedir,"FullWords.txt")

#Populating list with all words in file
LUGHAT = list_populate(FILE_NAME)

#Creating dictionary of word lists
dictWords,totWords = dictWordsListfunc(totWords,LUGHAT)

#Printing statistics about program
program_stats(totWords,LUGHAT)

#Writing one file for all words starting, with a specific letter
file_writes(basedir,dictWords)

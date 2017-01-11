# -*- coding: utf-8 -*-

import csv
import re
import os
from random import randint

LIFECOUNTER = 10

def csvReader():
    wordlist = []
    table = {
            ord(u'ä'): u'ae',
            ord(u'ö'): u'oe',
            ord(u'ü'): u'ue',
            ord(u'Ä'): u'ae',
            ord(u'Ö'): u'oe',
            ord(u'Ü'): u'ue',
            ord(u'ß'): u'ss'
            }

    with open ('defaultWords.csv', 'rb') as csvfile:
        words = csv.reader(csvfile, delimiter='\n')
        for row in words:
            wordlist.append(row[0].decode('utf8').translate(table))
    return wordlist

def clearScreen():
    # cross platform clearscreen
    os.system('cls' if os.name == 'nt' else 'clear')


def showWinningTable():
    print"""
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
                                                    JUHUUUU WINNER :)
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
            """

def showGameOverLabel(word):
    print """

Das gesuchte Wort waere gewesen: """ + "".join(word[0]) + """
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
                                                     GAME OVER!
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
    """

def headlineOutput():
    print"""
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
                                                   HANGMAN THE GAME
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
            """

def start_game():
    step = 0
    show_startUp()
    raw_input("""Aber genug zur Erklärung des Spiels, nachdem du den Text gelesen hast, sollte das System schon bereit sein!
Klick doch mal auf Enter um nachzusehen!
""")
    print """
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
                                                Spiel startet!
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
    """

    clearScreen()

    wordList = csvReader()
    word = wordList[randint(0, len(wordList))]
    #print word
    word = preProcessWord(word)

    correctCharCounter = 0
    usedLetters = []
    print ""
    while step < LIFECOUNTER:


        headlineOutput()
        print get_hangman(step)
        print step


        print "Dein Wort:  " + " ".join(word[2]) + "\n"

        if correctCharCounter == word[1]:
            showWinningTable()
            break

        letter = getUserInput()

        clearScreen()

        if len(letter) != 1:
            print "Du sollst genau einen Buchstaben eingeben! Versuch es nochmal!"
            continue

        else:
            if re.match(r"[^a-zA-Z]", letter):
                print "Du hast ein ungültiges Zeichen eingegeben. Bitte gib nur Buchstaben von a-z ein."
                continue

            if letter in usedLetters:
                print "Buchstabe bereits verwendet! Versuch es nochmal!"
                continue

            else:
                print ""
                usedLetters.append(letter)
                letterInWord = False
                for i in range(0, word[1]):
                    if letter == word[0][i]:
                        word[2][i] = letter
                        letterInWord = True
                        correctCharCounter += 1

                if letterInWord == False:
                    step += 1


    if step == LIFECOUNTER:
        showGameOverLabel(word)



def preProcessWord(word):
    underscored = ""
    for i in range(0, len(word)):
        underscored += " _"
    processedWord = [list(word.upper()), len(list(word.upper())), underscored.split()]
    return processedWord

def getUserInput():
    letter = raw_input("Dein Buchstabe: ")
    return letter.upper()


def show_startUp():
    clearScreen()
    print get_title()
    print """
Zur Erklärung des Spiels:
Bei diesem Spiel errätst du Wörter! Das machst du, indem du einzelne Buchstaben mit deiner Tastatur in die Konsole
eingibst. Aber Achtung: du kannst nur Buchstaben (egal ob groß oder klein) eingeben, Zahlen und Sonderzeichen werden
im Spiel nicht vorkommen. Deshalb solltest du sie auch nicht eintippen!
Du hast für jedes Spiel 10 Leben, die dir als Hangman angezeigt werden. Jeder vollständige Strich bedeutet, dass du ein
weiteres Leben verloren hast. Sobald der Hangman vollständig am Galgen baumelt, heißt es für dich:
                                        GAME OVER!
Aber keine Angst: du kannst direkt im Anschluss einen weiteren Versuch wagen.
Wir haben genügend Hangmans vorrätig!
Und wir haben ein kleines Gimmick für dich: Solltest du dich bei den von uns ausgewählten Worten langweilen, dann kannst
du gerne eigene Wortlisten als .csv-Datei erstellen und einfach im Dateiordner ersetzen!
    """

def get_title():
    hangman_title = """
()    ()    ()()    ()   ()   ())))))   ()      ()    ()()    ()   ()
()    ()   ()  ()   ())) ()  ()         ()))  ((()   ()  ()   ())) ()
()(())()  ()(())()  () ()()  ()   ))))  () (()) ()  ()(())()  () ()()
()    ()  ()    ()  ()  )))  ()     ))  ()      ()  ()    ()  ()  )))
()    ()  ()    ()  ()   ()   ())))))   ()      ()  ()    ()  ()   ()
        """
    return hangman_title

def get_hangman(step):
    if step == 0:
        return """






 ______________________
/                     /|
                     / |
____________________/  /
                    | /
____________________|/
            """
    elif step == 1:
        return """

     |
     |
     |
     |
     |
 ____|_________________
/    |                /|
                     / |
____________________/  /
                    | /
____________________|/
            """
    elif step == 2:
        return """
     ____________
     |
     |
     |
     |
     |
 ____|_________________
/    |                /|
                     / |
____________________/  /
                    | /
____________________|/
            """
    elif step == 3:
        return """
     ____________
     |          |
     |
     |
     |
     |
 ____|_________________
/    |                /|
                     / |
____________________/  /
                    | /
____________________|/
            """
    elif step == 4:
        return """
     ____________
     |          |
     |          @
     |
     |
     |
 ____|_________________
/    |                /|
                     / |
____________________/  /
                    | /
____________________|/
            """
    elif step == 5:
        return """
     ____________
     |          |
     |          @
     |          |
     |          |
     |
 ____|_________________
/    |                /|
                     / |
____________________/  /
                    | /
____________________|/
            """
    elif step == 6:
        return """
     ____________
     |          |
     |          @
     |         /|
     |          |
     |
 ____|_________________
/    |                /|
                     / |
____________________/  /
                    | /
____________________|/
            """
    elif step == 7:
        return """
     ____________
     |          |
     |          @
     |         /|\\
     |          |
     |
 ____|_________________
/    |                /|
                     / |
____________________/  /
                    | /
____________________|/
            """
    elif step == 8:
        return """
     ____________
     |          |
     |          @
     |         /|\\
     |          |
     |         /
 ____|_________________
/    |                /|
                     / |
____________________/  /
                    | /
____________________|/
            """
    elif step == 9:
            return """
     ____________
     |          |
     |          @
     |         /|\\
     |          |
     |         / \\
 ____|_________________
/    |                /|
                     / |
____________________/  /
                    | /
____________________|/
            """
    else:
        return ""

#starting the game
start_game()

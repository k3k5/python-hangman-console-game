# -*- coding: utf-8 -*-

import csv
import re
from random import randint

usedLetters = []

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
    wordList = csvReader()
    word = wordList[randint(0, len(wordList))]
    print word
    word = preProcessWord(word)
    print "Dein Wort: " + " ".join(word[2]) + " ( " + str(word[1]) + " Buchstaben ) \b"
    for i in range(0, 10):
        for j in range(0, len(word[2])):
            for k in range(0, len(usedLetters)):
                if word[0][j] == usedLetters[k]:
                    word[2][j] = usedLetters[k]
        if i != 0:
            print "Dein Wort:  " + " ".join(word[2]) + "\n"
            letter = getUserInput(word)
            if len(letter) == 0:
                print "Leere Eingabe! Versuch es nochmal!"

            elif len(letter) == 1:
                if letter not in usedLetters:
                    usedLetters.append(letter)
                    if letter not in word[0]:
                        step += 1
                        print get_hangman(step)
            else:
                if letter[0] not in usedLetters:
                    usedLetters.append(letter[0])
                    if letter[0] not in word[0]:
                        step += 1
                        print get_hangman(step)

            if letter in usedLetters:
                print "Buchstabe bereits verwendet!"
                print "Neuer Versuch."

            elif re.match(r"[^a-zA-Z]", letter):
                print "Du hast ein ungültiges Zeichen eingegeben. Bitte gib nur Buchstaben von a-z ein."

    if step == 10:
    print """

Das gesuchte Wort ist: """ + "".join(word[0]) + """
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
                                                GAME OVER!
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
    """
    #elif step <=10 and

def preProcessWord(word):
    underscored = ""
    for i in range(0, len(word)):
        underscored += " _"
    processedWord = [list(word.upper()), len(list(word.upper())), underscored.split()]
    return processedWord

def getUserInput(word):
    letter = raw_input("Dein Buchstabe: ")
    return letter.upper()


def show_startUp():
    print get_title()
    print get_hangman(0)
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
    elif step == 1:
        return """
 ______________________
/                     /|
                     / |
____________________/  /
                    | /
____________________|/
            """
    elif step == 2:
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
    elif step == 3:
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
    elif step == 4:
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
    elif step == 5:
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
    elif step == 6:
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
    elif step == 7:
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
    elif step == 8:
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
    else:
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

#starting the game
start_game()

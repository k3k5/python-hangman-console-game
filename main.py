# -*- coding: utf-8 -*-

from random import randint

usedLetters = []

def start_game():

    step = 0
    counter = 0

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
    word = "test"
    word = preProcessWord(word)
    print "Dein Wort: " + word[2] + " ( " + str(word[1]) + " Buchstaben )"
    for i in range(0, 10):
        print "Benutzte Buchstaben: " + str(usedLetters)
        letter = getUserInput(word)
        if letter in word[0]:
            if letter not in usedLetters:
                counter += 1
                usedLetters.append(letter)
        else:
            usedLetters.append(letter)
            step += 1
            print get_hangman(step)
    print """
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
                                                GAME OVER!
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
    """

def preProcessWord(word):
    underscored = ""
    for i in range(0, len(word)):
        underscored += " _"
    processedWord = [list(word.upper()), len(list(word.upper())), underscored]
    return processedWord

def getUserInput(word):
    letter = raw_input("Dein Buchstabe: ")
    if letter not in usedLetters:
        return letter.upper()
    else:
        letter = raw_input("Neuer Versuch! Diesen Buchstaben hast du schon genutzt!")
        return letter

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


import csv

wordlist = []
table = {
        ord(u'ä'): u'ae',
        ord(u'ö'): u'oe',
        ord(u'ü'): u'ue',
        ord(u'Ä'): u'ae',
        ord(u'Ö'): u'oe',
        ord(u'Ü'): u'ue',
        ord (u'ß'): u'ss'
        }

with open ('defaultWords.csv', 'rb') as csvfile:
    words = csv.reader(csvfile, delimiter='\n')
    for row in words:
        wordlist.append(row[0])

    for word in wordlist:
            s = word.decode('utf8')
            print s.translate(table)

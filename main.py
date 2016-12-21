# -*- coding: utf-8 -*-

from random import randint

def start_game():
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
    startWord()

def show_startUp():
    print get_title()
    print get_hangman(0)
    print """
Zur Erklärung des Spiels:
Bei diesem Spiel errätst du Wörter! Das machst du, indem du einzelne Buchstaben mit deiner Tastatur in die Konsole
eingibst. Aber Achtung: du kannst nur Buchstaben (egal ob groß oder klein) eingeben, Zahlen und Sonderzeichen werden
im Spiel nicht vorkommen. Deshalb solltest du sie auch nicht eintippen!
Du hast für jedes Spiel 9 Leben, die dir als Hangman angezeigt werden. Jeder vollständige Strich bedeutet, dass du ein
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

def startWord():
    print randint(0,9)
    print "_ _ _ _ _ _ _ _"



start_game()

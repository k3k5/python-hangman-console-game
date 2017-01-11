# Hangman console game

Little implementation of the game "Hangman" in Python for an university course.

()    ()    ()()    ()   ()   ())))))   ()      ()    ()()    ()   ()
()    ()   ()  ()   ())) ()  ()         ()))  ((()   ()  ()   ())) ()
()(())()  ()(())()  () ()()  ()   ))))  () (()) ()  ()(())()  () ()()
()    ()  ()    ()  ()  )))  ()     ))  ()      ()  ()    ()  ()  )))
()    ()  ()    ()  ()   ()   ())))))   ()      ()  ()    ()  ()   ()
        

     ____________
     |          |
     |          @
     |         /|\
     |          |
     |         / \
 ____|_________________
/    |                /|
                     / |
____________________/  /
                    | /
____________________|/


## Language
The game is written in German Language and coded in Python 2.7.

## Contributors
- k3k5
- bekkkka
- violetta41
- Anna-Maria00660077

## Funktionsumfang

- Das Programm liest eine CSV-Datei ein, die eine Liste an möglichen Wörtern enthält.
- Alle Wörter der CSV-Datei werden in Großbuchstaben umgewandelt.
- Ein Zufallsgenerator wählt ein beliebiges Wort aus der Liste aus.
- Die Länge des Wortes wird auf der Konsole mit Hilfe von Unterstrichen (_) visualisiert.
- Zu Beginn wird ein Begrüßungstext und die Anzahl der Leben eingeblendet.
  * 1 Leben = 1 Strich, des Hangmans 
- Das Programm erkennt Nutzereingaben. Zulässig sind hierbei nur Buchstaben von a-z
  * Keine Sonderzeichen, keine Zahlen
  * Umwandlung der Nutzereingaben in Großbuchstaben

- Beim Umgang mit der Nutzereingabe werden drei Fälle unterschieden.
  * a) Buchstabe kommt im Wort vor
    * Buchstabe anzeigen: an der richtigen Stelle wird der Unterstrich durch den entsprechenden Buchstaben ersetzt 
    * Buchstabe wird in einer Liste gespeichert, die alle bereits verwendeten Buchstaben enthält
    * Aufforderung an den Nutzer, den nächsten Buchstaben einzugeben
  * b) Buchstabe kommt im Wort nicht vor
    * Hangman bekommt ein neues Element. Diese bestehen aus Strichen und weiteren Zeichen.
    * Buchstabe wird ebenfalls in der Liste der bereits verwendeten Buchstaben gespeichert
    * Prüfen, ob Hangman komplett ist mit Hilfe eines rückwärtslaufenden Counters. Der Counter beginnt bei der Anzahl der Leben und endet bei 0
  * Hangman noch nicht vollständig: Aufforderung an den Nutzer, den nächsten Buchstaben einzugeben.

- Hangman vollständig: Game Over-Anzeige wird eingeblendet

  * c) Fehlermeldung bei einer unzulässigen Eingabe des Nutzers anzeigen (=Zahl, Sonderbuchstabe oder bereits verwendeter Buchstabe)
  * im Anschluss neuen Buchstaben eingeben lassen

- Bei vielen Ausgaben des Programms (Spielstart, Spielende und die einzelnen Hangmans) werden Bilder in ASCII-Art angezeigt, die durch Bilder erzeugt werden (Game-Start und Spielende) bzw. durch vorgefertigte Hangmans (manuell eingetippt)

- Während des Spiels wird für einen besseren Überblick über den Spielverlauf bei jedem Spielschritt die Konsole "geleert". Das heißt, dass alle vorherigen Konsolenausgaben mit der Funktion clear_board() geleert.

  * def clear_board():
    os.system('cls' if os.name=='nt' else 'clear')
    >> Übernommen von: http://stackoverflow.com/questions/517970/how-to-clear-python-interpreter-console

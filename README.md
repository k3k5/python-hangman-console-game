# Hangman console game

Little implementation of the game "Hangman" in Python for an university course.

![hangman_image](https://lh5.ggpht.com/Uz8u6HRnoQffXamOEYMcrENi4D6buhw7CXjMBdeeTYGmw0AvXdrn9BsZs92SWIdJWg0=w300)
<sub><sup>(Image-Source: https://lh5.ggpht.com/Uz8u6HRnoQffXamOEYMcrENi4D6buhw7CXjMBdeeTYGmw0AvXdrn9BsZs92SWIdJWg0=w300)</sup></sub>

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

## Übernommener Code

- ASCII-Art (Kommentare entfernt)

  ```
  from PIL import Image
import random
from bisect import bisect

greyscale = [
            " ",
            " ",
            ".,-",
            "_ivc=!/|\\~",
            "gjez2]/(YL)t[+T7Vf",
            "mdK4ZGbNDXY5P*Q",
            "W8KMA",
            "#%$"
            ]


zonebounds=[36,72,108,144,180,216,252]


im=Image.open(r"c:\test.jpg")
im=im.resize((160, 75),Image.BILINEAR)
im=im.convert("L") # convert to mono

str=""
for y in range(0,im.size[1]):
    for x in range(0,im.size[0]):
        lum=255-im.getpixel((x,y))
        row=bisect(zonebounds,lum)
        possibles=greyscale[row]
        str=str+possibles[random.randint(0,len(possibles)-1)]
    str=str+"\n"

print str
  ```
  <sub><sup>>> Übernommen von: https://stevendkay.wordpress.com/2009/09/08/generating-ascii-art-from-photographs-in-python/</sup></sub>


- Leeren der Konsole:

  ```def clear_board():
     os.system('cls' if os.name=='nt' else 'clear')
  ```
    <sub><sup>>> Übernommen von: http://stackoverflow.com/questions/517970/how-to-clear-python-interpreter-console</sup></sub>

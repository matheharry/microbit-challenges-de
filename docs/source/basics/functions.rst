************
Funktionen I
************

Funktionen und Methoden beziehen sich auf nützliche Codeschnipsel, die einem bestimmten Zweck dienen und normalerweise viele Male in deinem Programm verwendet werden. 
Wahrscheinlich hast du sowohl Funktionen als auch Methoden schon benutzt, ohne es unbedingt zu merken. 
In diesem Abschnitt werden wir nicht weiter auf Methoden eingehen, aber wir werden erklären, wie man Funktionen benutzt und schreibt. 

Funktionen verwenden
====================

Eine großartige Sache an Funktionen ist, dass sie in mehr als einem Programm verwendet werden können und Code-Wiederholungen vermeiden. Auf die gleiche Weise kannst du Funktionen verwenden, die andere Leute 
geschrieben haben. 
In Python können nützliche Funktionen zu Modulen zusammengestellt werden (obwohl du das nicht tun musst) - das ``random`` Modul ist ein gutes Beispiel. 
Um die Funktionen des Random-Moduls zu nutzen, musst du das Modul zuerst `importieren`. Sobald du das getan hast, kannst du alle Funktionen des Moduls benutzen. Hier sind zwei Beispiele 
von Funktionen aus 'random'.

Die Funktion ``random.randint()`` erlaubt es uns, eine zufällige Ganzzahl (Integer) aus einem bestimmten Bereich zu erzeugen::

	from microbit import *
	import random
	
	display.show(str(random.randint(1, 6)))

Im obigen Code wird eine Zufallszahl zwischen 1 und 5 generiert - die obere Grenze, in diesem Fall 6, wird nie einbezogen.
	
In diesem Codeschnipsel prüft die Funktion ``random.choice`` wie viele Elemente in der Namensliste sind, erzeugt eine zufällige Ganzzahl im Bereich von 0 bis zur Listenlänge 
und gibt ein Listenelement mit dem Index der erzeugten Ganzzahl zurück::

	from microbit import *
	import random
	
	namen = ["Maria", "Jolanda", "Damien", "Alia", "Kushal", "Mei Xiu", "Zoltan" ]
	
	display.scroll(random.choice(namen))


Eigene Funktionen erstellen
============================

Funktionen können dir helfen, deinen Code zu organisieren und ihn ordentlich zu halten. Hier ist ein Beispiel für eine einfache Funktion, die eine Nachricht ausgibt::


	def zeigeBegruessung():
		print("Hallo alle miteinander!")

		Um die Funktion zu nutzen, muss sie *aufgerufen* werden: ::

	zeigeBegruessung()

Das ist keine sehr interessante Funktion, oder? Du kannst Funktionen mächtiger machen, indem du `Parameter` und `Rückgabewerte` benutzt. Wenn du dir eine Funktion wie eine Black Box vorstellst 
dann ist ein Parameter ein Eingabewert und ein Rückgabewert ist das, was du am anderen Ende bekommst. Nehmen wir an, wir wollen ein kleines Programm schreiben, das einige 
Freunde mit einer Nachricht begrüßt, die ihren Namen und ihr Alter enthält: ::

	from microbit import *

	def printBirthdayGreeting(name, age):
	    return "Happy Birthday " + name + ", du bist " + str(age) + " Jahre alt"   


 	display.scroll(printBirthdayGreeting("Toni", 8))
 	display.scroll(printBirthdayGreeting("Sonja", 9))
 	display.scroll(printBirthdayGreeting("Maria", 11))
		
Die Funktion ``printBirthdayGreeting`` stellt die Geburtstagsnachricht für uns zusammen und gibt einen String zurück. ``str()`` wird benutzt, um das ``Alter``, 
welches eine Zahl ist, in einen String zu verwandeln.  Du musst keine Funktionen oder Rückgabewerte in deinen Funktionen verwenden, es sei denn, du willst/brauchst sie.	

Übungsaufgaben
===================

1. Schreibe eine Funktion ``blink(x, y)``, die eine LED an den Koordinaten, die durch die Parameter x und y angegeben werden, einmal blinken lässt.

2. Benutze die Funktion ``blink(x, y)`` um alle LEDs nacheinander blinken zu lassen.

3. Schreibe eine Funktion button_count() die ein Tupel zurückgibt, das die Anzahl der Betätigungen von Taste A und Taste B enthält. (fix)

4. Kombiniere die beiden Funktionen in einem Programm, das es dem Benutzer ermöglicht, die Koordinaten der blinkenden LED durch Drücken der Tasten einzustellen.

5. Schau dir die Skripte an, die du zuvor geschrieben hast und prüfe, ob du deinen Code durch die Verwendung von Funktionen verbessern könntest (oder nicht).
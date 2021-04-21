*********************
Beschleunigungsmesser
*********************

Wie der Name schon sagt, misst der Beschleunigungsmesser auf einem BBC micro:bit die Beschleunigung.
Der Beschleunigungsmesser ist so eingestellt, dass er Beschleunigungswerte im Bereich von +2g bis -2g misst, 
und diese Werte können mit MicroPython ausgelesen werden und auf den Bereich 0 ... 1024 abgebildet. 

.. figure:: assets/accelerometer.png
   :scale: 40 %
   :align: center

Der micro:bit misst die Bewegung entlang dreier Achsen:

* X - Kippen von links nach rechts.
* Y - Kippen nach vorne und hinten.
* Z - Bewegung nach oben und unten.

.. figure:: assets/microbit_axes.png
   :align: center 	

Grundfunktionen
===============
Die Messung für jede Achse ist eine positive oder negative Zahl
die einen Wert in milli-g's (g ist die Erdbeschleunigung) 
angibt. Wenn der Messwert 0 ist, bist du "ruhig"
entlang der jeweiligen Achse. 

Du kannst die Beschleunigungswerte einzeln oder alle drei
Werte auf einmal abrufen und sie in einer Liste speichern.
Du kannst mehr über Listen in den Grundlagen der Programmierung lernen, 
aber für den Moment verwende einfach den folgenden Code: :: 

	from microbit import *

	while True:
	    x = accelerometer.get_x()
	    y = accelerometer.get_y()
	    z = accelerometer.get_z()
	    print("x, y, z:", x, y, z)
	    sleep(500)

Lade den Code auf den micro:bit und öffne den seriellen Monitor. Halte den 
micro:bit flach mit den LEDs nach oben. Du solltest sehen, dass die X- und 
Y-Beschleunigungen nahe Null sind, und die Z-Beschleunigung nahe bei -1024. 
Das bedeutet, dass die Schwerkraft relativ zum micro:bit nach unten wirkt. 
Drehe das Board um so dass die LEDs dem Boden am nächsten sind. Der Z-Wert 
sollte positiv werden bei +1024 milli-g. Wenn du den micro:bit kräftig genug 
schüttelst, wirst du sehen, dass die Beschleunigungen bis zu ±2048 milli-g 
ansteigen. Das liegt daran, dass der Beschleunigungssensor auf ein Maximum 
von ±2048 milli-g eingestellt ist: die tatsächliche Zahl kann höher sein als 
das.

Wenn du dich jemals gefragt hast, woher ein Mobiltelefon weiß, in welche Richtung 
es den Bildschirm ausrichten soll, dann liegt das daran, dass es den Beschleunigungssensor 
auf genau die gleiche Weise wie das obige Programm abfragt. Auch Gamecontroller 
enthalten Beschleunigungssensoren, um die Steuerung zu ermöglichen.
	
Gesten
--------

Der wirklich interessante Nebeneffekt des Beschleunigungssensors ist die Gestenerkennung. 
Wenn du deinen BBC micro:bit auf eine bestimmte Art und Weise bewegst (als Geste), dann 
ist der micro:bit in der Lage, dies zu erkennen.

Der micro:bit ist in der Lage, die folgenden Gesten zu erkennen: 
* ``up``, ``down``
* ``left``, ``right``
* ``face up``, ``face down``
* ``freefall``, ``3g``, ``6g``, ``8g``, 
* ``shake``.
 
Gesten werden immer als Strings dargestellt. Während die meisten Namen 
offensichtlich sein sollten, gelten die ``3g``, ``6g`` und ``8g`` Gesten, wenn
das Gerät entsprechend schnell beschleunigt wird.

Um die aktuelle Geste zu erhalten, benutze die Methode ``accelerometer.current_gesture``.
Das Ergebnis wird eine der oben genannten Gesten sein. 

Zum Beispiel wird dieses Programm ein glückliches Emoticon anzeigen, wenn das Display nach
oben zeigt::

    from microbit import *

    while True:
        geste = accelerometer.current_gesture()
        if geste == "face up":
            display.show(Image.HAPPY)
        else:
            display.show(Image.ANGRY)

1. Innerhalb des *Geltungsbereichs (Scope)* der Schleife wird die aktuelle Geste gelesen und der Variablen ``geste`` zugewiesen. 
2. Die ``if``-Bedingung prüft, ob ``geste`` gleich ``"face up"`` ist (Python verwendet ``==``, um auf Gleichheit zu testen, ein einzelnes Gleichheitszeichen ``=`` wird für die Zuweisung verwendet - genau wie wir die gelesenen Gesten der ``geste``-Variablen zuweisen). 
3. Wenn die Geste gleich ``"face up"`` ist, dann benutze das Display, um ein glückliches Gesicht zu zeigen. 
4. Ansonsten wird das Gerät dazu gebracht, wütend dreinzuschauen!

Was macht das folgende Programm?::

	from microbit import *
	while True:
		if accelerometer.is_gesture("up"):
			display.show(Image.ARROW_S)
		elif accelerometer.is_gesture("right"):
			display.show(Image.ARROW_E)
		elif accelerometer.is_gesture("down"):
			display.show(Image.ARROW_N)
		elif accelerometer.is_gesture("left"):
			display.show(Image.ARROW_W)
		else:
			display.clear()
		sleep(20)

Fortgeschrittene Funktionen
===========================

Für den Beschleunigungssensor gibt es keine, aber es lohnt sich zu schauen, wie 
wie wir die 3D-Beschleunigung nutzen können, um verschiedene Arten von Bewegung zu erkennen. 
Wir könnten zB erkennen wollen, ob er geschüttelt wird. Die Beschleunigung ist eine so genannte 
Vektorgröße - sie hat einen Betrag (Größe, Länge) und eine Richtung. Um den Gesamtbetrag in 
X- und Y-Richtung zu erhalten, ohne auf die Z-Achse zu achten (d.h. wir hätten einen 
2D-Beschleunigungsmesser), würde die Situation so aussehen:

.. image:: assets/microbitOverallAcceleration.jpg
   :scale: 60 %
   :align: left

Wir können den Betrag (Länge) der Resultierenden mit dem Satz des Pythagoras berechnen:

.. math::

   beschleunigung = \sqrt{x^2 + y^2}

Das gleiche Prinzip gilt für einen 3D-Beschleunigungsmesser. Der Gesamtbetrag des 
resultierenden Beschleunigungsvektors ist also gleich:

.. math::

	beschleunigung = \sqrt{x^2 + y^2 + z^2}

Berechnung der Gesamtbeschleunigung: ::

	from microbit import *
	import math

	while True:
	    x = accelerometer.get_x()
	    y = accelerometer.get_y()
	    z = accelerometer.get_z() 
	    beschleunigung = math.sqrt(x**2 + y**2 + z**2)
	    print("Beschleunigung", beschleunigung)
	    sleep(500)

Wenn du den Beschleunigungssensor still hältst (auf den Tisch legst), ergibt dies eine Beschleunigung 
von etwa 1g, unabhängig davon, in welcher Orientierung du den BBC micro:bit hältst - und sie wird davon 
abweichen, wenn du ihn bewegst. Tatsächlich wird der Wert leicht variieren, auch wenn du ihn still hältst, 
weil der Beschleunigungsmesser kein perfektes Messgerät ist. 

Immer wenn wir eine Größe genau wissen wollen, ist eine sogenannte *Kalibrierung* nötig, bei der die Sensordaten 
genau eingemessen und mit einem Richtwert verglichen werden.


Übungsaufgaben
===============
* Benutze die BBC micro:bit Musikbibliothek und spiele eine Note, die auf dem Messwert des Beschleunigungsmessers basiert. Tipp: Stelle die Tonhöhe auf den Wert des Beschleunigungsmessers ein.
* Zeige die Zeichen 'L' oder 'R' an, je nachdem, ob der BBC micro:bit nach links oder rechts gekippt ist.
* Lasse die LEDs aufleuchten, wenn die Größe der Beschleunigung größer als 1024 milli-g's ist.
* Schüttle den micro:bit, um die LEDs aufleuchten zu lassen.
* Mache einen Würfel. Tipp: benutze eine der Python Zufallsfunktionen. Gib ``import random`` am Anfang deines Programms ein und verwende ``random.randrange(start, stop)``. Dies wird eine Zufallszahl zwischen ``start`` und ``stop - 1`` erzeugen.

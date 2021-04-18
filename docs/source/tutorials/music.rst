********
Musik
********
Der **micro:bit V2** kann direkt zum Abspielen einfacher Melodien verwendet werden. Auch das ältere Modell
ist dazu in der Lage, vorausgesetzt du verbindest einen Lautsprecher mit deinem Board. 

Wenn du Kopfhörer verwendest, kannst du Krokodilklemmen verwenden, um deinen micro:bit mit Kopfhörern zu verbinden: 

..  figure:: assets/headphones_connect.png
    :align: center	
    :scale: 70 %

.. warning:: Du kannst die Lautstärke des Tonpegels nicht über den micro:bit steuern. 
	Bitte sei sehr vorsichtig, wenn du Kopfhörer verwendest. Ein Lautsprecher ist die 
	sicherere Wahl bei der Arbeit mit Klängen.

Du kannst deinen micro:bit auch mittels Krokodilklemmen mit einem Lautsprecher verbinden: 

.. figure:: assets/connect_speaker.jpg
   :align: center

   Source: <https://www.kitronik.co.uk/blog/microbit-alarm-kitronik-university/>

Grundfunktionen
================

Eine Melodie spielen
---------------------
Um eine Melodie zu spielen, kannst du die Funktion ``play`` verwenden: ::

	from microbit import *
	import music

	music.play(music.NYAN)

.. note:: Du musst das Modul ``music`` importieren, um Klänge zu spielen und zu regeln.

Das Musikmodul enthält eine Reihe von eingebauten Melodien. Hier sind einige von ihnen: 

 *  ``music.DADADADUM``
 *  ``music.ENTERTAINER``
 *  ``music.PRELUDE``
 *  ``music.ODE``
 *  ``music.NYAN``
 * ``music.RINGTONE``
 
 
Mach deine eigene Melodie
---------------------------
Um eine Melodie zu spielen, gibst du die zu spielende Note an (C,D,E,F,G,A,B; inkl. der 
Halbtöne (z.B.: C#)). Wahlweise kannst du auch die Oktave (1-8) und die Dauer der 
Wiedergabe angeben: ::
	
	from microbit import *
	import music

	# Play a 'C'
	music.play('C')

	# Spiele ein 'C' 4 Schläge lang
	music.play('C:4')

	# Spiele 4 Schläge lang ein 'C' in der 3. Oktave
	music.play('C3:4')

	Eine Reihe von Noten nacheinander zu spielen ist einfach, du fügst die Noten, die du spielen 
	willst, einfach in eine Liste ein::

	from microbit import *
	import music

	# Lied: Frere Jacques
	lied = ["C4:4", "D4:4", "E4:4", "C4:4", "C4:4", "D4:4", "E4:4", "C4:4",
        	"E4:4", "F4:4", "G4:8", "E4:4", "F4:4", "G4:8"]
	music.play(lied)
	
Der Micro:bit merkt sich die Oktave der zuvor definierten Note. Daher kann die obige Melodie wie 
folgt umgeschrieben werden: ::

	lied = ["C4:4", "D4:4", "E4:4", "C:4", "C:4", "D:4", "E:4", "C:4",
        	"E:4", "F4:4", "G4:8", "E:4", "F:4", "G:8"]


Fortgeschrittene Funktionen
============================
Du kannst auch die Note, die du spielen willst, über ihre Frequenz mit der Methode ``pitch`` bestimmen. 
Zum Beispiel, um einen Polizeisirenen-Effekt zu erzeugen ::

	while True:
		for freq in range(880, 1760, 16):
		        music.pitch(freq, 6)
		for freq in range(1760, 880, -16):
			music.pitch(freq, 6)
	 
Kannst du erraten, was hier passiert? Jedes Mal, wenn du die Schleife durchläufst, wird eine neue Frequenz 
berechnet, indem du 16 addierst (oder subtrahierst). 

Übungsaufgaben
===============
* Erfinde deine eigene Melodie.
* Baue ein Musikinstrument. Verändere die Tonhöhe des gespielten Tons basierend auf den Messwerten des Beschleunigungsmessers.  

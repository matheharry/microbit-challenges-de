******
Funk
******
Der Micro:bit verfügt über eine Bluetooth Lowe Energy (BLE) Antenne, die zum Senden und 
Empfangen von Nachrichten genutzt werden kann.

.. image:: assets/radio.png
   :scale: 40 %
   :align: center


Grundfunktionen
================

Vorbereitung 
-------------
Bevor du den Funk benutzen kannst, darfst du nicht vergessen, das Modul ``radio`` zu importieren und 
den Funk mit ``radio.on()`` einzuschalten. Sobald der Funk eingeschaltet ist, kannst du damit Nachrichten 
von jedem anderen micro:bit in Reichweite empfangen: :: 

	from microbit import *
	import radio		

	radio.on()			

Einstellen des Kanals (Funkgruppe)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Wenn du nur Nachrichten innerhalb einer Gruppe von Geräten teilen willst, dann muss jeder micro:bit 
in der Gruppe so konfiguriert werden, dass er die gleiche Kanalnummer besitzt. Die Kanalnummer muss 
eine Zahl zwischen ``0`` und ``100`` sein: ::

	# Wähle die Kanalnummer 19
	radio.config(channel=19)	 

Es ist wichtig, dies zu tun, besonders wenn du dich in einem Raum mit anderen Leuten, die auch ihre 
micro:bits benutzen, befindest, weil dein micro:bit sonst alle Nachrichten in der Nähe mitbekommt und das 
ist nicht das, was du normalerweise willst. 

Einstellen der Sendeleistung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Zum Schluss solltest du die Sendeleistung für den Funk einstellen. Standardmäßig sendet dein micro:bit auf 
der Leistungsstufe 0, was bedeutet, dass deine Nachrichten nicht sehr weit übertragen werden. Die Sendeleistung 
kann ein Wert zwischen ``0`` und ``7`` sein.::

	# Sendeleistung auf 7 stellen
	radio.config(power=7)	

Eine Nachricht senden und empfangen
------------------------------------
Jetzt bist du bereit, eine Nachricht zu senden oder zu empfangen. Du kannst eine Zeichenkette mit einer Länge von 
bis zu 250 Zeichen senden: ::

	message_to_master = "Zwischen uns funkt es!"

	radio.send(message_to_master)


Empfange eine Nachricht: ::

    message_received = radio.receive()

Alle Teile zusammengefügt
--------------------------
::

	from microbit import * 
	import radio

	radio.on()
	radio.config(channel=19)	# Wähle deine eigene Kanalnummer
	radio.config(power=7)		# Setze das Signal auf die volle Stärke 

	message_to_master = "Zwischen uns funkt es!"
	
	# Event loop.
	while True:
		radio.send(message_to_master) 
		incoming = radio.receive()
		if incoming is not None:
		    display.show(incoming)
		    print(incoming)
		sleep(500)

Wenn du die eingehende Nachricht ausgibst, wirst du sehen, dass sie manchmal den Wert ``None`` enthält. 
Das liegt daran, dass der micro:bit manchmal nach einer Nachricht sucht, aber noch nichts angekommen ist. 
Wir können diese ``None``-Ereignisse ignorieren, indem wir prüfen, ob ``incoming`` gleich ``None`` ist 
und dann ganz einfach nichts ausgeben.

Verbindung zum Smartphone
----------------------------

Mit Hilfe der microbit Bluetooth Antenne ist es möglich, deinen micro:bit mit deinem Telefon zu verbinden und 
drahtlos mit dem micro:bit zu kommunizieren. Allerdings unterstützt MicroPython diese Fähigkeit aufgrund 
mangelnder RAM-Kapazität nicht. 

Übungsaufgaben
====================
* Sende jedes Mal eine Nachricht, wenn die Taste ``A`` gedrückt wird.
* Du benötigst für diese Aufgabe 2 micro:bits. Programmiere einen micro:bit, um Nachrichten zu empfangen und gib die empfangene Nachricht mit der Methode ``print()`` aus. Lass diesen micro:bit mit einem USB-Kabel an deinem Computer angeschlossen. Programmiere den andere micro:bit so, dass er die Beschleunigungsmesserwerte oder die Temperaturmesswerte jede Sekunde als Nachricht sendet. Trenne diesen micro:bit vom Computer und benutze eine Batterie, um ihn zu betreiben. Glückwunsch! Du hast einen Datenlogger erstellt!

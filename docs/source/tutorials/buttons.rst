***********
Tasten 
***********

.. py:module:: microbit.button

Bis jetzt haben wir Code erstellt, der das Gerät dazu bringt, einfach irgendetwas zu machen
und auszugeben. Wir reden davon, dass ein *Output* bzw. eine *Ausgabe* erzeugt wurde. Wir wollen
aber auch, dass das Gerät auf Ereignisse von Außen reagiert. Solche Ereignisse werden *Inputs*
oder *Eingaben* genannt.

Es ist leicht zu merken: Output ist das, was das Gerät in die Welt hinausgibt, während Input das
ist, was in das Gerät hineingeht, um dann verarbeiten zu werden.

Man spricht auch vom **EVA**-Prinzip: **E**ingabe - **V**erarbeitung - **A**usgabe

Das augenscheinlichste Eingabegerät auf dem micro:bit sind die beiden Tasten, die mit ``A`` und ``B``
bezeichnet sind. Du kannst die Tasten verwenden, um Eingaben vom Benutzer zu erhalten.

.. image:: assets/buttons.png
   :scale: 40 %
   :align: center

Irgendwie sollte MicroPython auf das Drücken der Tasten reagieren können. Vielleicht möchtest du dein Programm mit 
einem Tastendruck starten oder stoppen oder vielleicht möchtest du wissen, wie oft jede Taste gedrückt wurde. All 
das ist recht einfach umzusetzen.

Link zur `englischsprachigen MicroPython-Dokumentation <https://microbit-micropython.readthedocs.io/en/latest/tutorials/buttons.html>`_

Grundfunktionen
================

Wenn wir wollen, dass MicroPython auf Tastendruck-Ereignisse reagiert, sollten wir das in eine Endlosschleife setzen 
und prüfen, ob die Taste zB. gedrückt (``is_pressed``) ist.

Eine Endlosschleife ist einfach::

    while True:
        # Mach etwas

(Erinnere dich, ``while`` prüft, ob etwas wahr (``True``) ist, um herauszufinden, ob es seinen Codeblock ausführen soll. 
Da ``True`` offensichtlich immer ``True`` ist, erhältst du eine unendliche Schleife).

Prüfen, ob eine Taste gedrückt ist
------------------------------------

Manchmal wollen wir nur, dass ein Programm wartet, bis etwas passiert, zum Beispiel: wir könnten den micro:bit bitten, zu warten, bis, sagen wir, die Taste 
``A`` gedrückt wird und dann eine Nachricht ausgeben. Das geht zum Beispiel so: ::

	from microbit import *

	while True:
		if button_a.is_pressed():
			display.scroll("A")
		else:
			display.show(Image.ASLEEP)				

Das heißt, wenn die Taste ``A`` gedrückt wird, wird ein ``A`` und ansonsten ``Image.ASLEEP`` auf dem LED Display angezeigt. 

Das Problem bei der Verwendung von ``is_pressed()`` ist, dass du, wenn du die Taste nicht genau in dem Moment der Abfrage drückst, nicht 
feststellen kannst, ob die Taste jemals gedrückt wurde oder nicht. Es könnte der Fall sein, dass der Benutzer die Taste drückt, während der Code etwas anderes macht, und der Tastendruck wird übersehen. 
Die ``was_pressed()`` Funktion ist nützlich, wenn du Code schreiben willst, der gelegentlich prüft, ob die Taste gedrückt wurde, dann aber etwas anderes macht. 
Auf diese Weise solltest du nie wieder einen Tastendruck verpassen: ::

	from microbit import *

	while True:
	    if button_a.was_pressed(): 
	        display.scroll("A")
	    else:
		display.show(Image.ASLEEP)

	    sleep(1000)

Am Display wird ein ``A`` für eine Sekunde angezeigt, wenn du die Taste drückst, und dann wird ``Image.ASLEEP`` angezeigt. Wenn du die Taste drückst, während das 
Programm gerade die Zeitverzögerung auslöst, dann wird das ``A`` nicht sofort angezeigt, sondern erst, wenn die Testbedingung der if-Anweisung ausgeführt wird. Das wird umso deutlicher, je 
länger du die Verzögerung einstellst.

Versuche nun ``button_a.isPressed()`` anstelle von ``button_a.was_pressed()`` zu verwenden.

Lass uns ein ganz einfaches Cyber-Pet machen. Es ist immer traurig, außer du drückst die Taste ``A``. Wenn du die Taste ``B`` drückst, stirbt es. (Mir ist klar, dass das kein sehr angenehmes 
Spiel ist, vielleicht fällt dir etwas ein, wie man es verbessern kann)::

	from microbit import *

	while True:
		if button_a.is_pressed():
			display.show(Image.HAPPY)
		elif button_b.is_pressed():
			break
		else:
			display.show(Image.SAD)

	display.clear()

Siehst du, wie wir prüfen, welche Tasten gedrückt werden? Wir benutzen ``if``, ``elif`` (kurz für "else if") 
und ``else``. Diese werden *Bedingungen* genannt und funktionieren so::

	if something is True:
		# do one thing
	elif some other thing is True:
		# do another thing
	else:
		# do yet another thing.

Das ähnelt dem Englischen schon sehr, findest du nicht?

Die Methode ``is_pressed`` liefert nur zwei Ergebnisse: ``True`` oder ``False``.
Wenn du die Taste drückst, gibt sie ``True`` zurück, ansonsten gibt sie ``False``. 
Den obigen Code könnte man so ins Deutsche übersetzen: 
"Für immer und ewig, wenn Taste A gedrückt wird, zeige ein glückliches Gesicht, oder, wenn Taste B gedrückt wird, 
beende die Schleife. Immer sonst zeige ein trauriges Gesicht." 
Mit der ``break`` Anweisung "brechen" wir aus der Schleife aus und stoppen das eigentlich für immer und ewig laufende Programm.

Ganz am Ende, wenn das Cyber-Pet tot ist, löschen (``clear``) wir das Display.

	- Fällt dir ein Weg ein, dieses Spiel weniger tragisch zu gestalten? 
	- Wie würdest du überprüfen, ob *beide* Tasten gedrückt sind? (Tipp: weiter unten wird das behandelt).

Zählen der Anzahl der Tastendrücke
------------------------------------
Um zu zählen, wie oft eine Taste gedrückt wurde, kannst du die 
``get_presses()`` Methode verwenden.  Hier ist ein Beispiel::

	from microbit import *

	while True:
	   sleep(3000)
	   count = button_a.get_presses()
	   display.scroll(str(count))	

Der micro:bit pausiert für 3 Sekunden, wacht dann auf und überprüft, wie oft die Taste ``A`` gedrückt wurde. 
Die Anzahl der Tastendrücke wird in ``count`` gespeichert. Um ``count`` am Display auszugeben, muss man beachten, 
dass es sich dabei um eine Zahl - die Anzahl der Tastendrücke - handelt. ``scroll`` kann aber nur Strings ausgeben, 
weshalb wir den numerischen Wert in einen String aus Zeichen umwandeln müssen. Das machen wir mit der ``str`` Funktion 
(kurz für "string" ~ sie wandelt alle möglichen Objekte in Strings um).

Kannst du deine eigene ``get_presses`` Funktion erstellen? 

Erweiterte Funktionen
=====================

Überprüfung beider Tasten
---------------------------
Es ist möglich, eine Reihe von Ereignissen mit Hilfe von bedingten Anweisungen zu überprüfen. Sagen wir, du möchtest prüfen, ob die Taste ``A`` gedrückt wurde oder die Taste ``B`` gedrückt wurde oder 
ob beide Tasten zur gleichen Zeit gedrückt wurden: ::  

	from microbit import *

	while True:
	    if button_a.is_pressed() and button_b.is_pressed():
	        display.scroll("AB")
	        break
	    elif button_a.is_pressed():
	        display.scroll("A")
	    elif button_b.is_pressed():
	        display.scroll("B")
	    sleep(100)

Der obige Code zeigt den Buchstaben an, der der Taste entspricht. Wenn beide Tasten gleichzeitig gedrückt werden, wird ``AB`` angezeigt. 
Was passiert, wenn ``sleep(0)`` gesetzt bzw. ganz weggelassen wird?

 
Übungsaufgaben
===================
* Ändere, was angezeigt wird, wenn du eine Taste drückst.
* Spiele, die Benutzereingaben benötigen.

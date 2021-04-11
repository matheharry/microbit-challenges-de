***********
Tasten 
***********

.. py:module:: microbit.button

Der micro:bit hat zwei Tasten: ``A`` und ``B``.

.. image:: assets/buttons.png
   :scale: 40 %
   :align: center

Du kannst die Tasten verwenden, um Eingaben vom Benutzer zu erhalten. Vielleicht möchtest du dein Programm mit einem Tastendruck starten oder stoppen 
oder vielleicht möchtest du wissen, wie oft jede Taste gedrückt wurde. 

Grundfunktionen
================

Prüfen, ob eine Taste gedrückt ist
------------------------------------

Manchmal wollen wir nur, dass ein Programm wartet, bis etwas passiert, zum Beispiel: wir könnten den micro:bit bitten, zu warten, bis, sagen wir, die Taste 
``A`` gedrückt wird und dann eine Nachricht ausgeben. Das geht zum Beispiel so: ::

	from microbit import *

	while True:
		if button_a.is_pressed():
			display.scroll("A")
		else:
			display.scroll(Image.ASLEEP)				

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
		display.scroll(Image.ASLEEP)

	    sleep(1000)

Am Display wird ein ``A`` für eine Sekunde angezeigt, wenn du die Taste drückst, und dann wird ``Image.ASLEEP`` angezeigt. Wenn du die Taste drückst, während das 
Programm gerade die Zeitverzögerung auslöst, dann wird das ``A`` nicht sofort angezeigt, sondern erst, wenn die Testbedingung der if-Anweisung ausgeführt wird. Das wird umso deutlicher, je 
länger du die Verzögerung einstellst.

Versuche nun ``button_a.isPressed()`` anstelle von ``button_a.was_pressed()`` zu verwenden.

Zählen der Anzahl der Tastendrücke
------------------------------------
Um zu zählen, wie oft eine Taste gedrückt wurde, kannst du die 
``get_presses()`` Methode verwenden.  Hier ist ein Beispiel::

	from microbit import *

	while True:
	   sleep(3000)
	   count = button_a.get_presses()
	   display.scroll(str(count))	

Der micro:bit pausiert für 3 Sekunden, wacht dann auf und überprüft, wie oft die Taste ``A`` gedrückt wurde. Die Anzahl der Tastendrücke wird 
in ``count`` gespeichert. 

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

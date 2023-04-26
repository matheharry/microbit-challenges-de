**********
Variablen
**********

Eine Variable ist ein Name, den du verwendest, um auf einen Speicherplatz zu verweisen, an dem 
ein Wert gespeichert ist. Einfacher ausgedrückt kann man sie sich als eine Box vorstellen, die 
einen Wert speichert. Alle Variablen bestehen aus drei Teilen: einem Namen, einem Datentyp und 
einem Wert. In der Abbildung unten gibt es drei Variablen mit unterschiedlichen Datentypen:

.. figure:: assets/variable.jpg
   :scale: 50 %
   :align: center

   Source: <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables>

Die Variable ``name`` enthält die Zeichenkette ``Bob``, die Variable ``winner`` enthält den Wert ``True`` 
und die Variable ``score`` enthält den Wert ``35``.

In Python wird eine Variable erstellt, wenn ihr zum ersten Mal ein Wert zugewiesen wird. Wenn du eine 
Variable ``n`` im Code verwendest, der du vorher keinen Wert zugewiesen hast, kommt es zu folgender 
Fehlermeldung: ::

	>>> # Versuche eine undefinierte Variable abzurufen
	... n
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	NameError: name 'n' is not defined

Sobald einer Variablen ein Wert zugewiesen wurde, kann sie verwendet und dieser Wert auch verändert werden 
(es sei denn, sie ist unveränderlich - mehr darüber erfährst du im Abschnitt :ref:`Datenstrukturen`). ::

	from microbit import *

	meineAnzahl = 0

	while True:
    		if button_a.was_pressed(): 
	    		meineAnzahl = meineAnzahl + 1
	    		print("Die Taste wurde " + str(meineAnzahl) + " mal gedrückt.")
				sleep(2000)

Hier haben wir die Variable ``meineAnzahl`` benutzt, um mitzuzählen, wie oft die taste ``A`` gedrückt wird.  
Kannst du sagen, was dieser Codeschnipsel sonst noch macht?

Die ``sleep()``-Funktion werden wir oft verwenden. Um sie richtig einzusetzen, musst du dein Programm so planen, dass die 
Verzögerungen, die durch den Aufruf dieser Funktion ausgelöst werden, zu der jeweils richtigen Zeit passieren. Das
musst du genau planen!

**********
Variablen
**********

Eine Variable ist ein Name, den du verwendest, um auf einen Speicherplatz zu verweisen, an dem ein Wert gespeichert ist. Einfacher ausgedrückt kann man sie sich als eine Box vorstellen, die einen Wert speichert. 
Alle Variablen bestehen aus drei Teilen: einem Namen, einem Datentyp und einem Wert. In der Abbildung unten gibt es drei Variablen mit unterschiedlichen Datentypen:

.. figure:: assets/variable.jpg
   :scale: 50 %
   :align: center

   Source: <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables>

Die Variable ``name`` enthält die Zeichenkette ``Bob``, die Variable ``winner`` enthält den Wert ``True`` und die Variable ``score`` enthält den Wert ``35``.

In Python wird eine Variable erstellt, wenn sie zum ersten Mal zugewiesen wird. Sobald dies geschehen ist, kann der Wert der Variable verändert werden (es sei denn, sie ist unveränderlich - mehr darüber erfährst du 
im Abschnitt :ref:`Datenstrukturen`). ::

	from microbit import *

	myCount = 0

	while True:
    	   if button_a.was_pressed(): 
	   myCount = myCount + 1
	   sleep(2000)
	   print("Number of presses: " + str(myCount))

Hier haben wir die Variable ``myCount`` benutzt, um die Anzahl der Tastebetätigungen für Button ``A`` zu zählen.  Kannst du sagen, was dieser Codeschnipsel sonst noch macht?

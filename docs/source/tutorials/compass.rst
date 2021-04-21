**********
Kompass
**********
.. py:module:: microbit.compass

Ein Magnetometer misst die magnetische Feldstärke in jeder der drei Achsen. Es kann verwendet 
werden, um einen digitalen Kompass zu erstellen oder um Magnetfelder zu erforschen, wie die, 
die von einem Permanentmagneten erzeugt werden oder die um eine Spule, durch die ein Strom fließt,
entstehen.  

.. image:: assets/compass.png
   :scale: 40 %
   :align: center

Die Auswertung der magnetischen Feldstärke ist nicht einfach. Der Treiber für das Magnetometer gibt 
Rohwerte zurück. Jedes Magnetometer ist anders und muss kalibriert werden, um Abweichungen in den Rohwerten 
und Verzerrungen durch das Magnetfeld zu berücksichtigen, die durch die sogenannte Hart- und 
Weicheiseninterferenz entstehen.

Bevor du zu messen beginnst, solltest du deinen BBC micro:bit also unbedingt jedesmal kalibrieren, 
aber beachte dabei folgendes:

.. warning::

    Das Kalibrieren des Kompasses führt dazu, dass dein Programm pausiert, bis die Kalibrierung abgeschlossen 
    ist. Die Kalibrierung besteht aus einem kleinen Spiel, um durch Drehen des Geräts einen Kreis auf das LED 
    Display zu zeichnen.


Grundfunktionen
================

Die *Schnittstelle* des Magnetometers (die Art und Weise, wie Daten ausgetauscht werden) sieht sehr ähnlich aus 
wie die des Beschleunigungsmessers, außer dass wir nur die x- und y-Werte zur Richtungsbestimmung verwenden.

Denke daran, bevor du den Kompass benutzt, solltest du ihn kalibrieren, sonst können die Messwerte falsch sein: ::

    from microbit import *

    compass.calibrate()

    while True:
        x = compass.get_x() 
        y = compass.get_y() 
	print("x Wert: ", x, ", y Wert: ", y)
	sleep(500)

Dieser Code liest das Magnetfeld in zwei Richtungen (wie ein echter Kompass) aus und gibt dann die Werte zurück, 
was einfacher aussieht als es ist. Je stärker das Feld ist, desto größer ist die Zahl. Experimentiere damit und finde 
heraus, welches die x-Achse für das Magnetometer ist.

Die oberen Werte sind nicht sehr sinnvoll einsetzbar. Der micro:bit kann nach der Kalibrierung aber zum Glück die genaue 
Richtung zurückgeben, in die er gedreht ist::

   compass.heading()

Das gibt die Kompassrichtung als Ganzzahl im Bereich von 0 bis 360 an, was dem Winkel in Grad im Uhrzeigersinn 
entspricht. Norden wäre also 0. Du musst das Gerät erst kalibrieren, bevor du ``compass.heading()`` verwendest.

Übungsaufgaben
===============
* Mache den micro:bit zu einem Kompass, der die LED aufleuchten lässt, die dem Norden am nächsten liegt.
* Kalibriere dein Magnetometer. Finde heraus, ob die Kalibrierung über die Zeit (ungefähr) gleich bleibt und ob sie innerhalb oder außerhalb eines Gebäudes oder in der Nähe von etwas, das viel Stahl enthält (z.B. ein Aufzug), gleich ist.

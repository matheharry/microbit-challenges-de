Ein-/Ausgänge (E/A)
====================

An der Unterkante des BBC micro:bit befinden sich Metallstreifen, die den Eindruck erwecken, 
dass das Gerät Zähne hat. Das sind die Eingabe- und Ausgabe-Pins (oder kurz E/A Pins). Man 
nennt sie auch Input/Output bzw. I/O Pins.

Platinenstecker
----------------

Um den micro:bit und seine Funktionen vollständig zu nutzen, um mit der Welt zu kommunizieren, musst 
du etwas über seinen Platinenstecker lernen. Dieser kann verwendet werden, um sich mit externen 
Schaltungen und Komponenten zu verbinden.

.. figure:: assets/edge_connector.svg
    :align: center

    Source: https://tech.microbit.org/hardware/edgeconnector/

Einige der Stifte sind größer als andere, so dass es möglich ist, Krokodilklemmen an ihnen zu 
befestigen. Das sind die mit 0, 1, 2, 3V und GND bezeichneten Pins (Computer beginnen immer bei 
Null zu zählen). Wenn du ein sogenanntes Edge-Connector- oder BreakOut-Board am Gerät anschließt, 
kannst du auch ganz leicht Kabel an die anderen (kleineren) Pins anschließen. Die kleineren Pins 
ermöglichen dir Verbindungen zu den verschiedenen Bauteilen des micro:bit oder du
kannst sie für deine eigenen Zwecke verwenden.

Auf dem neuesten micro:bit **V2** kann auch das micro:bit Logo als Touch-Eingang verwendet werden.

Die Beschreibung der einzelnen Pins und wofür sie verwendet werden können, findest du unter <https://microbit.pinout.xyz/>. 
Siehe auch die `Entwicklerreferenz`_ für weitere Informationen. 

_`Entwicklerreferenz`: https://tech.microbit.org/hardware/edgeconnector/

Verwendung der Pins
--------------------
Jeder Pin auf dem BBC micro:bit wird durch ein *Objekt* namens ``pinN`` repräsentiert wobei ``N`` 
die Nummer des Pins ist. Um also zum Beispiel mit dem Pin etwas zu tun der mit einer 0 (Null) beschriftet 
ist, musst du in deinem Skript das Objekt namens ``pin0`` benutzen. Der Logo-Pin des **V2** 
verwendet ``pin_logo``.

Diese Pin-Objekte haben verschiedene *Methoden*, die mit ihnen verbunden sind, je nachdem, was der spezifische 
Pin kann.

Kitzeliges Python
+++++++++++++++++

Das einfachste Beispiel für eine Eingabe über die Pins ist eine Überprüfung, ob sie berührt werden. Du kannst also 
deinen micro:bit kitzeln, um ihn zum Lachen zu bringen! Und das geht so: ::

    from microbit import *

    while True:
        if pin0.is_touched():
            display.show(Image.HAPPY)
        else:
            display.show(Image.SAD)

Halte deinen micro:bit mit einer Hand am GND-Pin. Dann berührst (oder kitzelst) du mit deiner anderen Hand den 0 (Null) 
Pin. Du solltest sehen, wie sich das Display von grantig zu glücklich verändert!

Wenn du den neuesten micro:bit **V2** verwendest, kannst du auch das Standardverhalten des Pins ändern, so dass du GND 
gar nicht mehr berühren musst.::

    from microbit import *
    pin0.set_touch_mode(pin0.CAPACITIVE)
    while True:
        if pin0.is_touched():
            display.show(Image.HAPPY)
        else:
            display.show(Image.SAD)


Dabei handelt es sich um eine sehr einfache Messung eines Eingangs. Der Spaß fängt aber erst richtig an, 
wenn du Schaltungen und andere Geräte über die Pins ansteckst.

Piepsen und Quietschen
++++++++++++++++++++++

Das Einfachste, das wir an unserem micro:bit anschließen können, ist ein Piezo-Summer. Wir werden ihn für 
den Output verwenden, dh über ihn werden Töne abgespielt (oder "ausgegeben").

.. image:: https://microbit-micropython.readthedocs.io/en/v2-docs/_images/piezo_buzzer.jpg
    :width: 250px
    :align: center
    :alt: Piezo-Summer (Buzzer)


Diese kleinen Geräte spielen einen hohen Piepton, wenn sie an einen Stromkreis angeschlossen werden. Um so einen 
Summer an deinen micro:bit anzuschließen, musst du Krokodilklemmen an Pin 0 und GND befestigen, wie das unten 
gezeigt wird.

.. image:: https://microbit-micropython.readthedocs.io/en/v2-docs/_images/pin0-gnd.png
    :width: 250px
    :align: center
    :alt: Piezo-Summer verbunden mit Pin0 und GND

Das Kabel von Pin 0 sollte an den (meist längeren) positiven Anschluss des Summers angeschlossen werden.

Das folgende Programm erzeugt am Summer (Buzzer) einen Ton::

    from microbit import *

    pin0.write_digital(1)

Das macht etwa 5 Sekunden lang Spaß und dann willst du nur noch, dass das schreckliche 
Quietschen aufhört. Verbessern wir unser Beispiel und lassen das Gerät sinnvoller piepsen::

    from microbit import *

    while True:
        pin0.write_digital(1)
        sleep(20)
        pin0.write_digital(0)
        sleep(480)

Kommst du drauf, was dieses Skript macht? Denke daran, dass ``1`` in der digitalen 
Welt "an" und ``0`` "aus" bedeutet.

Das Gerät wird in eine Endlosschleife versetzt und schaltet sofort den Pin 0 ein. Das bewirkt, 
dass der Buzzer einen Piepton abgibt. Während der Buzzer piepst, macht das Gerät für 20 Millisekunden 
Pause (es "schläft") und schaltet dann Pin 0 aus. Das ergibt den Effekt eines kurzen Piepsens. 
Danach macht das Gerät eine 480 Millisekunden Pause, bevor an den Beginn der Schleife zurückgesprungen
wird und alles wieder von vorne anfängt. Das bedeutet, dass du zwei Pieptöne pro Sekunde (einer alle 
500 Millisekunden) hörst.

Wir haben ein sehr einfaches Metronom gebaut!

.. footer:: Das Bild des Pizeo Buzzers ist CC BY-NC-SA 3.0 von https://www.flickr.com/photos/tronixstuff/4821350094

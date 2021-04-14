Input/Output
------------

An der Unterkante des BBC micro:bit befinden sich Metallstreifen, die den Eindruck erwecken, 
dass das Gerät Zähne hat. Das sind die Input/Output Pins (oder kurz I/O Pins).

.. image:: https://microbit-micropython.readthedocs.io/en/v2-docs/_images/blue-microbit.png
    :width: 300px
    :align: center
    :alt: micro:bit mit beschrifteten Pins

Einige der Stifte sind größer als andere, so dass es möglich ist, Krokodilklemmen an ihnen zu 
befestigen. Das sind die mit 0, 1, 2, 3V und GND bezeichneten Pins (Computer beginnen immer bei 
Null zu zählen). Wenn du ein sogenanntes Edge-Connector- oder BreakOut-Board am Gerät anschließt, 
kannst du auch ganz leicht Kabel an die anderen (kleineren) Pins anschließen.

Auf dem neuesten micro:bit **V2** kann auch das micro:bit Logo als Touch-Eingang verwendet werden.

Jeder Pin auf dem BBC micro:bit wird durch ein *Objekt* namens ``pinN`` repräsentiert wobei ``N`` 
die Nummer des Pins ist. Um also zum Beispiel mit dem Pin etwas zu tun der mit einer 0 (Null) beschriftet 
ist, musst du in deinem Skript das Objekt namens ``pin0`` benutzen. Der Logo-Pin des **V2** 
verwendet ``pin_logo``.

Einfach!

Diese Objekte haben verschiedene *Methoden*, die mit ihnen verbunden sind, je nachdem, was der spezifische 
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

Bleeps and Bloops
+++++++++++++++++

The simplest thing we can attach to the device is a Piezo buzzer. We're going
to use it for output.

.. image:: https://microbit-micropython.readthedocs.io/en/v2-docs/_images/piezo_buzzer.jpg

These small devices play a high-pitched bleep when connected to a circuit. To
attach one to your BBC micro:bit you should attach crocodile clips to pin 0 and
GND (as shown below).

.. image:: https://microbit-micropython.readthedocs.io/en/v2-docs/_images/pin0-gnd.png

The wire from pin 0 should be attached to the positive connector on the buzzer
and the wire from GND to the negative connector.

The following program will cause the buzzer to make a sound::

    from microbit import *

    pin0.write_digital(1)

This is fun for about 5 seconds and then you'll want to make the horrible
squeaking stop. Let's improve our example and make the device bleep::

    from microbit import *

    while True:
        pin0.write_digital(1)
        sleep(20)
        pin0.write_digital(0)
        sleep(480)

Can you work out how this script works? Remember that ``1`` is "on" and ``0``
is "off" in the digital world.

The device is put into an infinite loop and immediately switches pin 0 on. This
causes the buzzer to emit a beep. While the buzzer is beeping, the device
sleeps for twenty milliseconds and then switches pin 0 off. This gives the
effect of a short bleep. Finally, the device sleeps for 480 milliseconds before
looping back and starting all over again. This means you'll get two bleeps per
second (one every 500 milliseconds).

We've made a very simple metronome!

.. footer:: The image of the pizeo buzzer is CC BY-NC-SA 3.0 from https://www.flickr.com/photos/tronixstuff/4821350094

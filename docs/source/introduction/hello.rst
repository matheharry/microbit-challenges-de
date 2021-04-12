**************************
Hello, World!
**************************

Der traditionelle Weg, mit der Programmierung in einer neuen Sprache zu beginnen, ist, den
Computer dazu zu bringen, "Hello, World!" zu sagen.

.. image:: ../scroll-hello.gif

Mit MicroPython ist das ganz einfach::

    from microbit import *
    display.scroll("Hello, World!")

Erklärungen und Grundbegriffe
=============================

Jede Zeile führt etwas Bestimmtes aus. Die erste Zeile::

    from microbit import *

...sagt MicroPython, dass es sich alles besorgen soll, was es benötigt, um mit dem BBC micro:bit 
zu arbeiten. All dieses     Zubehör befindet sich in einem Modul namens ``microbit`` (ein Modul 
ist eine Bibliothek mit bereits existierendem Code). 
Wenn du etwas mit ``import`` importierst, sagst du MicroPython, dass du es benutzen willst, und ``*`` 
ist Pythons Art, *alles* zu sagen. Also bedeutet ``from microbit import *`` auf Deutsch: "Ich möchte 
alles aus der microbit Code Bibliothek verwenden können".

Die zweite Zeile::

    display.scroll("Hello, World!")

...weist MicroPython an, das Display zum Scrollen der Zeichenkette "Hello, World!" zu verwenden. 
Der ``display`` Teil dieser Zeile ist ein sogenanntes *Objekt* aus dem ``microbit``-Modul, das 
das LED-Display des Gerätes repräsentiert (wir sagen "Objekt" anstelle von "Ding", "Dings" oder "Dingsbums"). 
Wir können dem Display sagen was es tun soll, indem wir einen Punkt ans Ende setzen ``display.``, gefolgt von 
etwas, das wie ein Befehl aussieht (tatsächlich nennt man das eine *Methode*). In diesem Fall benutzen wir die 
Methode ``scroll`` die eine Laufschrift erzeugt. Da ``scroll`` wissen muss, welche Zeichen über das Display gescrollt 
werden sollen, übergeben wir diese Zeichen zwischen doppelten Anführungszeichen (``"``) innerhalb von Klammern (``(`` und ``)``). 
Diese werden die *Argumente* genannt. 

Zum Beispiel bedeutet ``display.scroll("Hello, World!")`` auf Deutsch: "Ich möchte, dass du mit dem Display den Text 
'Hello, World!' über den Bildschirm laufen lässt". Wenn eine Methode keine Argumente benötigt, machen wir dies durch 
leere Klammern wie diese deutlich: ``()`` - die Klammern dürfen also nie weggelassen werden!

Kopiere den "Hello, World!"-Code in deinen Editor und flashe ihn auf das Gerät. 

    - Kannst du herausfinden, wie du die Nachricht ändern kannst? 
    - Kannst du den micro:bit dazu bringen, dass er "Hallo" zu dir sagt? Er könnte zum Beispiel "Hallo, Nikolaus!" sagen. 
    Kleiner Tipp: du musst das Argument der Scroll-Methode ändern.

.. warning::

    Es kann sehr leicht sein, dass etwas nicht funktioniert. :-)

    Dann beginnt der Spaß erst richtig! MicroPython versucht, hilfreich zu sein. Wenn
    es auf einen Fehler stößt, scrollt es eine hilfreiche Nachricht auf dem micro:bit
    Display. Wenn möglich, wird es dir die Zeilennummer sagen, in der der Fehler
    gefunden werden kann.

    Python erwartet, dass du **EXAKT** das Richtige tippst. Also, zum Beispiel,
    ``Microbit``, ``microbit`` und ``microBit`` sind alle unterschiedliche Dinge für
    Python. Wenn MicroPython sich über einen ``NameError`` beschwert, ist es wahrscheinlich
    weil du etwas ungenau getippt hast. Es ist wie der Unterschied
    zwischen "Nicholas" und "Nicolas". Es sind zwei verschiedene Personen
    aber ihre Namen sehen sich sehr ähnlich.

    Wenn MicroPython sich über einen ``SyntaxError`` beschwert, hast du den Code einfach
    auf eine Weise eingegeben, die MicroPython nicht verstehen kann. Überprüfe, ob du nicht irgendwelche
    Sonderzeichen wie ``"`` oder ``:`` vergessen oder hinzugefügt hast. Das ist so, als ob du einen Punkt in der
    Mitte eines Satzes stehen hast. Es ist dann schwer zu verstehen, was du genau meinst.

    Dein Microbit reagiert möglicherweise nicht mehr: Du kannst keinen neuen Code flashen oder
    Befehle in der REPL eingeben. Wenn das passiert, versuche es mit einem Neustart. Das
    heißt, ziehe das USB-Kabel (und das Batteriekabel, falls es angeschlossen ist), dann stecke
    das Kabel wieder ein. Eventuell musst du auch deine Code-Editor Anwendung beenden und neu starten.

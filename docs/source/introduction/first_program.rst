**********************
Ein Programm schreiben
**********************

Im Allgemeinen besteht der Prozess des Code-Entwurfs aus diesen 4 Schritten. Du kannst davon ausgehen, 
dass du die Schleife ein paar Mal durchlaufen musst, bevor dein Code funktioniert.

.. image:: assets/microbit_lifecycle.jpg
   :scale: 70%   
   :align: center


Den Code entwerfen (Design & Edit)
----------------------------------

Als erstes wirst du ein Programm schreiben, das die Nachricht "Hallo PH Graz!" gefolgt von einem Bild auf dem Display 
deines micro:bit anzeigt. Danach soll "Hello world" auf der REPL-Befehlszeile ausgegeben werden. 

Es ist ratsam, darüber nachzudenken, was du mit deinem Code erreichen willst und wie du es erreichen willst, 
bevor du mit dem Schreiben beginnst. Es gibt hier zwar nicht viel zu planen oder entwerfen, aber nur, damit du
verstehst, wie so ein Plan aussehen könnte::

    Für immer wiederholen:
      Scrolle "Hallo PH Graz" über das LED Display
      Ein lachendes Gesicht anzeigen 
      Gib "Hello world!" auf der Konsole aus
      Für zwei Sekunden warten

Es gibt zwei Möglichkeiten, die Ausgabe deines Codes anzuzeigen: Entweder du nutzt die auf dem micro:bit verfügbaren 
Ausgaben (z.B. die LEDs) oder die :ref:`REPL`-Konsole, die im Editor mit der ``print`` Anweisung 
ansteuerbar ist. Die Konsole ist besonders nützlich, um Bugs (Fehler) in deinem Code zu finden oder
neue Konzepte oder Ideen auszuprobieren.  

Gehen wir den Code, der unsere Planung in Python realisiert, Zeile für Zeile durch::

    from microbit import *

Der Import von Paketen (wie microbit) in Python ermöglicht es uns, Funktionen oder Objekte zu verwenden, die in reinem
Python nicht definiert sind. In unserem Fall sind es zum Beispiel die Funktionen ``display`` oder ``show``. ::     

	while True: 

In diesem Fall soll etwas (was auch immer dieser Anweisung folgt und eingerückt ist) ausgeführt werden, während die Bedingung,
die auf ``While`` folgt, wahr ist. In diesem Fall ist die Bedingung das Schlüsselwort ``True``, was bedeutet, dass diese Schleife
ewig weiterläuft. Es ist dasselbe, als wenn du zB "Mach das solange wie 5 > 1 ist" schreiben würdest, was ja für immer und ewig
der Fall sein wird. 

Der Rest des Programms ist ganz einfach ::

	display.scroll('Hallo PH Graz')
   display.show(Image.HAPPY)
	print('Hello world!')    
   sleep(2000)
      
Es wird ``Hallo PH Graz`` und dann das lachende Gesicht auf dem LED Display angezeigt. 
Die Anweisung ``print('Hello world!')``, gibt die Nachricht in der REPL-Konsole aus. 

Programm auf den micro:bit laden (Flashen)
------------------------------------------

Klicke nun auf die Taste ``Send to micro:bit`` und schau was passiert.

.. image:: assets/first_program.gif
   :scale: 70%
   :align: center 

Das Ergebnis auf dem micro:bit sollte in etwa so aussehen wie in der simulierten Vorschau. 

Um das REPL-Fenster des micro:bit anzuzeigen, musst du die untere ``Show Serial``-Schaltfläche anklicken:

.. image:: assets/microbiteditor-serial.png
   :scale: 50%
   :align: center

Das REPL-Fenster zeigt uns Nachrichten vom micro:bit an und erlaubt uns auch, Befehle direkt an den micro:bit zu senden. Für den
Moment werden wir die REPL nur benutzen um Nachrichten und Fehlermeldungen zu sehen, die wir mit dem ``print``-Befehl ausgeben. 

Etwas ändern 
-------------

Der beste Weg, um zu lernen, wie etwas funktioniert, ist zu versuchen, den Code ein wenig 
zu verändern, um zu sehen was dann passiert. Und die *Dokumentation zu lesen*, um zu sehen, 
was alles möglich ist, gehört sowieso auch zum Alltag von Programmierern.

**Fragen, die du dir stellen könntest:**

   - Wozu ist die Verzögerung (``sleep()``) da? Ist sie notwendig? Versuche einmal sie zu entfernen.
   - Was passiert, wenn du ``True`` durch ``False`` ersetzst?
   - Was passiert, wenn du ``scroll()`` durch ``show()`` ersetzst?

Überblick über die Arbeitsweise
---------------------------------

Um Programme für den micro:bit schreiben zu können, musst du wissen, welche Befehle er verstehen kann 
und wie man diese in Python hinschreiben muss. Da man sich die ganzen Regeln und Begriffe (vor allem 
am Anfang) schwer merken kann, muss man wissen wo man nachschauen kann. Du wirst also sehr oft zwischen 
diesem Tutorial und dem **Web-Editor** hin- und herwechseln, oder in der Referenz nachsehen, wenn etwas
unklar ist. 

Da in diesem Tutorial nur das allernötigste zu Python beschrieben wird, um mit dem micro:bit arbeiten 
zu können, sind auch noch andere Unterlagen vorhanden, mit denen man noch mehr über Python erfahren kann.

.. seealso:: 
   - Schau dir auch die komplette `micro:bit Dokumentation für MicroPython`_ an.
   - Um die Programmiersprache Python besser kennenzulernen stehen auch interaktive `Jupyter-Notebooks`_ zur Verfügung. Hier kannst du direkt Dinge ausprobieren und lernst dabei, wie Python 3 funktioniert.

   .. _`micro:bit Dokumentation für MicroPython`: https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html
   .. _`Jupyter-Notebooks`: https://matheharry.github.io/Python-Crashkurs/

   .. image:: assets/arbeitsweise.png

Nun hast du dein erstes Programm geschrieben und damit herumexperimentiert. In den nächsten Abschnitten erfährst
du mehr über das Schreiben komplexerer Programme und über weitere Einsatzmöglichkeiten des micro:bit.

**************************
Micro:bit - Übersicht 
**************************

Der BBC micro:bit ist ein programmierbarer Mikrocomputer bzw. Mikrocontroller - mit dem man alle möglichen Projekte erstellen kann, von Robotern bis hin zu Musikinstrumenten - 
die Möglichkeiten sind endlos. Lass uns einen Blick auf die Funktionen werfen, die du in deinen Programmen verwenden kannst:

 * 25 rote LED-Lichter, die Nachrichten und Bilder anzeigen können.
 * Zwei programmierbare Tasten (A und B), mit denen du dem micro:bit sagen kannst, wann er etwas starten und stoppen soll.
 * Ein Thermistor, um die Temperatur zu messen.
 * Ein Lichtsensor, um die Veränderung des Lichts zu messen.
 * Ein Beschleunigungssensor, um Bewegungen zu erkennen.
 * Ein Magnetometer, um dir zu sagen, in welche Richtung du gehst.
 * Eine Funk- und eine Bluetooth-Verbindung, um mit anderen Geräten zu interagieren.

.. figure:: assets/microbit-hardware-access.jpg
   :scale: 35%
   :align: center
   
   Source: https://microbit.org/guide/features/

Du kannst den micro:bit mit verschiedenen Sprachen_ programmieren.

.. _Sprachen: https://microbit.org/code/

Zur Auswahl stehen MicroPython, C++ oder JavaScript. Dieses Tutorial konzentriert sich auf das Programmieren von 
micro:bit mit MicroPython, aber wenn du bereits mit Python vertraut bist oder eine zusätzliche Herausforderung suchst, 
schau dir den Abschnitt :ref:`Programmierung des micro:bit mit anderen Sprachen` an. 
C/C++ könnte besonders nützlich sein, da es die Hauptsprache ist, die für die Programmierung von Embedded-Geräten verwendet wird.

MicroPython ist eine Version von Python_, die auf Mikrocontrollern wie dem micro:bit laufen kann. Da die Funktionalität der beiden nahezu identisch ist (siehe hier_ für den Unterschied 
im Verhalten), beziehen wir uns in diesen Tutorials auf die verwendete Sprache als Python. Programmieren in Python besteht aus
dem Beschreiben einer Reihe von Schritten, die ausgeführt werden sollen. An welche genau einzuhaltende Regeln (ähnlich wie der Grammatik beim Sprachenlernen) du dich dabei halten musst,
lernst du Schritt für Schritt, wenn du deine ersten Programme schreibst.  

.. _Python: https://www.python.org/
.. _hier: https://docs.micropython.org/en/latest/genrst/index.html
.. figure:: assets/programming.jpg
   :align: center 
   :scale: 30 %

   Source: HOMEWORK

Leitfaden für diese Anleitung
===============================

Die Abschnitte dieses Tutorials führen dich durch das Programmieren mit dem micro:bit, die Grundlagen der Programmierung und die Funktionen des micro:bit. Das Ziel ist es, dich mit dem Programmieren vertraut zu machen 
Programmierung zu bringen, so dass du ein eigenes kleines Projekt erstellen kannst, das du uns in der ersten Woche zeigen wirst, um dich mit der Programmierung von #circular_definition vertraut zu machen. 

Du brauchst dich nicht unbedingt akribisch durch die ganze 
Theorie, die in Grundlagen der Programmierung behandelt wird, durcharbeiten, besonders wenn du ein Anfänger bist. Fange an, einfache Programme mit dem micro:bit zu schreiben und lerne nach und nach  
weitere Programmierkonzepte kennen indem du weiterliest. Fühle dich frei, die Teile zu überspringen, in denen du dich sicher fühlst und wähle die Teile, die wichtig sind. Während du mehr über das Programmieren lernst, wirst du natürlich immer 
bessere und effizientere Wege finden, um deine Projekte der Vergangenheit zu erledigen, aber im Moment solltest du dich darauf konzentrieren, den Einstieg zu finden.

Die hier behandelten Themen werden in der Regel nur gestreift und viele Dinge werden absichtlich nicht erklärt. Einige der wichtigen Fähigkeiten
die du im Laufe der Schule und deiner späteren Arbeit brauchen wirst, sind das selbstständige Erforschen von Materialien und die Fähigkeit, offizielle Dokumente zu lesen. 
Daher solltest du ruhig auch andere Unterlagen lesen, als die, die du hier findest.  

Wenn deine Fähigkeiten mittel bis fortgeschritten sind, wirst du diese Dokumentation vielleicht nicht sehr interessant finden. Wie auch immer, der micro:bit ist ein äußerst flexibles Gerät und du könntest dann vielleicht 
die micro:bit runtime_ erkunden, die dir mehr Flexibilität bei der Verwendung des Geräts bietet.  

.. _runtime: https://lancaster-university.github.io/microbit-docs/

.. note:: Wenn du dich beim Lesen der Tutorials verwirrt fühlst oder das Gefühl hast, dass du mehr Anleitung brauchst, um mit dem Programmieren zu beginnen, 
   lass dich nicht entmutigen! Es gibt eine Reihe von kostenlosen Online-Kurse, die dir die Grundlagen der Programmierung mit Python näher bringen, wie zum Beispiel 
   dieser_. Versuche, die ersten paar Lektionen durchzugehen, und alles sollte mehr Sinn machen.

.. _dieser: https://www.python-lernen.de/ 
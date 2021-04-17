********************
Klassen und Objekte
********************

Python ist eine objektorientierte Sprache - sie basiert auf dem Konzept der "Objekte", die verschiedene Felder 
(Variablen) und Methoden (Funktionen, die diese Variablen verändern) enthalten. Alles in Python ist ein Objekt - 
egal ob es ein Integer oder ein String ist. 

Ein Objekt ``object`` ist ein praktisches Konzept, um eine Abbildung von etwas Abstraktem zu erzeugen - zum 
Beispiel ein nützlicher Weg, um Daten geordnet zu speichern. 

Erinnert dich das an etwas, das wir schon behandelt haben? 

Eine Liste ist ein schönes Beispiel dafür, dass in einem Objekt Daten geordnet gespeichert werden. Wie würdest 
du ein Listenobjekt beschreiben? Welche Attribute hat es? Wann und wie wird es verwendet? 

.. tip:: Erinnerst du dich an den Befehl ``dir(ClassName)``? Er listet alle Attribute und Methoden einer benötigten 
    Klasse auf, wie zum Beispiel ``dir(str)``. 

Wenn du feststellst, dass du ein Objekt brauchst, das Python nicht hat, kannst du dein eigenes erstellen. Bevor du 
ein konkretes Exemplar deines Objekts (eine *Instanz*) verwenden kannst, musst du zuerst eine "Vorlage" definieren, 
die beschreibt, wie das Objekt aussehen wird und was es kann. Dieser Prototyp wird als *Klasse* bezeichnet::

    class Player():                                                 

Dieses Beispiel zeigt die Vorlage eines Player-Objekts, das im Moment noch leer und nicht sehr nützlich ist. Um es 
nützlicher zu machen, können wir ihm Attribute hinzufügen - ``total_count`` ist ein 
Klassenattribut, das alle Instanzen von Objekten der Klasse Player zählt, indem es jedes Mal, wenn ein neues Player()-Objekt 
erzeugt wird, einen Wert erhöht. ::

    class Player():
        total_count = 0

Ein Klassenattribut ist für jede Instanz der Klasse Player gleich, und so kannst du die Gesamtzahl der Spieler über jede erzeugte 
Instanz herausfinden.
Andere Attribute, die nützlich sein könnten, wären Instanzattribute (unterschiedlich für jede Instanz eines Objekts) wie Name und 
Punktestand. 
Wie sollen diese definiert werden? Und wie können wir wissen, wann ein neues Objekt erstellt wird, um die ``total_count`` zu erhöhen? 

Es ist möglich, eine ``__init__()`` Methode für deine Klasse zu definieren, die bei der Erzeugung eines neuen Objekts verwendet 
wird und die weitere Argumente aufnehmen und 
den Anfangszustand eines Objekts festlegen kann. Auf diese Weise wird bei der Erzeugung des untenstehenden Objekts ``player_1`` 
der anfängliche Punktestand des Spielers Null sein, 
der Name wird als Argument angegeben und ``total_count`` wird um eins erhöht. ::

    class Player():
        total_count = 0
        
        def __init__(self, name):
            self.name = name
            self.score = 0
            self.__class__.total_count += 1

Außerdem können wir Methoden speziell für unsere Klasse von Objekten definieren. Zum Beispiel die Klassenmethoden ``update_score()`` 
und ``change_name`` um die Werte von ``name``
und dem Punktestand ``score`` zu aktualisieren.  ::

    class Player():
        total_count = 0

        def __init__(self, name):
            self.name = name
            self.score = 0
            self.__class__.total_count += 1

        def update_score(self, score):
            self.score = score

        def change_name(self, name):
            self.name = name    

Die Erzeugung von Objekten und die Verwendung von Methoden ist ziemlich einfach: ::

    # Erzeuge eine Instanz eines Objekts der Klasse Player
    player_1 = Player("griever418")
    player_2 = Player("r00t")

    # Verändere den Punktestand von player_1 
    player_1.update_score(40)
    # Ändere den Namen von player_1 
    player_2.change_name("bott0m")


Nun könntest du dich fragen, warum der Aufruf von Methoden auf ``player_1`` oder ``player_2`` nur mit einem 
Argument funktioniert, während die Methodendefinitionen zwei Argumente haben? 
Sicherlich gibt Python in diesem Fall einen Fehler aus. Wie du vielleicht schon vermutet hast, wird die Instanz 
des Objekts - ``player_1`` - als erstes Argument übergeben, und ist eigentlich gleichbedeutend mit 
der Anweisung ``player.update_score(player_1, 40)``. 

.. note:: Das Schlüsselwort ``self`` hat in Python keine besondere Bedeutung, es ist nur eine Art Gewohnheit. Du 
    solltest es benutzen, wenn auch nur aus dem Grund, um deinen Code besser lesbarer zu machen, wenn du nach 
    einiger Zeit wieder darauf zurückkommst (du kannst mehr über die Diskussion von ``self`` in diesem Blogpost_ 
    von Guido van Rossum lesen - dem Vater von Python).

.. _Blogpost: http://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html


Der Zugriff auf Attribute ist für alle Objekte wieder gleich: ``obj.attribute_name``. Um zum Beispiel den Namen eines 
Player-Objekts auszugeben, schreibst du: ::

    print(player_1.name)

Um ein Attribut für eine Klasse zu erstellen, musst du es nicht in der Klassendefinition deklarieren - sie sind wie 
lokale Variablen, da sie entstehen, wenn ihnen ein Wert 
zugewiesen wird. Auf diese Weise können wir ein ``counter``-Attribut für unser ``player_1`` Objekt erstellen. Was gibt 
das folgende Programm dann aus? ::

    player_1.counter = 0

    while (player_1.counter < 10):
        player_1.counter += 1

    print(player_1.counter)    

Es gibt noch viele weitere Besonderheiten und nützliche Eigenschaften von Klassen, auf die wir in diesem Tutorial nicht 
eingehen. Wenn du mehr erfahren willst, schau in die Python Dokumentation_.

.. _Dokumentation: https://docs.python.org/3/tutorial/classes.html#a-word-about-names-and-objects

.. figure:: assets/snake_nokia.png 
    :scale: 70%
    :align: center

Um dir ein weiteres Beispiel für die Verwendung von Klassen zu geben, schau dir diese *Snake*-Klasse an, die für eine 
micro:bit Version des Snake Spiels verwendet werden könnte. :: 

    class Snake:

            def __init__(self):
                self.x_position = 0
                self.y_position = 0
                self.direction = "w"

            def move_snake(self, x_position, y_position, direction):
                self.x_position = x_position
                self.y_position = y_position 
                self.direction = direction

            def show_snake(self):
                display.set_pixel(self.x_position, self.y_position, 9)
                sleep(600)
                display.set_pixel(self.x_position, self.y_position, 0)

    # Erstelle eine Instanz eines Snake Objekts unter der Bezeichnung python
    python = Snake()

    # greife auf seine Position auf der X-Achse zu und gib sie aus
    print(python.x_position)

    # Bewege python nach rechts
    python.move_snake(python.x_position + 1, python.y_position)   
   

.. figure:: assets/snake.png 
	 :align: center
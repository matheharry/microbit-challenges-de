**********************
Schere, Stein, Papier
**********************

Wir wollen hier versuchen, das bekannte Spiel *Schere - Stein - Papier* auf 
unterschiedliche Art und Weise umzusetzen. Dabei lernen wir Schritt für 
Schritt mittels Python unseren micro:bit zu steuern.

SSP 1 - Die Grundlagen
======================
Hier wollen wir den micro:bit nur dazu verwenden, ein entsprechendes Bild am Display 
anzuzeigen. Das Spiel kann dann mit anderen gespielt werden, nur dass man keine 
Hände verwendet.

Wir benötigen also 3 Bilder. Diese speichern wir in 3 Variablen. Um anzuzeigen, dass die
Werte dieser Variablen im Programm nicht verändert werden sollen, schreiben wir sie in
Großbuchstaben. Die Bilder könnten zB so aussehen: ::

    from microbit import *

    SCHERE = Image("99009:99090:00900:99090:99009:")
    STEIN  = Image("09990:99999:99999:09990:00000:")
    PAPIER = Image("00000:09990:09990:09990:09990:")

Die Auswahl soll mittels der Tasten erfolgen.

* ``Taste A`` -> zeige die Schere an
* ``Taste B`` -> zeige den Stein an
* ``Tasten A+B`` -> zeige das Papier an

Da das Spiel nicht nur einmal zu spielen sein soll, soll der micro:bit andauernd darauf 
achten, welche Taste gedrückt wurde. Deshalb benötigen wir, wie bei fast allen Programmen 
die auf einem Mikrochip laufen, eine :ref:`Endlosschleife` mit ``while True``. 

SSP 2 - Zufälliges Bild
========================
Dieses mal bestimmen nicht wir, welches Bild angezeigt wird. Der micro:bit soll zufällig eines der
3 Bilder auswählen und zeigen, wenn wir die ``Taste A`` drücken. So können wir miteinander
oder auch selbst gegen den micro:bit spielen. 

Spannender wird das, wenn wir auch einen Countdown einbauen, der 3 - 2 - 1 herunterzählt, bevor er 
das Bild anzeigt! Kannst du das mit einer for-Schleife machen?

SSP 3 - Schütteln und Highscore
================================
Wir können die vorige Variante so abändern, dass alles ganz ohne Taste und nur durch Schütteln 
des micro:bit funktioniert!

Die 2 Tasten verwenden wir, um den Punktestand mitzuzählen und anzuzeigen.

* ``Taste A`` zählt die Siege des micro:bits 
* ``Taste B`` zählt deine Siege

SSP 4 - Der micro:bit lernt die Regeln
=======================================
Wir kombinieren die ersten 2 Versionen und bringen dem micro:bit die Regeln des Spiels bei.

* Wie in *SSP 1* wählen wir über die Tasten unser Bild, das dann angezeigt wird.
* Jetzt wählt der micro:bit wie in *SSP 2* ein zufälliges Bild, das uns nach einem Countdown angezeigt wird.
* Für uns ist jetzt natürlich klar, wer gewonnen hat. Wir freuen uns, wenn wir gewonnen haben, langweilen uns über ein Unentschieden oder sind traurig, wenn wir verloren haben. Genau diese Reaktionen wollen wir auch von unserem micro:bit sehen!

In einem ersten Schritt müssen wir uns die Regeln als *Wenn ..., dann ...* Sätze notieren. 
Wir stellen uns das Ganze aus der Sicht des micro:bit vor, der glücklich dreinschauen soll,
wenn er gewonnen hat. Beim Verlieren soll er natürlich traurig sein und sonst solala.
Das könnte, angelehnt an die Schreibweise der Python ``if``-Bedingungen, so aussehen: ::

    Wenn microbit == spieler:
        Unentschieden (😐)
    Sonst wenn spieler == SCHERE:
        Wenn microbit == STEIN:
            Gewonnen! (😁)
        Sonst:
            Verloren! (😞)
    Sonst wenn spieler == STEIN:
        ...

So kommen wir zu verschachtelten ``if``-Bedingungen. Das funktioniert zwar, ist aber nicht 
sehr elegant. Besser geht das, wenn wir sogenannte :ref:`Logische Operationen` verwenden.
Auf diese Weise können wir mit Und ``and`` bzw. Oder ``or`` die Regeln schöner formulieren. 
zB. ::

    Wenn (microbit == SCHERE and spieler == PAPIER) or (microbit == STEIN and ...

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

SSP 4 - 


SSP 4 - 




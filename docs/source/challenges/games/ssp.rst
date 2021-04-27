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
Großbuchstaben. ::

    from microbit import *

    SCHERE = Image("99009:99090:00900:99090:99009:")
    STEIN  = Image("09990:99999:99999:09990:00000:")
    PAPIER = Image("00000:09990:09990:09990:09990:")


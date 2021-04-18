********
Theremin
********

Beschreibung
============
In diesem Projekt werden wir den Beschleunigungsmesser benutzen, um die Frequenz eines Tons zu kontrollieren.  

Das Theremin ist ein seltsames und wunderbares elektronisches Instrument, das keinen Körperkontakt benötigt. 
Das Theremin wurde 1920 von Léon Theremin, einem frühen russischen Elektronik-Ingenieur, erfunden. Es wird gespielt, 
indem man seine Hände in der Nähe von zwei Antennen bewegt - die erste steuert die Lautstärke des Ausgangs und die 
zweite die Tonhöhe.

Für die musikinteressierten ist es wissenswert, dass das Theremin Robert Moog zur Erfindung des Synthesizers 
inspiriert hat. Obwohl es also ein wenig genutztes Instrument ist, hatte es einen starken Einfluss auf die Geschichte 
der Musik.

.. figure::  assets/leon_theremin.jpg

   Bild: Leon Theremin, Quelle: Wikipedia


Übrigens: ein kurzer Blick auf Listen
--------------------------------------

Als Teil dieser Aufgabe musst du einige Werte des Beschleunigungsmessers sammeln und in einer Liste 
speichern und dann deren Durchschnitt berechnen. Hier sind einige Informationen darüber, wie man das macht. 

Eine Liste ist eine Datenstruktur, die in so gut wie allen Programmiersprachen verwendet wird. In unserem Fall, 
ist es eine nummerierte Sammlung von Beschleunigungssensorwerten. Im Wesentlichen ist es eine Sammlung von Kästchen, 
in die wir Werte eintragen können - jedes Kästchen hat eine Nummer, beginnend bei 0 und aufsteigend.

Angenommen, wir wollen die letzten 30 Werte des Beschleunigungssensors speichern, dann erstellen wir eine Liste 
und fügen jedes Mal, wenn wir die Schleife wie folgt durchlaufen, den Wert des Beschleunigungssensors 
zu dieser Liste hinzu:: 
        
        while True:

            x_acceleration = accelerometer.get_x()

            # Zur Liste der Messwerte hinzufügen
            messungen.append(x_acceleration)
        
            # Wenn die Messwerte mehr als 30 Werte enthalten, wird der erste Wert vom Anfang an gelöscht.
            if len(messungen) > 30:
                messungen.pop(0)
            sleep(1)
        
Wie du sehen kannst, wenn die Liste mehr als 30 Einträge hat, löschen wir nur den ersten Eintrag, 
Element Nummer 0, mit der Methode ``pop()``::

        messungen.pop(0)
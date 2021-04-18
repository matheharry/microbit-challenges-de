**************
Morsealphabet
**************

Beschreibung
============

Das Morsealphabet wurde 1836 von einer Gruppe von Menschen erfunden, zu denen 
auch der amerikanische Künstler Samuel F. B. Morse gehörte. Mit dem Morsealphabet 
wird eine Nachricht als eine Reihe von elektrischen Impulsen dargestellt, die entlang 
von Kabeln zu einem Elektromagneten am empfangenden Ende des Systems gesendet werden 
können.  Die Symbole, die für jeden Buchstaben verwendet werden, sind in der Abbildung 
unten dargestellt. 

.. figure:: assets/morse.png
   :scale: 60 %
   :align: center
   
   Source: raspberrypi.org

Natürlich bist du nicht auf elektrische Impulse beschränkt, du kannst eine Morsebotschaft 
auch mit Licht oder sogar mit Ton übertragen. Eine Morsenachricht, die über elektrische Kabel 
gesendet wird, ist als Telegramm bekannt - eine Nachricht, die von einem Funker am sendenden 
Ende mit einer Morsetaste wie der hier abgebildeten in Morsecode übersetzt wird.

.. figure:: assets/J38TelegraphKey.jpg
   :scale: 60 %
   :align: center

    Morsetaste, Quelle: Wikipedia 

Die Nachricht wird von einem anderen Funker auf der Empfangsseite wieder in normalen Text umgewandelt. 

Deine Aufgabe ist es, den micro:bit in eine Maschine zu verwandeln, die Nachrichten mit Morsecode 
verschlüsseln kann. Wir werden die zu konvertierende Nachricht *plain Text* nennen.  

Du wirst das Alphabet mit dem Morsecode in deinem Programm speichern müssen. Du kannst dafür ein Python 
*Dictionary* verwenden. Hier ist ein Teil eines Python-Dictionarys für Morsecode::

    morse_code = { 'A':'.-', 
                   'B':'-...',
                   'C':'---.', 
                    ...  }

Auf Deutsch bedeutet das: das Zeichen `A` soll durch die Zeichenkette `.-` ersetzt werden; das Zeichen `B` 
soll durch die Zeichenkette `-...` ersetzt werden und so weiter. Du kannst ein Dictionary so ausgeben::

    print(morse_code)

Probiere das aus, experimentiere mit der REPL. 
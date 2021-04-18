***********************
Cäsar-Verschlüsselung
***********************
	
Beschreibung
=============

Seit Menschen die Schrift benutzen, versuchen sie, Geheimbotschaften zu verfassen. Eine der 
frühesten Verschlüsselungen ist als Cäsar-Verschlüsselung bekannt, benannt nach Julius Cäsar, 
und wurde vom römischen Kaiser benutzt, um mit Truppen auf dem Schlachtfeld zu kommunizieren. 
Mit der Cäsar-Verschlüsselung verschlüsselst du alle Buchstaben in einer Nachricht, indem du das 
Alphabet um eine Anzahl von Stellen verschiebst. Die Abbildung unten zeigt, wie man eine Nachricht 
mit einer Verschiebung von 3 Buchstaben verschlüsselt:

.. figure:: assets/shift.png
   :align: center

   Source: https://upload.wikimedia.org/wikipedia/commons/f/fa/Ascii-proper-color.svg

Deine Aufgabe ist es, deinen micro:bit in eine Maschine zu verwandeln, die Nachrichten mit der 
Cäsar-Verschlüsselung **verschlüsseln** kann. Wir nennen die zu verschlüsselnde Nachricht 
*plain text* und die verschlüsselte Nachricht *cipher text*. 

Es gibt einen Trick, den du verwenden kannst, um die Nachricht zu verschlüsseln, oder zu verschieben. 
Der Trick beruht auf der Tatsache, dass dein micro:bit die Buchstaben des Alphabets als Zahlen sieht. 
Du kannst einen Buchstaben in eine Zahl übersetzen und wieder zurück, indem du die Python Funktionen 
``ord()`` und ``chr()`` benutzt.
                                                                     
Sagen wir, du willst jeden Buchstaben um 4 Stellen verschieben. Versuche diesen Code zu benutzen, 
um das Zeichen in eine Zahl zu verwandeln und 4 zu addieren::

	ascii_char = ord(plaintext_char) + 4      	               
                                                                     
Auf Deutsch heißt das: übersetze ``plaintext_char`` in eine Zahl mit der Funktion ``ord()`` und addiere 4, 
die Anzahl der Zeichen, um die wir verschieben wollen. 

Das funktioniert, weil Zeichen in Python als Zahlen kodiert sind. Eines der beliebtesten (und kleinsten) 
Systeme ist ASCII (American Standard Code for Information Interchange). Wenn du dir jedoch die Tabelle unten 
ansiehst, kannst du sehen, dass es nur lateinische und einige Sonderzeichen beinhaltet. Deshalb ist das native 
Kodierungssystem von Python (und den meisten Sprachen) UTF-8, welches auch rückwärtskompatibel zu ASCII ist. 

.. figure:: assets/ascii_table.png

Aber halt, es gibt noch eine Sache, die wir beachten müssen. Da wir nur Großbuchstaben von A-Z akzeptieren, 
müssen wir sicherstellen, dass wir uns nur innerhalb dieser Grenzen bewegen. Wenn wir 4 zu Z addieren 
landen wir in der ASCII-Tabelle bei '^', deshalb müssen wir von dieser Stelle 26 abziehen um zum `D` zu 
kommen. ::

    ascii_char = ord(plaintext_char) + 4    

	if ascii_char > ord('Z')
        ascii_char = ascii_char - 26

	encrypted_char = chr(ascii_char) 

Versuche nun einige Nachrichten zu verschlüsseln und dann zu entschlüsseln.  Du kannst versuchen, 
den folgenden englischen Text zu entschlüsseln. Kannst du dein Programm dazu bringen, den richtigen 
Klartext selbständig zu erkennen?

    S kw k csmu wkx... S kw k gsmuon wkx. Kx exkddbkmdsfo wkx. S drsxu wi vsfob rebdc. Rygofob, S nyx'd uxyg k psq klyed wi csmuxocc, kxn kw xyd cebo grkd sd sc drkd 
    rebdc wo. S kw xyd losxq dbokdon kxn xofob rkfo loox, dryeqr S boczomd wonsmsxo kxn nymdybc. Grkd'c wybo, S kw kvcy cezobcsdsyec sx dro ohdbowo; govv, kd vokcd 
    oxyeqr dy boczomd wonsmsxo. (S'w ceppsmsoxdvi onemkdon xyd dy lo cezobcdsdsyec, led S kw.) Xy, csb, S bopeco dy lo dbokdon yed yp gsmuonxocc. Xyg, iye gsvv mobdksxvi 
    xyd lo cy qyyn kc dy exnobcdkxn drsc. Govv, csb, led S exnobcdkxn sd. S gsvv xyd, yp myebco, lo klvo dy ohzvksx dy iye zbomscovi gry sc qysxq dy ceppob sx drsc mkco 
    pbyw wi gsmuonxocc; S uxyg zobpomdvi govv drkd S gsvv sx xy gki "wemu drsxqc ez" pyb dro nymdybc li bocoxdsxq drosb dbokdwoxd; S uxyg loddob drkx kxiyxo drkd li kvv 
    drsc S kw rkbwsxq yxvi wicovp kxn xy yxo ovco. Led cdsvv, sp S nyx'd qoddbokdon, sd sc yed yp gsmuonxocc. Wi vsfob rebdc; govv, drox vod sd rebd ofox gybco! 
    
        -- P. Nycdyiofcui, Xydoc Pbyw Exnobqbyexn 
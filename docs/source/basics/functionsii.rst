**************
Funktionen II
**************

Jetzt, wo du weißt, wie man Funktionen in der Praxis einsetzt, gibt es einige weitere Konzepte, die dir 
helfen werden, das Verhalten von Funktionen nicht nur in Python zu verstehen, sondern auch in anderen Sprachen.  

Geltungsbereich (Scope)
=======================

Globale und lokale Variablen
----------------------------

Stell dir vor, du möchtest eine leicht abgeänderte Funktion ``printBirthdayGreeting()`` von vorher verwenden 
und du möchtest das Alter bei jedem Aufruf der Funktion erhöhen: ::

	name = "Johann"
	alter = 32
	
	def printBirthdayGreeting():
		alter += 1
	    return "Happy Birthday " + name + ", du bist " + str(alter) + " Jahre alt!" 

	printBirthdayGreeting()	

Kannst du erkennen, was falsch ist? Wenn du versuchst, den Code auszuführen, wirst du wahrscheinlich diese 
Meldung erhalten: UnboundLocalError: local variable 'alter' referenced before assignment``.

Um dies zu verstehen, müssen wir über den Geltungsbereich (Scope) sprechen. Scope ist eine 'Umgebung', in der 
eine Variable definiert ist, und auf die dort zugegriffen und in die geschrieben werden kann. Unter diesem Gesichtspunkt 
kennen wir zwei Typen von Variablen: globale und lokale.

Standardmäßig sind alle Variablen, die innerhalb einer Funktion definiert sind, lokal - du kannst nicht auf sie außerhalb 
der Funktion zugreifen. Und da der Geltungsbereich innerhalb der Funktion anders ist als der globale, ist es möglich, den 
gleichen Namen für zwei verschiedene Variablen zu verwenden.

Kannst du jetzt erklären, was im obigen Codeschnipsel passiert ist?

``alter`` außerhalb der ``printBirthdayGreeting()`` Funktion ist eine globale Variable. Wenn wir jedoch innerhalb der 
Funktion darauf zugreifen wollen, betrachtet Python es als eine neue lokale Variable. Wie lösen wir das Problem? Wir 
können die Variable ``alter`` als ``global`` deklarieren: ::

	name = "Johann"
	alter = 32

	def printBirthdayGreeting():
		global alter
		alter += 1
		return "Happy Birthday " + name + ", du bist " + str(alter) + " Jahre alt!"


Dadurch weiß Python, dass die age-Variable, die wir meinen, im globalen "Namespace" (wortwörtlich *Namensbereich*) liegt.

.. warning:: Globale Variablen zu verwenden ist generell eine schlechte Praxis und du solltest es vermeiden, da es den Zweck deiner Funktionen weniger offensichtlich macht und du am Ende mit 
			'Spaghetti' Code kämpfen musst. Ein besserer Weg ist es, die Variable ``age`` als eines der Argumente der Funktion zu übergeben (Beispiel unten).

Hier ist ein Beispiel für eine Funktion, die Variablen als Argumente übergibt::

	def printBirthdayGreeting(name, alter):
		alter += 1
		return "Happy Birthday " + name + ", du bist " + str(alter) + " Jahre alt!"


.. tip:: Du wirst oft von "Best Practices" hören. Wie bestimmst du, was eine Best Practice ist und was nicht? Im Allgemeinen ist eine Best Practice das, was deinen
		Code für andere besser lesbar macht. Du kannst dir Styleguides_ für eine Sprache ansehen, in der du programmierst, aber am Ende geht es immer um gutes Urteilsvermögen, da keine Regel 
		in allen Fällen passt. 

.. _Styleguides: https://www.python.org/dev/peps/pep-0008/

.. figure:: assets/code_quality.png
	:align: center

	Quelle: xkcd https://xkcd.com/1513/


Nicht-lokale Variablen
----------------------

Ein kurioser Fall tritt bei der Verwendung von verschachtelten Funktionen auf. Sagen wir, du willst eine lokale Variable der Funktion ``nurEinBeispiel()`` ändern, indem du die verschachtelte
Funktion: ::

	def nurEinBeispiel():
		def weiteresBeispiel():
			variable = "Innere Funktion, die alles verändert!"

		variable = "Äußere Funktion"
		weiteresBeispiel()

		print(variable)

	nurEinBeispiel() 

Du weißt bereits, warum das nicht funktioniert. Aber wie kannst du das Problem umgehen? Du kannst die Variable nicht global deklarieren, weil sie innerhalb einer Funktion ist - sie ist lokal und es gibt 
einen weiteren lokalen Bereich innerhalb der Funktion ``weiteresBeispiel()``. Um diese Situation zu lösen, kannst du eine Variable als ``nonlocal`` deklarieren: ::

	def nurEinBeispiel():
		def weiteresBeispiel():
			nonlocal variable
			variable = "Innere Funktion, die alles verändert!"

		variable = "Äußere Funktion"
		weiteresBeispiel()

		print(variable)

	nurEinBeispiel() 

Jetzt sollte der Code ``"Innere Funktion, die alles verändert!"`` genau so ausgeben, wie wir es wollten.

.. note:: Um mehr über Namespace und Scope in Python zu erfahren, schau dir die Dokumentation_ an.

.. _Dokumentation: https://docs.python.org/3/tutorial/classes.html

Parameter übergeben
====================

Ein wichtiges Konzept, das einen sichtbaren Einfluss auf die Funktionsweise deiner Funktionen haben wird, ist die Übergabe von Parametern. Dies beschreibt die Art und Weise, wie eine Variable verarbeitet wird, wenn man sie an 
eine Funktion übergibt - in einem *Pass-by-Value* Szenario wird das Argument als neue lokale Variable behandelt und hat keinen Einfluss auf die ursprüngliche Variable (falls eine Variable als 
Argument übergeben wurde). Im Falle von *Pass-by-Reference* kann die als Argument übergebene Variable innerhalb einer Funktion beeinflusst werden. In Python ist die Methode der Parameterübergabe 
eine spezielle Kombination aus beidem - Parameter werden per `Wert der Objektreferenz`_ übergeben.

Für eine gute Erklärung der Parameterübergabe und den Unterschied zwischen den verschiedenen Techniken, empfehle ich dir diesen `Blogpost von Robert Heaton`_ zu lesen.

.. _Wert der Objektreferenz: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
.. _Blogpost von Robert Heaton: https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/

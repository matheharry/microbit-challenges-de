****************
Datenstrukturen
****************

Listen
======

Eine Liste ist eine Datenstruktur, die verwendet wird, um einen beliebigen Datentyp (oder eine andere Struktur) in geordneter Weise zu speichern. Eine Liste ist die Datenstruktur, die du wahrscheinlich am häufigsten benutzen wirst. Sagen wir, wir wollen 
den Punktestand eines Spielers speichern. Wir könnten eine Liste wie die oben abgebildete verwenden. Die Liste hat eine "Box" für jeden Wert. Die Daten, die in einer Liste gespeichert sind, werden "Elemente" genannt. 

.. figure:: assets/list_arrow.png 
	 :align: center
     
	 Eine Liste.

Um eine Liste zu erstellen, gibst du ihren Inhalt in eckigen Klammern an und trennst die einzelnen Elemente durch Kommas: :: 

	from microbit import *

	high_scores = [25, 20, 10, 15, 30]       # Erstelle eine Liste und speichere einige Werte in ihr.
	print(high_scores[0])			# Gibt 25 aus
	print(high_scores[3])			# Gibt 15 aus


Den Wert eines der Elemente in einer Liste zu finden ist einfach, solange du im Hinterkopf behältst, dass Python die Elemente ab '0' zählt. In der ``high_scores`` Liste 
oben, ist ``high_scores[0]`` 25 und ``high_scores[3]`` ist 15.

Hier kannst du auch sehen, dass auf bestimmte Elemente in einer Liste über ihren Index zugegriffen werden kann. Außerdem ist es möglich, Listen zu zerschneiden, um nur einen Teil der Liste 
abhängig vom Index zu erhalten. Wenn du nur die ersten drei willst, kannst du ``high_scores[0:3]`` schreiben, oder, da wir bei 0 anfangen, können wir es zu ``high_scores[:3]`` abkürzen. Beachte, dass
der rechte Endpunkt immer ausgeschlossen ist, also bezieht sich der obige "Ausschnitt" auf das mathematische Intervall ``[0,2]``.

Natürlich besitzt Python schon Funktionen für die Arbeit mit Listen. Der folgende Codeschnipsel berechnet die Summe aller Elemente und berechnet dann den durchschnittlichen Punktestand. ::		

	punkte_gesamt = 0
	
	for punkte in high_scores: 		# Für jedes Element ...
		punkte_gesamt = punkte_gesamt + punkte

	durchschnitt = punkte_gesamt / len(high_scores)  # Benutze hier die Funktion len() um die "Länge" der Liste zu ermitteln 

Das Gleiche kann sogar in einer Zeile mit der Funktion ``sum`` gemacht werden::

	durchschnitt_kurzfassung = sum(high_score) / len(high_score)	 


Da du nicht unbedingt weißt, welche Werte in der Liste sein werden, oder wie groß die Liste sein wird, ist es nützlich, die ``append`` Funktion zu kennen. 
Du kannst sie zum Beispiel benutzen, um eine Liste mit Temperaturmesswerten oder Beschleunigungsmessungen zu füllen:: 

	from microbit import *

	temperaturaufzeichnungen = [] 		# Erstelle eine leere Liste
	for i in range(100):			# 100 Temperaturwerte hinzufügen
		temperaturaufzeichnungen.append(temperature())
		sleep(1000)			 

Die ``for`` Schleife wird 100 mal ausgeführt und ``i`` hat Werte von 0 bis 99. Dadurch wird die Temperatur jede Sekunde für 100 Sekunden gemessen und der Wert 
an das Ende der Liste angefügt. 


Das Löschen von Elementen aus einer Liste ist genauso einfach::

	high_scores.delete(24)

Dadurch wird das erste Element mit dem Wert 24 gelöscht.
Alternativ kannst du auch ein Element an einer bestimmten Position löschen, wenn du es kennst:: 
 
	high_scores.pop(3)

Dies löscht oder 'poppt' das Element an der angegebenen Position in der Liste. Beachte, dass::

	high_scores.pop() 

das letzte Element in der Liste löscht.


.. tip:: Du kannst hier_ nachschauen, um weitere nützliche Methoden für Listen zu sehen.

.. _hier: https://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences

.. note:: Du fragst dich vielleicht, ob Strings als Liste betrachtet werden können. Auch wenn string ein Array von Zeichen ist und wir sogar ähnliche Operationen mit ihnen durchführen können (wie z.B. 
(wie z.B. Slicing), sind sie beide unterschiedliche Objekttypen mit unterschiedlichen Methoden (versuche ``dir(str)`` und ``dir(list)`` in deiner Konsole einzugeben). 

Sorting
^^^^^^^

Often you'll find the need to have data in your list sorted, for example when implementing search algorithms. In Python, sorting lists is easy using the 
``sort(key=, reverse=)`` method::

	high_scores = [25, 20, 10, 15, 30]
	high_scores.sort()

You don't only have to sort numbers - its optional key parameter allows you to specify your own	function for comparing elements in your list (for example, while 
sorting a list of strings according to length, you can pass the len() function as the parameter). Passing false to reverse parameter allows you to sort in a descending 
order. ::

	list = ['longest', 'short', 'longer']

	# Sort list in ascending order of string length
	list.sort(key=len)
	# Sort list in descending order of string length
	list.sort(key=len, reverse=True)

Tuples
=======

Tuples are similar to lists in that they are used to store an ordered sequence of items, usually of varying datatype.::

    high_scores_immutable = (25, 20, 10, 15, 30)

You can retrieve values in the same way as with lists, but the most important difference is that tuples are `immutable`. This means, that in the ``high_scores`` 
list above, you can change the value of individual elements: ::

    high_scores[0] = 42

However, trying to change a value inside ``high_scores_immutable`` will return a ``TypeError: Object tuple does not support item assignment``. Once you assign values 
inside a tuple, they cannot be changed. 

Mutability is another difference between strings and lists - while lists are mutable, string are not.

Sets
=====

Unlike lists and tuples, sets hold an **unordered** collection of elements with no duplicates. This makes them suitable for testing membership or removing 
duplicate elements. ::

	set = {8, 12, 22}

	# Add a single element to set
	set.add(42)

	# Add several elements to set
	set.update([16, 32, 64])

	# Remove an element from set - throws an error if element not in set 
	set.remove(42)

	# Remove an element if present in set 
	set.discard(42)

	 

Since a set is an unordered collection of elements, indexing is not possible. Python supports typical set operation methods: ::

	set_a = {1,2,3,4,5}
	set_b = {4,5,6,7}
	set_c = {1,2}

	# Check for membership
	2 in set_a

	# Return elements in the intersection of set_a and set_b
	set_a.intersection(set_b)
	# Return true if set_a contains all the elements of set_c
	set_a.issuperset(set_c)

An empty set is created using a ``set()`` method, as using braces creates an empty dictionary (see below).  	

For more methods, visit Python documentation_.

.. _documentation: https://docs.python.org/2/library/stdtypes.html#set

.. figure:: assets/sets_i.png
   :align: center

   All elements within a set are unique

Dictionaries
=============

Dictionary is an unordered set of ``key : value`` pairs. It's a rule that all keys are unique and have no duplicates. Unlike lists or tuples, which are indexed by numbers, 
you can retrieve a value from a dictionary by using the key as an index.

For example, you can store the highscores of all the players: ::

	game_register = { 'googolplex': 100,
			  'terminat0r': 27,
			  'r00t': 150,
			  'dent': 42,
			  'teapot418' : 0 } 

	# Access elements
	game_register['dent']

	# Add or update and existing entry
	game_register['pepper'] = 50

	# Delete an entry
	del game_register['pepper']	

	# Delete all entries
	game_register.clear()

	# Delete the dictionary
	del game_register

	# Retrieve a value for the key or default if not in dicionary
	game_register.get('dent')		


Practice Questions
===================

1. Use micro:bit list Image.ALL_CLOCKS and iterate over all items in the list with a for loop, showing them on the LED screen.

2. Using the same item list, show only items with an index divisible by 3.

3. Sort an integer list (for example ``list = [20, 112, 45, 80, 23]``) using the last digit of each item and keep their relative positions in case the digit is the same
   (the result in this case would be ``[20, 80, 112, 23, 45]``).

4. Create an animation of your own using a tuple and play it on the micro:bit LED screen.

5. Program microbit to take a compass reading upon press of a button and store the results in a tuple.

6. Write a program to keep record of gestures recognizable by microbit and the number of times they've been detected using a dictionary. 
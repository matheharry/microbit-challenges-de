*************
Substitution
*************
	
Beschreibung
===========

Die Verschlüsselung durch Substitutions ist trügerisch einfach. Nachrichten werden mit einem Schlüssel 
verschlüsselt, der im Voraus erstellt wird. Du erzeugst den Schlüssel, indem du die Positionen der Buchstaben 
im Alphabet veränderst:

.. figure:: assets/substitution.png

Um Nachrichten durch Substitution verschlüsseln und entschlüsseln zu können, musst du einen Schlüssel erstellen, 
der zur Erzeugung des Chiffriertextes verwendet wird, und ihn speichern. Ein Dictionary könnte eine gute 
Datenstruktur für diesen Zweck sein.

Ein Python-Dictionary für die obige Substitutions-Verschlüsselung würde etwa so aussehen::

	key =  {'A':'V', 
		'B':'J', 
		'C':'Z', 
		'D':'B',
		  ...   }

Versuche deine eigenen Nachrichten zu verschlüsseln und zu entschlüsseln und wenn du dich der Herausforderung 
gewachsen fühlst, versuche den untenstehenden englischen Text zu entschlüsseln. Um dir die Mühe zu ersparen: 
der obige Schlüssel gilt nicht für diese Nachricht. 

Versuche an Spracheigenschaften oder Methoden zu denken (oder suche danach), die dir helfen könnten, 
den Schlüssel zu finden. 

	O zay vcur xzfyozx fr nb gorfuj rdfr lftm rcttat ydokd youu zcgct ucfgc nc rouu O, raa, fn fr tcjr; “fkkolczrfuub” at ardctyojc. Pctjpflozx rdc yolay rdfr nb kazzchoaz 
	yord dct dpjefzl’j “rckdzokfu nfrrctj” yfj jpvvokoczr ra czroruc nc ra doj nfzpjktowr, O eatc rdc lakpnczr fyfb fzl ecxfz ra tcfl or az rdc Uazlaz eafr. Or yfj f jonwuc, 
	tfneuozx rdozx—f zfogc jfouat’j cvvatr fr f wajr-vfkra loftb—fzl jrtagc ra tckfuu lfb eb lfb rdfr ufjr fyvpu gabfxc. O kfzzar frrcnwr ra rtfzjktoec or gctefron oz fuu 
	orj kuaplozcjj fzl tclpzlfzkc, epr O youu rcuu orj xojr czapxd ra jdcy ydb rdc japzl av rdc yfrct fxfozjr rdc gcjjcu’j jolcj eckfnc ja pzczlptfeuc ra nc rdfr O jrawwcl 
	nb cftj yord karraz. Qadfzjcz, rdfzm xal, lol zar mzay iporc fuu, cgcz rdapxd dc jfy rdc korb fzl rdc Rdozx, epr o jdfuu zcgct juccw kfunub fxfoz ydcz O rdozm av rdc 
	dattatj rdfr uptm kcfjcucjjub ecdozl uovc oz ronc fzl oz jwfkc, fzl av rdajc pzdfuuaycl eufjwdcnocj vtan culct jrftj ydokd ltcfn eczcfrd rdc jcf, mzayz fzl vfgaptcl 
	eb f zoxdrnftc kpur tcflb fzl cfxct ra uaajc rdcn az rdc yatul ydczcgct fzardct cftrdipfmc jdfuu dcfgc rdcot nazjrtapj jrazc korb fxfoz ra rdc jpz fzl fot.

	-- D.W. Uagcktfvr, Kfuu Av Krdpudp
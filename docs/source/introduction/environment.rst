********************************
Deine Arbeitsumgebung einrichten
********************************

Bevor du mit dem Programmieren beginnst, benötigst du einen Quellcode-Editor, um Programme auf deinem micro:bit schreiben, laden und ausführen zu können. 
Es gibt im Wesentlichen vier Optionen: 

    - Im Web-Browser: `micro:bit Editor`_ (momentan empfehle ich allerdings die aktuelle `Beta-Version`_!)
    - Für Anfänger am PC: `Mu Editor`_ 
    - `MicroPython App`_ wenn du ein Chromebook benutzt  
    - Dein normaler Python-Editor mit einer Reihe von CLI-Befehlen (fortgeschritten)  

Für dieses Tutorial werden wir den Mu-Editor verwenden, aber du kannst natürlich auch einen anderen Editor verwenden, der dir besser gefällt.
Um Mu herunterzuladen, gehe auf die Mu Website_. Hier steht eine `Schritt-für-Schritt-Anleitung`_ zur Verfügung.

.. _`micro:bit Editor`: https://python.microbit.org
.. _`Beta-Version`: https://python.microbit.org/v/beta
.. _`Mu Editor`: https://codewith.mu/
.. _`Schritt-für-Schritt-Anleitung`: https://docs.google.com/document/d/1U-UTHD-6ji6kDecHd4lGKwDZGI4WQ8nTN7-ju4AIrtI/preview
.. _`MicroPython App` : https://chrome.google.com/webstore/detail/micropython/lhdjeebhcalhgnbigbngiaglmladclbo?hl=de-GE
.. _Website: https://codewith.mu/en/

Du kannst verschiedene Optionen wählen, um Mu zu installieren. Die, die du höchstwahrscheinlich auf deinem eigenen Gerät benutzen wirst, 
wenn du Administratorenrechte hast, ist ein Installer für dein Gerät (Mac/Windows), oder die Installation durch ein
Python-Paket (pip) über die :ref:`Kommandozeile`, wenn du Python auf deinem Computer installiert hast.

Falls du keine Administratorenrechte besitzt und Python auf deinem Gerät nicht installiert ist, bietet sich *Portable Mu* an.

.. note:: Für diejenigen, die vorher mit Python gearbeitet haben, MicroPython unterstützt keine regulären externen Python-Bibliotheken, 
    da viele zu groß für ein Embedded Gerät sind. Allerdings wurde ein Subset speziell für die `MicroPython-Umgebung`_ neu erstellt. 

.. _`MicroPython-Umgebung`: https://docs.micropython.org/en/latest/library/index.html

.. figure:: assets/installation_options.PNG
   :align: center
   :scale: 70% 
   :target: https://codewith.mu/en/download

Sobald der Editor installiert ist, starte ihn und schließe den micro:bit an deinen Computer an.

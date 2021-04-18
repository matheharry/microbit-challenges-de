***************
Thermometer
***************
.. py:module:: microbit

Das Thermometer auf dem micro:bit ist in einem der Chips eingebettet - und Chips werden warm, 
wenn sie eingeschaltet werden. Deshalb misst es die Raumtemperatur nicht sehr genau. 
Der Chip, mit dem die Temperatur gemessen wird, befindet sich auf der Rückseite des micro:bit links:

.. image:: assets/thermometer.png
   :scale: 40 %
   :align: center


Grundfunktionen
================
Das Thermometer hat nur eine grundlegende Funktion - die Temperatur zu messen, die als Ganzzahl in 
Grad Celsius zurückgegeben wird:: 

   from microbit import *
   
   while True:
      temp = temperature()
      display.scroll(str(temp) + 'C')
      sleep(500)

Die Temperatur, die das Thermometer misst, wird typischerweise höher sein als die tatsächliche Temperatur, 
da es sowohl vom Raum als auch von der Elektronik auf dem Board erwärmt wird. Wenn wir wissen, dass die 
Temperatur 27°C beträgt, aber das micro:bit ständig Temperaturen anzeigt, die, sagen wir, 3 Grad höher sind, 
dann können wir die Messung korrigieren. Dazu musst du die wirkliche Temperatur kennen bzw. ohne den 
micro:bit mit einem anderen Thermometer messen. 

Wie könnte das aussehen?

Übungsaufgaben
===================
* Versuche das Thermometer zu kalibrieren. Zeigt es immer noch die richtige Temperatur an, wenn du es an einen wärmeren oder kühleren Ort stellst?
* Lass die LEDs ihr Muster ändern, wenn sich die Temperatur ändert.
* Finde heraus, wie sehr sich die Temperatur in einem Raum ändert, wenn du ein Fenster öffnest - was denkst du, sagt das über die verschwendete Heizenergie aus?

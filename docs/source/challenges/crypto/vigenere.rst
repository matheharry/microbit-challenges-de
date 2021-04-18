*************************
Vigenère-Verschlüsselung
*************************

Diese Verschlüsselung, auch 'le chiffre indéchiffrable' genannt, wurde erstmals von Giovan Battista Belazzo 
beschrieben. Obwohl das Konzept leicht zu verstehen ist, konnte die Verschlüsselung drei Jahrhunderte lang 
nicht geknackt werden, bis Friedrich Kasiski einen ersten erfolgreichen Generalangriff vorstellte.  

.. figure:: assets/vigenere_table.jpg
   :align: center
   
   Vigenère Tabelle (Source: https://tinyurl.com/yxmbt48f)

Sie funktioniert ähnlich wie die Cäsar-Verschlüsselung, da sie ebenfalls auf der Verschiebung von Buchstabenpositionen 
basiert. Anstatt alle Buchstaben um den gleichen Wert zu verschieben, wählen wir diesmal ein Schlüsselwort, das für 
jeden Buchstaben im Klartext einen anderen Wert bestimmt.

Als Beispiel, nehmen wir an, dass dies unser Klartext ist: ::
    
    ATTACKATDAWN

Dann wählst du ein Schlüsselwort (z.B. Snake) und wiederholst es für jede Zeile des Klartextes: ::

    SNAKESNAKESN

Dann benutzt du jeden Buchstaben des Schlüssels, um die Verschiebung jedes Buchstabens des Klartextes zu bestimmen: ::

    Plaintext:  ATTACKATDAWN
    Key:        SNAKESNAKESN
    Ciphertext: SGTKGCNTNEOA

Du kannst versuchen, deine eigenen Nachrichten zu verschlüsseln und zu entschlüsseln. Wenn du Lust auf eine 
Herausforderung hast, versuche den Schlüssel zu finden und diesen mit der Vigenère-Verschlüsselung 
verschlüsselten Text zu entschlüsseln (Hinweis: Es ist nicht einfach):    

    Wckl'g jwym avr Tlvfqydnxkwn Vyehqgxat oof im lhm nqmna oyrmavz. Vi  qtfg gwym  hzpdfhs  wf  p  ahschgjxzg  idjtawyt  jbxivs  dhyars  zr  avr  ucktsaiympca  dd  lbungq  
    tur  naqh  ucgtq  bag  vcrhewpprbuu  rudxjh  bc  axyhnxl  vhfodl-­‐uhgrs  jbms  sdpfz.

    Hut  Fbaquwgdlf'f  Vsbks  Gd Ral Unayqf  oyhm  flbgxmgz  oyrmavz.  Vi  qtfg  gwym  avr  qcla  rexld  pb  rmglasarc  bz  hut  ntu  unayvawp  vyknzr  qjtzhrg.  Gm  
    zolh  rahh  gwc  xmtrrr  hm  o  cpl  zhznrrbj  ungeel  pypqmlf  vh  jbrs  uptbuu  ldsk  ifnxll  zanhfxk  chi  zr  h  gyxax  vt  ytkhu  kepnilr  edsgk  o  yppzl  
    ubab  uywpz.  Ral  uhxbx  hzfd  rxszf  nmn  vb  jwgvo  dyplxag  gwc  ulgg  eyg  noypampq  tppzss  oaylaseh  ykl  avmcw,  ocj  bsvo  mbj  atu  skecva  hb  eyr  mce  
    dlx  hbq  lfta  jbasgaoen  mknoaxxtawbcq  xewfi  rh  osye  whb  frwyupzviyml  osickdoesq.

    Mos  Uxrvovvzck'z  Uhxbx  Ac  Gwc  Zhznmw  llzyh  ptavrg  zxahrg  rahb  gwc  Xuqlrjhwsqxy  Zhznrrbjo.
        
    
    -- Smnnznh Ywhaf, Wgmjvuxixy'g Txswl Hb Ifx Noypvr
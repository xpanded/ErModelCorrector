*************************************************************************
Projekt Phase 1 DBS-ProPra SS2021						 README.TXT
*************************************************************************

Information about Projekt Phase 1 DBS 2
-------------------------------------------------------------------------

Da keine k�nstlichen Prim�rschl�ssel erstellt werden sollen und dies in der �bung nochmals extra erw�hnt wurden, wurde keiner Entity ein Prim�rschl�ssel hinzugef�gt, au�er es wurde mit �eindeutig� darauf hingewiesen. Die Entit�ten werden im Laufe der weiteren Phasen dann k�nstliche PKs bekommen.

Die Administrativen Rechte, wie etwa bearbeiten, l�schen und entfernen wurden nicht im ER-Modell dargestellt, da diese in sp�teren Phasen zugeordnet werden m�ssten.


Es wurden Begriffe leicht gek�rzt, wie Passwort zu PW, E-Mail-Adresse zu Mail usw. um die Benutzbarkeit generell und vor allem in den weiteren Phasen zu erleichtern.

Bei Nutzer wurde nur Mail als Prim�rschl�ssel ausgew�hlt, um den Prim�rschl�ssel so klein wie m�glich zu halten. (Wie gelernt soll es auch nur einen Geben).

Es gibt zwei Beziehungen zwischen Nutzer und Blogeintrag, da die Beziehungen sich in den Kardinalit�ten unterscheiden. Erkl�rbar ist dies, dass ein Nutzer ein Blogeintrag ansehen kann, aber diesen nicht bewerten muss. W�rde man beides in einer Beziehung darstellen, k�nnte so etwas rauskommen, wie jeder angesehene Blogeintrag hat eine Bewertung. Dies w�re nat�rlich falsch.
Die Beziehung bewertet enth�lt das Attribut Bewertung, welche in der sp�teren Phase die Skalierung von 1-10 haben wird. �hnlich auch beim Geschlecht, wo sp�ter angegeben werden kann, ob w/m/d.

Der Gedanke einer Ten�ren Beziehung zwischen Nutzer Kommentare und Blogeintrag wurde in der �bung nicht empfohlen, weshalb es in getrennten Beziehungen erbaut wurde. So sind Nutzer mit den Kommentaren und diese mit den Blogeintr�gen verbunden. Die Kardinalit�ten wurden [0,*] gew�hlt, da Nutzer beliebig viele Kommentare (auch mehrfach Kommentare) zu beliebig vielen Blogeintr�gen verfassen k�nnen (und auch andersrum). 

Chefredakteur hat eine IST-Beziehung zu Redakteur, da dieser ein Redakteur mit besonderen Administrativen Rechten ist. Diese wurden wie oben erw�hnt nicht dargestellt.

Schlagwort ist ein Entity mit einem Attribut Schlagwort. Dies h�tte auch ein Attribut sein k�nnen, als Entity schien es aber richtiger, da in der Aufgabenstellung von mindestens einem die Rede ist und dies als Entity besser zu bearbeiten ist. Daher sind die Kardinalit�ten [1,*] und [0,*].

Das Attribut Status (bei Album) beschreibt, ob das Album �ffentlich oder privat ist. Dieser wird als Boolean ab der dritten Phase dargestellt.
Die Kardinalit�ten sind [1,15] da mindestens 1 aber max 15 Bilder ein Album hat, aber beliebig viele Bilder in verschiedenen Alben sein k�nnen, daher [0,*].

Produktrezension hat eine IST-Beziehung zu Blogeintrag, da es wie angegeben ein Blogeintrag ist, welcher speziell ist (vor allem da es weitere Attribute hat). Falls es eine normale Beziehung h�tte, w�rde es hei�en, dass Blogeintr�ge auch Produktrezensionen hat, welches nicht korrekt ist. 

Es gibt trotz Produktrezension eine weitere Beziehung zwischen Redakteur und Blogeintrag, da nicht jeder Blogeintrag eine Produktrezension ist und Redakteure diese nur als solche anlegen k�nnen.

Das Attribut Inhalt bei Kommentare ist der Kommentartext. Dieser wurde in der Aufgabenstellung nicht erw�hnt, jedoch in der �bung f�r notwendig erw�hnt.


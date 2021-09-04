*************************************************************************
Projekt Phase 1 DBS-ProPra SS2021						 README.TXT
*************************************************************************

Information about Projekt Phase 1 DBS 2
-------------------------------------------------------------------------

Da keine künstlichen Primärschlüssel erstellt werden sollen und dies in der Übung nochmals extra erwähnt wurden, wurde keiner Entity ein Primärschlüssel hinzugefügt, außer es wurde mit „eindeutig“ darauf hingewiesen. Die Entitäten werden im Laufe der weiteren Phasen dann künstliche PKs bekommen.

Die Administrativen Rechte, wie etwa bearbeiten, löschen und entfernen wurden nicht im ER-Modell dargestellt, da diese in späteren Phasen zugeordnet werden müssten.


Es wurden Begriffe leicht gekürzt, wie Passwort zu PW, E-Mail-Adresse zu Mail usw. um die Benutzbarkeit generell und vor allem in den weiteren Phasen zu erleichtern.

Bei Nutzer wurde nur Mail als Primärschlüssel ausgewählt, um den Primärschlüssel so klein wie möglich zu halten. (Wie gelernt soll es auch nur einen Geben).

Es gibt zwei Beziehungen zwischen Nutzer und Blogeintrag, da die Beziehungen sich in den Kardinalitäten unterscheiden. Erklärbar ist dies, dass ein Nutzer ein Blogeintrag ansehen kann, aber diesen nicht bewerten muss. Würde man beides in einer Beziehung darstellen, könnte so etwas rauskommen, wie jeder angesehene Blogeintrag hat eine Bewertung. Dies wäre natürlich falsch.
Die Beziehung bewertet enthält das Attribut Bewertung, welche in der späteren Phase die Skalierung von 1-10 haben wird. Ähnlich auch beim Geschlecht, wo später angegeben werden kann, ob w/m/d.

Der Gedanke einer Tenären Beziehung zwischen Nutzer Kommentare und Blogeintrag wurde in der Übung nicht empfohlen, weshalb es in getrennten Beziehungen erbaut wurde. So sind Nutzer mit den Kommentaren und diese mit den Blogeinträgen verbunden. Die Kardinalitäten wurden [0,*] gewählt, da Nutzer beliebig viele Kommentare (auch mehrfach Kommentare) zu beliebig vielen Blogeinträgen verfassen können (und auch andersrum). 

Chefredakteur hat eine IST-Beziehung zu Redakteur, da dieser ein Redakteur mit besonderen Administrativen Rechten ist. Diese wurden wie oben erwähnt nicht dargestellt.

Schlagwort ist ein Entity mit einem Attribut Schlagwort. Dies hätte auch ein Attribut sein können, als Entity schien es aber richtiger, da in der Aufgabenstellung von mindestens einem die Rede ist und dies als Entity besser zu bearbeiten ist. Daher sind die Kardinalitäten [1,*] und [0,*].

Das Attribut Status (bei Album) beschreibt, ob das Album öffentlich oder privat ist. Dieser wird als Boolean ab der dritten Phase dargestellt.
Die Kardinalitäten sind [1,15] da mindestens 1 aber max 15 Bilder ein Album hat, aber beliebig viele Bilder in verschiedenen Alben sein können, daher [0,*].

Produktrezension hat eine IST-Beziehung zu Blogeintrag, da es wie angegeben ein Blogeintrag ist, welcher speziell ist (vor allem da es weitere Attribute hat). Falls es eine normale Beziehung hätte, würde es heißen, dass Blogeinträge auch Produktrezensionen hat, welches nicht korrekt ist. 

Es gibt trotz Produktrezension eine weitere Beziehung zwischen Redakteur und Blogeintrag, da nicht jeder Blogeintrag eine Produktrezension ist und Redakteure diese nur als solche anlegen können.

Das Attribut Inhalt bei Kommentare ist der Kommentartext. Dieser wurde in der Aufgabenstellung nicht erwähnt, jedoch in der Übung für notwendig erwähnt.


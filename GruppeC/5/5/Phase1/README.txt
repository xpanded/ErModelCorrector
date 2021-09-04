README 

Ich habe mich zwischen den beiden eindeutigen Schl�sselkandidaten bei der Entit�t Nutzer f�r den Benutzername entschieden. Der Grund daf�r ist, dass ich die einzelnen Nutzer anhand Ihrer Benutzernamen unterscheiden m�chte und diese dementsprechend einzigartig sind. Passwort wurde zu Pw abgek�rzt, damit weniger Text verwendet werden muss. 

Ich habe mich f�r eine IST-Beziehung von der Entit�t Redakteur zu der Entit�t Nutzer entschieden. So erh�lt der Redakteur, die Attribute von Nutzer Der Vorstellungstext oder Bibliographie habe ich als Vorstellung benannt. Vorstellung wurde als optionales Attribut gekennzeichnet. 

Ich habe eine Redakteur erstellt Blogeintrag Beziehung erstellt und diese mit [0, *] zu [1,1] betitelt. Der Grund daf�r ist, dass ein Redakteur beliebig viele Blogeintr�ge erstellen kann und jeder Blogeintrag nur von einem Redakteur erstellt wird. Dadurch erhalten wir zudem eine direkte Verbindung zwischen Redakteur und Blogeintrag. Auch wenn es sich hierbei um ein Anlegen einer Datei handelt, kann diese nicht erst in Schritt 4 durchgef�hrt werden, da der Blogeintrag eine direkte Verbindung zu dem Redakteur ben�tigt, der den Blogeintrag erstellt. 

Ein Chefredakteur IST ein Redakteur und hat als Prim�rschl�ssel seine Telefonnummer.
Redakteur schreibt Rezension ist eine [0,*] zu [1,1] Relation, da ein Redakteur beliebig viele Rezensionen schreiben kann, eine Rezension jedoch von genau einem Redakteur geschrieben wird.

Eine Rezension ist ein besonderer Blogeintrag und wurde deswegen von mir mit einer IST Beziehung gel�st. So erh�lt die Rezension die Attribute des Blogeintrags. Der Hintergedanke ist, dass jede Rezension ein Blogeintrag ist, jedoch nicht jeder Blogeintrag eine Rezension ist.

Bei der Relation Nutzer bewertet Blogeintrag habe ich an das Beziehungselement das Attribut Skala hinzugef�gt. Dieses spiegelt die Bewertung wider, die ein Nutzer f�r einen Blogeintrag von 1-10 abgeben kann. Ich habe dieses Objekt an dieser Stelle hinzugef�gt, da es sonst verloren gehen w�rde und es weder ein direktes Attribut von Nutzer noch des Blogeintrags ist.

Bei der Relation Nutzer sieht Blogeintrag habe ich beide Richtungen auf [0, *] gesetzt. Der Grund daf�r ist, dass ein Nutzer beliebig viele Blogeintr�ge sehen kann und ein Blogeintrag von beliebig vielen Nutzern gesehen werden kann. Dadurch wird der gesehene Blogeintrag mit dem Nutzer verbunden.

Bei der Relation Nutzer schreibt Kommentar habe ich ebenfalls beide Seiten auf [0, *] gesetzt. Der Grund daf�r ist, dass ein Nutzer Mehrfachkommentare absenden kann und ein Kommentar nicht einzigartig sein muss. So kann der gleiche Kommentar von mehreren Personen abgegeben werden.

Bei der Relation Kommentar zu Blogeintrag habe ich beide Seiten auf [0, *] gesetzt. Das bedeutet, dass ein Kommentar zu beliebig vielen Blogeintr�gen sein kann und ein Blogeintrag beliebig viele Kommentare beinhalten kann.

Ich habe bei der Entit�t Album, dass Attribut privat hinzugef�gt. Die Idee dahinter ist, dass es nur die M�glichkeit zwischen privat und �ffentlich gibt und so in weiteren Schritten der Wert als Boolean deklariert wird. In diesem Fall w�rde 1 f�r privat und 0 f�r �ffentlich stehen. Zus�tzlich entsteht dadurch keine Datenredundanz.

Bei der Relation Blogeintrag hat Schlagwort, habe ich die Kardinalit�ten auf [1, *] zu [0, *] gesetzt. Der Grund daf�r ist, dass jeder Blogeintrag mindestens 1 Stichwort hat, aber ein Stichwort zu beliebig vielen Blogeintr�gen passt (auch 0).

Bei der Entit�t Blogeintrag habe ich das Objekt Lastedit, welches f�r das �nderungsdatum steht.

Die Befehle L�schen, bearbeiten und anlegen(ausser die Ausnahme zwischen Redakteur und Blogeintrag) sind noch nicht im er Modell durchzuf�hren und werden in den sp�teren Phasen bearbeitet.



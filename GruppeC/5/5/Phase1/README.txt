README 

Ich habe mich zwischen den beiden eindeutigen Schlüsselkandidaten bei der Entität Nutzer für den Benutzername entschieden. Der Grund dafür ist, dass ich die einzelnen Nutzer anhand Ihrer Benutzernamen unterscheiden möchte und diese dementsprechend einzigartig sind. Passwort wurde zu Pw abgekürzt, damit weniger Text verwendet werden muss. 

Ich habe mich für eine IST-Beziehung von der Entität Redakteur zu der Entität Nutzer entschieden. So erhält der Redakteur, die Attribute von Nutzer Der Vorstellungstext oder Bibliographie habe ich als Vorstellung benannt. Vorstellung wurde als optionales Attribut gekennzeichnet. 

Ich habe eine Redakteur erstellt Blogeintrag Beziehung erstellt und diese mit [0, *] zu [1,1] betitelt. Der Grund dafür ist, dass ein Redakteur beliebig viele Blogeinträge erstellen kann und jeder Blogeintrag nur von einem Redakteur erstellt wird. Dadurch erhalten wir zudem eine direkte Verbindung zwischen Redakteur und Blogeintrag. Auch wenn es sich hierbei um ein Anlegen einer Datei handelt, kann diese nicht erst in Schritt 4 durchgeführt werden, da der Blogeintrag eine direkte Verbindung zu dem Redakteur benötigt, der den Blogeintrag erstellt. 

Ein Chefredakteur IST ein Redakteur und hat als Primärschlüssel seine Telefonnummer.
Redakteur schreibt Rezension ist eine [0,*] zu [1,1] Relation, da ein Redakteur beliebig viele Rezensionen schreiben kann, eine Rezension jedoch von genau einem Redakteur geschrieben wird.

Eine Rezension ist ein besonderer Blogeintrag und wurde deswegen von mir mit einer IST Beziehung gelöst. So erhält die Rezension die Attribute des Blogeintrags. Der Hintergedanke ist, dass jede Rezension ein Blogeintrag ist, jedoch nicht jeder Blogeintrag eine Rezension ist.

Bei der Relation Nutzer bewertet Blogeintrag habe ich an das Beziehungselement das Attribut Skala hinzugefügt. Dieses spiegelt die Bewertung wider, die ein Nutzer für einen Blogeintrag von 1-10 abgeben kann. Ich habe dieses Objekt an dieser Stelle hinzugefügt, da es sonst verloren gehen würde und es weder ein direktes Attribut von Nutzer noch des Blogeintrags ist.

Bei der Relation Nutzer sieht Blogeintrag habe ich beide Richtungen auf [0, *] gesetzt. Der Grund dafür ist, dass ein Nutzer beliebig viele Blogeinträge sehen kann und ein Blogeintrag von beliebig vielen Nutzern gesehen werden kann. Dadurch wird der gesehene Blogeintrag mit dem Nutzer verbunden.

Bei der Relation Nutzer schreibt Kommentar habe ich ebenfalls beide Seiten auf [0, *] gesetzt. Der Grund dafür ist, dass ein Nutzer Mehrfachkommentare absenden kann und ein Kommentar nicht einzigartig sein muss. So kann der gleiche Kommentar von mehreren Personen abgegeben werden.

Bei der Relation Kommentar zu Blogeintrag habe ich beide Seiten auf [0, *] gesetzt. Das bedeutet, dass ein Kommentar zu beliebig vielen Blogeinträgen sein kann und ein Blogeintrag beliebig viele Kommentare beinhalten kann.

Ich habe bei der Entität Album, dass Attribut privat hinzugefügt. Die Idee dahinter ist, dass es nur die Möglichkeit zwischen privat und öffentlich gibt und so in weiteren Schritten der Wert als Boolean deklariert wird. In diesem Fall würde 1 für privat und 0 für öffentlich stehen. Zusätzlich entsteht dadurch keine Datenredundanz.

Bei der Relation Blogeintrag hat Schlagwort, habe ich die Kardinalitäten auf [1, *] zu [0, *] gesetzt. Der Grund dafür ist, dass jeder Blogeintrag mindestens 1 Stichwort hat, aber ein Stichwort zu beliebig vielen Blogeinträgen passt (auch 0).

Bei der Entität Blogeintrag habe ich das Objekt Lastedit, welches für das Änderungsdatum steht.

Die Befehle Löschen, bearbeiten und anlegen(ausser die Ausnahme zwischen Redakteur und Blogeintrag) sind noch nicht im er Modell durchzuführen und werden in den späteren Phasen bearbeitet.



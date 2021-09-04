
date: 18.04.2021

Ich nehme diese kritische Entscheidungen auf Grund der Deutschen
Sprache beziehungsweise was ich verstehe als NICHT Muttersprachler!

-------------------------------------------------------------------
Die kritische entscheidungen:

1. Ich habe Benutzername und E-mail als Primäre Attribute gewählt,
weil beide als 'eindeutig' genannt werden in der Stellung.

2. Ich habe Skala als Attribut zu der Relation bewertet gewählt,
weil der Nutzer bewertet der Blogeintrag.

3. Die Relation fuegt und enfernt habe ich als 3er Relation zwischen
Nutzer, Redakteur und Chefredakteur gewählt, weil Chefredakteur
Redakteure und Nutzern managen kann. Damit habe ich auch das Verb
"managiert" genommen. Außerdem ist die Kardinalität bei Redakteur
und bei Nutzer [1,1], weil meiner Meinung nach Nutzer können
von genau einem Chefredakteur entfernt/hinzugefügt. Das gleiche
gilt für die Redakteure, die von einem Chefredakteur managiert
sind. [0,*] bei Chefredakteur, weil er beliebig viele von den
Nutzern/Redakteure managieren kann.

4. Fazit ist bei mir extra noch ein Entity, weil es wegen sein
Attribut "Limit(1000 Zeichen)". So ist es für mich klarer, statt
einfach als Attribut zu Produktrezension hinzufügen. Jeder
Produktrezension hat einen Fazit. Und ein bestimmte Fazit gehört
zu eine Produktrezension bzw. 1:1 Relation benutze ich hier.

5. Die Beziehung wo Redakteur folgt Redakteur habe ich auf Grund
der Satz "beliebig vielen Redakteuren folgen kann", anstatt eine
neue Entity "Follower" zu entwickeln.

6. Für mich ist letzte Änderungsdatum ein optionales Attribut zu
Blogeintrag, weil dieses Änderungsdatum existiert nur wenn ein
Blogeintrag geändert wird, ansonsten zeigt das System nur das
Erstellungsdatum.

7. Das Entity Album bekommt ein Attribut was ich "Art" genannt habe.
Damit representiere ich ob es privat oder öffentlich ist. Es soll
wie ein Boolean funktionieren (in meinem Kopf).

8. Auf Grund der Transitivität => Ein Redakteur ist Nutzer und ein
Chefredakteur ist Redakteur, folgt dann automatisch dass
Chefredakteur auch ein Nutzer ist.

9. Zwischen Blogeintrag und Redakteur habe ich die Beziehung, statt
legt an, löscht und ändert, das Verb verwaltet gewählt.

10. Zwischen Nutzer und Kommentar habe ich die Beziehung wieder
als verwaltet genannt mit dem gleichen Argument.

11. Die Kardinalitäten bei Bild sind [1,1] weil in meinem Kopf,
erlaube ich Bilder zu verschiedenen Alben zu gehören. Also ein
bestimmter Bild kann in ein Album sein so.

12. Der Attribut Ort (speichern) steht für die fiktive Pfäde
die Sie im Blatt genannt haben.

13. Die Kardinalität bei Produktrezension habe ich [1,1] genommen
weil ich nehme an das eine Rezension von einem Redakteur
geschrieben sind, aber ein Redakteur kann beliebig viele Produkt-
rezensionen schreiben d.h. [0,*]

14. Kommentare die Mehrfachkommentare habe ich durch [0,*]
Kardinalität bei Beziehung gehört zu zwischen Blogeintrag und
Kommentar. Noch dazu, speichert ein Kommentar Text als Attribut
in meiner Kommentar Entity.

-------------------------------------------------------------------
latest update

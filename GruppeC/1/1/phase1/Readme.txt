Ein Nutzer kann zu jedem Eintrag maximal eine Bewertung abgeben.
Zu einem BlogEintrag kann beliebig viele Bewertung gehören.
Eine Bewertung kann von genau einem Nutzer abgegeben werden, und gehört genau einem Eintrag.

die von Nutzern angeschaute Einträge kann man so speichern, indem man die Eintrag-Id aller angeschauten Eintäge in einer Liste bei "Nutzer" speichert,
aber da es noch kein Primärschlüssel bei Blogeintrag gibt, habe ich das mit einer Beziehung dargestellt.   


Da die Verwaltungsspezifische Beziehungen im Er-Modell nicht sinnvoll sind, habe ich z.b Bearbeiten, Löschen einfach in eine Beziehung "verwaltet" zusammengefasst.
(Redakteur_verwaltet_Blogeintag).
Ein Redakteur kann alle eigene Blogeintäge verwalten, und jeder Blogeintrag kann von genau einem Redakteur verwaltet werden.

auch bei Chefredakteur dasselbe. (Chefredakteur_verwaltet_Blogeintag).Aber Blogeintrag kann von beliebig vielen Chefedakteur verwaltet werden




Ein Chefredakteur kann Komentare löschen, und ein Komentar kann von allen (beliebig vielen) Chefredakteuren gelöscht werden.

Durch die Beziehung "legt an" kann man direkt herausfinden, welcher Redakteur  was geschrieben hat, und somit ist der Satz
"Zu jedem Blogeintrag wird der Redakteur gespeichert" schon mit realisiert. 

Ein Nutzer kann beliebig viele Kommentare abgeben, aber ein Komentar kann von genau einem Nutzer abgegeben

Ein Bild kann in beliebig vielen Einträgen enthalten sein.
zu dem Entity "Bild" habe ich das Atributt "Pfad" hinzugefügt, um die Pfade zu Speichern. 

ich habe da den abgekürzten Beziehungsname "verwaltet" mehrmals benutzt, aber die Beziehung heißt eigentlich
z.b "Chefredakteur_verwaltet_Nutzer" das umfasst entfernen, hinzufügen, bearbeiten... 

Kommentare können im Nachhinein vom jeweiligen Nutzer bearbeitet und gelöscht werden => Nutzer können ihre Kommentare verwalten
 => Nutzer_verwaltet_Komentar

Dass ein Chefredakteur  die Nutzer, die Redakteur, und die Blogeinträge löschen/bearbeiten/hinzufügen usw. kann, wird mit einfach nur mit der Beziehung "vewaltet", dargestellt
und das zeigt einfach dass Chefredakteur  Zugriff auf alles hat. 
Kritische Entscheidungen:

1. Man könnte in "Nutzer" entweder Attribut "E-Mail-Adresse" oder "Benutzername" als Primärschlüssel wählen. 
Ich habe mich für "E-Mail-Adresse" entschieden.

2. "Telefonnummer" Attribut könnte in "Chefredakteur" ein Primärschlüssel sein, aber ich habe mich entschieden, "E-Mail" von Nutzer zu benutzen.
(Das wird dann in Phase 2 klar gezeigt.)

3. Alle Bearbeiten/Löschen/Hinzufügen Verben habe ich nicht als Beziehungen gemacht, 
weil es meiner Meinung nach, mehr Sinn macht, sie erst in Phase 4 als Funktionen der API zu implementieren 
und es nicht explizit gefordert wird, die Person zu speichern, die eine dieser Aktionen macht.

4. "Text" Attribut in Kommentar geaddet, weil es kein Sinn macht, ein Kommentar "ohne Kommentar" zu haben.

5. "Bild" Attribut in Bild aus gleichen Grund wie Punkt 4 geaddet.

6. "Wort" Attribut in Schlagwort ist ein Primärschlüssel, damit es keine gleiche Schlagwörter geben kann und auch minimale Datenredundanz gibt.

7. Änderungsdatum ist ein optionales Attribut, weil es genau dann gesetzt wird, wenn ein Blogeintrag geändert wird. Und das kann auch nie passieren.

8. Produktrezension hat keine direkte Beziehung mit Redakteur, da sie ein Blogeintrag ist. Zu jedem Blogeintrag wird der Redakteur gespeichert. Deswegen wurde eine direkte Beziehung zwischen Redakteur und Produktrezension zur Datenredundanz führen.


Kritische Stellen:

Beim Nutzer sind die Attribute E-Mail-Adresse und Benutzername eindeutig, 
ich habe mich dafür entschieden nur Benutzername als Primärschlüssel zu unterstreichen.

Die eindeutige Telefonnummer des Chefredakteurs wird nicht unterstrichen, da es sich um eine 
Sub-Entity handelt.


Ich habe lange überlegt, ob die Beziehung "von" zwischen Nutzer und Kommentare nötig ist. Ich habe mich
letztentlich dafür entschieden, da man ansonsten einen Kommentar nicht eindeutig einem Nuter zuordnen kann.
Er soll ja später seine Kommentare bearbeiten können.
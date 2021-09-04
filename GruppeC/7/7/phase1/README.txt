Aus der Aufgabenstellung geht nicht klar hervor, ob ein Blogeintrag von mehreren Redakteuren geschrieben werden kann. Da dies in der realen Welt durchaus vorkommt, habe ich das im ER-Modell dementsprechend umgesetzt.
In der Relation "legt_an" wird gespeichert, von wem ein Blogartikel angelegt wurde. Somit ist es nicht nötig dies in der Entität selbst nochmal zu speichern.
Das Attribut "privat" in der Entität "Album" ist ein bool'scher Wert. "true" heißt das Alnum ist privat und "false" heißt das Album ist öffentlich.

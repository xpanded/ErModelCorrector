Es wird davon ausgegangen, dass ein Blogeintrag von genau einem Redakteur angelegt wird[1,1].

Kardinalität zwischen Schlagwort [0,*] Blogeintrag, dadurch soll die Möglichkeit gegeben sein, dass ein Schlagwort keinem Blogeintrag zugeteilt ist (z.B: bei Löschung eines Eintrags o.Ä.).

Kommentar wurde als Entity dargestellt und nicht als Attribut und die Kardinalitäten wurden wie im ER-Modell dargestellt gewählt, um Mehrfachkommentare eines Nutzers möglich zu machen.

Attribut Status bei Album steht dafür, dass es privat oder öffentlich ist.

Eine Beziehung zwischen Produktrezension und Redakteur wurde nicht eingepflegt (Redakteur [0,*] schreibt [1,1] Produktrezension), da es redundant wäre. Da bereits die Beziehung "Redakteur - legt an - Blogeintrag" vorhanden ist, und eine Produktrezension
eine Produktrezension ein Blogeintrag  ist (durch die Ist Beziehung) ist der Fall bereits abgedeckt, dass ein Redakteur auch eine Produktrezension anlegen/schreiben kann.


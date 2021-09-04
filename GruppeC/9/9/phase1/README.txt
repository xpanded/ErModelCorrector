-Die Kardinalität von "löscht", "entfernt" und "hinzufügt"  ist [0:1], [0,*]. 
Weil ein Nutzer (bzw. Kommentar, Blogeintrag und Redakteur) beispielerweise nicht zweimal entfernt(gelöscht) oder hinzufügt werden kann.  
-Die "bearbeitet"-Beziehung von Blogeintrag hat Änderungsdatum als Attribut, damit ein Blogeintrag mehrfach von einem Redakteur oder von einem Chefredakteur bearbeitet werden kann. 
Außerdem ist damit „Nullwert“ vermeidbar. (falls Blogentität Änderungsdatum als Attribut hätte, dann entsteht „Nullwert“, wo Blogeintrag nicht bearbeitet ist.)
-Die „bearbeitet"-Beziehung von Kommentar hat Änderungsdatum als Attribut, damit ein Kommentar mehrfach von einem Nutzer oder von einem Chefredakteur bearbeitet werden kann.

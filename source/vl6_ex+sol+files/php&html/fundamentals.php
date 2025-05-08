<?php
// durch "<?php" am Anfang und "Fragezeichen>" am Ende wird dem Interpreter signalisiert, 
// dass es sich um PHP handelt

// Variablen deklarieren
#string
$name = "Anna";
#int
$alter = 22;
#array
$obst = ["Apfel", "Banane", "Kirsche"];

// Ausgabe
echo "Hallo Martin";
echo "Hallo " . $name . "!"; # . ist Verkettungsoperator (python wäre mit komma)
echo "Hallo " . $name . "!<br>"; # <br> ist html für Zeilenumbruch

# echo vs. print -> beides gibt es
#echo ist etwas schneller als print, aber beide funktionieren fast gleich.
#echo kann mehrere Argumente haben, print nicht.
echo "Hallo Jelena" . "<br>";
print("Hallo Viktor");

// Altersprüfung
if ($alter >= 18) {
    echo "Du bist volljährig.<br>";
} else {
    echo "Du bist noch minderjährig.<br>";
}

// Array-Zugriff über Index
echo "printe die erste Frucht: " . $obst[0] . "<br>";

// Schleife über Array
echo "Weitere Früchte:<br>";
for ($i = 1; $i < count($obst); $i++) {
    echo "- " . $obst[$i] . "<br>";
}
?>
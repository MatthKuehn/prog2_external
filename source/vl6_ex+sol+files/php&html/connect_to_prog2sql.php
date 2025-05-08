<?php
// parameter für den Aufbau der Verbindung zu mysql --> host ist standard, port ist standard
// passwort kommt aus mysqlworkbench, sofern gesetzt
// database: name der Datenbank, nicht des schemes
$host = "127.0.0.1";  // or localhost
$port = 3306;         // or whatever port Workbench uses, 3306 ist der default
$user = "root";
$password = "";       //  actual MySQL password from workbench
$database = "prog2";

// aufbau der Verbindung
$conn = new mysqli($host, $user, $password, $database, $port);
if ($conn->connect_error) die("Connection failed");

echo "Connected successfully - juhu!";

// Test: einsetzen eines Werts in einen Table, den es nicht geben sollte

$ergebnis = $conn->query("SELECT * FROM mitglieder");

while ($row = $ergebnis->fetch_assoc()) {
  echo "<br>User: " . $row["nachname"] . " (" . $row["vorname"] . ")";
}


$ergebnis=$conn->query("INSERT INTO mitglieder_neu (name, alter) VALUES ('ronalda', 37)");
if (!$ergebnis) {
    echo "<br>Query error: " . $conn->error;
}
echo "User inserted!";

$conn->close();
?>

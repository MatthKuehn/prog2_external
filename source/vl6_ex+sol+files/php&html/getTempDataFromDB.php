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

    // Test: einsetzen eines Werts in einen Table, den es nicht geben sollte
    $ergebnis=$conn->query("SELECT zeit, temperature FROM temperatur_kempten ORDER BY zeit DESC LIMIT 10");
    if (!$ergebnis) {
        echo "Query error: " . $conn->error;
    }

    while($row = $ergebnis->fetch_assoc()) {
        echo "zeit " . $row['zeit'] . " temperatur in KE  " . $row['temp'] . "<br>";
    }

    $conn->close();
?>
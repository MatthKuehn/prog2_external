<?php

$host = "127.0.0.1";  // or localhost
$port = 3306;         // or whatever port Workbench uses, 3306 ist der default
$user = "root";
$password = "";       //  actual MySQL password from workbench
$database = "prog2";
$conn = new mysqli($host, $user, $password, $database, $port);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT zeit, temp,ort FROM temperatur_kempten ORDER BY zeit DESC LIMIT 10";
$result = $conn->query($sql);

$data = [];

# in json packen zur Übergabe, array mag js nicht
while ($row = $result->fetch_assoc()) {
    $data[] = $row;
}

# return data als json
header('Content-Type: application/json');
echo json_encode($data);

$conn->close();
?>
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>Temperatur-Website  </title>
  <style>
    h1 {
      font-family: "Comic Sans MS", sans-serif;
      margin: 40px;
      background-color:rgb(255, 0, 102);
      text-shadow: 6px 11px 2px #1C6EA4;
    }
    body {
      font-family: "Impact", sans-serif;
      margin: 40px;
      background-color:rgb(45, 245, 0);
    }
    table {
      width: 100%;
      max-width: 600px;
      border-collapse: collapse;
      margin-top: 20px;
      background: #fff;
    }
    th, td {
      padding: 12px 15px;
      border: 1px solid #ccc;
      text-align: center;
    }
    th {
      background:rgb(185, 110, 110);
    }
    tr:nth-child(even) {
      background:rgb(11, 230, 189);
    }
  </style>
</head>
<body>

  <h1>🦄 Temperaturen der letzten Tage 🦄</h1>
  <table>
    <thead>
      <tr>
        <th>Datum</th>
        <th>Temperatur (°C)</th>
        <th>Ort</th>
      </tr>
    </thead>
    <tbody>
            <?php
            while(true){
                include "getTempDataFromDB2.php";
                flush(); // send buffer to browser
                ob_flush(); // make sure output buffering sends content
                sleep(1);
            }
            ?>
    </tbody>
    
  </table>

</body>
</html>
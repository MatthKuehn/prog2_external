<?php
            $host = "127.0.0.1";  // or localhost
            $port = 3306;         // or whatever port Workbench uses, 3306 ist der default
            $user = "root";
            $password = "";       //  actual MySQL password from workbench
            $database = "prog2";
            
            $conn = new mysqli($host, $user, $password, $database, $port);
            $result = $conn->query("SELECT zeit, temp,ort FROM temperatur_kempten ORDER BY zeit DESC LIMIT 100");

            while($row = $result->fetch_assoc()) {
                
                echo "<tr>
                        <td>{$row['zeit']}</td>
                        <td>{$row['temp']}</td>
                        <td>{$row['ort']}</td>
                        
                      </tr>";
            }

            $conn->close();
            ?>
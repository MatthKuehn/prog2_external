<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Live Temperature Feed</title>
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

<h1>🦄 LIVE Temperaturen der letzten Tage 🦄</h1>
<table id="tempTable">
    <thead>
        <tr>
            <th>Zeitstempel</th>
            <th>Temerature (°C)</th>
        </tr>
    </thead>
    <tbody></tbody>
</table>

<! ab hier javascript, weil php-endlosschleife schlecht >

<script>
function loadData() {
    fetch('getTempDataFromDBasJSON.php')
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector("#tempTable tbody");
            tbody.innerHTML = ""; // clear old rows

            data.forEach(row => {
                const tr = document.createElement("tr");
                tr.innerHTML = `<td>${row.zeitstempel}</td><td>${row.temperaturwert}</td>`;
                tbody.appendChild(tr);
            });
        })
        .catch(err => console.error("Fetch error:", err));
}

// Load initially and then every 6 seconds
loadData();
setInterval(loadData, 6000);
</script>

</body>
</html>
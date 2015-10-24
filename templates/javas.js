var data = {"a": 1, "b": 3, "ds": 4};    

// Create a new table
var table = document.createElement("table");

// Add the table header
var tr = document.createElement('tr');
var leftRow = document.createElement('td');
leftRow.innerHTML = "Name";
tr.appendChild(leftRow);
var rightRow = document.createElement('td');
rightRow.innerHTML = "Value";
tr.appendChild(rightRow);
table.appendChild(tr);

// Add the table rows
for (var name in data) {
    var value = data[name];
    var tr = document.createElement('tr');
    var leftRow = document.createElement('td');
    leftRow.innerHTML = name;
    tr.appendChild(leftRow);
    var rightRow = document.createElement('td');
    rightRow.innerHTML = value;
    tr.appendChild(rightRow);
    table.appendChild(tr);
}

// Add the created table to the HTML page
document.body.appendChild(table);

let tbody = document.getElementById("tbody");
json_to_array = Object.values(json_parsed); 

let array_date = Object.values(json_to_array[0])
let array_open = Object.values(json_to_array[1]);
let array_high = Object.values(json_to_array[2]);
let array_low = Object.values(json_to_array[3]);
let array_close = Object.values(json_to_array[4]);
let array_volume = Object.values(json_to_array[5]);
let array_dividends = Object.values(json_to_array[6]);
let array_stocks = Object.values(json_to_array[7]);

function arrayToTable(index){
    let tr = document.createElement("tr"); 

    tr_data = [array_date[index],
        array_open[index], 
        array_high[index],
        array_low[index],
        array_close[index],
        array_volume[index],
        array_dividends[index],
        array_stocks[index]];
    
    for(i=0; i < tr_data.length; i++){
        let td = document.createElement("td"); 

        td.innerText = tr_data[i];

        tr.appendChild(td);
    };

    tbody.appendChild(tr);
};

for(c=0; c < array_open.length; c++){
    arrayToTable(c);
};


















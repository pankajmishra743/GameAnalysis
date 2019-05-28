function updateMetaData(data) {
    // Reference to Panel element for sample metadata
    var PANEL = document.getElementById("year-metadata");
    // Clear any existing metadata
    PANEL.innerHTML = '';
    // Loop through all of the keys in the json response and
    // create new metadata tags
    for(var key in data) {
        h6tag = document.createElement("h6");
        h6Text = document.createTextNode(`${key}: ${data[key]}`);
        h6tag.append(h6Text);
        PANEL.appendChild(h6tag);
    }
}
function buildCharts(sampleData, otuData) {
    // Loop through sample data and find the OTU Taxonomic Name
    var labels = sampleData[0]['otu_ids'].map(function(item) {
        return otuData[item]
    });
    // Build Bubble Chart
    var bubbleLayout = {
        margin: { t: 0 },
        hovermode: 'closest',
        xaxis: { title: 'OTU ID' }
    };
    var bubbleData = [{
        x: sampleData[0]['otu_ids'],
        y: sampleData[0]['sample_values'],
        text: labels,
        mode: 'markers',
        marker: {
            size: sampleData[0]['sample_values'],
            color: sampleData[0]['otu_ids'],
            colorscale: "Earth",
        }
    }];
    var BUBBLE = document.getElementById('bubble');
    Plotly.plot(BUBBLE, bubbleData, bubbleLayout);
    
};
function updateCharts(sampleData, otuData) {
    var sampleValues = sampleData[0]['sample_values'];
    var otuIDs = sampleData[0]['otu_ids'];
    // Return the OTU Description for each otuID in the dataset
    var labels = otuIDs.map(function(item) {
        return otuData[item]
    });
    // Update the Bubble Chart with the new data
    var BUBBLE = document.getElementById('bubble');
    Plotly.restyle(BUBBLE, 'x', [otuIDs]);
    Plotly.restyle(BUBBLE, 'y', [sampleValues]);
    Plotly.restyle(BUBBLE, 'text', [labels]);
    Plotly.restyle(BUBBLE, 'marker.size', [sampleValues]);
    Plotly.restyle(BUBBLE, 'marker.color', [otuIDs]);
    
}
function getData(year) {
    // Use a request to grab the json data needed for all charts
	Plotly.d3.json(`/metadata/${year}`, function(error, metaData) {
        if (error) return console.warn(error);
        updateMetaData(metaData);
		
    });
    Plotly.d3.json(`/homedata/${year}`, function(error, homeWinData) {
        if (error) return console.warn(error);
        Plotly.d3.json(`/awaydata/${year}`, function(error, awayWinData) {
            if (error) return console.warn(error);
            barGraph(homeWinData, awayWinData);
        });
    });
	
	
    
    
}
function getOptions() {
    // Grab a reference to the dropdown select element
    var selDataset = document.getElementById('selDataset');
    // Use the list of sample names to populate the select options
    Plotly.d3.json('/names', function(error, yearList) {
        for (var i = 0; i < yearList.length;  i++) {
            var currentOption = document.createElement('option');
            currentOption.text = yearList[i];
            currentOption.value = yearList[i]
            selDataset.appendChild(currentOption);
        }
        getData(yearList[0]);
    })
}
function optionChanged(year) {
    // Fetch new data each time a new sample is selected
    getData(year);
}
function init() {
    getOptions();
}
// Initialize the dashboard
init();
/**
* BONUS Solution
**/

function barGraph(hData,aData) {
	$('#barChart').remove(); // this is my <canvas> element
  $('#ChartContainer').append('<canvas id="barChart" width="650" height="400"></canvas>');
var densityCanvas = document.getElementById("barChart");

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

var homeData = {
  label: 'Home Team Winning Count',
  data: hData,
  backgroundColor: 'rgba(25, 108, 225, 1)',
  borderWidth: 0,
  yAxisID: "y-axis-home"
};

var awayData = {
  label: 'Away Team Winning Count',
  data: aData,
  backgroundColor: 'rgba(225, 125, 25, 1)',
  borderWidth: 0,
  yAxisID: "y-axis-away"
};

var chartData = {
  labels: [ "Low Humidity", "Low Temp", "Low Wind Chill", "Low Wind Mph", "High Humidity", "High Temp", "High Wind Chill", "High Wind Mph"],
  datasets: [homeData, awayData]
};

var chartOptions = {
  scales: {
    xAxes: [{
      barPercentage: 1,
      categoryPercentage: 0.6
    }],
    yAxes: [{
      id: "y-axis-home",
	  ticks:{
              beginAtZero:true
	  }
    }, {
      id: "y-axis-away",
	  ticks:{
              beginAtZero:true
	  }
    }]
  }
};

var barChart = new Chart(densityCanvas, {
  type: 'bar',
  data: chartData,
  options: chartOptions
});
}
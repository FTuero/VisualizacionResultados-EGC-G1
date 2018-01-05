var censusCtx = document.getElementById("census-chart").getContext('2d');
var censusChart = new Chart(censusCtx, {
  type: 'bar',
  data: {
    labels: ["Final"],
    datasets: [{
      label: 'Participacion',
      data: [3],
      backgroundColor: "rgba(153,255,51,1)"
    }, {
      label: 'Censo total',
      data: [5],
      backgroundColor: "rgba(255,153,0,1)"
    }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
});
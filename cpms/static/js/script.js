// Get the canvas element
var donutCanvas = document.getElementById('donutChart');

// Create the donut chart
var donutChart = new Chart(donutCanvas, {
    type: 'doughnut',
    data: {
        labels: [],
        datasets: [{
            data: [1, 0, 1, 0, 0], // Modify these values as needed
            backgroundColor: ['#0D73CD', '#FEFB2A', '#06d46d', '#DC3030', '#3E3E3E'], // Change colors
            borderWidth: 1
        }]
    },
    options: {
        cutout: '60%', // Adjust the size of the hole in the middle
        responsive: true,
        maintainAspectRatio: false,
        legend: {
            display: false // Hide the default legend
        }
    }
});






var lineChartCanvas = document.getElementById('lineChart').getContext('2d');
var gradient = lineChartCanvas.createLinearGradient(0, 0, 0, 300); // Adjust the gradient dimensions as needed
gradient.addColorStop(0, 'rgba(0, 200, 0, 0.8)'); // Starting color with opacity
gradient.addColorStop(1, 'rgba(0, 200, 0, 0.2)'); // Ending color with opacity

var lineChart = new Chart(lineChartCanvas, {
  type: 'line',
  data: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'],
    datasets: [{
      label: 'Line Chart Data',
      data: [10, 20, 15, 25, 23, 50, 45, 55, 75, 50, 65, 100],
      borderColor: '#06d46d',
      backgroundColor: gradient, // Use the gradient color
      borderWidth: 2,
      cubicInterpolationMode: 'monotone',
      fill: 'origin'
    }]
  },
  options: {
    maintainAspectRatio: false,
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
        suggestedMax: 100 // Adjust as needed to control the chart height
      }
    }
  }
});




const fromDateInput = document.getElementById('fromDate');
        const toDateInput = document.getElementById('toDate');

        fromDateInput.addEventListener('change', () => {
            const fromDate = new Date(fromDateInput.value);
            toDateInput.min = fromDateInput.value;
        });





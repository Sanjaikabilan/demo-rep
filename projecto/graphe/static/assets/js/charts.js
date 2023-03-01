$(document).ready(function() {
    // Get the canvas element and create a new chart
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: [],
        datasets: [{
          label: 'Sensor Data',
          data: [],
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  
    // Set up a timer to update the chart every 5 seconds
    setInterval(function() {
      // Send an AJAX request to the server to get the data
      $.ajax({
        url: '{% url "sensor_data_json" team.id %}',
        dataType: 'json',
        success: function(data) {
          // Update the chart with the new data
          myChart.data.labels = data.labels;
          myChart.data.datasets[0].data = data.data;
          myChart.update();
        },
        error: function() {
          alert('Error retrieving sensor data');
        }
      });
    }, 1000);
  });
  
  $(document).ready(function() {
      // Send AJAX request to fetch data
      $.getJSON('{% url "sensor_data_json" team.id %}', function(data) {
        // Get the table body element
        var tableBody = $('#data-table tbody');
  
        // Clear existing table rows
        tableBody.empty();
  
        // Iterate over the data and create a new table row for each item
        $.each(data.labels, function(index, label) {
          var newRow = $('<tr>');
          newRow.append($('<td>').text(label));
          newRow.append($('<td>').text(data.data[index]));
          tableBody.append(newRow);
        });
      });
  
      // Set a timer to update the table every 5 seconds
      setInterval(function() {
        $.getJSON('{% url "sensor_data_json" team.id %}', function(data) {
          var tableBody = $('#data-table tbody');
  
          // Clear existing table rows
          tableBody.empty();
  
          // Iterate over the data and create a new table row for each item
          $.each(data.labels, function(index, label) {
            var newRow = $('<tr>');
            newRow.append($('<td>').text(label));
            newRow.append($('<td>').text(data.data[index]));
            tableBody.append(newRow);
          });
        });
      }, 1000); // Refresh the table every 5 seconds
    });
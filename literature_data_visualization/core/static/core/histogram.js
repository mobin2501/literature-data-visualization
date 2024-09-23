// static/your_app/histogram.js

document.addEventListener('DOMContentLoaded', function () {
    fetch('/core/demo/api/') // Update this to your API endpoint
        .then(response => response.json())
        .then(data => {
            const titles = data.map(book => book.title);
            const pages = data.map(book => book.pages);

            const histogramData = {
                labels: titles, // Use book titles for the x-axis
                datasets: [{
                    label: 'Number of Pages',
                    data: pages, // Use page counts for the y-axis
                    backgroundColor: 'rgba(75, 192, 192, 0.5)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            };

            const ctx = document.getElementById('pagesHistogram').getContext('2d');
            const histogramChart = new Chart(ctx, {
                type: 'bar',
                data: histogramData,
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Pages'
                            }
                        },
                        x: {
                            title: {
                                display: true,
                                text: 'Book Titles'
                            }
                        }
                    }
                }
            });
        })
        .catch(error => {
            console.error('Error loading the data:', error);
        });
});

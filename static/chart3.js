$.ajax({
        url: "chart3_query",
        dataType: "json",
        /* beforeSend: function() {
          loader_gif.show();
          console.log("beforeSend");
        },
        complete: function() {
          loader_gif.hide();
        }, */
        success: function( data ) {
           createChart(data);
        }
})

function createChart(data) {
		
                        var json_data = JSON.stringify(data);
			var result = JSON.parse(json_data);

    $('#chart3').highcharts({
        chart: {
            zoomType: 'x'
        },
        title: {
            text: 'DEPARTMANLARA GÖRE İŞ İLANLARI DAĞILIMI'
        },
        xAxis: {
            type: 'datetime',
            minRange: 14 * 24 * 3600000 // fourteen days
        },
        yAxis: {
            title: {
                text: 'İlan Sayısı'
            }
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            area: {
                fillColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1},
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            }
        },

        series: [{
            type: 'area',
            name: 'ilan sayısı',
            pointInterval: 24 * 3600 * 1000,
            pointStart: Date.UTC(2006, 0, 1),
            data: result
        }]
    });



};

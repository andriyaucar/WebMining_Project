$.ajax({
        url: "chart4_query",
        dataType: "json",
        success: function( data ) {
           createChart(data);
        }
})

function createChart(data) {
	var json_data = JSON.stringify(data);
	var result = JSON.parse(json_data);

$('#chart4').highcharts({

        title: {
            text: 'İLLERE GÖRE İŞ İLAN DAĞILIMI',
        },

        xAxis: {
           // categories: cate
        },
        yAxis: {
            title: {
                text: 'ilan sayısı'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },

        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
	  name:'ilan sayısı',
          data:result
        }]
    });

}

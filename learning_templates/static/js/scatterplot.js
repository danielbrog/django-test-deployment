
window.onload = function () {

    hit_data.map((hit) => {
        hit.pitchside = (hit.pitchside=='R')? 'Right' : 'Left'
    })

        var chart = new CanvasJS.Chart("chartContainer", {
            animationEnabled: false,
            backgroundColor: "transparent",
            zoomEnabled: false,
            width: 400,
            height: 400,
            title: {
                text: "Hits"
            },
            axisX: {
                title: "distance (in ft.)",
                minimum: -200,
                maximum: 200
            },
            axisY: {
                title: "distance (in ft.)",
                minimum: 0,
                maximum: 420
            },
            data: [{
                type: "scatter",
                toolTipContent: "<b>Date: </b>{date}</br><b>Pitcher: </b>{pitcher} who pitches with his {pitchside} hand </br><b>LaunchSpeed: </b>{launchspeed}mph</br><b>Result:</b>{result_type}",
                dataPoints: hit_data
            }]
        });
        chart.render();
    }

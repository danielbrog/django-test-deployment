
window.onload = function () {
    const hitData= []
    '{% if hit_data %}'
'{% for hit in hit_data %}'
console.log('{{hit.landing_location_x}}')
hitData.push({
    x: parseInt('{{hit.landing_location_x}}',10),
    y: parseInt('{{hit.landing_location_y}}',10),
    pitcher: '{{hit.pitchername}}',
    pitchside: '{{hit.pitchside}}',
    launchspeed: '{{hit.launch_speed}}'
})
'{% endfor %}'
hitData.push({x:0,y:0})
var chart = new CanvasJS.Chart("chartContainer", {
  animationEnabled: false,
  backgroundColor: "transparent",
  zoomEnabled: false,
  width: 400,
  height: 400,
  title:{
    text: "Hits"
  },
  axisX: {
    title:"distance (in ft.)",
    minimum: -200,
    maximum: 200
  },
  axisY:{
    title: "distance (in ft.)",
    minimum: 0,
    maximum: 420
  },
  data: [{
    type: "scatter",
    toolTipContent: "<b>Pitcher: </b>{pitcher} who pitches with his {pitchside} hand </br><b>LaunchSpeed: </b>{launchspeed}mph",
    dataPoints: hitData
  }]
});
chart.render();
'{% endif %}'
}

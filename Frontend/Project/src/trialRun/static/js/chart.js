
  var $element = document.getElementById("myChart"),
  $btn = document.getElementById("showYear");

  var $elementTwo = document.getElementById("myChartTwo"),
  $btnTwo = document.getElementById("showYearTwo");

  //create a drawing context on the canvas
  var ctx = $element.getContext("2d");
  var ctxTwo = $elementTwo.getContext("2d");

  //--------------------------------------------------------------------------------------------------------------------------------------------------
  //-------------------------------------------------------------------------------------------------------------------------------------------------

  //declare variables
  var myChart;
  var data = { },
  processedData = { },
  orderClosingByMonth = { };
  var labels = [];

  //using jQuery ajax method get data from the external file. ( while using react you will do it differently)
  var jsonData = $.ajax({
    type:'GET',
  url:('/get_info'),
  dataType: 'json',
}).done(function(results) {
    //get values that only needed
    processedData = processData(results);
  data = {
    labels: processedData.labels,
  datasets: [{
    label: "Panel Temperature °C (Highest recorded) - 2021",
  data: processedData.data,
  backgroundColor: 'rgba(242, 120, 75,0.2)',
  borderColor: 'red',
  borderWidth: 4
}]
};

  myChart = new Chart(ctx, {
    type: 'line',
  data: data,
  options: {
    "scales": {
    "yAxes": [{
    "ticks": {
    "beginAtZero": true
    }
  }]
}
}
});
});

  var processData = function(jsonData) {

var jsonVal = jsonData["Time Series (Daily)"]

  var dataSet = [];

  var date;
  var locale = "en-us";
  var months = Object.keys(jsonVal).map(function(item) {
    date = new Date(item);

  return date.toLocaleDateString(locale, {
    month: "long"
});
}).filter(function(elem, index, self) {
return index == self.indexOf(elem);
});

  function sortByMonth(arr) {
var exactMonths = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
  ];
  arr.sort(function(a, b) {
return exactMonths.indexOf(a) - exactMonths.indexOf(b);
});
  return arr;
};

  labels = sortByMonth(months);

  for (var i = 0, total = labels.length; i < total; i++) {
    orderClosingByMonth[labels[i]] = {
      high: 0,
      allValue: [],
      allKey: []
    }
  }

  var thisMonth;
  Object.keys(jsonVal).filter(function(item) {
    date = new Date(item + " 00:00:00");
  thisMonth = date.toLocaleDateString(locale, {
    month: "long"
});

  if (orderClosingByMonth[thisMonth]["high"] < jsonVal[item]["2. high"]) {
    orderClosingByMonth[thisMonth]["high"] = jsonVal[item]["2. high"];
}

  orderClosingByMonth[thisMonth]["allKey"].push(item);
  orderClosingByMonth[thisMonth]["allValue"].push(parseFloat(jsonVal[item]["2. high"]));

  return 0;
});

  for (var i in orderClosingByMonth) {
    dataSet.push(orderClosingByMonth[i].high);
}
  ///debugger;

  return {
    labels: labels,
  data: dataSet
}
};

  $element.onclick = function(event) {
var activePoints = myChart.getElementsAtEvent(event);

if (activePoints.length > 0) {
//get the internal index of slice on the chart
var clickedElementindex = activePoints[0]["_index"];

  //get specific label by index 
  var label = myChart.data.labels[clickedElementindex];

  //get value by index      
  var value = myChart.data.datasets[0].data[clickedElementindex];


  /* update chart data */
  if(labels.indexOf(label) != -1) {
    myChart.data.labels = orderClosingByMonth[label].allKey.reverse();
  myChart.data.datasets[0].data = orderClosingByMonth[label].allValue.reverse();
  myChart.update();
  $btn.classList.remove("hide");
}

}
};
  $btn.onclick = function(event) {
    myChart.data.labels = processedData.labels;
  myChart.data.datasets[0].data = processedData.data;
  myChart.update();
  $btn.classList.add("hide");
}

  //---------------------------------------------------------------------------------------------------------------------------------------------
  //---------------------------------------------------------------------------------------------------------------------------------------------

  //declare variables
  var myChartTwo;
  var dataTwo = { },
  processedDataTwo = { },
  orderDailyYeildByMonth = { };
  var labelsTwo = [];

  //using jQuery ajax method get data from the external file. ( while using react you will do it differently)
  var jsonData = $.ajax({
    type:'GET',
  url:('/get_info'),                             //file path/URL for the json file
  dataType: 'json',             
}).done(function(results) {
    //get values that only needed
    processedDataTwo = processDataTwo(results);   //Assign the result of processDataTwo variable - labelsTwo[] and dataTwo[]
  dataForChartTwo = {
    labels: processedDataTwo.labelsTwo,         //labels names for chart Two
  datasets: [{                                //data for chart Two
    label: "Panel Daily Yeild (kW) - 2021",
  data: processedDataTwo.dataTwo,             // assign data from processDataTwo() to the data parameter of the chartTwo
  backgroundColor: 'rgba(162, 228, 255, 0.2)',
  borderColor: 'rgba(60, 99, 255, 1)',
  borderWidth: 4
}]
};

  myChartTwo = new Chart(ctxTwo, {
    type: 'line',
  data: dataForChartTwo,                                //myChartTwo Object
  options: {
    "scales": {
    "yAxes": [{
    "ticks": {
    "beginAtZero": true
    }
  }]
}
}
});
});


  var processDataTwo = function(jsonData) {

var jsonVal = jsonData["Time Series (Daily)"]

  var dataSet = [];

  var date;
  var locale = "en-us";
  var months = Object.keys(jsonVal).map(function(item) {
    date = new Date(item);

  return date.toLocaleDateString(locale, {
    month: "long"
});
}).filter(function(elem, index, self) {
return index == self.indexOf(elem);
});

  function sortByMonth(arr) {
var exactMonths = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
  ];
  arr.sort(function(a, b) {
return exactMonths.indexOf(a) - exactMonths.indexOf(b);
});
  return arr;
};

  labelsTwo = sortByMonth(months);

  for (var i = 0, total = labelsTwo.length; i < total; i++) {
    orderDailyYeildByMonth[labelsTwo[i]] = {
      dailyYeild: 0,
      allValue: [],
      allKey: []
    }
  }

  var thisMonth;
  Object.keys(jsonVal).filter(function(item) {
    date = new Date(item + " 00:00:00");
  thisMonth = date.toLocaleDateString(locale, {
    month: "long"
});

  if (orderDailyYeildByMonth[thisMonth]["dailyYeild"] < jsonVal[item]["1. dailyYeild"]) {
    orderDailyYeildByMonth[thisMonth]["dailyYeild"] = jsonVal[item]["1. dailyYeild"];
}

  orderDailyYeildByMonth[thisMonth]["allKey"].push(item);
  orderDailyYeildByMonth[thisMonth]["allValue"].push(parseFloat(jsonVal[item]["1. dailyYeild"]));

  return 0;
});

  for (var i in orderDailyYeildByMonth) {
    dataSet.push(orderDailyYeildByMonth[i].dailyYeild);
}
  ///debugger;

  return {
    labelsTwo: labelsTwo,
  dataTwo: dataSet
}
};

  $elementTwo.onclick = function(event) {
var activePoints = myChartTwo.getElementsAtEvent(event);

if (activePoints.length > 0) {
//get the internal index of slice on the chart
var clickedElementindex = activePoints[0]["_index"];

  //get specific label by index 
  var label = myChartTwo.data.labels[clickedElementindex];

  //get value by index      
  var value = myChartTwo.data.datasets[0].data[clickedElementindex];


  /* update chart data */
  if(labels.indexOf(label) != -1) {
    myChartTwo.data.labels = orderDailyYeildByMonth[label].allKey.reverse();
  myChartTwo.data.datasets[0].data = orderDailyYeildByMonth[label].allValue.reverse(); //here the data and labels are connected.
  myChartTwo.update();
  $btnTwo.classList.remove("hide");
}

}
};
  $btnTwo.onclick = function(event) {
    myChartTwo.dataForChartTwo.labels = processedDataTwo.labelsTwo;
  myChartTwo.dataForChartTwo.datasets[0].data = processedDataTwo.dataTwo;
  myChartTwo.update();  //before update the "labels" and "datasets" should be set as necessery
  $btnTwo.classList.add("hide");
}

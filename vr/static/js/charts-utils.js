var ajaxCache = {};
$(function(){
    $(".chart").each((i,e) => generateChart(i, $(e)));
});

function generateChart(i, element) {
    type = element.attr('data-type');
    path = element.attr('data-path');
    label = element.attr('data-label');

    element.html("<canvas></canvas>");
    var ctx = element.find("canvas")[0].getContext("2d");
    
    if(ajaxCache[path] == undefined) {
        $.getJSON(path, onGet(ctx, type, label));
    } else {
        drawChart(ctx, type, ajaxCache[path], label);
    }
}

function onGet(ctx, type, label) {
    return function(data) {
        ajaxCache[path] = data;
        drawChart(ctx, type, data, label);
    }
}

function drawChart(ctx, type, data, label) {
    var colors = new Array();
    if(type == 'bar' || type == 'line') {
        var colR = Math.floor(Math.random()*256);
        var colG = Math.floor(Math.random()*256);
        var colB = Math.floor(Math.random()*256);
        var colors = new Array();
        for(var i = 0; i<data.len; i++)  {
            colors.push('rgba('+ colR +','
                                + colB +','
                                + colG +','
                                + '1)');
        }
    } else {
        for(var i = 0; i<data.len; i++) {
            colors.push('rgba('+ Math.floor(Math.random()*256)+','
                                + Math.floor(Math.random()*256)+','
                                + Math.floor(Math.random()*256)+','
                                + '1)');
        }
    }

    var objs;
    if(type != "line") {
        objs =  {
            type: type,
            data: {
                labels: data.labels,
                datasets: [{
                    label: label,
                    data: data.data,
                    backgroundColor: colors
                }]
            }
        };
    } else {
        objs =  {
            type: type,
            data: {
                labels: data.labels,
                datasets: [{
                    label: label,
                    data: data.data,
                    borderColor: colors[0],
                    lineTension: 0,
                    fill: true
                }]
            }
        };
    }
    
    var chart = new Chart(ctx, objs);
}
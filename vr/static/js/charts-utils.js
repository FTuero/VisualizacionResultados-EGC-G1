var ajaxCache = {};
$(function(){
    $(".chart").each((i,e) => generateChart($(e)));
});

function generateChart(element) {
    type = element.data("type");
    path = element.data("path");
    label = element.data("label");

    element.html("<canvas></canvas>");
    var ctx = element.find("canvas")[0].getContext("2d");
    
    if(ajaxCache[path] == undefined) {
        $.getJSON(path, function(data) {
            ajaxCache[path] = data;
            drawChart(ctx, type, data, label);
        });
    } else {
        drawChart(ctx, type, ajaxCache[path], label);
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
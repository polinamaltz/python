
import justpy as jp
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


spline_chart = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: ''
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: ''
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: ''
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: ''
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: '',
        data: [[1,2], [3,4]]
    }]
}
"""
area_spline_chart = """
{
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""
pie_chart = """
{
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in January, 2018'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }]
    }]
}
"""
def app():
    data = pd.read_csv("../reviews.csv", parse_dates=True)

    data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')
    data['Day'] = data['Timestamp'].dt.date
    day_avg = data.groupby('Day')
    days = day_avg.mean()
    data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
    week_avg = data.groupby('Week')
    weeks = week_avg.mean()
    data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
    month_avg = data.groupby('Month')
    months = month_avg.mean()
    data['Weekday'] = data['Timestamp'].dt.strftime('%A')
    data['Weekday_num'] = data['Timestamp'].dt.strftime('%w')
    weekday_avg = data.groupby(['Weekday', 'Weekday_num']).mean()
    weekday_avg = weekday_avg.sort_values('Weekday_num')
    #   data_for_plot = [list(x) for x in zip(days.index.tolist(), [i[0] for i in days.values])]
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Course Reviews", classes = "text-h4 text-center q-pa-md")
    p1 = jp.QDiv(a = wp, text = "Analysis of The Course Reviews", classes = "text-h5 q-pl-md")
    #   Average Rating by Day
    hc = jp.HighCharts(a = wp, options = spline_chart)
    hc.options.title.text = "Average Rating by Day"
    hc.options.xAxis.categories = list(days.index)
    hc.options.series[0].data = list(days['Rating'])
    hc.options.series[0].name = "Rating"
    hc.options.xAxis.title.text = "Day"
    hc.options.yAxis.title.text = "Rating"
    #   Average Rating by Week
    hc1 = jp.HighCharts(a = wp, options = spline_chart)
    hc1.options.title.text = "Average Rating by Week"
    hc1.options.xAxis.categories = list(weeks.index)
    hc1.options.series[0].data = list(weeks['Rating'])
    hc1.options.series[0].name = "Rating"
    hc1.options.xAxis.title.text = "Week"
    hc1.options.yAxis.title.text = "Rating"
    #   Average Rating by Month
    hc2 = jp.HighCharts(a = wp, options = spline_chart)
    hc2.options.title.text = "Average Rating by Month"
    hc2.options.xAxis.categories = list(months.index)
    hc2.options.series[0].data = list(months['Rating'])
    hc2.options.series[0].name = "Rating"
    hc2.options.xAxis.title.text = "Month"
    hc2.options.yAxis.title.text = "Rating"
    #   Average Rating by Weekday
    hc3 = jp.HighCharts(a = wp, options = spline_chart)
    hc3.options.title.text = "What Day Are Reviews The Most Positive?"
    hc3.options.xAxis.categories = list(weekday_avg.index.get_level_values(0))
    hc3.options.series[0].data = list(weekday_avg['Rating'])
    hc3.options.series[0].name = "Rating"
    hc3.options.xAxis.title.text = "Weekday"
    hc3.options.yAxis.title.text = "Rating"
    #   Rating average by month by course
    mac = data.groupby(['Month', 'Course Name'])['Rating'].count().unstack()
    hc4 = jp.HighCharts(a = wp, options = area_spline_chart)
    hc4.options.title.text = "Rating average by month by course"
    labels = ['Python I', 'Python II', 'Data Processing', 'Data Visualization', 'GIS', 'Python: Beginner Level', 'Python: Advanced, Part I', 'Python: Advanced, Part II']
    mac.columns = labels
    hc4.options.xAxis.categories = list(mac.index)
    for i in range(0,8):
        hc4.options.series[i].data = list(mac[f'{labels[i]}'].values)
        hc4.options.series[i].name = labels[i]
    
    hc4.options.xAxis.title.text = "Month"
    hc4.options.yAxis.title.text = "Rating"
    #   Pie chart
    share = data.groupby(['Course Name'])['Rating'].count()
    hc5 = jp.HighCharts(a = wp, options = pie_chart)
    hc5.options.title.text = "Course Share"
    hc5.options.series[0].data = [{"name": x, "y": y} for x, y in zip(labels, share)]
    hc5.options.series[0].name = "Sales"
    return wp

jp.justpy(app)
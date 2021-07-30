import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv('reviews.csv', parse_dates=['Timestamp'])
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_average = data.groupby(['Week']).mean()

chart_def = """{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Course Rating by Week'
    },
    subtitle: {
        text: 'According to Coursera'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 5.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating for Week'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 5.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating by Week',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Analysis of Course Reviews by Week', classes='text-h3 text-center q-pt-lg')
    p1 = jp.QDiv(a=wp, text='These graphs represent course review analaysis', classes='text-body1 text-center q-pt-md')
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(week_average.index)
    hc.options.series[0].data = list(week_average['Rating'])

    return wp

jp.justpy(app)
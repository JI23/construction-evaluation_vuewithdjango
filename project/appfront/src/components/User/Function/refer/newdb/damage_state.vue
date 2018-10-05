<template>
  <!--为echarts准备一个具备大小的容器dom-->
    <div id="container" style="max-width:800px;height:400px"></div>
</template>

<script>
import Highcharts from "Highcharts"
export default{
    data() {
        return {
            chart: null,
        }
    },
    mounted() {
        var chart = Highcharts.chart('container', {
            title: {
                text: '易损性曲线'
            },
            subtitle: {
               // text: '数据来源：thesolarfoundation.com'
            },
            yAxis: {
                title: {
                    text: 'P(D>DS | Story Drift Ratio)'
                }
            },
            xAxis: {
                title: {
                    text: 'Story Drift Ratio(rad)'
                }
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle'
            },
            plotOptions: {
                series: {
                    label: {
                        connectorAllowed: false
                    },
                    pointStart: 0,
                    pointInterval: 0.02
                }
            },
            series: [{
                name: '安装，实施人员',
                data: [1, 3, 5, 7, 9, 1, 137133, 154175]
            }, {
                name: '工人',
                data: [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434,1,2,3,4,6,6,6,6,6,6]
            }, {
                name: '销售',
                data: [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
            }, {
                name: '项目开发',
                data: [null, null, 7988, 12169, 15112, 22452, 34400, 34227]
            }, {
                name: '其他',
                data: [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
            }],
            responsive: {
                rules: [{
                    condition: {
                        maxWidth: 500
                    },
                    chartOptions: {
                        legend: {
                            layout: 'horizontal',
                            align: 'center',
                            verticalAlign: 'bottom'
                        }
                    }
                }]
            }
        });
    }
}
    

</script>
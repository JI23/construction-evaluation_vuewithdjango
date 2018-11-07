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
            datachart: []
        }
    },
    methods :{
        getData(){
            let _this = this
            _this.$ajax({
                method:'get',
                url:'getChart',
                params:{
                    part_id : localStorage.getItem('part_id')
                },
            }).then(function(response){
                //console.log(response)
                var res = response.data
                //_this.chart.series = []
                _this.datachart = []
                for(var i = 0; i < res.data.length; i++){
                    var temp = {
                        name: i,
                        data: res.data[i]
                    }
                    _this.datachart.push(temp)
                }
                console.log(_this.datachart)
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
                    series: _this.datachart,
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




                    
            }).catch(function(err){
                console.log(err);
            });
        }
    },
    mounted() {
        let _this = this
        _this.getData()
    }
}
    

</script>
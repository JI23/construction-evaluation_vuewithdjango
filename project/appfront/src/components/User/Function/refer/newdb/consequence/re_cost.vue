<template>
    <div>
        <div class="wrapper4" >
            <el-col>
              <span class="lebal">Lower Quantity</span>
              <el-input v-bind:disabled="temp1" @change="re_draw" size="mini" style="width:100%" v-model="l_Quantity" placeholder="请输入内容"></el-input>
              <span class="lebal">Average Repair Cost for Lower Quantity of</span>
              <el-input v-bind:disabled="temp1" @change="re_draw" size="mini" style="width:100%" v-model="aver_re_l" placeholder="请输入内容"></el-input>
              <span class="lebal">Upper Quantity</span>
              <el-input v-bind:disabled="temp1" @change="re_draw" size="mini" style="width:100%" v-model="u_Quantity" placeholder="请输入内容"></el-input>
              <span class="lebal">Average Repair Cost for Upper Quantity of</span>
              <el-input v-bind:disabled="temp1" @change="re_draw" size="mini" style="width:100%" v-model="aver_re_u" placeholder="请输入内容"></el-input>
              <span class="lebal">COV</span>
              <el-input v-bind:disabled="temp1" @change="re_draw" size="mini" style="width:100%" v-model="COV" placeholder="请输入内容"></el-input>
          </el-col>
        </div>
        <div class="wrapper4">
            <el-col >
                <span class="lebal">CurveType</span>
                    <el-select v-bind:disabled="temp1" size="mini" v-model="CurveType" placeholder="请选择">
                        <el-option
                            v-for="item in options0"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                        </el-option>
                    </el-select>
            </el-col>
            <!--<div id="container" style="max-width:800px;height:400px"></div>-->
            <!--<schart class="wrapper" :canvasId="canvasId" :type="type" :data="data" :options="options"></schart>-->
            <div id="container" style="max-width:800px;height:400px"></div>
            <el-button style="display:block;margin:0 auto; position:relative; top: -30px" @click="save_next">下一步</el-button>
        </div>
    </div>
</template>

<script>
    import Highcharts from "Highcharts"
    export default {
        data() {
            return {
                temp1:false,
                test: null,
                chart: null,
                COV: '',
                l_Quantity: '',
                u_Quantity: '',
                aver_re_l: '',
                aver_re_u: '',
                options0: [{
                    value: '选项1',
                    label: 'DB_Common'
                }, {
                    value: '选项2',
                    label: 'DB_School'
                }, {
                    value: '选项3',
                    label: 'DB_Hospital'
                }, {
                    value: '选项4',
                    label: 'DB_Office'
                }, {
                    value: '选项6',
                    label: 'DB_FEMA'
                }],
                CurveType:'',
                canvasId: 'myCanvas',
                type: 'line',
                data: [
                    {name: '2014', value: 1342},
                    {name: '2015', value: 2123},
                    {name: '2016', value: 1654},
                    {name: '2017', value: 1795},
                ],
                options: {
                    title: 'Repair Cost'
                }
            }
        },

        beforeRouteLeave(to, from, next){
            if(sessionStorage.getItem('check') === 'DB_User'){
                var re_cost = {
                    l_Quantity: this.l_Quantity, 
                    aver_re_l: this.aver_re_l,
                    u_Quantity: this.u_Quantity,
                    aver_re_u: this.aver_re_u,
                    COV:this.COV,
                    CurveType:this.CurveType
                };
                var temp = localStorage.getItem("functionnum")+"_cost"
                sessionStorage.setItem(temp,JSON.stringify(re_cost));
            }
            next()
        },

        created(){
            if(sessionStorage.getItem('check') === 'DB_User'){
                this.temp1 = false
            }
            else{
                this.temp1 = true
            }
            var temp = localStorage.getItem("functionnum")+"_cost"
            try{
                var re_cost=JSON.parse(sessionStorage.getItem(temp))
                this.l_Quantity = re_cost['l_Quantity']
                this.aver_re_l = re_cost['aver_re_l']
                this.u_Quantity = re_cost['u_Quantity']
                this.aver_re_u = re_cost['aver_re_u']
                this.COV = re_cost['COV']
                this.CurveType = re_cost['CurveType']
            }
            catch(err){
                //console.log(err)
            }
        },



        methods: {
            save_next(){
                if(sessionStorage.getItem('check') === 'DB_User'){
                    let _this=this;
                    var re_cost = {
                        l_Quantity: this.l_Quantity, 
                        aver_re_l: this.aver_re_l,
                        u_Quantity: this.u_Quantity,
                        aver_re_u: this.aver_re_u,
                        COV:this.COV,
                        CurveType:this.CurveType,
                    };
                    localStorage.setItem("re_cost",JSON.stringify(re_cost));
                    this.$ajax({
                    method:'get',
                    url:'refer_check_re_costAndTime',
                    params:{
                        re_cost:re_cost,
                        path:localStorage.getItem('path2'),
                        statenum:localStorage.getItem('statenum'),
                        flag:'cost',
                    },
                    }).then(function(response){
                        console.log(response)
                        var res = response.data
                        console.log(res)
                        if (res.error_num == 0) {
                            console.log(res['msg'])
                            _this.$message.success(res['msg'])
                            _this.$router.push({name:'re_time'});
                        } 
                        else {
                            _this.$message.error(res['msg'])
                            console.log(res['msg'])
                        }
                    }).catch(function(err){
                        console.log(err);
                    });
                }
                this.$router.push({name:'re_time'});
                
            },
//实现更新图表
            re_draw(){
                //console.log(this.chart)
                this.test.series[0].update({
                    data: [29.9, 71.5, 306.4, 429.2, 144.0, 176.0, 135.6, 248.5, 216.4, 194.1, 95.6, 54.4]
                });
            }
        },

        mounted() {
            var chart = Highcharts.chart('container', {
                title: {
                    text: 'Damage State Group'
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
                    name: 'hhh',
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
            this.test = chart
        }
    }
</script>


<style scoped>
    .wrapper4{
        position:relative;/*相对定位:参考物*/
        float: left;;/*浮动:左浮动 与父元素的左端对齐 依次的往右端显示 一行显示不下就换行接着依次显示*/
        top:5px;
        width:43%;
        height:300px;
        margin:18px 20px;
    
}


    .wrapper{
        width: 18rem;
        height: 18rem;
  }


    .lebal{
        position:relative;
        display: inline-block;
        padding:9px 0;
        color: #333;
    }

</style>
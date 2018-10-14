<template>
    <div>
        <div class="wrapper6" >
            <el-col>
                <span class="lebal">易损性编号</span>
                <el-input v-bind:disabled="temp" style="width:100%" v-model="id" placeholder="请输入内容"></el-input>
                <span class="lebal">名称</span>
                <el-input v-bind:disabled="temp" style="width:100%" v-model="name" placeholder="请输入内容"></el-input>
                <span class="lebal">描述</span>
                <el-input v-bind:disabled="temp" style="width:100%" type="textarea" :rows="4" placeholder="请输入内容" v-model="description"></el-input>
            </el-col>
        </div>
        <div class="wrapper6">
            <el-col>
                <span class="lebal">构件造价</span>
                <el-input v-bind:disabled="temp" style="width:100%" v-model="id" placeholder="请输入内容"></el-input>
                <span class="lebal">方向性</span><br>
                <el-radio v-bind:disabled="temp" v-model="choose1" label="1">确定方向</el-radio>
                <el-radio v-bind:disabled="temp" v-model="choose1" label="2">无方向</el-radio><br><br>
                <el-button style="display:block;margin:0 auto" @click="savegen">下一步</el-button>
            </el-col>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                temp:false,
                dialogTableVisible: false,
                dialogFormVisible: false,
                form: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: ''
                },
                typename: '',
                DP_Dimension: '',
                units: '',
                formLabelWidth: '120px',
                value2: false,
                value1: false,
                choose1: '1',
                choose2: '1',
                options: [{
                    value: '选项1',
                    label: 'Store Drift Radio'
                }, {
                    value: '选项2',
                    label: 'Acceleration'
                }, {
                    value: '选项3',
                    label: 'Building Residual Drift'
                }, {
                    value: '选项4',
                    label: 'Peak Floor Velocity'
                }, {
                    value: '选项5',
                    label: 'Link Rotation Angle'
                }, {
                    value: '选项6',
                    label: 'Link Beam Chord Rotation'
                }],
                id:"",
                name:"",
                demand_Para:'',
                description: '',
                edit_options: [{
                    value: 'each',
                    label: 'Each',
                    children: [{
                        value: 'each',
                        label: 'Each',
                    }]
                    }, {
                    value: 'length',
                    label: 'Length',
                    children: [{
                        value: 'mil',
                        label: 'Mil',
                    }, {
                        value: 'inch',
                        label: 'Inch',
                    }, {
                        value: 'foot',
                        label: 'Foot',
                    }, {
                        value: 'yard',
                        label: 'Yard',
                    }, {
                        value: 'mile',
                        label: 'Mile',
                    }, {
                        value: 'nautical_mile',
                        label: 'Nautical_mile',
                    },{
                        value: 'micron',
                        label: 'Micron',
                    }, {
                        value: 'milliMeter',
                        label: 'Millimeter',
                    }, {
                        value: 'centiMeter',
                        label: 'Centimeter',
                    }, {
                        value: 'meter',
                        label: 'Meter',
                    },{
                        value: 'kilometer',
                        label: 'Kilometer',
                    }, {
                        value: 'furlong',
                        label: 'FurLong',
                    }, {
                        value: 'rod',
                        label: 'Rod',
                    }, {
                        value: 'light_year',
                        label: 'LightYear',
                    }]
                }, {
                    value: 'area',
                    label: 'Area',
                }, {
                    value: 'acceleration',
                    label: 'Acceleration',
                }, {
                    value: 'volume',
                    label: 'Volume',
                }, {
                    value: 'dryVolume',
                    label: 'DryVolume',
                }, {
                    value: 'mass',
                    label: 'Mass',
                }, {
                    value: 'energy',
                    label: 'Energy',
                }, {
                    value: 'force',
                    label: 'Force',
                }, {
                    value: 'velocity',
                    label: 'Velocity',
                }, {
                    value: 'angle',
                    label: 'Angle',
                }, {
                    value: 'smallTime',
                    label: 'SmallTime',
                }, {
                    value: 'largeTime',
                    label: 'LargeTime',
                }]
            }
        },

        beforeRouteLeave(to, from, next){
            if(sessionStorage.getItem('check') === 'DB_User'){
                var gen_info = {
                    name: this.name, 
                    id: this.id, 
                    //req_coe: this.req_coe,
                    //cus_name: this.cus_name,
                    description:this.description,
                    demand_Para:this.demand_Para,
                    value1: this.value1,
                    value2: this.value2,
                    choose1: this.choose1,
                    choose2: this.choose2,
                    typename: this.typename,
                    DP_Dimension: this.DP_Dimension,
                    units: this.units,
                };
                console.log(gen_info)
                sessionStorage.setItem("gen_info",JSON.stringify(gen_info));
            }
            next()
        },

        created(){
            if(sessionStorage.getItem('check') === 'DB_User'){
                this.temp = false
            }
            else{
                this.temp = true
            }
            try{
                var gen_info=JSON.parse(sessionStorage.getItem("gen_info"))
                console.log(gen_info)
                this.name = gen_info['name']
                this.id = gen_info['id'] 
                //req_coe: this.req_coe,
                //cus_name: this.cus_name,
                this.description = gen_info['description']
                this.demand_Para = gen_info['demand_Para']
                this.value1 = gen_info['value1']
                this.value2 = gen_info['value2']
                this.choose1 = gen_info['choose1']
                this.choose2 = gen_info['choose2']
                this.typename = gen_info['typename']
                this.DP_Dimension = gen_info['DP_Dimension']
                this.units = gen_info['units']
            }
            catch(err){
                //console.log(err)
            }
        },

        mounted: function () {
            var vm = this
            // 用$on事件来接收参数
            var label = JSON.parse(sessionStorage.getItem("label"));
            //console.log(input+'!!!!!');
            //var tempdata = this.data[input];
            //this.newData[input] = tempdata;
            sessionStorage.removeItem("label");
        },


        methods: {
            saveReq_Coe(){
                this.dialogFormVisible = false;
                //post数据去后台提交新建请求或修改
                let typename=this.typename
                let DP_Dimension= this.DP_Dimension
                let units=this.units
            },

            editReq(){
                this.dialogFormVisible = true;
                //向后台请求数据改变data的值
            },

            savegen() {//保存当前页面内容
                if(sessionStorage.getItem('check') === 'DB_User'){
                    if (this.value1==false){
                        var v1='False'
                    }
                    else{var v1='True'}
                    if (this.value2==false){
                        var v2='False'
                    }
                    else{var v2='True'}
                    var gen_info = {
                        name: this.name, 
                        id: this.id, 
                        //req_coe: this.req_coe,
                        //cus_name: this.cus_name,
                        description:this.description,
                        demand_Para:this.demand_Para,
                        value1: v1,
                        value2: v2,
                        choose1: this.choose1,
                        choose2: this.choose2,
                        typename: this.typename,
                        DP_Dimension: this.DP_Dimension,
                        units: this.units,
                    };
                    sessionStorage.setItem("gen_info",JSON.stringify(gen_info));
                    console.log(sessionStorage.getItem('gen_info'))
                    if(sessionStorage.getItem('part_id')==null){
                        var part_id=0
                    }
                    else{ 
                        var part_id=sessionStorage.getItem('part_id')
                    }
                    console.log(part_id)
                    console.log('!!!!')
                    let _this=this;
                    this.$ajax({
                        method:'get',
                        url:'savegen_gen_info',
                        params: {
                            'gen_info':gen_info,
                            'username':localStorage.getItem('phone'),
                            'part_id':part_id,
                        },
                    }).then(function(response){
                        console.log(response)
                        console.log('!')
                        var res = response.data
                        console.log(res)
                        console.log('!')
                        if (res['error_num'] == 0) {
                            console.log('111')
                            _this.$message.success(res['msg'])
                            _this.$router.push({name:'notes'});
                        } 
                        else {
                            _this.$message.error(res['msg'])
                            console.log(res['msg'])
                        }
                    }).catch(function(err){
                        console.log(err);
                        console.log('222')
                    });   
                }
                this.$router.push({name:'notes'});
            },
            open() {
                this.$alert('这是一段内容', '要求系数编辑', {
                    confirmButtonText: '确定',
                    callback: action => {
                        this.$message({
                            type: 'info',
                            message: `action: ${ action }`
                        });
                    }
                });
            }
        }
    }
</script>


<style>
    .wrapper6{
        position:relative;/*相对定位:参考物*/
        float:left;/*浮动:左浮动 与父元素的左端对齐 依次的往右端显示 一行显示不下就换行接着依次显示*/
        top:-15px;
        width:40%;
        height:350px;
        margin:18px 20px;
      
    }


    .lebal{
        position:relative;
        display: inline-block;
        padding:12px 0;
        color: #333;
    } 

</style>
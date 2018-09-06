<template>
    <div>
        <div class="wrapper6" >
            <el-col>
                <span class="lebal">ID</span>
                <el-input style="width:100%" v-model="id" placeholder="请输入内容"></el-input>
                <span class="lebal">Name</span>
                <el-input  style="width:100%" v-model="name" placeholder="请输入内容"></el-input>
                <span class="lebal">Description</span>
                <el-input style="width:100%" type="textarea" :rows="4" placeholder="请输入内容" v-model="description"></el-input>
                <span class="lebal">要求系数</span><br>
                <el-select size="mini" v-model="demand_Para" placeholder="请选择">
                    <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"><!--data未设置 -->
                    </el-option>
                </el-select>
                <el-row style="float: right; top: -27px; left:45px">
                    <el-button size="mini" @click="editReq">编辑</el-button><!--弹窗 未实现 -->
                    <el-button size="mini" @click="dialogFormVisible = true">添加</el-button>
                    <el-dialog title="要求系数" :visible.sync="dialogFormVisible">
                        <el-form :model="form">
                            <el-form-item label="type_name" :label-width="formLabelWidth">
                                <el-input v-model="typename" placeholder="请输入内容"></el-input>
                            </el-form-item>
                            <span style="position:relative; left:20px;">default units</span>
                            <el-cascader
                                :options="edit_options"
                                change-on-select
                                v-model="units" 
                                placeholder="请选择"
                                style="position:relative; left:30px;"
                            ></el-cascader><br><br>
                            <el-form-item label="DP Dimension" :label-width="formLabelWidth">
                                <el-select v-model="DP_Dimension" placeholder="请选择">
                                    <el-option label="区域一" value="shanghai"></el-option>
                                    <el-option label="区域二" value="beijing"></el-option>
                                </el-select>
                            </el-form-item>
                        </el-form>
                        <div slot="footer" class="dialog-footer">
                            <el-button @click="dialogFormVisible = false">取 消</el-button>
                            <el-button type="primary" @click="saveReq_Coe">确 定</el-button>
                        </div>
                    </el-dialog>
                </el-row>
            </el-col>
        </div>
        <div class="wrapper6">
            <el-col><br>
                <el-switch style="position:relative;" v-model="value1" active-text="use demand value from floor" inactive-text=" ">></el-switch><br><br>
                <el-switch style="position:relative;" v-model="value2" active-text="use supplied data needed" inactive-text=" ">></el-switch><br><br>
                <span class="lebal">Directional</span><br>
                <el-radio v-model="choose1" label="1">Directional</el-radio>
                <el-radio v-model="choose1" label="2">Non-Directional</el-radio><br>
                <span class="lebal">Correlation</span><br>
                <el-radio v-model="choose2" label="1">Correlated</el-radio>
                <el-radio v-model="choose2" label="2">Not Correlated</el-radio><br><br><br>
                <el-button style="display:block;margin:0 auto" @click="savegen">下一步</el-button>
            </el-col>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
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
            next()
        },

        created(){
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
            var label = JSON.parse(localStorage.getItem("label"));
            //console.log(input+'!!!!!');
            //var tempdata = this.data[input];
            //this.newData[input] = tempdata;
            localStorage.removeItem("label");
        },


        methods: {
            check(){
                this.$emit('check','');
            },
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
                console.log('111')
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
                localStorage.setItem("gen_info",JSON.stringify(gen_info));
                console.log(localStorage.getItem('gen_info'))
                if(localStorage.getItem('part_id')==null){
                    var part_id=0
                }
                else{ 
                    var part_id=localStorage.getItem('part_id')
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
        width:43%;
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
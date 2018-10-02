<template>
    <div style="overflow:scroll">
        <el-row >
            <el-button size="small" class='btn' @click="next">下一步</el-button>
            <el-button size="small" class='btn' @click="back">上一步</el-button>
        </el-row>
        <div class="div_table">
            <div>
                <el-col :span="24">
                    <el-col :span="4">
                        <span class="lebal">方向</span><br>
                        <el-input style="width:100%"  v-model="data[0].direction"  placeholder="X方向" :disabled="true"></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="6">
                        <span class="lebal">EDP类型</span><br>
                        <el-input style="width:100%"  v-model="data[0].EDP_type"  placeholder="Story Drift Ratio/层间位移角" :disabled="true"></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="5">
                        <span class="lebal">楼层数量</span><br>
                        <el-input style="width:100%"  @change="change_level_1" v-model="data[0].floor_no" ></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="5">
                        <span class="lebal">地震数量</span><br>
                        <el-input style="width:100%"  @change="change_level_1" v-model="data[0].earthquake_no" ></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                </el-col>
            </div>
            <div v-if="data[0].floor_no && data[0].earthquake_no">
                <el-table :data="data1"  border max-height="200">
                    <el-table-column prop="floor" label="楼层">
                        <template slot-scope="scope">
                            <el-input v-model="scope.row.floor"></el-input>
                        </template>
                    </el-table-column>
                    <el-table-column :label="col" v-for="(col,index) in temp1" :key="col">
                        <template slot-scope="scope">
                            <el-input v-model=scope.row[col]></el-input>
                        </template>
                    </el-table-column>
                </el-table>
            </div>
        </div>
        <div class="div_table">
            <div>
                <el-col :span="24">
                    <el-col :span="4">
                        <span class="lebal">方向</span><br>
                        <el-input style="width:100%"  v-model="data[1].direction"  placeholder="X方向" :disabled="true"></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="6">
                        <span class="lebal">EDP类型</span><br>
                        <el-input style="width:100%"  v-model="data[1].EDP_type"  placeholder="Acceleration/楼层加速度" :disabled="true"></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="5">
                        <span class="lebal">楼层数量</span><br>
                        <el-input style="width:100%"  @change="change_level_2" v-model="data[1].floor_no" ></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="5">
                        <span class="lebal">地震数量</span><br>
                        <el-input style="width:100%"  @change="change_level_2" v-model="data[1].earthquake_no" ></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                </el-col>
            </div>
            <div v-if="data[1].floor_no && data[1].earthquake_no">
                <el-table :data="data2"  border max-height="200">
                    <el-table-column prop="floor" label="楼层">
                        <template slot-scope="scope">
                            <el-input v-model="scope.row.floor"></el-input>
                        </template>
                    </el-table-column>
                    <el-table-column :label="col" v-for="(col,index) in temp2" :key="col">
                        <template slot-scope="scope">
                            <el-input v-model=scope.row[col]></el-input>
                        </template>
                    </el-table-column>
                </el-table>
            </div>
        </div>
        <div class="div_table">
            <div>
                <el-col :span="24">
                    <el-col :span="4">
                        <span class="lebal">方向</span><br>
                        <el-input style="width:100%"  v-model="data[2].direction"  placeholder="Y方向" :disabled="true"></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="6">
                        <span class="lebal">EDP类型</span><br>
                        <el-input style="width:100%"  v-model="data[2].EDP_type"  placeholder="Story Drift Ratio/层间位移角" :disabled="true"></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="5">
                        <span class="lebal">楼层数量</span><br>
                        <el-input style="width:100%"  @change="change_level_3" v-model="data[2].floor_no" ></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="5">
                        <span class="lebal">地震数量</span><br>
                        <el-input style="width:100%"  @change="change_level_3" v-model="data[2].earthquake_no" ></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                </el-col>
            </div>
            <div v-if="data[2].floor_no && data[2].earthquake_no">
                <el-table :data="data3"  border max-height="200">
                    <el-table-column prop="floor" label="楼层">
                        <template slot-scope="scope">
                            <el-input v-model="scope.row.floor"></el-input>
                        </template>
                    </el-table-column>
                    <el-table-column :label="col" v-for="(col,index) in temp3" :key="col">
                        <template slot-scope="scope">
                            <el-input v-model=scope.row[col]></el-input>
                        </template>
                    </el-table-column>
                </el-table>
            </div>
        </div>
        <div class="div_table">
            <div>
                <el-col :span="24">
                    <el-col :span="4">
                        <span class="lebal">方向</span><br>
                        <el-input style="width:100%"  v-model="data[3].direction"  placeholder="Y方向" :disabled="true"></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="6">
                        <span class="lebal">EDP类型</span><br>
                        <el-input style="width:100%"  v-model="data[3].EDP_type"  placeholder="Story Drift Ratio/层间位移角" :disabled="true"></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="5">
                        <span class="lebal">楼层数量</span><br>
                        <el-input style="width:100%"  @change="change_level_4" v-model="data[3].floor_no" ></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="5">
                        <span class="lebal">地震数量</span><br>
                        <el-input style="width:100%"  @change="change_level_4" v-model="data[3].earthquake_no" ></el-input>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                </el-col>
            </div>
            <div v-if="data[3].floor_no && data[3].earthquake_no">
                <el-table :data="data4"  border max-height="200">
                    <el-table-column prop="floor" label="楼层">
                        <template slot-scope="scope">
                            <el-input v-model="scope.row.floor"></el-input>
                        </template>
                    </el-table-column>
                    <el-table-column :label="col" v-for="(col,index) in temp4" :key="col">
                        <template slot-scope="scope">
                            <el-input v-model=scope.row[col]></el-input>
                        </template>
                    </el-table-column>
                </el-table>
            </div>
        </div>

        <div class="btn-group">
            <el-button>点击预览</el-button>
            <el-button @click='rate'>提交并生成结果</el-button>
            <el-button @click="save6">保存</el-button>
        </div>
        
    </div>
</template>

<script>
export default {
    beforeRouteLeave(to, from, next){
        let structure_response = JSON.stringify(this.data)
        localStorage.setItem('structure_response', structure_response)
        next()
    },
    created(){
      //从localStorage中读取条件并赋值给查询表单
        let data_temp=JSON.parse(localStorage.getItem('structure_response'))
        console.log
        if(data_temp==null||data_temp=='')
            {
                console.log('没有值')
            }    
        else
            this.data=data_temp
        //let data = JSON.parse(localStorage.getItem('structure_response'))
        console.log('step6.vue')
        // if (data != '') {
        //     this.data = data
        // }
        
    },
    methods:{
        next(){
            this.$emit('next','');
        },
        back(){
            this.$emit('back','');
        },
        save6(){
            let _this=this;
            console.log(this.Floor_info)
            var project=localStorage.getItem('project')
            this.$ajax({
                method:'get',
                url:'step6',
                params:{
                    data:this.data,
                    project:project,
                },
            })
            .then(function(response){
                console.log(response)
                var res = response.data
                console.log(res)
                if (res.error_num == 0) {
                    console.log(res['msg'])
                    _this.$message.success(res['msg'])
                } 
                else {
                    _this.$message.error(res['msg'])
                    console.log(res['msg'])
                }
            })
            .catch(function(err){
                    console.log(err);
                    });
        },
        rate(){
            let _this=this;
            console.log(this.Floor_info)
            var project=localStorage.getItem('project')
            this.$ajax({
                method:'get',
                url:'rate',
                params:{
                    project:project,
                },
            }).then(function(response){
                console.log(response)
                var res = response.data
                console.log(res)
                if (res.error_num == 0) {
                    console.log(res['msg'])
                    _this.$message.success(res['msg'])
                } 
                else {
                    _this.$message.error(res['msg'])
                    console.log(res['msg'])
                }
            }).catch(function(err){
                console.log(err);
            });
        },
        change_level_1(){
            if(this.data[0].floor_no && this.data[0].earthquake_no){
                console.log("buweikong1")
                console.log(this.data[0].earthquake_no)
                this.temp1={}
                for(var i = 0; i < this.data[0].earthquake_no; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp1[i] = temp
                }
                this.option_num = "1"
                this.data1=[]
                for(var j = 0; j < this.data[0].floor_no; j++){
                    var temp = [{}]
                    for(var i = 0; i < this.data[0].earthquake_no; i++){
                        var temp_1 = "earthquake" + (i+1)
                        temp[0][temp_1] = ''
                    }
                    temp[0].floor = '情况1'
                    this.data1.push(temp[0])
                }

            }
        },
        change_level_2(){
            //console.log(this.data[1].earthquake_no)
            //console.log(this.data[1].floor_no)
            console.log("buweikong2")
            console.log(this.data[1].earthquake_no)
            if(this.data[1].floor_no && this.data[1].earthquake_no){
                this.temp2={}
                console.log("change_level_2")
                console.log(this.temp2)
                for(var i = 0; i < this.data[1].earthquake_no; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp2[i] = temp
                }
                this.option_num = "2"
                        this.data2=[]
                        for(var j = 0; j < this.data[1].floor_no; j++){
                            var temp = [{}]
                            for(var i = 0; i < this.data[1].earthquake_no; i++){
                                var temp1 = "earthquake" + (i+1)
                                temp[0][temp1] = ''
                            }
                            temp[0].floor = '情况2'
                            this.data2.push(temp[0])
                        }
            }
        },
        change_level_3(){
            if(this.data[2].floor_no && this.data[2].earthquake_no){
                this.temp3={}
                for(var i = 0; i < this.data[2].earthquake_no; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp3[i] = temp
                }
                this.option_num = "3"
                        this.data3=[]
                        for(var j = 0; j < this.data[2].floor_no; j++){
                            var temp = [{}]
                            for(var i = 0; i < this.data[2].earthquake_no; i++){
                                var temp1 = "earthquake" + (i+1)
                                temp[0][temp1] = ''
                            }
                            temp[0].floor = '情况3'
                            this.data3.push(temp[0])
                        }
            }
        },
        change_level_4(){
            if(this.data[3].floor_no && this.data[3].earthquake_no){
                this.temp4={}
                for(var i = 0; i < this.data[3].earthquake_no; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp4[i] = temp
                }
                this.option_num = "4"
                        this.data4=[]
                        for(var j = 0; j < this.data[3].floor_no; j++){
                            var temp = [{}]
                            for(var i = 0; i < this.data[3].earthquake_no; i++){
                                var temp1 = "earthquake" + (i+1)
                                temp[0][temp1] = ''
                            }
                            temp[0].floor = '情况4'
                            this.data4.push(temp[0])
                        }
                }
        },
        
    },
    data(){
        return {
            option_num:'0',
            data1:[],
            temp:'',
            temp1:'',
            temp2:'',
            temp3:'',
            temp4:'',
            data2:[],
            data3:[],
            data4:[],
            data:[{
                direction:'X方向',
                EDP_type:'Story Drift Ratio/层间位移角',
                floor_no:null,
                earthquake_no:null
            },{
                direction:'X方向',
                EDP_type:'Acceleration/楼层加速度',
                floor_no:null,
                earthquake_no:null
            },
            {
                direction:'Y方向',
                EDP_type:'Story Drift Ratio/层间位移角',
                floor_no:null,
                earthquake_no:null
            },
            {
                direction:'Y方向',
                EDP_type:'Acceleration/楼层加速度',
                floor_no:null,
                earthquake_no:null
            }
            ],
            EDP_option:[{
                value:'1',
                label: 'Story Drift Ratio/层间位移角',
            }, {
                value:'2',
                label: 'Acceleration/楼层加速度',
            }],
            direction_option:[{
                value:'1',
                label: 'X方向',
            }, {
                value:'2',
                label: 'Y方向',
            }]
        }    
    }
}
</script>


<style scoped>
    /* .el-row{
        margin-bottom: 20px;
    } */
    .div_table{
        margin-bottom:20px;
        margin-top:20px;
    }
    .wrapper{  
        margin:10px auto;
        max-width:800px;
    }
    .lebal{
        display: inline-block;
        padding:12px 0;
        color: #333;
    }
    .btn-group{
        margin:15px 0;
    }
    .clearfix:after{
        content:'';
        display: block;
        clear: both;
    }
    .btn{
        margin-top:12px;
    }
</style>

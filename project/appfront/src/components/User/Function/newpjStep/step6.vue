<template>
    <div>
        <el-row>
            <el-button size="small" class='btn' @click="next">下一步</el-button>
            <el-button size="small" class='btn' @click="back">上一步</el-button>
        </el-row>
        <div>
            <el-col :span="24">
                <el-col :span="11">
                    <span class="lebal">方向</span><br>
                    <el-select @change="change_level" style="width:100%" v-model="data[0].direction" placeholder="请选择">
                        <el-option
                            v-for="item in direction_option"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">                    
                        </el-option>
                    </el-select>
                    <span class="lebal">EDP类型</span><br>
                    <el-select @change="change_level" style="width:100%" v-model="data[0].EDP_type" placeholder="请选择">
                        <el-option
                            v-for="item in EDP_option"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">                    
                        </el-option>
                    </el-select>
                </el-col>
                <el-col :span="1" style="color:transparent">''</el-col>
                <el-col :span="11">
                    <span class="lebal">楼层数量</span>
                    <el-input @change="change_level" v-model="data[0].floor_no" placeholder="请输入内容"></el-input>
                    <span class="lebal">地震数量</span>
                    <el-input @change="change_level" v-model="data[0].earthquake_no" placeholder="请输入内容"></el-input>
                </el-col>
            </el-col>
        </div>
        <div >
            <el-table :data="data1" v-if="option_num === '1'" border max-height="200">
                <el-table-column prop="floor" label="楼层">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.floor"></el-input>
                    </template>
                </el-table-column>
                <el-table-column :label="col" v-for="(col,index) in temp" :key="col">
                    <template slot-scope="scope">
                        <el-input v-model=scope.row[col]></el-input>
                    </template>
                </el-table-column>
            </el-table>
            <el-table :data="data2" v-if="option_num === '2'" border max-height="200">
                <el-table-column prop="floor" label="楼层">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.floor"></el-input>
                    </template>
                </el-table-column>
                <el-table-column :label="col" v-for="(col,index) in temp" :key="col">
                    <template slot-scope="scope">
                        <el-input v-model=scope.row[col]></el-input>
                    </template>
                </el-table-column>
            </el-table>
            <el-table :data="data3" v-if="option_num === '3'" border max-height="200">
                <el-table-column prop="floor" label="楼层">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.floor"></el-input>
                    </template>
                </el-table-column>
                <el-table-column :label="col" v-for="(col,index) in temp" :key="col">
                    <template slot-scope="scope">
                        <el-input v-model=scope.row[col]></el-input>
                    </template>
                </el-table-column>
            </el-table>
            <el-table :data="data4" v-if="option_num === '4'" border max-height="200">
                <el-table-column prop="floor" label="楼层">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.floor"></el-input>
                    </template>
                </el-table-column>
                <el-table-column :label="col" v-for="(col,index) in temp" :key="col">
                    <template slot-scope="scope">
                        <el-input v-model=scope.row[col]></el-input>
                    </template>
                </el-table-column>
            </el-table>
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
                    data1:this.data1,
                    data2:this.data2,
                    data3:this.data3,
                    data4:this.data4,
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
        change_level(){
            console.log(this.data1)
            if(this.data[0].direction !== null && this.data[0].EDP_type !== null && this.data[0].floor_no && this.data[0].earthquake_no){
                this.temp={}
                for(var i = 0; i < this.data[0].earthquake_no; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp[i] = temp
                }
                if(this.data[0].direction === '1'){
                    if(this.data[0].EDP_type === "1"){
                        this.option_num = "1"
                        this.data1=[]
                        for(var j = 0; j < this.data[0].floor_no; j++){
                            var temp = [{}]
                            for(var i = 0; i < this.data[0].earthquake_no; i++){
                                var temp1 = "earthquake" + (i+1)
                                temp[0][temp1] = ''
                            }
                            temp[0].floor = '情况1'
                            this.data1.push(temp[0])
                        }
                        console.log('!!!')
                        console.log(this.data1)
                        console.log('!!!!')
                    }
                    else{
                        this.option_num = "2"
                        this.data2=[]
                        for(var j = 0; j < this.data[0].floor_no; j++){
                            var temp = [{}]
                            for(var i = 0; i < this.data[0].earthquake_no; i++){
                                var temp1 = "earthquake" + (i+1)
                                temp[0][temp1] = ''
                            }
                            temp[0].floor = '情况2'
                            this.data2.push(temp[0])
                        }
                    }
                }
                else if(this.data[0].direction === '2'){
                    if(this.data[0].EDP_type === "1"){
                        this.option_num = "3"
                        this.data3=[]
                        for(var j = 0; j < this.data[0].floor_no; j++){
                            var temp = [{}]
                            for(var i = 0; i < this.data[0].earthquake_no; i++){
                                var temp1 = "earthquake" + (i+1)
                                temp[0][temp1] = ''
                            }
                            temp[0].floor = '情况3'
                            this.data3.push(temp[0])
                        }
                    }
                    else{
                        this.option_num = "4"
                        this.data4=[]
                        for(var j = 0; j < this.data[0].floor_no; j++){
                            var temp = [{}]
                            for(var i = 0; i < this.data[0].earthquake_no; i++){
                                var temp1 = "earthquake" + (i+1)
                                temp[0][temp1] = ''
                            }
                            temp[0].floor = '情况4'
                            this.data4.push(temp[0])
                        }
                    }
                }
            }
            console.log(this.option_num)
        },
    },
    data(){
        return {
            option_num:'0',
            data1:[],
            temp:'',
            data2:[],
            data3:['1'],
            data4:[],
            data:[{
                direction:'',
                EDP_type:null,
                floor_no:null,
                earthquake_no:null
            },{
                direction:'Y',
                EDP_type:null,
                floor_no:null,
                earthquake_no:null
            }],
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

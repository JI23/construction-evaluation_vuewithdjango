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
                        <span class="lebal">方向：X方向</span><br>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="12">
                        <span class="lebal">EDP类型：Story Drift Ratio/层间位移角</span><br>
                    </el-col>
                </el-col>
            </div><br>
            <div>
                <el-table :data="data1"  style="width:50%" class="tb-edit" border max-height="200" highlight-current-row :header-cell-style="rowClass">
                    <el-table-column width="80" prop="floor" label="楼层">
                        <template slot-scope="scope">
                            <el-input size="small" v-model="scope.row.floor" :disabled="true"></el-input><span>{{scope.row.floor}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column width="250" :label="col" v-for="(col,index) in temp1" :key="col">
                        <template width="140" slot-scope="scope">
                            <el-input size="small" v-model=scope.row[col]></el-input><span>{{scope.row[col]}}</span>
                        </template>
                    </el-table-column>
                </el-table>
            </div>
        </div>
        <div class="div_table">
            <div>
                <el-col :span="24">
                    <el-col :span="4">
                        <span class="lebal">方向：X方向</span><br>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="12">
                        <span class="lebal">EDP类型：Acceleration/楼层加速度</span><br>
                    </el-col>
                </el-col>
            </div><br>
            <div>
                <el-table :data="data2"  style="width:50%" class="tb-edit" border max-height="200" highlight-current-row :header-cell-style="rowClass">
                    <el-table-column width=80px prop="floor" label="楼层">
                        <template slot-scope="scope">
                            <el-input size="small" v-model="scope.row.floor" :disabled="true"></el-input><span>{{scope.row.floor}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column width="250" :label="col" v-for="(col,index) in temp2" :key="col">
                        <template slot-scope="scope">
                            <el-input size="small" v-model=scope.row[col]></el-input><span>{{scope.row[col]}}</span>
                        </template>
                    </el-table-column>
                </el-table>
            </div>
        </div>
        <div class="div_table">
            <div>
                <el-col :span="24">
                    <el-col :span="4">
                        <span class="lebal">方向：Y方向</span><br>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="12">
                        <span class="lebal">EDP类型：Story Drift Ratio/层间位移角</span><br>
                    </el-col>
                </el-col>
            </div><br>
            <div>
                <el-table :data="data3" style="width:50%" class="tb-edit" border max-height="200" highlight-current-row :header-cell-style="rowClass">
                    <el-table-column width=80px prop="floor" label="楼层">
                        <template slot-scope="scope">
                            <el-input size="small" v-model="scope.row.floor" :disabled="true"></el-input><span>{{scope.row.floor}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column width="250" :label="col" v-for="(col,index) in temp3" :key="col">
                        <template slot-scope="scope">
                            <el-input size="small" v-model=scope.row[col]></el-input><span>{{scope.row[col]}}</span>
                        </template>
                    </el-table-column>
                </el-table>
            </div>
        </div>
        <div class="div_table">
            <div>
                <el-col :span="24">
                    <el-col :span="4">
                        <span class="lebal">方向：Y方向</span><br>
                    </el-col>
                    <el-col :span="1" style="color:transparent">''</el-col>
                    <el-col :span="12">
                        <span class="lebal">EDP类型：Acceleration/楼层加速度</span><br>
                    </el-col>
                </el-col>
            </div><br>
            <div>
                <el-table :data="data4" style="width:50%" class="tb-edit" border max-height="200" highlight-current-row :header-cell-style="rowClass">
                    <el-table-column width=80px prop="floor" label="楼层">
                        <template slot-scope="scope">
                            <el-input size="small" v-model="scope.row.floor" :disabled="true"></el-input><span>{{scope.row.floor}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column width="250" :label="col" v-for="(col,index) in temp4" :key="col">
                        <template slot-scope="scope">
                            <el-input size="small" v-model=scope.row[col]></el-input><span>{{scope.row[col]}}</span>
                        </template>
                    </el-table-column>
                </el-table>
            </div>
        </div>

        <div class="btn-group">
            <el-button @click='preview'>点击预览</el-button>
            <el-button @click='rate'>提交并生成结果</el-button>
            <el-button @click="save6">保存</el-button>
        </div>
        
    </div>
</template>

<script>
export default {
    beforeRouteLeave(to, from, next){
        let structure_response=new Array
        structure_response[0]=this.data1
        structure_response[1]=this.data2
        structure_response[2]=this.data3
        structure_response[3]=this.data4
        structure_response=JSON.stringify(structure_response)
        localStorage.setItem('structure_response', structure_response)
        console.log("路由离开前")
        console.log(JSON.parse(localStorage.getItem('structure_response')))
        next()
    },
    created(){
      //从localStorage中读取条件并赋值给查询表单
        var floors_num = localStorage.getItem('floors')
        let quake_num = localStorage.getItem('number')
        this.floors_num = floors_num
        this.quake_num = quake_num
        this.change_level_1()
        this.change_level_2()
        this.change_level_3()
        this.change_level_4()
        //let data_temp=JSON.parse(localStorage.getItem('structure_response'))

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
            var isFull=true
            for(var j = 0; j < this.floors_num; j++){
                for(var i=0;i<this.quake_num;i++)
                {
                    var temp="earthquake"+(i+1)
                    if(this.data1[j][temp]===''||this.data1[j][temp]==null){
                        isFull=false
                        _this.$message.error("请完整填写构建信息好吗")
                    }
                }   
            }
            for(var j = 0; j < this.floors_num; j++){
                for(var i=0;i<this.quake_num;i++)
                {
                    var temp="earthquake"+(i+1)
                    if(this.data2[j][temp]===''||this.data2[j][temp]==null){
                        isFull=false
                        _this.$message.error("请完整填写构建信息好吗")
                    }
                }   
            }
            for(var j = 0; j < this.floors_num; j++){
                for(var i=0;i<this.quake_num;i++)
                {
                    var temp="earthquake"+(i+1)
                    if(this.data3[j][temp]===''||this.data3[j][temp]==null){
                        isFull=false
                        _this.$message.error("请完整填写构建信息好吗")
                    }
                }   
            }
            for(var j = 0; j < this.floors_num; j++){
                for(var i=0;i<this.quake_num;i++)
                {
                    var temp="earthquake"+(i+1)
                    if(this.data4[j][temp]===''||this.data4[j][temp]==null){
                        isFull=false
                        _this.$message.error("请完整填写构建信息好吗")
                    }
                }   
            }
            if(isFull){
            // var floors_num = localStorage.getItem('floors')
            // let quake_num = localStorage.getItem('number')
            let data=[{
                        direction:'X方向',
                        EDP_type:'Story Drift Ratio/层间位移角',
                        floor_no:this.floors_num,
                        earthquake_no:this.quake_num
                    },{
                        direction:'X方向',
                        EDP_type:'Acceleration/楼层加速度',
                        floor_no:this.floors_num,
                        earthquake_no:this.quake_num
                    },
                    {
                        direction:'Y方向',
                        EDP_type:'Story Drift Ratio/层间位移角',
                        floor_no:this.floors_num,
                        earthquake_no:this.quake_num
                    },
                    {
                        direction:'Y方向',
                        EDP_type:'Acceleration/楼层加速度',
                        floor_no:this.floors_num,
                        earthquake_no:this.quake_num
                    }
                    ]
            var project=localStorage.getItem('project')
            this.$ajax({
                method:'get',
                url:'step6',
                params:{
                    data:data,
                    data1:this.data1,
                    data2:this.data2,
                    data3:this.data3,
                    data4:this.data4,
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
                    _this.$message.error("保存失败！")
                    console.log(res['msg'])
                }
            })
            .catch(function(err){
                    console.log(err);
                    });
            }
        },
        rate(){
            let _this=this;
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
        preview(){
            window.open('http://47.105.86.170/project.pdf')
            let _this=this;
            var project=localStorage.getItem('project')
            this.$ajax({
                method:'get',
                url:'preview',
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
            let data_temp=JSON.parse(localStorage.getItem('structure_response'))
            if(data_temp==null||data_temp=='')
            {
                console.log("为空，说明第一次进入")
                this.temp1={}
                for(var i = 0; i < this.quake_num; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp1[i] = temp
                }
                this.option_num = "1"
                this.data1 = []
                for(var j = 0; j < this.floors_num; j++){
                    var temp = [{}]
                    for(var i = 0; i < this.quake_num; i++){
                        var temp1 = "earthquake" + (i+1)
                        temp[0][temp1] = ''    
                    }       
                    temp[0].floor = j+1
                    this.data1.push(temp[0])
                }
            }    
            else if(Array.isArray(data_temp[0][0]))
            {
                console.log("数组，说明是点编辑的")
                this.temp1={}
                for(var i = 0; i < this.quake_num; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp1[i] = temp
                }
                this.option_num = "1"
                this.data1 = []
                for(var j = 0; j < this.floors_num; j++){
                    var temp = [{}]
                    for(var i = 0; i < this.quake_num; i++){
                        var temp1 = "earthquake" + (i+1)
                        temp[0][temp1] = data_temp[1][j][i]        
                    }
                    temp[0].floor = j+1
                    this.data1.push(temp[0])
                }
            }
            else
                {
                    console.log("有值，说明点了上一步")
                    let data_back_next=JSON.parse(localStorage.getItem('structure_response'))
                    this.temp1={}
                    for(var i = 0; i < this.quake_num; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp1[i] = temp
                    }
                    this.option_num = "1"
                    this.data1 = []
                    for(var j = 0; j < this.floors_num; j++){
                        var temp = [{}]
                        for (var item in data_back_next[0][j])
                        {
                            temp[0][item] = data_back_next[0][j][item]        
                        }
                        temp[0].floor = j+1
                        this.data1.push(temp[0])
                    }    
                }
        },
        change_level_2(){
            let data_temp=JSON.parse(localStorage.getItem('structure_response'))
            if(data_temp==null || data_temp=='')
            {
                console.log("为空，说明第一次进入")
                this.temp2={}
                for(var i = 0; i < this.quake_num; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp2[i] = temp
                }
                this.option_num = "2"
                this.data2 = []
                for(var j = 0; j < this.floors_num; j++){
                    var temp = [{}]
                    for(var i = 0; i < this.quake_num; i++){
                        var temp2 = "earthquake" + (i+1)
                        temp[0][temp2] = ''    
                    }       
                    temp[0].floor = j+1
                    this.data2.push(temp[0])
                }
            }
            else if(Array.isArray(data_temp[0][0]))
            {
                console.log("数组，说明是点编辑的")
                this.temp2={}
                for(var i = 0; i < this.quake_num; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp2[i] = temp
                }
                this.option_num = "2"
                this.data2 = []
                for(var j = 0; j < this.floors_num; j++){
                    var temp = [{}]
                    for(var i = 0; i < this.quake_num; i++){
                        var temp2 = "earthquake" + (i+1)
                        temp[0][temp2] = data_temp[0][j][i]   
                    }
                    temp[0].floor = j+1
                    this.data2.push(temp[0])
                }
            }
                else
                {
                    console.log("有值，说明点了上一步")
                    let data_back_next=JSON.parse(localStorage.getItem('structure_response'))
                    this.temp2={}
                    for(var i = 0; i < this.quake_num; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp2[i] = temp
                    }
                    this.option_num = "2"
                    this.data2 = []
                    for(var j = 0; j < this.floors_num; j++){
                        var temp = [{}]
                        for (var item in data_back_next[1][j])
                        {
                            temp[0][item] = data_back_next[1][j][item]        
                        }
                        temp[0].floor = j+1
                        this.data2.push(temp[0])
                    }
                    
                }
        },
        change_level_3(){
            let data_temp=JSON.parse(localStorage.getItem('structure_response'))
            if(data_temp==null || data_temp=='')
            {
                console.log("为空，说明第一次进入")
                this.temp3={}
                for(var i = 0; i < this.quake_num; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp3[i] = temp
                }
                this.option_num = "3"
                this.data3 = []
                for(var j = 0; j < this.floors_num; j++){
                    var temp = [{}]
                    for(var i = 0; i < this.quake_num; i++){
                        var temp3 = "earthquake" + (i+1)
                        temp[0][temp3] = ''    
                    }       
                    temp[0].floor = j+1
                    this.data3.push(temp[0])
                }
                }
            else if(Array.isArray(data_temp[0][0]))
            {
                console.log("数组，说明是点编辑的")
                this.temp3={}
                for(var i = 0; i < this.quake_num; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp3[i] = temp
                }
                this.option_num = "3"
                this.data3 = []
                for(var j = 0; j < this.floors_num; j++){
                    var temp = [{}]
                    for(var i = 0; i < this.quake_num; i++){
                        var temp3 = "earthquake" + (i+1)
                        temp[0][temp3] = data_temp[3][j][i]     
                    }
                    temp[0].floor = j+1
                    this.data3.push(temp[0])
                }
            }
            else
                {
                    console.log("有值，说明点了上一步")
                    let data_back_next=JSON.parse(localStorage.getItem('structure_response'))
                    this.temp3={}
                    for(var i = 0; i < this.quake_num; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp3[i] = temp
                    }
                    this.option_num = "3"
                    this.data3 = []
                    for(var j = 0; j < this.floors_num; j++){
                        var temp = [{}]
                        for (var item in data_back_next[2][j])
                        {
                            temp[0][item] = data_back_next[2][j][item]        
                        }
                        temp[0].floor = j+1
                        this.data3.push(temp[0])
                    }
                    
                }
        },
        change_level_4(){
            let data_temp=JSON.parse(localStorage.getItem('structure_response'))
            if(data_temp==null || data_temp=='')
            {
                console.log("为空，说明第一次进入")
                this.temp4={}
                for(var i = 0; i < this.quake_num; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp4[i] = temp
                }
                this.option_num = "4"
                this.data4 = []
                for(var j = 0; j < this.floors_num; j++){
                    var temp = [{}]
                    for(var i = 0; i < this.quake_num; i++){
                        var temp4 = "earthquake" + (i+1)
                        temp[0][temp4] = ''    
                    }       
                    temp[0].floor = j+1
                    this.data4.push(temp[0])
                }
                }
            else if(Array.isArray(data_temp[0][0]))
            {
                console.log("数组，说明是点编辑的")
                this.temp4={}
                for(var i = 0; i < this.quake_num; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp4[i] = temp
                }
                this.option_num = "4"
                this.data4 = []
                for(var j = 0; j < this.floors_num; j++){
                    var temp = [{}]
                    for(var i = 0; i < this.quake_num; i++){
                        var temp4 = "earthquake" + (i+1)
                        temp[0][temp4] = data_temp[2][j][i]       
                    }
                    temp[0].floor = j+1
                    this.data4.push(temp[0])
                }
            }
            else
                {
                    console.log("有值，说明点了上一步")
                    let data_back_next=JSON.parse(localStorage.getItem('structure_response'))
                    this.temp4={}
                    for(var i = 0; i < this.quake_num; i++){
                    var temp = "earthquake" + (i+1)
                    this.temp4[i] = temp
                    }
                    this.option_num = "4"
                    this.data4 = []
                    for(var j = 0; j < this.floors_num; j++){
                        var temp = [{}]
                        for (var item in data_back_next[3][j])
                        {
                            temp[0][item] = data_back_next[3][j][item]        
                        }
                        temp[0].floor = j+1
                        this.data4.push(temp[0])
                    }
                    
                }
        },
        rowClass(){
            return 'background:#eee'
        }
   
    },
    data(){
        return {
            quake_num:'',
            floors_num:'',
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
                floor_no:localStorage.getItem('floors'),
                earthquake_no:localStorage.getItem('number')
            },{
                direction:'X方向',
                EDP_type:'Acceleration/楼层加速度',
                floor_no:localStorage.getItem('floors'),
                earthquake_no:localStorage.getItem('number')
            },
            {
                direction:'Y方向',
                EDP_type:'Story Drift Ratio/层间位移角',
                floor_no:localStorage.getItem('floors'),
                earthquake_no:localStorage.getItem('number')
            },
            {
                direction:'Y方向',
                EDP_type:'Acceleration/楼层加速度',
                floor_no:localStorage.getItem('floors'),
                earthquake_no:localStorage.getItem('number')
            }
            ],
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
        padding:8px 0;
        color: #333;
        font-size:14px
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
    .tb-edit .el-input {
        display: none
    }
    .tb-edit .current-row .el-input {
        display: block
    }
    .tb-edit .current-row .el-input+span {
        display: none
    }
</style>

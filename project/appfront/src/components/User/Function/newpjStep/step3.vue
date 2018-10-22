<template>
    <div>
        <el-row>
            <el-button size="small" class='btn' @click="next">下一步</el-button>
            <el-button size="small" class='btn' @click="back">上一步</el-button>
        </el-row>
        <el-table :data="tableData" style="width:90%" max-height="350" highlight-current-row class="tb-edit">
        <el-table-column prop="order1" label="易损性编号" width="150">
            <template slot-scope="scope">
                <el-input size="small" v-model="scope.row.id" placeholder="点击可选" @focus="chooseId(scope.$index, tableData)"></el-input><span>{{scope.row.id}}</span>
            </template>
        </el-table-column>
        <el-table-column prop="order1" width="80" label="单位" >
            <template slot-scope="scope">
                <el-input size="small" disabled v-model="scope.row.unit"></el-input><span>{{scope.row.unit}}</span>
            </template>
        </el-table-column>
        <el-table-column prop="order2" width="80"  label="起始楼层">
            <template slot-scope="scope">
                <el-input size="small" v-model="scope.row.start_floor" placeholder="请输入内容"></el-input><span>{{scope.row.start_floor}}</span>
            </template>
        </el-table-column>
        <el-table-column prop="order2" width="80"  label="终止楼层">
            <template slot-scope="scope">
                <el-input size="small" v-model="scope.row.stop_floor" placeholder="请输入内容"></el-input><span>{{scope.row.stop_floor}}</span>
            </template>
        </el-table-column>
        <el-table-column prop="order2" width="130" label="x方向易损性数量">
            <template slot-scope="scope">
                <el-input size="small" v-model="scope.row.X" placeholder="请输入内容"></el-input><span>{{scope.row.X}}</span>
            </template>
        </el-table-column>
        <el-table-column prop="order2" width="130" label="y方向易损性数量">
            <template slot-scope="scope">
                <el-input size="small" v-model="scope.row.Y" placeholder="请输入内容"></el-input><span>{{scope.row.Y}}</span>
            </template>
        </el-table-column>
            <el-table-column prop="order2" width="140" label="无方向易损性数量">
            <template slot-scope="scope">
                <el-input size="small"  v-model="scope.row.Non" placeholder="请输入内容"></el-input><span>{{scope.row.Non}}</span>
            </template>
        </el-table-column>
        <el-table-column
            fixed="right"
            label="操作"
            width="120">
            <template slot-scope="scope">
                <el-button
                @click.native.prevent="deleteRow(scope.$index, tableData)"
                type="text"
                size="small">
                移除
                </el-button>
            </template>
            </el-table-column>
        </el-table> 
        <el-button @click="newComponent">新增结构构件</el-button>
        <!-- <el-button @click="saveElements">保存所有结构构件</el-button> -->
        <el-button @click="view_db">查看易损性数据库详情</el-button>
        <el-dialog
        title="选择易损性数据库"
        :visible.sync="dialogVisible"
        width="50%"
        top=10px
        :center=true
        :before-close="handleClose">
        <div class="block">
            <el-select @change="chooseId(temp1,temp2)" style="position:relative; top:-10px" v-model="value4" filterable placeholder="请选择">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
            <el-button style="position:relative; float:right; top:-10px" type="primary" @click="new_db">创建易损性数据库</el-button>
        </div>
        <el-scrollbar class = "el-scrollbar">
            <el-tree class="el-tree" :default-expand-all="true" :data="data"  @node-click="handleNodeClick" ></el-tree>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
            </span>
        </el-scrollbar>
        </el-dialog>
    </div>
    
</template>


<script>
    export default {
      data() {
          return{
            temp1:'',
            temp2:'',
            choose_value:'',
            index: null,
            dialogVisible:false,
            tableData: [{
                id: '',
                unit: '',
                start_floor: '',
                stop_floor:'',
                X:null,
                Y:null,
                Non:null
            }],
            options: [{
                    value: 'DB_common',
                    label: 'DB_Common'
                }, {
                    value: 'DB_school',
                    label: 'DB_School'
                }, {
                    value: 'DB_hospital',
                    label: 'DB_Hospital'
                }, {
                    value: 'DB_user',
                    label: 'DB_User'
                }, {
                    value: 'DB_office',
                    label: 'DB_Office'
                }, {
                    value: 'DB_fEMA',
                    label: 'DB_FEMA'
                }],
                value4:'DB_common',
            data:[],
            data1:[]
            
        };
    },
    beforeRouteLeave(to, from, next){
        let structure_element = JSON.stringify(this.tableData)
        localStorage.setItem('structure_element', structure_element)
        console.log(structure_element)
        next()
    },
    created(){
      //从localStorage中读取条件并赋值给查询表单
        let tableData = localStorage.getItem('structure_element')
        console.log('step3.vue')
        console.log(tableData)
        if(tableData!=null){
            tableData=JSON.parse(tableData)
            if (tableData.length!=0) {
            console.log("飞空")
            console.log(tableData)
            this.tableData = tableData
            }
        }
    },
    methods: {
        view_db(){
            localStorage.setItem('new_db_ret','true')
            this.$router.push({name:'viewdb'});
        },
        chooseId(index, rows){
            this.temp1 = index
            this.temp2 = rows
            this.dialogVisible = false;
            this.index = index;
            let _this=this
            this.$ajax({
                method:'get',
                url:'step3-get-all-parts',
                params:{
                    value: this.value4
                },
                headers:{"Content-Type": "application/json"}
            })
            .then(function(response){
                console.log(response)
                //console.log('111')
                var res=response.data
                console.log(res['first'])
                console.log(res['second'])
                if(res.error_num==0){
                    console.log(res['list'])
                    var returnData = []
                    for(var i = 0; i < res['first'].length; i++){
                        var temp = {
                            label: "",
                            children: []
                        }
                        temp.label=res['first'][i]
                        for(var j = 0; j < res['second'].length; j++){
                            if(res['first'][i] === res['second'][j][0]){
                                var item = {
                                    label: res['second'][j][1],
                                    children: []
                                }
                                for(var k = 0; k < res['list'].length; k++){
                                    if(res['list'][k].fields.second === res['second'][j][1]){
                                        var item1 = {
                                            label: res['list'][k].fields.part_id + " " + res['list'][k].fields.part_name + " " + res['list'][k].fields.description + " " + res['list'][k].fields.basic_unit,
                                            children:[]
                                        }
                                        item.children.push(item1)
                                    }
                                }
                                temp.children.push(item)
                            }
                        }
                        returnData.push(temp)
                    }
                    _this.data=returnData
                }
                else {
                    _this.$message.error(res['msg'])
                    console.log(res['msg'])
                }
            })
            .catch(function(err){
                    console.log(err);
                    console.log('!!')
                    console.log(_this.data)
                    });
            this.dialogVisible = true
        },
        // saveElements(){
        //     let _this=this;
        //     var floors=localStorage.getItem('floors')
        //     var project=localStorage.getItem('project')
        //     console.log(this.tableData)
        //     this.$ajax({
        //         method:'get',
        //         url:'step3-save-elements',
        //         params:{
        //             is_structure:'True',
        //             project:project,
        //             floors:floors,
        //             tableData:this.tableData,
        //         },
        //     })
        //     .then(function(response){
        //         console.log(response)
        //         var res=response.data
        //         if(res.error_num==0){
        //             console.log(res['msg'])
        //             _this.$message.success(res['msg'])
        //             //console.log(_this.tableData[0].id) id里存的确实是字符串形式啊
        //         }
        //         else {
        //             _this.$message.error(res['msg'])
        //             console.log(res['msg'])
        //         }
        //     })
        //     .catch(function(err){
        //             console.log(err);
        //             });
        // },
        deleteRow(index, rows) {
            rows.splice(index, 1);
        },
        handleClose(done) {
            this.$confirm('确认关闭？')
            .then(_ => {
                done();
            })
            .catch(_ => {});
        },
        newComponent(){
            this.tableData.push({
                id:'',
                unit:'',
                start_floor: '',
                stop_floor:'',
                X:null,
                Y:null,
                Non:null
            })
        },
        handleNodeClick(data,node){
              //console.log(data);
              console.log(this.choose_value)
              if(node.level==3){
                  console.log(data)
                  var temp = data.label.split(' ')
                  this.tableData[this.index].id = temp[0];
                  this.tableData[this.index].unit = temp[temp.length-1];
                  this.dialogVisible = false;   
              }
        },
        next(){
            let _this=this;
            var floors=localStorage.getItem('floors')
            var project=localStorage.getItem('project')
            console.log(this.tableData)
            console.log(this.tableData.length)
            var isFull=true
            for(var i=0;i<this.tableData.length;i++)
            {   
                console.log(this.tableData[i].id)
                console.log(this.tableData[i].start_floor)
                console.log(this.tableData[i].stop_floor)
                console.log(this.tableData[i].X)
                console.log(this.tableData[i].Y)
                console.log(this.tableData[i].Non)
                
                if (this.tableData[i].id==='' || this.tableData[i].start_floor==='' || this.tableData[i].stop_floor==='' || 
                    this.tableData[i].X===null || this.tableData[i].Y===null || this.tableData[i].Non===null){
                    _this.$message.error("请完整填写构建信息好吗")
                    isFull=false
                }
            }
                if(isFull){
                    this.$ajax({
                    method:'get',
                    url:'step3-save-elements',
                    params:{
                        is_structure:'True',
                        project:project,
                        floors:floors,
                        tableData:this.tableData,
                    },
                    })
                    .then(function(response){
                        console.log(response)
                        var res=response.data
                        if(res.error_num==0){
                            console.log(res['msg'])
                            _this.$message.success(res['msg'])
                            //console.log(_this.tableData[0].id) id里存的确实是字符串形式啊
                            setTimeout(()=>{
                                        _this.$emit('next','');
                                    },500)
                        }
                        else {
                            _this.$message.error(res['msg'])
                            console.log(res['msg'])
                        }
                    })
                    .catch(function(err){
                            console.log(err);
                            });                   
                }
            },

            //this.$emit('next','');
        
        back(){
            this.$emit('back','');
        },
        changed(value){//请求数据
            console.log(value)
        },

        new_db(){
            localStorage.setItem('new_db_ret','true')
            sessionStorage.setItem('check','DB_User')
            this.$router.push({name:'newdb'});
        }
    }
           
}
    
  </script>


<style scoped>
    .el-table{
        margin:20px 0;
    }
    .btn{
            margin-top:12px;
        }

    .el-scrollbar{
        height: 450px;
    }

    .el-scrollbar__wrap {
        overflow-x: hidden;
    }

    .el-tree{
        display:inline-block;
    }
    body {
        font-family: Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB, Microsoft YaHei, SimSun, sans-serif;
        overflow: auto;
        font-weight: 400;
        -webkit-font-smoothing: antialiased;
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

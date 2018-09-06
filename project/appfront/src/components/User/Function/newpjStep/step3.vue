<template>
    <div>
        <el-row>
            <el-button size="small" class='btn' @click="next">下一步</el-button>
            <el-button size="small" class='btn' @click="back">上一步</el-button>
        </el-row>
        <el-table :data="tableData" border style="width:100%" max-height="350">
        <el-table-column prop="order1" label="易损性编号" width="180">
            <template slot-scope="scope">
                <el-input v-model="scope.row.id" placeholder="点击可选" @focus="chooseId(scope.$index, tableData)"></el-input>
            </template>
        </el-table-column>
        <el-table-column prop="order2" label="起始楼层">
            <template slot-scope="scope">
                <el-input v-model="scope.row.start_floor" placeholder="请输入内容"></el-input>
            </template>
        </el-table-column>
        <el-table-column prop="order2" label="终止楼层">
            <template slot-scope="scope">
                <el-input v-model="scope.row.stop_floor" placeholder="请输入内容"></el-input>
            </template>
        </el-table-column>
        <el-table-column prop="order2" label="x方向易损性数量">
            <template slot-scope="scope">
                <el-input v-model="scope.row.X" placeholder="请输入内容"></el-input>
            </template>
        </el-table-column>
        <el-table-column prop="order2" label="y方向易损性数量">
            <template slot-scope="scope">
                <el-input v-model="scope.row.Y" placeholder="请输入内容"></el-input>
            </template>
        </el-table-column>
            <el-table-column prop="order2" label="无方向易损性数量">
            <template slot-scope="scope">
                <el-input v-model="scope.row.Non" placeholder="请输入内容"></el-input>
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
        <el-button @click="saveElements">保存所有结构构件</el-button>
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
        console.log('leave3')
        console.log(structure_element)
        next()
    },
    created(){
      //从localStorage中读取条件并赋值给查询表单
        let tableData = localStorage.getItem('structure_element')
        console.log(tableData)
        if (tableData != null) {
            this.tableData = JSON.parse(tableData)
        }
    },
    methods: {
        view_db(){
            window.open('http://localhost:8080/#/refer/viewdb')
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
                console.log(77777777)
                console.log(res['first'])
                console.log(88888888)
                console.log(res['second'])
                if(res.error_num==0){
                    /*console.log(res['list'])
                    console.log(res['detail'])
                    console.log(res['first'])
                    console.log(res['second'])
                    _this.data =  _this.data1
                    
                    var max=res['list'].length

                    for(var i = 0; i < max; i++){
                        //console.log(res['list'][i+1].fields.part_id+' !'+res['list'][i+1].fields.description)
                        const newchild={label: res['list'][i].fields.part_id+' '+res['list'][i].fields.description, children:[]}
                        _this.data[i]=newchild
                    }
                    console.log('000')
                    var temp=new Array()
                    for(var i = 0; i < max; i++){
                        temp[i] = 0
                    }
                    
                    console.log('111')
                    for(var i = 0; i < res['detail'].length; i++){
                        const newchild={label: res['detail'][i].fields.DB_part+res['detail'][i].fields.damage_id+res['detail'][i].fields.damage_description, children:[]}
                        _this.data[res['detail'][i].fields.DB_part-1].children[temp[res['detail'][i].fields.DB_part-1]] = newchild
                        temp[res['detail'][i].fields.DB_part-1] += 1
                    }
                    console.log('222')
                    _this.$index=res['list'][0].fields.part_id*/
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
                                            label: res['list'][k].fields.part_id + " " + res['list'][k].fields.part_name + " " + res['list'][k].fields.description,
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
                    console.log(returnData)
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
        saveElements(){
            let _this=this;
            var floors=localStorage.getItem('floors')
            var project=localStorage.getItem('project')
            console.log(this.tableData)
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
                  this.dialogVisible = false;   
              }
          },
          next(){
            this.$emit('next','');
        },
        back(){
            this.$emit('back','');
        },
        changed(value){//请求数据
            console.log(value)
        }
    },
           
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


</style>

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
            <el-select style="position:relative; top:-10px" v-model="value4" filterable placeholder="请选择">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
        </div>
        <el-scrollbar style='height:450px'>
            <el-tree :default-expand-all="true" :data="data"  @node-click="handleNodeClick" ></el-tree>
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
                    value: 'DB_Common',
                    label: 'DB_Common'
                }, {
                    value: 'DB_School',
                    label: 'DB_School'
                }, {
                    value: 'DB_Hospital',
                    label: 'DB_Hospital'
                }, {
                    value: 'DB_User',
                    label: 'DB_User'
                }, {
                    value: 'DB_Office',
                    label: 'DB_Office'
                }, {
                    value: 'DB_FEMA',
                    label: 'DB_FEMA'
                }],
                value4:'DB_Common',
            data:[],
            data1:[]
            
        };
    },
    beforeRouteLeave(to, from, next){
    //  if (to.name == 'step2') {
        //let id = JSON.stringify(this.id)
        //sessionStorage.setItem('id', id)
        let structure_element = JSON.stringify(this.tableData)
        sessionStorage.setItem('structure_element', structure_element)
      next()
    },
    created(){
      //从localStorage中读取条件并赋值给查询表单
        let tableData = sessionStorage.getItem('structure_element')
        if (tableData != null) {
            this.tableData = JSON.parse(tableData)
        }
    },
    methods: {
        view_db(){
            window.open('http://localhost:8080/#/refer/viewdb')
        },
        chooseId(index, rows){
            this.dialogVisible = true;
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
                if(res.error_num==0){
                    console.log(res['list'])
                    console.log(res['detail'])
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
                    _this.$index=res['list'][0].fields.part_id
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
        },
        saveElements(){
            let _this=this;
            var floors=localStorage.getItem('floors')
            var project=localStorage.getItem('project')
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
              if(node.level==1){
                  console.log(data)
                  this.tableData[this.index].id = data.label.substr(0,10);
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
</style>

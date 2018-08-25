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
        <el-button @click="newComponent">新增非结构构件</el-button>
        <el-button @click="saveElements">保存所有非结构构件</el-button>
        <el-dialog
        title="提示"
        :visible.sync="dialogVisible"
        width="30%"
        :before-close="handleClose">
        <span>这是一段信息</span>
        <el-tree :default-expand-all="true" :data="data"  @node-click="handleNodeClick" ></el-tree>
        <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
        </span>
        </el-dialog>
    </div>
    
</template>


<script>
    export default {
      data() {
          return{
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
            data: [{
                    label: 'General Info',
                    children: [{
                        label: 'Damage State Type',
                        children: [{
                            label: 'Damage State 1',
                            children: [{
                                label: 'A1101 Consequence Functions'
                            }]
                        }]
                    }],
                  }]
        };
    },
    methods: {
        chooseId(index, rows){
            this.dialogVisible = true;
            this.index = index;
            let _this=this
            this.$ajax({
                method:'get',
                url:'step3-get-all-parts',
                headers:{"Content-Type": "application/json"}
            })
            .then(function(response){
                console.log(response)
                var res=response.data
                if(res.error_num==0){
                    console.log(res['list'])
                    _this.data[0].label=res['list'][0].fields.part_id
                    console.log(_this.data[0].label)
                    console.log(_this.data.label=res['list'][0].fields.part_id)
                    _this.$index=res['list'][0].fields.part_id
                    
                }
                else {
                    _this.$message.error('获取非结构构件失败')
                    console.log(res['msg'])
                }
            })
            .catch(function(err){
                    console.log(err);
                    });
        },
        saveElements(){
            let _this=this;
            var project=localStorage.getItem('project')
            this.$ajax({
                method:'get',
                url:'step3-save-elements',
                params:{
                    is_structure:'False',
                    project:project,
                    tableData:this.tableData,
                },
                headers:{"Content-Type": "application/json"}
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
              if(node.level == 1){
                  console.log(data)
                  this.tableData[this.index].id = data.label.substr(0,5);
                  this.dialogVisible = false;   
              }
          },
          next(){
            this.$emit('next','');
        },
        back(){
            this.$emit('back','');
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

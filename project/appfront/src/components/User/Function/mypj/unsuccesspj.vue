<template> 
    <div style="top:-73px; position:relative; height:400px; margin:18px 20px;">
        <el-table
            :data="projects.slice((currentPage-1)*pagesize,currentPage*pagesize)"
            border
            style="width: 100%">
            <el-table-column
                prop="create_time"
                label="日期"
                width="150">
            </el-table-column>
            <el-table-column
                prop="project_name"
                label="项目名称"
                width="120">
            </el-table-column>
            <el-table-column
                prop="id"
                label="项目编号"
                width="120">
            </el-table-column>
            <el-table-column
                prop="client_name"
                label="客户姓名"
                width="270">
            </el-table-column>
            <el-table-column
                prop="project_leader"
                label="项目负责人"
                width="120">
            </el-table-column>
            <el-table-column
                prop="rate"
                label="等级"
                width="120">
            </el-table-column>
            <el-table-column
                prop="project_description"
                label="项目说明"
                width="270">
            </el-table-column>

            <el-table-column
                fixed="right"
                label="操作"
                width="130">
            <template slot-scope="scope">
                <el-button @click="editpj(row)" type="text" size="small">编辑</el-button>
                <el-button @click="deletepj(row)" type="text" size="small">删除</el-button>
            </template>
            </el-table-column>
        </el-table>
        <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="currentPage"
            :page-sizes="[5, 20, 50, 100]"
            :page-size="pagesize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="projects.length"
            style="text-align: center">
        </el-pagination>
    </div>
  
</template>

<script>
    export default {
        
        beforeMount: function() {
            this.showProjects()
        },

        methods:{
            handleSizeChange: function (size) {
                this.pagesize = size;
            },
            handleCurrentChange: function(currentPage){
                this.currentPage = currentPage;
            },
            editpj: function(row){
                localStorage.setItem("pjNum",JSON.stringify(row.pjNum));
                //掉用setp1进行编辑
                //console.log(pjname)
            },
            deletepj: function(row){
                //传值给数据库进行删除
                //console.log(pjname)
            },
            showProjects(){
                let _this = this;
                /*_this.$http.get('http://localhost:8000/api/show_projects')
                    .then((response) => {
                        var res = JSON.parse(response.bodyText)
                        console.log(res)
                        if (res.error_num == 0) {
                            _this.projects = res['list']
                        } 
                        else {
                            _this.$message.error('查询项目失败')
                            console.log(res['msg'])
                        }
                    })
                    .catch(function(error){
                        console.log(error)
                    })*/
                this.$ajax({
                    method:'post',
                    url:'http://localhost:8000/api/show_projects',
                    data: JSON.stringify({
                       'id': "123456", 
                    }),
                    headers:{"Content-Type": "application/json"}
                })
                    .then(function(response){
                        console.log(response)
                        var res = response.data
                        console.log(res)
                        if (res.error_num == 0) {
                            console.log(res['list'][0].fields)
                            //_this.projects[0] = res['list'][0].fields
                            //_this.projects[1] = res['list'][1].fields
                            //vue.set(_this.projects[0],'',res['list'][0].fields);
                            _this.projects = res['list']
                            for(var i = 0; i < res['list'].length; i++){
                                _this.projects[i] = res['list'][i].fields
                            }
                            //_this.projects[0] = res['list'][0].fields
                            //_this.projects[1] = res['list'][1].fields
                            console.log(_this.projects)
                        } 
                        else {
                            _this.$message.error('查询项目失败')
                            console.log(res['msg'])
                        }
                    })
                    .catch(function(err){
                        console.log(err);
                    });
                /*this.$ajax.get('http://localhost:8000/api/show_projects')
                    .then(function(response){
                        console.log(response)
                        var res = JSON.parse(response.bodyText)
                        console.log(res)
                        if (res.error_num == 0) {
                            _this.projects = res['list']
                        } 
                        else {
                            _this.$message.error('查询项目失败')
                            console.log(res['msg'])
                        }
                    })
                    .catch(function(err){
                        console.log(err);
                    });*/
            },
        },

          data () {
              return {
                  projects: [{create_time: '2016-05-03',
                      project_leader: '王小虎',
                      client_name:'王小五',
                      project_name: '上海',
                      user: '普陀区',
                      rate: '上海市',
                      project_description: 200333},],
                  currentPage:1,
                  pagesize:5,
        
            }
        } 
    }
</script>
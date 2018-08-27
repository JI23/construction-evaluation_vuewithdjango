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
                label="定级"
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
<<<<<<< HEAD
            <template slot-scope="{row,$index}">
                <el-button @click="editpj($index,row)" type="text" size="small">编辑</el-button>
                <el-button @click="deletepj($index,row)" type="text" size="small">删除</el-button>
=======
            <template slot-scope="scope">
                <el-button @click="editpj(scope.row)" type="text" size="small">编辑</el-button>
                <el-button @click="deletepj(scope.row)" type="text" size="small">删除</el-button>
>>>>>>> upstream/master
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
<<<<<<< HEAD
            editpj: function(index,row){
                localStorage.setItem("project",JSON.stringify(row.id));
                let project = localStorage.getItem('project');
                //console.log(project_name);
                //掉用setp1进行编辑
                //console.log(pjname)
                var username=localStorage.getItem('phone')
                this.$ajax({
                    method:'get',
                    url:'step0-edit',
                    params:{
                        username:username,
                        project:project
                    }
                }).then(function(response){
                    //判断后弹窗
                    var res = response.data
                    console.log(res['base_info'])
                    console.log(res['base_info'][0].fields.project_name)
                }).catch(function(err){
                    console.log(err)
                })
                this.$router.push({name:'step1'});
            },
            deletepj: function(index,row){//未连接

                var username=localStorage.getItem('phone')
=======
            editpj: function(row){
                //console.log(row.value)
                localStorage.setItem("project_name",JSON.stringify(row.project_name));
                //this.$router.push({name:'step1'});
                console.log('111')
                var username=localStorage.getItem('phone')
                var project=row.id
                console.log(username)
                this.$ajax({
                    method:'get',
                    url:'step0-edit',
                    params:{
                        project:project,
                        username:username,
                    },
                }).then(function(response){
                    //判断后弹窗
                    var res=response.data
                    if (res.error_num==0){
                        
                        console.log(res['msg'])
                    }
                    else{
                        console.log(res['msg'])
                    }
                }).catch(function(err){
                    console.log(err)
                })
                //console.log(localStorage.getItem('pjNum'))
                //掉用setp1进行编辑
                //console.log("!!!")
            },
            deletepj: function(row){//未连接
                console.log('111')
                var username=localStorage.getItem('phone')
                var project=row.id
>>>>>>> upstream/master
                this.$ajax({
                    method:'get',
                    url:'step0-delete',
                    params:{
<<<<<<< HEAD
                        project:row.id,
                        username:username
                    }
                }).then(function(response){
                    //判断后弹窗
                    var res = response.data
                    console.log(res['msg'])
=======
                        project:project,
                        username:username,
                    }
                }).then(function(response){
                    //判断后弹窗
                    //this.reload()
                    var res=response.data
                    if (res.error_num==0){
                        
                        console.log(res['msg'])
                    }
                    else{
                        console.log(res['msg'])
                    }
>>>>>>> upstream/master
                }).catch(function(err){
                    console.log(err)
                })
            },
            reload(){
                this.isRouteAlive = false
                this.$nextTick(function(){
                    this.isRouteAlive = true
                })
            },
            
            showProjects(){
                let _this = this;
                var username=localStorage.getItem('phone')
                this.$ajax({
                    method:'get',
                    url:'show_projects',
                    params: {
                       'is_finished': 'False', 
                       username:username,
                    },
                })
                    .then(function(response){
                        console.log(response)
                        var res = response.data
                        console.log(res['list'][0].pk)
                        console.log('234567')
                        if (res.error_num == 0) {
                            //console.log(res['list'][0].fields)
                            //_this.projects[0] = res['list'][0].fields
                            //_this.projects[1] = res['list'][1].fields
                            //vue.set(_this.projects[0],'',res['list'][0].fields);
                            _this.projects = res['list']
                            for(var i = 0; i < res['list'].length; i++){
                                var id=res['list'][i].pk
                                console.log(id)
                                _this.projects[i] = res['list'][i].fields
<<<<<<< HEAD
                                _this.projects[i].id=id
=======
                                
                                _this.projects[i].id = id
                                console.log(_this.projects[i])
>>>>>>> upstream/master
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
                projects: [{
                    create_time: '2016-05-03',
                    project_leader: '王小虎',
                    client_name:'王小五',
                    project_name: '上海',
<<<<<<< HEAD
                    id:'12',
                    user: '普陀区',
=======
                    id: 12,
>>>>>>> upstream/master
                    rate: '上海市',
                    project_description: 200333},],
                currentPage:1,
                pagesize:5,
                isRouteAlive: true
            }
        } 
    }
</script>
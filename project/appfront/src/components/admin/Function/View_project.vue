<template> 
    <div style=" position:relative; height:400px; margin:18px 20px;">
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
                label="项目名"
                width="150">
            </el-table-column>
            <el-table-column
                prop="rate"
                label="等级"
                width="150">
            </el-table-column>
            <el-table-column
                prop="client_name"
                label="创建者姓名"
                width="150">
            </el-table-column>
            <el-table-column
                prop="user"
                label="创建者所属公司"
                width="150">
            </el-table-column>
            <el-table-column
                prop="project_leader"
                label="项目负责人"
                width="150">
            </el-table-column>
            <el-table-column
                fixed="right"
                label="操作"
                width="200">
                <template slot-scope="scope">
                    <el-button @click="overlook(scope.row)" type="text" size="small">查看详情</el-button><!--未写 -->
                    <el-button @click="delete(scope.row)" type="text" size="small">删除</el-button>
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
        methods:{
            handleSizeChange: function (size) {
                this.pagesize = size;
            },
            handleCurrentChange: function(currentPage){
                this.currentPage = currentPage;
            },
            overlook: function(row){//跳转未写
                //console.log(row)
                localStorage.setItem("pjNum",JSON.stringify(row.pjNum));
                //this.$router.push({name:'view'});
            },
            delete: function(){
                //给后台发送删除项目的对应ID
            },
            showProjects(){
                let _this = this;
                this.$ajax({
                    method:'get',
                    url:'show_projects_filter',
                    params: {
                        'condition' : 'finish'
                    },
                    headers:{"Content-Type": "application/json"}
                }).then(function(response){
                    //console.log(response)
                    var res = response.data
                    console.log(res)
                    if (res.error_num == 0) {
                        _this.projects = res['projects']
                        for(var i = 0; i < res['projects'].length; i++){
                             _this.projects[i] = res['projects'][i].fields
                        }
                    } 
                    else {
                        _this.$message.error('查询项目失败')
                        //console.log(res['msg'])
                    }
                }).catch(function(err){
                    console.log(err);
                });
            },


            show_userProjects(){
                let _this = this;
                this.$ajax({
                    method:'get',
                    url:'show_user_projects',
                    params: {
                        'username' : localStorage.getItem('filtername')
                    },
                    headers:{"Content-Type": "application/json"}
                }).then(function(response){
                    //console.log(response)
                    var res = response.data
                    console.log(res)
                    if (res.error_num == 0) {
                        _this.projects = res['projects']
                        for(var i = 0; i < res['projects'].length; i++){
                             _this.projects[i] = res['projects'][i].fields
                        }
                    } 
                    else {
                        _this.$message.error('查询项目失败')
                        //console.log(res['msg'])
                    }
                }).catch(function(err){
                    console.log(err);
                });
            },
        },

        beforeMount: function() {
            var temp = localStorage.getItem('filter');
            if(temp == 'true'){
                this.show_userProjects()
                localStorage.setItem('filter','flase')
            }
            else{
                this.showProjects()
            }
        },
        data () {
            return {
                projects: [{
                    create_time: '2016-05-03',
                    project_name:'王小五',
                    rate: '普陀区',
                    client_name: 200333,
                    user: 'aaa',
                    project_leader: 'asa',
                    },],
                currentPage:1,
                pagesize:5,
            }
        }, 
    }
</script>
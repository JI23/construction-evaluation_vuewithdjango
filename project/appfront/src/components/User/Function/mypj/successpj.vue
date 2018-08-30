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
                width="120">
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
                <template slot-scope="scope">
                    <el-button @click="overlook(scope.row)" type="text" size="small">查看</el-button><!--未写 -->
                    <el-button @click="jumpstep1(scope.row)" type="text" size="small">拷贝</el-button>
                    <el-button @click="deletepj(scope.row)" type="text" size="small">删除</el-button>
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
            jumpstep1: function(row){
                localStorage.setItem("pjNum",JSON.stringify(row.pjNum));
                this.$router.push({name:'step1'});
            },
            overlook: function(row){
                //console.log(row)
                localStorage.setItem("pjNum",JSON.stringify(row.pjNum));
                this.$router.push({name:'view'});
            },
            deletepj: function(){
                //给后台发送删除项目的对应ID
            },
            showProjects(){
                let _this = this;
                var name=localStorage.getItem('phone')
                console.log(name)
                this.$ajax({
                    method:'get',
                    url:'show_projects',
                    params: {
                       'is_finished': 'True', 
                       username:name
                    },
                    headers:{"Content-Type": "application/json"}
                }).then(function(response){
                    //console.log(response)
                    var res = response.data
                    //console.log(res)
                    if (res.error_num == 0) {
                        _this.projects = res['list']
                        for(var i = 0; i < res['list'].length; i++){
                             _this.projects[i] = res['list'][i].fields
                        }
                        //console.log(_this.projects)
                    } 
                    else {
                        _this.$message.error('查询项目失败')
                        //console.log(res['msg'])
                    }
                }).catch(function(err){
                    //console.log(err);
                });
            },
        },
//改成从后台重新获取数据，前端object的处理写不出来


        beforeMount: function() {
            this.showProjects()
        },
        data () {
            return {
                input: '',
                projects: [],
                currentPage:1,
                pagesize:5,
                search:''
            }
        }, 
    }
</script>
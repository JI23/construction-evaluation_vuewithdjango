<template> 
    <div style="top:-75px; position:relative; height:400px; margin:18px 20px;">
        <el-table
            :data="projects.slice((currentPage-1)*pagesize,currentPage*pagesize)"
            border
            style="width: 100%">
            <el-table-column
                prop="create_time"
                label="审核日期"
                width="200">
            </el-table-column>
            <el-table-column
                prop="name"
                label="真实姓名"
                width="200">
            </el-table-column>
            <el-table-column
                prop="com_Name"
                label="公司名"
                width="200">
            </el-table-column>
            <el-table-column
                prop="id"
                label="公司证件号"
                width="200">
            </el-table-column>
                <el-table-column
                    fixed="right"
                    label="操作"
                    width="200">
                <template slot-scope="scope">
                    <el-button @click="overlook(scope.row)" type="text" size="small">查看详情</el-button><!--未写 -->
                    <el-button @click="open(scope.row)" type="text" size="small">解禁用户</el-button>
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
            open: function(row){

            },
            overlook: function(row){//跳转未写
                //console.log(row)
                localStorage.setItem("pjNum",JSON.stringify(row.pjNum));
                this.$router.push({name:'detail_user'});
            },
            showProjects(){/*
                let _this = this;
                this.$ajax({
                    method:'get',
                    url:'',
                    params: {
                       
                    },
                }).then(function(response){
                    console.log(response)
                    var res = response.data
                    console.log(res)
                    if (res.error_num == 0) {
                        _this.projects = res['list']
                        for(var i = 0; i < res['list'].length; i++){
                            _this.projects[i] = res['list'][i].fields
                        }
                    } 
                    else {
                        _this.$message.error('查询项目失败')
                        console.log(res['msg'])
                    }
                }).catch(function(err){
                    console.log(err);
                });*/
            },
        },

        beforeMount: function() {
            this.showProjects()
        },
        data () {
            return {
                projects: [{create_time: '2016-05-03',
                    name:'王小五',
                    id: '普陀区',
                    com_Name: 200333},],
                currentPage:1,
                pagesize:5,
            }
        }, 
    }
</script>
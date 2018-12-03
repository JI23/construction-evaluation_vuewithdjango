<template> 
    <div style=" position:relative; height:400px; margin:18px 20px;">
        <el-table
            :data="users.slice((currentPage-1)*pagesize,currentPage*pagesize)"
            border
            style="width: 100%">
            <el-table-column
                prop="date_joined"
                label="申请日期"
                width="140">
            </el-table-column>
            <el-table-column
                prop="username"
                label="用户名"
                width="140">
            </el-table-column>
            <el-table-column
                prop="truename"
                label="真实姓名"
                width="140">
            </el-table-column>
            <el-table-column
                prop="com_name"
                label="公司名"
                width="140">
            </el-table-column>
            <el-table-column
                prop="company_id"
                label="公司税号"
                width="200">
            </el-table-column>
                <el-table-column
                    fixed="right"
                    label="操作"
                    width="200">
                <template slot-scope="scope">
                    <el-button @click="overlook(scope.row)" type="text" size="small">查看详情</el-button><!--未写 -->
                    <el-button @click="allow_user(scope.row)" type="text" size="small">同意</el-button>
                    <el-button @click="refuse(scope.row)" type="text" size="small">拒绝</el-button>
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
            :total="users.length"
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
            refuse: function(row){
                let _this=this;
                this.$ajax({
                    method:'get',
                    url:'refuse_user',
                    params:{
                        username:row.username
                    },
                    headers:{"Content-Type": "application/json"}
                }).then(function(response){
                        console.log(response)
                        var res = response.data
                        console.log(res)
                        if (res['error_num'] == 0) {
                            _this.$message.success(res['msg'])
                            _this.show_users()
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
            overlook: function(row){//跳转未写
                //console.log(row)
                localStorage.setItem("current_user_id",JSON.stringify(row.username));
                this.$router.push({name:'detail_user'});
            },
            allow_user: function(row){
                let _this=this;
                this.$ajax({
                    method:'get',
                    url:'allow_user',
                    params:{
                        username:row.username
                    },
                    headers:{"Content-Type": "application/json"}
                }).then(function(response){
                        console.log(response)
                        var res = response.data
                        console.log(res)
                        if (res['error_num'] == 0) {
                            _this.$message.success(res['msg'])
                            _this.show_users()
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
            show_users: function(){
                let _this=this;
                this.$ajax({
                    method:'get',
                    url:'filter_user',
                    params:{
                        flag:'2'
                    },
                    headers:{"Content-Type": "application/json"}
            })
            .then(function(response){
                        console.log(response)
                        var res = response.data
                        console.log(res)
                        if (res['error_num'] == 0) {
                            console.log("用户信息")
                            console.log(res['users'])
                            let users_info=new Array
                            let j=0
                            for(var i = 0; i < res['users'].length; i++){
                                users_info[j]=res['users'][i]
                                users_info[j].company_id=res['users'][i].company__certificate
                                users_info[j].com_name=res['users'][i].company__com_name
                                delete users_info[j].company__certificate
                                delete users_info[j].company__com_name
                                _this.users[i]=users_info[j]
                                j++;
                                }
                            _this.users=users_info
                            console.log(_this.users)
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

        beforeMount: function() {
            this.show_users()
        },
        data () {
            return {
                users: [{date_joined: '2016-05-03',
                    username:'username',
                    truename:'真实姓名',
                    company_id: '18位税号',
                    com_name: '公司名'},],
                currentPage:1,
                pagesize:5,
            }
        }, 
    }
</script>
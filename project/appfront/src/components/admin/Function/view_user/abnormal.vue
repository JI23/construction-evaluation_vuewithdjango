<template> 
    <div style="top:-75px; position:relative; height:400px; margin:18px 20px;">
        <el-table
            :data="abnormal_users.slice((currentPage-1)*pagesize,currentPage*pagesize)"
            border
            style="width: 100%">
            <el-table-column
                prop="date_joined"
                label="审核日期"
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
            :total="abnormal_users.length"
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
                localStorage.setItem("current_user_id",JSON.stringify(row.username));
                this.$router.push({name:'view_detail'});
            },
<<<<<<< HEAD
            show_users: function(){
                let _this=this;
=======
            showUser(){
                let _this = this;
>>>>>>> upstream/master
                this.$ajax({
                    method:'get',
                    url:'filter_user',
                    params:{
                        flag:'0'
                    },
<<<<<<< HEAD
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
                                //delete users_info[j].username
                                _this.abnormal_users[i]=users_info[j]
                                j++;
                                }
                            _this.abnormal_users=users_info
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
=======
                }).then(function(response){
                    console.log(response)
                    var res = response.data
                    console.log(res)
                }).catch(function(err){
                    console.log(err);
                });
            },
        },

        beforeMount: function() {
            this.showUser()
>>>>>>> upstream/master
        },
        data () {
            return {
                abnormal_users: [{date_joined: '2016-05-03',
                username:'username',
                    truename:'王小五',
                    company_id: '普陀区',
                    com_name: 200333},],
                currentPage:1,
                pagesize:5,
            }
        }, 
    }
</script>
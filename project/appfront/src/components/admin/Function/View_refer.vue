<template> 
    <div style=" position:relative; height:400px; margin:18px 20px;">
        <el-table
            :data="user_db.slice((currentPage-1)*pagesize,currentPage*pagesize)"
            border
            style="width: 100%">
            <el-table-column
                prop="date_joined"
                label="创建时间"
                width="140">
            </el-table-column>
            <el-table-column
                prop="username"
                label="创建者"
                width="140">
            </el-table-column>
            <el-table-column
                prop="truename"
                label="名称"
                width="140">
            </el-table-column>
            <el-table-column
                prop="com_name"
                label="材质"
                width="140">
            </el-table-column>
            <el-table-column
                prop="company_id"
                label="厚度"
                width="200">
            </el-table-column>
            <el-table-column
                fixed="right"
                label="操作"
                width="200">
            <template slot-scope="scope">
                <el-button @click="overlook(scope.row)" type="text" size="small">转换类型</el-button><!--未写 -->
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
            :total="user_db.length"
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

            show_db: function(){
                let _this=this;
                this.$ajax({
                    method:'get',
                    url:'step3-get-all-parts',
                    params:{
                        value: "DB_user",
                        username: localStorage.getItem('phone')
                    },
                    headers:{"Content-Type": "application/json"}
                }).then(function(response){
                    var res = response['data']
                    console.log(res)
                }).catch(function(err){
                    console.log(err);
            });
            }
        },

        beforeMount: function() {
            this.show_db()
        },
        data () {
            return {
                user_db: [{date_joined: '2016-05-03',
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
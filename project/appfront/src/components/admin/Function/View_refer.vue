<template> 
    <div style=" position:relative; height:400px; margin:18px 20px;">
        <el-table
            :data="user_db.slice((currentPage-1)*pagesize,currentPage*pagesize)"
            border
            style="width: 100%">
            <el-table-column
                prop="create_date"
                label="创建时间"
                width="140">
            </el-table-column>
            <el-table-column
                prop="user"
                label="创建者"
                width="140">
            </el-table-column>
            <el-table-column
                prop="part_id"
                label="名称"
                width="140">
            </el-table-column>
            <el-table-column
                prop="part_name"
                label="材质"
                width="140">
            </el-table-column>
            <el-table-column
                prop="description"
                label="厚度"
                width="200">
            </el-table-column>
            <el-table-column
                fixed="right"
                label="修改类型"
                width="200">
            <template slot-scope="scope">
                <el-select @change="change_db(scope.row)" v-model="value" placeholder="请选择">
                    <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
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

            change_db(row){
                let _this=this;

                this.$ajax({
                    method:'get',
                    url:'admin_db_part',
                    params:{
                        value: this.value,
                        part_id:row.part_id,
                        flag:'1',
                    },
                    headers:{"Content-Type": "application/json"}
                }).then(function(response){
                    _this.$message.error('转换类型成功')
                }).catch(function(err){
                    console.log(err);
                });

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
                    if (res.error_num == 0) {
                        _this.user_db = res['list']
                        for(var i = 0; i < res['list'].length; i++){
                             _this.user_db[i] = res['list'][i].fields
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
                    if (res.error_num == 0) {
                        _this.user_db = res['list']
                        for(var i = 0; i < res['list'].length; i++){
                             _this.user_db[i] = res['list'][i].fields
                        }
                    } 
                    else {
                        _this.$message.error('查询项目失败')
                        //console.log(res['msg'])
                    }
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
                options: [{
                    value: 'DB_common',
                    label: 'DB_Common'
                }, {
                    value: 'DB_school',
                    label: 'DB_School'
                }, {
                    value: 'DB_hospital',
                    label: 'DB_Hospital'
                }, {
                    value: 'DB_user',
                    label: 'DB_User'
                }, {
                    value: 'DB_office',
                    label: 'DB_Office'
                }, {
                    value: 'DB_fEMA',
                    label: 'DB_FEMA'
                }],
                value: 'DB_user'
            }
        }, 
    }
</script>
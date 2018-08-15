<template> 
    <div style="top:-73px; position:relative; height:400px; margin:18px 20px;">
        <el-table
            :data="newData.slice((currentPage-1)*pagesize,currentPage*pagesize)"
                border
                style="width: 100%">
                <el-table-column
                    prop="date"
                    label="日期"
                    width="150">
                </el-table-column>
                <el-table-column
                    prop="name"
                    label="项目名称"
                    width="120">
                </el-table-column>
                <el-table-column
                    prop="pjNum"
                    label="项目编号"
                    width="120">
                </el-table-column>
                <el-table-column
                    prop="pjHead"
                    label="项目负责人"
                    width="120">
                </el-table-column>
                <el-table-column
                    prop="grade"
                    label="等级"
                    width="120">
                </el-table-column>
                <el-table-column
                    prop="explain"
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
            :total="newData.length"
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
            }
        },
//改成从后台重新获取数据，前端object的处理写不出来


        beforeMount: function() {
            //console.log('hhh');
            let vm = this;
            var input;
            input = JSON.parse(localStorage.getItem("input"));
            //console.log(input+'!!!!!');
            //var tempdata = this.data[input];
            //this.newData[input] = tempdata;
            localStorage.removeItem("input");
            //post 有报错信息 配置未完成
            console.log(this.data)
            
            axios.post('/user', JSON.stringify({
                searchName: this.input,
            }))
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
            
        },


        data () {
            return {
                input: '',
                data: [{
                    date: '2016-05-03',
                    name: '王小虎',
                    pjNum: 'asdfghjkl',
                    pjHead: '普陀区',
                    grade: '上海市',
                    explain: 2003333,
                    hhh: 'ssada'
                },{
                    date: '2016-05-03',
                    name: '王小虎',
                    pjNum: 'qwerty',
                    pjHead: '普陀区',
                    grade: '上海市',
                    explain: 2003331
                }],
                newData: [{
                    date: '2016-05-03',
                    name: '王小虎',
                    pjNum: 'asdfghjkl',
                    pjHead: '普陀区',
                    grade: '上海市',
                    explain: 2003332
                },],
                currentPage:1,
                pagesize:5,
                search:''
            }
        }, 
    }
</script>
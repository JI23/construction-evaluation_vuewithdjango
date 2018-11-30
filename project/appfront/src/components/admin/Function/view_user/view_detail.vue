<template>
    <div>
        <div style="top:-75px; position:relative; width:950px; height:450px;">
            <div class="wrapper1" >
                <el-col>
                    <h2>个人资料</h2>
                    <span class="lebal">昵称</span>
                    <el-input :disabled="true" size="mini" style="width:100%" v-model="nickName" placeholder="请输入内容"></el-input>
                    <span class="lebal">真实姓名</span>
                    <el-input :disabled="true" size="mini" style="width:100%" v-model="realName" placeholder="请输入内容"></el-input>
                    <span class="lebal">身份证号码</span>
                    <el-input :disabled="true" size="mini" style="width:100%" v-model="id" placeholder="请输入内容"></el-input>
                    <span class="lebal">邮箱</span>
                    <el-input :disabled="true" size="mini" style="width:100%" v-model="email" placeholder="请输入内容"></el-input>
                    <span class="lebal">手机</span>
                    <el-input :disabled="true" size="mini" style="width:100%" v-model="phoneNum" placeholder="请输入内容"></el-input>
                    <span class="lebal">建筑师证件号</span>
                    <el-input :disabled="true" size="mini" style="width:100%" v-model="workId" placeholder="请输入内容"></el-input><br><br>
                </el-col>
            </div>
            <div class="wrapper1">
                <h2>公司资料</h2>
                <span class="lebal">公司名称</span>
                <el-input :disabled="true" size="mini" style="width:100%" v-model="comName" placeholder="请输入内容"></el-input>
                <span class="lebal">证件号</span>
                <el-input :disabled="true" size="mini" style="width:100%" v-model="comId" placeholder="请输入内容"></el-input>
                <span class="lebal">公司职务</span>
                <el-input :disabled="true" size="mini" style="width:100%" v-model="workName" placeholder="请输入内容"></el-input><br><br><br>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                nickName: '',
                realName: '',
                id: '',
                email: '',
                phoneNum: '',
                workId: '',
                comName: '',
                comId: '',
                workName: ''
            }
        },

        methods: {
            getUser_info(){//获取四个框的基本信息，以及图表的信息内容
                let _this = this
                this.$ajax({
                    method: 'get',
                    url: 'get_user_info',
                }).then(function(response){
                    console.log(response)
                    var res = response['data']['userinfo']
                    
                    //进行赋值
                })
                 
            }
        },
//用于传值
        mounted: function () {
            var vm = this
            //获取初始值并进行赋值
            var pjNum1 = JSON.parse(localStorage.getItem("pjNum"));

            localStorage.removeItem("pjNum");
            
        },
    }
</script>


<style scoped>
    .wrapper1{
        position:relative;/*相对定位:参考物*/
        float: left;;/*浮动:左浮动 与父元素的左端对齐 依次的往右端显示 一行显示不下就换行接着依次显示*/
        width:45%;
        height:450px;
        margin:18px 20px;
    }


    .lebal{
        position:relative;
        display: inline-block;
        padding:9px 0;
        color: #333;
    }


</style>
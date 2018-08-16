<template>
    <div>
        <el-col :span="10">
            <h3>基础资料</h3>
            <span class="lebal">昵称</span>
            <el-input v-model="nickname" placeholder="已注册内容"></el-input>
            <span class="lebal">公司名称</span>
            <el-input v-model="comName" placeholder="已注册内容"></el-input>
            <span class="lebal">证件号</span>
            <el-input v-model="comNum" placeholder="已注册内容"></el-input>
            <span class="lebal">公司职务</span>
            <el-input v-model="comPosition" placeholder="已注册内容"></el-input>
        </el-col>
        <el-col :span="3" style="color:transparent">''</el-col> 
        <el-col :span="11">
            <h3>更改绑定信息</h3>
            <br>
            <br>
             <el-button type="text" >更改邮箱</el-button>
             <br>
             <br>
             <el-button type="text" >更换手机号</el-button>
             <br>
             <br>
            <el-button type="text" >更改密码</el-button>
            <br>
            <el-button type="primary" style="margin-top:95px; " @click="goToMyinfo">确认修改</el-button>
        </el-col> 
    </div>
</template>

<script>
export default {
    data(){
        return{
            nickname: '',
            // realname:'',
            // idnumber:'',
            password:'',
            yourEmail:'',
            phone:'',
            //architectnum:'',
            comName:'',
            comNum:'',
            comPosition:''
        }
    },
    methods:{
            goToMyinfo()
            {
                this.$router.push({name:'myinfo'});
            }
    }
}
</script>

<style scoped>
    .lebal{
        display: inline-block;
        padding:12px 0;
        color: #333;
    }
    el-input{
        margin-top:5px;
        width:40px;
    }

</style>

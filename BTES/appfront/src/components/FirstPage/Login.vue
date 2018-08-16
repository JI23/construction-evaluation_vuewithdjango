<template>
    <el-card class="card">
        <h2>用户登录</h2>
        <el-form  label-width="80px" :model="LoginLabel">
            <el-form-item label="手机号">
            <el-input v-model="LoginLabel.phone" placeholder="请输入手机号"></el-input>
            </el-form-item>
            <el-form-item label="密　码">
            <el-input v-model="LoginLabel.password" placeholder="请输入密码"></el-input>
            </el-form-item>
        </el-form>
        <el-button @click="gotoRegister" type="text" size="small">没有账号？立即注册</el-button>
        <el-button type="primary" @click="login">登录</el-button>
    </el-card>
</template>



<script>
export default {
    data(){
        return{
            LoginLabel:{
                phone:'',
                password:''
            }
        }
    },
    methods:{
        login(){
            this.$router.push({name:'dashboard'});
        },
        gotoRegister()
        {
            this.$router.push({name:'register'});
        }

    }
}
</script>

<style scoped>
    /* .logindiv{
            width:300px;
            height:200px;
            float:right;
            margin-right:100px;
            margin-top: 100px;
            margin-bottom:120px;
            padding: 50px 30px 40px 10px;
            text-align: center;
            border-radius:10px;
            opacity:0.8; 
            box-shadow: 0 2px 3px rgba(0, 0, 0, 0.3);
    } */
    /* .outerdiv{
            height:510px;
            width:auto;
    } */
    .card{
        text-align: center;
        width:30%;
        margin:50px auto;
        padding: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .el-button{
        display: block;
        margin:0 auto;
        width:100px;
    }
    h2{
        color:#66209A;
        margin-top:0;
    }
</style>

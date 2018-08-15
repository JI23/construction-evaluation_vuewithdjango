<template>
    <nav>
        <ul>
            <div class="logo"></div>
            <li><router-link :to="{name:'product'}" class="link">产品</router-link></li>
            <li><router-link :to="{name:'service'}" class="link">服务</router-link></li>
        </ul>
        <div class="btn-group">
            <el-button @click="goToLogin">登录</el-button>
            <el-button @click="goToRegister">注册</el-button>  
        </div>
    </nav>
</template>
<script>
export default {
    methods:{
        goToLogin(){
            this.$router.push({name:'login'})
        },
        goToRegister(){
            this.$router.push({name:'register'})
        }
    }
}
</script>

<style scoped>
    .btn-group{
        position: absolute;
        top:0;
        right: 40px;
        height: 80px;
        display: flex;
        align-items: center;
    }
    .logo{
        background-color: transparent;
        width:80px;
        height: 80px;
        border-radius: 50%;
        margin-right: 40px;

    }
    ul{
        margin: 0;
        height: 80px;
        display: flex;
        align-items: center;
    }
    li{
        
        width:70px;
        list-style: none;
        color: #999;
        font-size: 19px;
        font-weight: 400;
    }
    .link{
        cursor: pointer;
        color:#eee;
        text-decoration: none;
    }
    .link:hover{
        color:#fff;
    }
    nav{
        box-sizing: border-box;
        position: relative;
        padding: 0 20px;
        height: 80px;
        background-color: #66209A;
        width:100%;
        box-shadow: 0 2px 3px rgba(0, 0, 0, 0.3);
    }
    body{
        transition: background .1s;
    }
</style>

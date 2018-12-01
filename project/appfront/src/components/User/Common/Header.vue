<template>
    <nav>
        <span>建筑抗震韧性评估系统</span>
        <div class="btn-group">
            <el-button @click="goToIndex">退出</el-button>
            <i class="el-icon-info" @click='goToUserInfo'></i>
            <span @click='goToUserInfo'>{{ username }}</span> 
        </div>
    </nav>
</template>
<style scoped>
    nav>span{
        height: 60px;
        line-height: 60px;
        font-size:24px;
        font-weight: 500;
    }
    nav{
        box-sizing: border-box;
        transition: background .1s; 
        padding:0 40px;
        width:100%;
        height: 60px;
        color:#66209A;
        box-shadow: 0 2px 3px rgba(0, 0, 0, 0.1);
    }
    .btn-group{
        position: absolute;
        top:0;
        right: 60px;
        height: 60px;
        display: flex;
        align-items: center;
    }
    .btn-group>span{
        cursor: pointer;
        margin-left: 5px;
        color:#66209A
    }
    .btn-group>span:hover{
        color: rgba(102, 32, 154, 0.7)
    }
    .btn-group>i{
        margin-left: 20px;
        cursor: pointer;
    }
</style>
<script>
export default {
    data(){
        return{
            username:null
        }
    },
    methods:{
        goToIndex(){
            // 需要增加路由守卫

            //this.$store.dispatch("setUser",null)
            localStorage.removeItem('phone')
            this.$router.push({name:'home_admin'})
        },
        goToUserInfo(){
            this.$router.push({name:'userinfo'})
        },

    },

    mounted:function(){
        var name = localStorage.getItem('phone')
        this.username = name
    }
}
</script>


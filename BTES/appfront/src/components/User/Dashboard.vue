<template>
    <div>
        <user-header></user-header>
        <div class="main clearfix">
            <el-col :span="4">
                <user-nav style="height:100%"></user-nav>
            </el-col>
            <el-col :span="20">
            <el-card class="card clearfix">
                <router-view></router-view>
            </el-card>  
            </el-col>
        </div>
        <common-footer class="footer"></common-footer>
    </div>
</template>
<script>
import Header from './Common/Header'
import Footer from "./Common/Footer"
import Nav from './Common/Nav'
export default {
    components:{
        "user-header": Header,
        "common-footer": Footer,
        "user-nav": Nav
    }
}
</script>
<style scoped>
    .clearfix:after{
        content:"";
        display: block;
        clear: both;
    }
    .main{
        overflow: scroll;
        position:absolute;
        top:60px;
        bottom: 60px;
        width:100%;
        margin-top: 5px;
    }
    .footer{
        position: absolute;
        bottom: 0;
    } 
    .card{
        padding: 10px;
    }
    body{
        width: 100%;
        height: 100%;
    }
</style>


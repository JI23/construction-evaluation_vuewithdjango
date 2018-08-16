<template>
    <div>
        <div class="div1">
            联系我们
        </div>
        <div class='div2'>
            <el-col :span="4" style="color:transparent">''</el-col>
            <el-col :span="15">
            <h3>评论反馈</h3>
            <span class="lebal">联系方式</span>
            <el-input v-model="yourEmail" placeholder="请输入您的邮箱"></el-input>
            <span class="lebal">标题</span>
            <el-input v-model="fbTitle" placeholder="请输入标题"></el-input>
            <span class="lebal">评论内容</span>
            <el-input type="textarea"   v-model="fbContent" placeholder="请输入您的反馈内容"></el-input>
            <el-button type="primary" style="float:right; margin-top:50px" @click="sendfeedback">发送</el-button>
        </el-col>
        </div>
    </div>
</template>
<script>
export default {
    data(){
        return{
            yourEmail:'',
            fbTitle:'',
            fbContent:''
        }
    },
     methods:{
                sendfeedback(){
                    this.$router.push({name:'feedbacklist'});
                }
             }
}
</script>

<style scoped>
  .lebal{
        display: inline-block;
        padding:10px 0;
        color: #333;
        font-size:13px;
    }
    el-input{
        margin-top:5px;
        width:60px;
    }
    .div1{
        height:410px;
        width:40%;
        float:left; 
        background-color:#F2F2F2;
        border-radius:5px;
        text-align: center;
    }
     .div2{
        width:60%;
        float:left; 
        
    }

</style>

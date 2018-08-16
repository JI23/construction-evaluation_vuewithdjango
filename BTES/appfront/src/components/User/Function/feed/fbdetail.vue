<template>
    <div>
        <div class="div1">
            这里放图片
        </div>
        <div class=div2>
            <el-col :span="4" style="color:transparent">''</el-col>
            <el-col :span="15">
            <h3>反馈详情</h3>
            <span class="lebal">标题</span>
            <el-input disabled="disabled" v-model="fbTitle" placeholder="标题"></el-input>
            <span class="lebal">评论内容</span>
            <el-input disabled="disabled" type="textarea"  v-model="fbContent" placeholder="反馈内容"></el-input>
            <span class="lebal">管理员回复</span>
            <el-input disabled="disabled" type="textarea"  v-model="admReply" placeholder="管理员回复"></el-input>
            <br>
            
            <el-button  type="primary" style="float: left; margin-left:30px;margin-top:20px;" @click="remindReply">提醒回复</el-button>
            <el-button  type="primary" style="float: right; margin-right:30px;margin-top:20px;" @click="gotoFbList">返回</el-button>
        </el-col>
        </div>
    </div>
</template>
<script>
export default {
    data(){
        return{
            fbTitle:'',
            fbContent:'',
            admReply:''
        }
    },
     methods:{
                gotoFbList(){
                    this.$router.push({name:'feedbacklist'});
                },
                remindReply()
                {

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
        width:100px;
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

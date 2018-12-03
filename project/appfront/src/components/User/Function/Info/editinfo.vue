<template>
    <div>
        <el-col :span="10">
            <h3>基础资料</h3>
            <!-- <span class="lebal">昵称</span>
            <el-input v-model="nickname" placeholder="已注册内容"></el-input> -->
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
            //nickname: '',
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
            show_user_detail:function(){
                    let _this=this;
                    let current_user_id = JSON.parse(localStorage.getItem("phone")); 
                    console.log(current_user_id)
                    this.$ajax({
                        method:'get',
                        url:'get_user_info',
                        params:{
                            username:current_user_id
                        },
                        headers:{"Content-Type": "application/json"}
                })
                .then(function(response){
                            console.log(response)
                            var res = response.data
                            console.log(res)
                            if (res['error_num'] == 0) {
                                console.log(res['user_info'])
                                //_this.realname=res['user_info'].truename
                                //_this.id=res['user_info'].
                                //_this.yourEmail=res['user_info'].email
                                //_this.phone=res['user_info'].telephone
                                //_this.architectNum=res['user_info'].architect_id
                                _this.comName=res['user_info'].company__com_name
                                _this.comNum=res['user_info'].company__certificate
                                _this.comPosition=res['user_info'].job
                            } 
                            else {
                                _this.$message.error(res['msg'])
                                console.log(res['msg'])
                            }
                        })
                        .catch(function(err){
                            console.log(err);
                        });
                },
            goToMyinfo()
            {
                this.$router.push({name:'myinfo'});
            }
    },
    mounted:function(){
        this.show_user_detail()
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

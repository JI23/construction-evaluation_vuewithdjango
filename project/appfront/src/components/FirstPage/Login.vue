<template>
    <el-card class="card">
        <h2>用户登录</h2>
        <el-form  label-width="80px" :model="LoginLabel">
            <el-form-item label="手机号">
            <el-input v-model="LoginLabel.phone" placeholder="请输入手机号" ref="focusPhone"></el-input>
            </el-form-item>
            <el-form-item label="密　码">
            <el-input v-model="LoginLabel.password" type="password" @keyup.enter.native="login" placeholder="请输入密码"></el-input>
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
    mounted(){
        this.$refs['focusPhone'].focus();
    },
    methods:{
        login(){

            let _this=this;
            this.$ajax({
                method:'get',
                url:'login',
                params:{
                    username:this.LoginLabel.phone,
                    password:this.LoginLabel.password
                },
                headers:{"Content-Type": "application/json"}
            })
            .then(function(response){
                        console.log(response)
                        var res = response.data
                        console.log(res)
                        
                        if (res['error_num'] == 0) {
                            localStorage.clear()
                            console.log(res['msg'])
                            localStorage.clear()
                            localStorage.setItem('phone', res['username'])
                            localStorage.setItem('project',0)
                            //localStorage.setItem('password', res['password'])
                            console.log(localStorage.getItem('phone')) 
                            _this.$store.dispatch("setUser",res['username'])
                            
                            console.log(res['admin'])
                            console.log('!!!!!!!!!!!!!!!!!!!!!')
                            if(res['admin'] === '1'){
                                _this.$router.push({name:'dashboard_admin'})
                                localStorage.setItem('admin',res['admin'])
                            }
                            else{
                                _this.$router.push({name:'dashboard'});   //这里前面要加个_
                            }
                        } 
                        else if(res['error_num']==1){
                            _this.$message.error('账号还在审核中')
                            console.log(res['msg'])
                        }
                        else {
                            _this.$message.error('用户名或密码错误')
                            console.log(res['msg'])
                        }
                    })
                    .catch(function(err){
                        console.log(err);
                    });

            
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

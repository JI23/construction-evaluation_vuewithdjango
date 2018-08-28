<template>
    <div >
       <br>
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="140px" label-position=left class="demo-ruleForm">  
          <el-row>
            <el-col :span="2" style="color:transparent">''</el-col>
            <el-col :span="10">
            <h3>个人信息</h3> 
            <el-form-item label="昵称" prop="nickname">
            <el-input v-model="ruleForm.nickname"></el-input>
            </el-form-item>
            <el-form-item label="真实姓名" prop="name">
            <el-input v-model="ruleForm.name"></el-input>
            </el-form-item>
            <el-form-item label="密码"  prop="password">
            <el-input v-model="ruleForm.password" type="password" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="请再次输入密码"  prop="checkPass">
            <el-input v-model="ruleForm.checkPass" type="password" auto-complete="off"></el-input>
            </el-form-item>
            <el-form-item label="邮箱" prop="yourEmail">
            <el-input v-model="ruleForm.yourEmail"></el-input>
            </el-form-item>
            <el-form-item label="手机号" prop="telephone">
            <el-input v-model="ruleForm.telephone"></el-input>
            </el-form-item>
            <el-form-item label="建筑师证号" prop="architectNum">
            <el-input v-model="ruleForm.architectNum"></el-input>
            </el-form-item>
        </el-col>
        <el-col :span="1" style="color:transparent">''</el-col>
        <el-col :span="10">
            <h3>公司信息</h3>
            <el-form-item label="公司名称" prop="comName">
            <el-input v-model="ruleForm.comName"></el-input>
            </el-form-item>
            <el-form-item label="证件号" prop="comNum">
            <el-input v-model="ruleForm.comNum"></el-input>
            </el-form-item>
            <el-form-item label="公司职务" prop="comPosition">
            <el-input v-model="ruleForm.comPosition"></el-input>
            </el-form-item>
            <el-form-item>
              <br>
              <br>
            <el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
            </el-form-item>
       </el-col>
    </el-row>
</el-form>
</div>
</template>

<script>
  export default {
    data() {
            var validatePass = (rule, value, callback) => {
                if (value === '') {
                 callback(new Error('请输入密码'));
                } else {
                 if (this.ruleForm.checkPass !== '') {
                    this.$refs.ruleForm.validateField('checkPass');
                }
                 callback();
                }
            };
            var validatePass2 = (rule, value, callback) => {
                if (value === '') {
                callback(new Error('请再次输入密码'));
                } else if (value !== this.ruleForm.password) {
                callback(new Error('两次输入密码不一致!'));
                } else {
                callback();
                }
            };
      return {
        ruleForm: {
          nickname: '',
          name:'',
          password:'',
          checkPass:'',
          yourEmail:'',
          telephone:'',
          architectNum:'',
          comName:'',
          comNum:'',
          comPosition:''
        },
        rules: {
          nickname: [
            { required: true, message: '请输入您的昵称', trigger: 'blur' },
            { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'blur' }
          ],
           realname: [
            { required: true, message: '请输入您的真实姓名', trigger: 'blur' },
            { min: 2, max: 5, message: '长度在 2 到 5 个字符', trigger: 'blur' }
          ],
          password: [
            { required: true, validator: validatePass, trigger: 'blur' }
          ],
          checkPass: [
            { required: true, validator: validatePass2, trigger: 'blur' }
          ],
           yourEmail: [
            { required: true, message: '请输入您的邮箱',trigger: 'blur' }
          ],
           phone: [
            { required: true, message: '请输入您的手机号', trigger: 'blur' }
          ],
           architectNum: [
            {   trigger: 'blur' }
          ],
          comName: [
            { required: true, message: '请输入公司名称',trigger: 'blur' }
          ],
         comNum: [
            { required: true, message: '请输入证件号',trigger: 'blur' }
          ],
        }
      };
    },
    methods: {
      submitForm(formName) {
              let _this=this;
              this.$ajax({
                  method:'get',
                  url:'http://localhost:8000/api/user_register',
                  params:{
                      username : this.ruleForm.telephone,  
                      password : this.ruleForm.password,
                      password_again:this.ruleForm.checkPass,
                      email:this.ruleForm.yourEmail,
                      nickname:this.ruleForm.nickname,
                      truename:this.ruleForm.name,
                      architect_id:this.ruleForm.architectNum,
                      com_name:this.ruleForm.comName,
                      certificate:this.ruleForm.comNum,
                      job:this.ruleForm.comPosition
                  },
                  headers:{"Content-Type": "application/json"}
              })
              .then(function(response){
                          console.log(response)
                          var res = response.data
                          console.log(res)
                          if (res['error_num'] == 0) {
                              console.log(res['msg'])
                              localStorage.setItem('telephone', res['telephone'])
                              localStorage.setItem('password', res['password'])
                              console.log(localStorage.getItem('telephone'))
                              
                              console.log(localStorage.getItem('password'))
                              _this.$router.push({name:'login'});   //这里前面要加个_
                          } 
                          else if (res['error_num'] == 1){
                              _this.$message.error('公司不在数据库中')
                          }
                          else {
                              _this.$message.error('注册失败')
                              console.log(res['msg'])
                          }
                      })
                      .catch(function(err){
                          console.log(err);
                      });
      }
    }
  }
</script>

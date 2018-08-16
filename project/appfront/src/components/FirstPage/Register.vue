<template>
    <div >
       <br>
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="140px" label-position=left class="demo-ruleForm">  
          <el-row>
            <el-col :span="2" style="color:transparent">''</el-col>
            <el-col span="10">
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
            <el-input v-model="ruleForm.youremail"></el-input>
            </el-form-item>
            <el-form-item label="手机号" prop="telephone">
            <el-input v-model="ruleForm.telephone"></el-input>
            </el-form-item>
            <el-form-item label="建筑师证号" prop="architectNum">
            <el-input v-model="ruleForm.architectnum"></el-input>
            </el-form-item>
        </el-col>
        <el-col :span="1" style="color:transparent">''</el-col>
        <el-col span="10">
            <h3>公司信息</h3>
            <el-form-item label="公司名称" prop="comName">
            <el-input v-model="ruleForm.comname"></el-input>
            </el-form-item>
            <el-form-item label="证件号" prop="comNum">
            <el-input v-model="ruleForm.comnum"></el-input>
            </el-form-item>
            <el-form-item label="公司职务" prop="comPosition">
            <el-input v-model="ruleForm.composition"></el-input>
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
            this.$router.push({name:'login'})
      }
    }
  }
</script>

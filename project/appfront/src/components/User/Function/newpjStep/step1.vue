<template> 
    <div>
        <el-row>
            <el-button size="small" class='btn' @click="next">下一步</el-button>
            <el-button size="small" class='btn' @click="back">上一步</el-button>
            <el-button size="small" class='btn' @click="save1">保存</el-button>
        </el-row>
        <el-row>
            <el-col :span="10">
            <h3>基本信息</h3>
            <span class="lebal">项目名称</span>
            <el-input v-model="project_name" placeholder="请输入内容"></el-input>
            <span class="lebal">客户名称</span>
            <el-input v-model="client_name" placeholder="请输入内容"></el-input>
            <span class="lebal">项目负责人</span>
            <el-input v-model="project_leader" placeholder="请输入内容"></el-input>
        </el-col>
        <el-col :span="1" style="color:transparent">''</el-col>
        <el-col :span="11">
            <h3>项目说明</h3>
            <el-input
                type="textarea"
                :rows="15"
                placeholder="请输入内容"
                v-model="project_description">
            </el-input>
        </el-col>
        </el-row> 
    </div>
</template>
<script>
export default {
    data(){
        return{
            project_name:'',
            client_name:'',
            project_leader:'',
            project_description:''
        }
    },
    beforeRouteLeave(to, from, next){
    //  if (to.name == 'step2') {
        let project_name = JSON.stringify(this.project_name)
        let client_name = JSON.stringify(this.client_name)
        let project_leader = JSON.stringify(this.project_leader)
        let project_description = JSON.stringify(this.project_description)
        sessionStorage.setItem('project_name', project_name)
        sessionStorage.setItem('client_name', client_name)
        sessionStorage.setItem('project_leader', project_leader)
        sessionStorage.setItem('project_description', project_description)
    //  }
    //   else{
    //     localStorage.removeItem('project_name')
    //     localStorage.removeItem('client_name')
    //     localStorage.removeItem('project_leader')
    //     localStorage.removeItem('project_description')
    //     console.log('到其他地方');
    //   }
      next()
    },
    created(){
      //从localStorage中读取条件并赋值给查询表单
        let project_name = sessionStorage.getItem('project_name')
        let client_name = sessionStorage.getItem('client_name')
        let project_leader = sessionStorage.getItem('project_leader')
        let project_description = sessionStorage.getItem('project_description')
        if (project_name != null) {
            this.project_name = JSON.parse(project_name)
        }
        if (client_name != null) {
            this.client_name = JSON.parse(client_name)
        }
        if (project_leader != null) {
            this.project_leader = JSON.parse(project_leader)
        }
        if (project_description != null) {
            this.project_description = JSON.parse(project_description)
        }
    //   this.$http.get('http://example.com/api/test', {params: this.searchForm})
    //   .then((response)=>{
    //     console.log(response.data)
    //   }).catch((error)=>{
    //     console.log(error)
    //   })
    },
    methods:{
        next(){
            this.$emit('next','');
        },
        back(){
            this.$emit('back','');
        },
        save1(){
            let _this=this;
            var username=localStorage.getItem('phone')
            this.$ajax({
                method:'get',
                url:'step1',
                params:{
                    username:username,
                    project_name:this.project_name,
                    client_name:this.client_name,
                    project_leader:this.project_leader,
                    project_description:this.project_description
                },
                headers:{"Content-Type": "application/json"}
            })
            .then(function(response){
                        console.log(response)
                        var res = response.data
                        console.log(res)
                        if (res['error_num'] == 0) {
                            console.log(res['msg'])
                            localStorage.setItem('project_name', res['project_name'])
                            localStorage.setItem('project_leader', res['project_leader'])
                            localStorage.setItem('project_description', res['project_description'])
                            localStorage.setItem('client_name', res['client_name'])
                            console.log(localStorage.getItem('project_name'))
                            console.log(res['project_leader'])
                            console.log(res['project_description'])
                            console.log(res['client_name'])
                            _this.$message.success(res['msg'])
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
    .btn{
        margin-top:12px;
    }

</style>

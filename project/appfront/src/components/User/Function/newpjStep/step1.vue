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
        {{ resonse_message }}
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
    methods:{
        next(){
            this.$emit('next','');
        },
        back(){
            this.$emit('back','');
        },
        save1(){
            let _this=this;
            this.$ajax({
                method:'get',
                url:'http://localhost:8000/api/step1',
                params:{
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

<template>
    <div>
        <el-row>
            <el-button size="small" class='btn' @click="next">下一步</el-button>
            <el-button size="small" class='btn' @click="back">上一步</el-button>
        </el-row>
        <el-row>
            <el-col :span="10">
            <h3>基本信息</h3>
            <span class="lebal">项目名称</span>
            <el-input v-model="pjname" placeholder="请输入内容"></el-input>
            <span class="lebal">项目编号</span>
            <el-input v-model="pjindex" placeholder="请输入内容"></el-input>
            <span class="lebal">客户名称</span>
            <el-input v-model="clientName" placeholder="请输入内容"></el-input>
            <span class="lebal">项目负责人</span>
            <el-input v-model="principal" placeholder="请输入内容"></el-input>
        </el-col>
        <el-col :span="1" style="color:transparent">''</el-col>
        <el-col :span="11">
            <h3>项目说明</h3>
            <el-input
                type="textarea"
                :rows="15"
                placeholder="请输入内容"
                v-model="textarea">
            </el-input>
        </el-col>
        </el-row> 
    </div>
</template>
<script>
export default {
    data(){
        return{
            pjname:'',
            pjindex:'',
            clientName:'',
            principal:'',
            textarea:''
        }
    },
    methods:{
        next(){
            this.$emit('next','');
        },
        back(){
            this.$emit('back','');
        }
        
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

<template>
    <div class="wrapper">
        <el-row>
            <el-button size="small" class='btn' @click="next">下一步</el-button>
            <el-button size="small" class='btn' @click="back">上一步</el-button>
        </el-row>
        <div class="clearfix">
            <el-col :span='11'>
            <span class="lebal">方向</span>
            <el-input v-model="data[0].direction" :disabled="true"></el-input>
            <span class="lebal">EDP类型</span>
            <el-input v-model="data[0].EDP_type" placeholder="请输入内容"></el-input>
            <span class="lebal">楼层数量</span>
            <el-input v-model="data[0].floor_no" placeholder="请输入内容"></el-input>
            <span class="lebal">地震数量</span>
            <el-input v-model="data[0].earthquake_no" placeholder="请输入内容"></el-input>
            </el-col>
            <el-col :span="1" style="color:transparent">''</el-col>
            <el-col :span='11'>
                <span class="lebal">方向</span>
                <el-input v-model="data[1].direction" :disabled="true"></el-input>
                <span class="lebal">EDP类型</span>
                <el-input v-model="data[1].EDP_type" placeholder="请输入内容"></el-input>
                <span class="lebal">楼层数量</span>
                <el-input v-model="data[1].floor_no" placeholder="请输入内容"></el-input>
                <span class="lebal">地震数量</span>
                <el-input v-model="data[1].earthquake_no" placeholder="请输入内容"></el-input>
            </el-col>
        </div>
        <div class="btn-group">
            <el-button>点击预览</el-button>
            <el-button>提交并生成结果</el-button>
        </div>
        
    </div>
</template>

<script>
export default {
    methods:{
        next(){
            this.$emit('next','');
        },
        back(){
            this.$emit('back','');
        }
    },
    data(){
        return {
            data:[{
                direction:'X方向',
                EDP_type:null,
                floor_no:null,
                earthquake_no:null
            },{
                direction:'Y方向',
                EDP_type:null,
                floor_no:null,
                earthquake_no:null
            }]
            
        }    
    }
}
</script>


<style scoped>
    .wrapper{  
        margin:10px auto;
        max-width:800px;
    }
    .lebal{
        display: inline-block;
        padding:12px 0;
        color: #333;
    }
    .btn-group{
        margin:15px 0;
    }
    .clearfix:after{
        content:'';
        display: block;
        clear: both;
    }
    .btn{
        margin-top:12px;
    }
</style>

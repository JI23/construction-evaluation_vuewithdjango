<template>
    <div>
        <el-steps :active="active" finish-status="success" align-center>
            <el-step title="项目信息"></el-step>
            <el-step title="建筑信息"></el-step>
            <el-step title="结构构件"></el-step>
            <el-step title="非结构构件"></el-step>
            <el-step title="地震信息"></el-step>
            <el-step title="结构响应"></el-step>
        </el-steps>
        <router-view  class="input clearfix"  @next="next" @back="back"></router-view>
        <el-button style="position:relative; left:80%; top:-430px" @click="createNew">重新建立项目</el-button>
        
    </div>
</template>
    
<script>
  export default {
    data() {
      return {
        active: 0,
        activeRouter:'step1'
      };
    },

    mounted(){
        this.get_url()
    },

    watch:{
        "$route": "get_url"
    },

    methods: {
        get_url(){
            let _this = this
            //console.log(_this.active)
            var path1 = parseInt(this.$route.name.substr(4,1))-1
            _this.active = path1
        },
        createNew(){
            this.$confirm('是否保存当前项目修改', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
                }).then(() => {
                    this.$router.push({name:'step1'})
                    //移除本地存储
                    //this.$message({
                    //    type: 'success',
                    //    message: '删除成功!'
                    //});
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消重新建立'
                    });          
            });
        },
        next() {  
            if (++this.active > 5) {
                this.active = 0;
            }
                this.activeRouter = 'step' + (this.active + 1)
                this.$router.push({name:this.activeRouter})
        },
        back(){
            if(this.active-- == 0) this.active = 0;
            this.activeRouter = 'step' + (this.active + 1)
                this.$router.push({name:this.activeRouter})
        },
    }
  }
</script>

<style scoped>
    .input{
        width: 100%;
        height: 430px;
    }
    .clearfix:after{
        content:"";
        display: block;
        clear: both;
    }
</style>



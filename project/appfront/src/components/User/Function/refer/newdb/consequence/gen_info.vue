<template>
    <div>
        <div class="wrapper2" >
            <el-col>
                <span class="lebal">修理信息</span>
                <el-input style="width:100%; top:-30px; position:relative" type="textarea" :rows="13" placeholder="请输入内容" v-model="re_info"></el-input>
                <el-button style="display:block;margin:0 auto; position:relative; top:-10px" @click="save_next">下一步</el-button>
            </el-col>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                re_info: '',
            }
        },

        methods: {
            save_next(){
                var re_info = {
                    reInfo: this.re_info, 
                };
                localStorage.setItem("re_info",JSON.stringify(re_info));
                this.$router.push({name:'re_cost'});
            },
        }
  }
</script>


<style scoped>
    .wrapper2{
        position:relative;/*相对定位:参考物*/
        left:20px;/*浮动:左浮动 与父元素的左端对齐 依次的往右端显示 一行显示不下就换行接着依次显示*/
        top:10px;
        width:85%;
        height:300px;
        margin:18px 20px;
    
}

    .lebal{
        position:relative;
        top:-30px;
        display: inline-block;
        padding:12px 0;
        color: #333;
    }

</style>
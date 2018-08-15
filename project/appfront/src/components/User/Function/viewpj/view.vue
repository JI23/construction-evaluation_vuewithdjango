<template>
    <div>
        <div style="width:950px; height:450px;">
            <div class="wrapper1" >
                <el-col>
                    <h2>基本信息</h2>
                    <span class="lebal">项目名称</span>
                    <el-input :disabled="true" size="mini" style="width:100%" v-model="pjName" placeholder="请输入内容"></el-input>
                    <span class="lebal">项目编号</span>
                    <el-input :disabled="true" size="mini" style="width:100%" v-model="pjNum" placeholder="请输入内容"></el-input>
                    <span class="lebal">客户名称</span>
                    <el-input :disabled="true" size="mini" style="width:100%" v-model="customer" placeholder="请输入内容"></el-input>
                    <span class="lebal">项目负责人</span>
                    <el-input :disabled="true" size="mini" style="width:100%" v-model="per" placeholder="请输入内容"></el-input>
                    <span class="lebal">创建时间</span>
                    <el-input :disabled="true" size="mini" style="width:100%" v-model="time" placeholder="请输入内容"></el-input><br><br>
                    <el-button style="display:block;margin:0 auto" @click="detail" type="success">查看认证信息</el-button>
                </el-col>
            </div>
            <div class="wrapper1">
                <h2>证书信息</h2>
                <div class="picture">
                </div>
                <h2>项目说明</h2>
                <el-input :disabled="true" style="width:100%" type="textarea" :rows="4" placeholder="请输入内容" v-model="textarea1"></el-input>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                pjName: '',
                pjNum: 'a',
                customer: '',
                per: '',
                time: '',
                textarea1: '',
            }
        },

        methods: {
            detail(){
                console.log(this.$route.query.pjNum);
                this.$router.push({name:'detail'});
                localStorage.setItem("pjNum",JSON.stringify(this.pjNum));
            }
        },
//用于传值
        mounted: function () {
            var vm = this
            // 用$on事件来接收参数
            var pjNum1 = JSON.parse(localStorage.getItem("pjNum"));

            localStorage.removeItem("pjNum");
        },
    }
</script>


<style scoped>
    .wrapper1{
        position:relative;/*相对定位:参考物*/
        float: left;;/*浮动:左浮动 与父元素的左端对齐 依次的往右端显示 一行显示不下就换行接着依次显示*/
        width:45%;
        height:450px;
        margin:18px 20px;
    }

    .picture{
        position:relative;/*相对定位:参考物*/
        float: left;;/*浮动:左浮动 与父元素的左端对齐 依次的往右端显示 一行显示不下就换行接着依次显示*/
        width:90%;
        height:45%;
        margin:18px 20px;
        background: url(../../../../assets/hometest1.jpg) center no-repeat;
    }

    .lebal{
        position:relative;
        display: inline-block;
        padding:9px 0;
        color: #333;
    }


</style>
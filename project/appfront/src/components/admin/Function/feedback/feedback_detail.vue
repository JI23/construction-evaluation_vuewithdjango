<template>
    <div>
        <div style="width:950px; height:450px;">
            <div class="wrapper1" >
                <el-col>
                    <h2>反馈信息</h2>
                    <span class="lebal">联系方式</span>
                    <el-input :disabled="true" style="width:100%" v-model="contact" placeholder="请输入内容"></el-input>
                    <span class="lebal">标题</span>
                    <el-input :disabled="true" style="width:100%" v-model="title" placeholder="请输入内容"></el-input>
                    <span class="lebal">反馈内容</span>
                    <el-input :disabled="true" type="textarea" rows=7 style="width:100%" v-model="feedback" placeholder="请输入内容"></el-input><br><br>
                </el-col>
            </div>
            <div class="wrapper1">
                <h2>回复信息</h2>
                <span class="lebal">公司名称</span>
                <el-input type="textarea" rows=13 style="width:100%" v-model="reply" placeholder="请输入内容"></el-input>
                <br><br>
                <el-button @click="send">发送</el-button><!--未写 -->
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                contact:'',
                title:'',
                feedback:'',
                reply:'',
            }
        },

        methods: {
            send(){

            }
        },
//用于传值
        mounted: function () {
            var vm = this
            //获取初始值并进行赋值
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


    .lebal{
        position:relative;
        display: inline-block;
        padding:9px 0;
        color: #333;
    }


</style>
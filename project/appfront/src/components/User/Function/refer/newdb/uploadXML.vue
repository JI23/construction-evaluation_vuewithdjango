<template>
    <div>
        <div class="wrapper6"><!--基本信息填写 -->
            <el-col>
                <span class="lebal">ID</span>
                <el-input style="width:100%" v-model="id" placeholder="请输入内容"></el-input>
                <span class="lebal">Name</span>
                <el-input  style="width:100%" v-model="name" placeholder="请输入内容"></el-input>
                <span class="lebal">Description</span>
                <el-input style="width:100%" type="textarea" :rows="4" placeholder="请输入内容" v-model="description"></el-input>
            </el-col>
        </div>
        <div class="wrapper6"><!--上传及保存按钮 -->
            <el-upload
                class="upload-demo"
                action="https://jsonplaceholder.typicode.com/posts/"
                :on-preview="handlePreview"
                :on-remove="handleRemove"
                :before-remove="beforeRemove"
                multiple
                :limit="3"
                :on-exceed="handleExceed"
                :file-list="fileList">
                <el-button size="small" type="primary">点击上传</el-button>
                <div slot="tip" class="el-upload__tip">请上传XML文件</div>
            </el-upload><br><br><br>
            <el-button style="display:block;margin:0 auto" @click="savegen">保存</el-button>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                fileList: [],
                id: '',
                name: '',
                description: ''
            };
        },

        methods: {
            handleRemove(file, fileList) {
                console.log(file, fileList);
            },
            handlePreview(file) {
                console.log(file);
            },
            handleExceed(files, fileList) {
                this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
            },
            beforeRemove(file, fileList) {
                return this.$confirm(`确定移除 ${ file.name }？`);
            }
        }
    }
</script>


<style scoped>
    .wrapper6{
        position:relative;/*相对定位:参考物*/
        float:left;/*浮动:左浮动 与父元素的左端对齐 依次的往右端显示 一行显示不下就换行接着依次显示*/
        top:-15px;
        width:43%;
        height:350px;
        margin:18px 20px;
      
    }


    .lebal{
        position:relative;
        display: inline-block;
        padding:12px 0;
        color: #333;
    } 

</style>
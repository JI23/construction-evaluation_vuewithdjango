<template>
    <div>
        <div class="wrapper9" >
            <el-col>
                <span class="lebal">name</span>
                <el-input style="width:100%" v-model="name" placeholder="请输入内容"></el-input>
                <span class="lebal">median</span>
                <el-input  style="width:100%" v-model="median" placeholder="请输入内容"></el-input>
                <span class="lebal">dispersion</span>
                <el-input  style="width:100%" v-model="dispersion" placeholder="请输入内容"></el-input>
                <span class="lebal">description</span>
                <el-input style="width:100%" type="textarea" :rows="4" placeholder="请输入内容" v-model="description"></el-input>
            </el-col>
        </div>
        <div class="wrapper9">
            <el-upload
                class="upload-demo"
                action="https://jsonplaceholder.typicode.com/posts/"
                :on-preview="handlePreview"
                :on-remove="handleRemove"
                :file-list="fileList2"
                list-type="picture">
                <el-button @click="addone" v-if="temp < 2" size="small" type="primary">点击上传</el-button>
                <el-button disabled v-if="temp >= 2" size="small" type="primary">点击上传</el-button>
                <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
            </el-upload><br><br>
            <el-button style="display:block;margin:0 auto" @click="savegen">保存</el-button>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                fileList2: [],
                data: [{
                }],
                description: '',
                name: '',
                median: '',
                dispersion: '',
                temp: '0',
            }
        },

        mounted: function () {
            var vm = this
            // 用$on事件来接收参数
            var label = JSON.parse(localStorage.getItem("label"));
            //console.log(label)
            var temp = label.substring(13,14)
            console.log(temp)
            localStorage.removeItem("label");
        },

        methods: {
            savegen(){
                var statenum_info = {
                    name: this.name, 
                    median: this.median, 
                    dispersion: this.dispersion,
                    description: this.description,
                };
                localStorage.setItem("statenum_info",JSON.stringify(statenum_info));
            },
            handleRemove(file, fileList) {
                console.log(file, fileList);
                this.temp--
            },
            handlePreview(file) {
                console.log(file);
            },
            addone(){
                this.temp++
                console.log(this.temp)
            }
        }
  }
</script>


<style scoped>
  .wrapper9{
    position:relative;/*相对定位:参考物*/
    float:left;/*浮动:左浮动 与父元素的左端对齐 依次的往右端显示 一行显示不下就换行接着依次显示*/
    top:10px;
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
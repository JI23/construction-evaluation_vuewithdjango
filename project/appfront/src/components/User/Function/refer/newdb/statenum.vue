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
                action="http://localhost:8000/api/savegen_image"
                :data='image_data'
                :on-preview="handlePreview"
                :on-remove="handleRemove"
                :file-list="fileList2"
                list-type="picture"
                name='image'>
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
                image_data:{
                    path:localStorage.getItem('path'),
                    statenum:localStorage.getItem('statenum'),
                },
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
            //console.log(input+'!!!!!');
            //var tempdata = this.data[input];
            //this.newData[input] = tempdata;
            localStorage.removeItem("label");
        },

        methods: {
            savegen(){
                let _this=this;
                var statenum_info = {
                    name: this.name, 
                    median: this.median, 
                    dispersion: this.dispersion,
                    description: this.description,
                    DamageImageName:'null',
                };
                localStorage.setItem("statenum_info",JSON.stringify(statenum_info));
                this.$ajax({
                method:'get',
                url:'refer_check_statenum',
                params:{
                    username:localStorage.getItem('phone'),
                    path:localStorage.getItem('path'),
                    statenum:localStorage.getItem('statenum'),
                    statenum_info:statenum_info
                },
            })
            .then(function(response){
                console.log(response)
                var res = response.data
                console.log(res)
                if (res.error_num == 0) {
                    console.log(res['msg'])
                    console.log(res['DamageImageName'])
                    _this.$message.success(res['msg'])
                    statenum_info['DamageImageName']=res['DamageImageName']
                    localStorage.setItem("statenum_info",JSON.stringify(statenum_info));
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
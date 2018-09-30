<template>
    <div>
        <div class="wrapper9" >
            <el-col>
                <span class="lebal">损伤状态名称</span>
                <el-input v-bind:disabled="temp" style="width:100%" v-model="name" placeholder="请输入内容"></el-input>
                <span class="lebal">中位值</span>
                <el-input v-bind:disabled="temp" style="width:100%" v-model="median" placeholder="请输入内容"></el-input>
                <span class="lebal">对数方差</span>
                <el-input v-bind:disabled="temp" style="width:100%" v-model="dispersion" placeholder="请输入内容"></el-input>
                <span class="lebal">描述</span>
                <el-input v-bind:disabled="temp" style="width:100%" type="textarea" :rows="4" placeholder="请输入内容" v-model="description"></el-input>
            </el-col>
        </div>
        <div class="wrapper9">
            <el-upload
                v-bind:disabled="temp"
                class="upload-demo"
                action="/savegen_image"
                :data='image_data'
                :on-preview="handlePreview"
                :on-remove="handleRemove"
                :before-upload="test"
                :file-list="fileList"
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
                temp:false,
                image_data:{
                    path:sessionStorage.getItem('path'),
                    statenum:sessionStorage.getItem('statenum'),
                },
                fileList: [],
                data: [{
                }],
                description: '',
                name: '',
                median: '',
                dispersion: '',
                temp: '0',
                DamageImageName:''
            }
        },

        mounted: function () {
            var vm = this
            // 用$on事件来接收参数
            var label = JSON.parse(sessionStorage.getItem("label"));
            //console.log(label)
            var temp = label.substring(13,14)
            console.log(temp)
            sessionStorage.removeItem("label");
        },

        beforeRouteLeave(to, from, next){
            if(sessionStorage.getItem('check') === 'DB_User'){
                console.log(this.fileList)
                var statenum_info = {
                    name: this.name, 
                    median: this.median, 
                    dispersion: this.dispersion,
                    description: this.description,
                    DamageImageName:this.DamageImageName,
                };
                var temp = sessionStorage.getItem("statenum")
                sessionStorage.setItem(temp,JSON.stringify(statenum_info));
            }
            next()
        },

        created(){
            if(sessionStorage.getItem('check') === 'DB_User'){
                this.temp = false
            }
            else{
                this.temp = true
            }
            var temp = sessionStorage.getItem("statenum")
            try{
                var statenum_info=JSON.parse(sessionStorage.getItem(temp))
                this.name = statenum_info['name']
                this.median = statenum_info['median']
                this.dispersion = statenum_info['dispersion']
                this.description = statenum_info['description']
                var item = {
                    name: statenum_info['DamageImageName']
                }
                this.DamageImageName = statenum_info['DamageImageName']
                this.fileList.push(item)
                console.log('111')
                console.log(this.fileList)
                console.log('111')
            }
            catch(err){
                console.log(err)
            }
        },


        methods: {
            savegen(){
                console.log(this.$refs.check)
                this.$refs.check.disabled = true
                if(sessionStorage.getItem('check') === 'DB_User'){
                    let _this=this;
                    var statenum_info = {
                        name: this.name, 
                        median: this.median, 
                        dispersion: this.dispersion,
                        description: this.description,
                        DamageImageName:this.DamageImageName,
                    };
                    sessionStorage.setItem("statenum_info",JSON.stringify(statenum_info));
                    this.$ajax({
                        method:'get',
                        url:'refer_check_statenum',
                        params:{
                            username:localStorage.getItem('phone'),
                            path:sessionStorage.getItem('path'),
                            statenum:sessionStorage.getItem('statenum'),
                            statenum_info:statenum_info
                        },
                    }).then(function(response){
                        console.log(response)
                        var res = response.data
                        console.log(res)
                        if (res.error_num == 0) {
                            console.log(res['msg'])
                            console.log(res['DamageImageName'])
                            _this.$message.success(res['msg'])
                            statenum_info['DamageImageName']=res['DamageImageName']
                            sessionStorage.setItem("statenum_info",JSON.stringify(statenum_info));
                        } 
                        else {
                            _this.$message.error(res['msg'])
                            console.log(res['msg'])
                        }
                    }).catch(function(err){
                        console.log(err);
                    });
                }  
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
            },
            test(file){
                console.log(file.name)
                this.DamageImageName = file.name
            }
        }
  }
</script>


<style scoped>
    .wrapper9{
        position:relative;/*相对定位:参考物*/
        float:left;/*浮动:左浮动 与父元素的左端对齐 依次的往右端显示 一行显示不下就换行接着依次显示*/
        top:10px;
        width:40%;
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
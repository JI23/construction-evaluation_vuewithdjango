<template>
    <div>
        <div class="wrapper7" >
            <el-col>
                <span class="lebal">Data quality</span>
                <el-select v-model="data" placeholder="请选择">
                    <el-option
                        v-for="item in options1"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                </el-select>
                <span class="lebal">Data relevance</span>
                <el-select v-model="relevance" placeholder="请选择">
                    <el-option
                        v-for="item in options1"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                </el-select>

                <span class="lebal">Documentation quality</span>
                <el-select v-model="quality" placeholder="请选择">
                    <el-option
                        v-for="item in options1"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                </el-select>

                <span class="lebal">Rationality</span>
                <el-select v-model="rationality" placeholder="请选择">
                    <el-option
                        v-for="item in options1"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                </el-select>
            </el-col>
          </div>
        <div class="wrapper7">
            <el-col>
                <span class="lebal">作者</span>
                <el-input  style="width:100%" v-model="author" placeholder="请输入内容"></el-input>
                <span class="lebal">备注</span>
                <el-input style="width:100%" type="textarea" :rows="6" placeholder="请输入内容" v-model="notes"></el-input><br><br>
                <el-button style="display:block;margin:0 auto" @click="savegen">保存</el-button>
            </el-col>
      </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                options1: [{
                    value: '选项1',
                    label: 'N/A'
                }, {
                    value: '选项2',
                    label: 'Marginal'
                }, {
                    value: '选项3',
                    label: 'Average'
                }, {
                    value: '选项4',
                    label: 'Superior'
                }],
                data: '',
                relevance: '',
                quality: '',
                rationality: '',
                author: '',
                notes: '',
            }
          },

        methods: {
            savegen() {//保存当前页面内容
                var notes_info = {
                    data: this.data, 
                    relevance: this.relevance, 
                    quality: this.quality,
                    rationality: this.rationality,
                    author: this.author,
                    notes: this.notes,
                };
                localStorage.setItem("notes_info",JSON.stringify(notes_info));
                var gen_info=localStorage.getItem('gen_info')
                var username=localStorage.getItem('phone')
                console.log(gen_info)
                console.log(localStorage.getItem('notes_info'))
                console.log(username)
                //提交给后台若成功则弹窗提示并跳转至下一部分
                //记得删除localStorage内容
                this.$ajax({
                    method:'get',
                    url:'savegen',
                    params: {
                       gen_info:gen_info,
                       notes_info:JSON.stringify(notes_info),
                       username:username,
                    },
                })
                    .then(function(response){
                        console.log(response)
                        var res = response.data
                        if (res.error_num == 0) {
                            console.log('111')
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
        }
    }
</script>


<style>
    .wrapper7{
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
<template>
    <div>
        <div class="wrapper7" >
            <el-col>
                <span class="lebal">Data quality</span>
                <el-select v-bind:disabled="temp" v-model="data" placeholder="请选择">
                    <el-option
                        v-for="item in options1"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                </el-select>
                <span class="lebal">Data relevance</span>
                <el-select v-bind:disabled="temp" v-model="relevance" placeholder="请选择">
                    <el-option
                        v-for="item in options1"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                </el-select>

                <span class="lebal">Documentation quality</span>
                <el-select v-bind:disabled="temp" v-model="quality" placeholder="请选择">
                    <el-option
                        v-for="item in options1"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                </el-select>

                <span class="lebal">Rationality</span>
                <el-select v-bind:disabled="temp" v-model="rationality" placeholder="请选择">
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
                <el-input v-bind:disabled="temp" style="width:100%" v-model="author" placeholder="请输入内容"></el-input>
                <span class="lebal">备注</span>
                <el-input v-bind:disabled="temp" style="width:100%" type="textarea" :rows="6" placeholder="请输入内容" v-model="notes"></el-input><br><br>
                <el-button style="display:block;margin:0 auto" @click="savegen">保存</el-button>
            </el-col>
      </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                temp:false,
                options1: [{
                    value: 'N/A',
                    label: 'N/A'
                }, {
                    value: 'Marginal',
                    label: 'Marginal'
                }, {
                    value: 'Average',
                    label: 'Average'
                }, {
                    value: 'Superior',
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

        beforeRouteLeave(to, from, next){
            if(sessionStorage.getItem('check') === 'DB_User'){
                var notes_info = {
                    data: this.data, 
                    relevance: this.relevance, 
                    quality: this.quality,
                    rationality: this.rationality,
                    author: this.author,
                    notes: this.notes,
                };
                sessionStorage.setItem("notes_info",JSON.stringify(notes_info));
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
            try{
                var notes_info=JSON.parse(sessionStorage.getItem("notes_info"))
                this.data = notes_info['data']
                this.relevance = notes_info['relevance']
                this.quality = notes_info['quality']
                this.rationality = notes_info['rationality']
                this.author = notes_info['author']
                this.notes = notes_info['notes']
            }
            catch(err){
                //console.log(err)
            }
        },


        methods: {
            check(){
                this.$emit('check','');
            },
            savegen() {//保存当前页面内容
                if(sessionStorage.getItem('check') === 'DB_User'){
                    let _this=this;
                    var notes_info = {
                        data: this.data, 
                        relevance: this.relevance, 
                        quality: this.quality,
                        rationality: this.rationality,
                        author: this.author,
                        notes: this.notes,
                    };
                    sessionStorage.setItem("notes_info",JSON.stringify(notes_info));
                    var gen_info=sessionStorage.getItem('gen_info')
                    var username=sessionStorage.getItem('phone')
                    console.log(gen_info)
                    console.log(sessionStorage.getItem('notes_info'))
                    console.log(username)
                    if(sessionStorage.getItem('part_id')==null){
                        var part_id=0
                    }
                    else{ var part_id=sessionStorage.getItem('part_id')}
                    console.log(part_id)
                    //提交给后台若成功则弹窗提示并跳转至下一部分
                    //记得删除localStorage内容
                    this.$ajax({
                        method:'get',
                        url:'savegen',
                        params: {
                        gen_info:gen_info,
                        notes_info:JSON.stringify(notes_info),
                        username:username,
                        part_id:part_id,
                        },
                    }).then(function(response){
                        console.log(response)
                        var res = response.data
                        if (res.error_num == 0) {
                            sessionStorage.setItem('path',res['path'])
                            console.log(res['path'])
                            console.log(res['path2'])
                            sessionStorage.setItem('path2',res['path2'])
                            sessionStorage.setItem('part_id',res['part_id'])
                            console.log('111')
                            _this.$message.success(res['msg'])
                            _this.$router.push({name:'statenum'});
                            sessionStorage.setItem("statenum","Damage State 1");
                        } 
                        else {
                            _this.$message.error(res['msg'])
                            console.log(res['msg'])
                        }
                    }).catch(function(err){
                        console.log(err);
                    });
                }
                this.$router.push({name:'statenum'});
                sessionStorage.setItem("statenum","Damage State 1");
                
            },
        }
    }
</script>


<style>
    .wrapper7{
        position:relative;/*相对定位:参考物*/
        
        float:left;/*浮动:左浮动 与父元素的左端对齐 依次的往右端显示 一行显示不下就换行接着依次显示*/
        top:-15px;
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
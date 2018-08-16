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

                <span class="lebal">Documentation quailty</span>
                <el-select v-model="quailty" placeholder="请选择">
                    <el-option
                        v-for="item in options1"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                </el-select>

                <span class="lebal">Retionality</span>
                <el-select v-model="retionality" placeholder="请选择">
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
                <el-input  style="width:100%" v-model="auther" placeholder="请输入内容"></el-input>
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
                quailty: '',
                retionality: '',
                auther: '',
                notes: '',
            }
          },

        methods: {
            savegen() {//保存当前页面内容
                var notes_info = {
                    data: this.data, 
                    relevance: this.relevance, 
                    quailty: this.quailty,
                    retionality: this.retionality,
                    auther: this.auther,
                    notes: this.notes,
                };
                localStorage.setItem("notes_info",JSON.stringify(notes_info));
                //提交给后台若成功则弹窗提示并跳转至下一部分
                //记得删除localStorage内容
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
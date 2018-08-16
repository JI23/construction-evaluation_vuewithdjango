<!--开始前加载表格信息 search需提交内容在前端或后端进行搜索 -->
<template>
    <div class="demo-input-suffix">
        <el-row>
            <el-form>
                <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
                    <el-tab-pane label="已完成项目" name="success"></el-tab-pane>
                    <el-tab-pane label="未完成项目" name="unsuccess"></el-tab-pane>
                </el-tabs>
                <el-button style="float: right; top:-60px; position:relative;" @click="search">搜索</el-button>
                <el-input @keyup.enter="search()" style="width:150px ; float: right; top:-60px;left:-10px" placeholder="请输入内容" prefix-icon="el-icon-search" v-model="input"></el-input>
            </el-form>    
        </el-row><!--enter有问题-->
        <br>
        <router-view v-if="isRouteAlive"></router-view>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                input: '',
                activeName: 'success',
                isRouteAlive: true
            }
        },

        methods: {
            handleClick(tab, event){
                if(tab.name === "success"){
                    this.$router.push({name:'successpj'});
                }
                else if(tab.name === "unsuccess"){
                    this.$router.push({name:'unsuccesspj'});
                }
            },
            search(){
                this.reload();
                this.$router.push({name:this.$router.name});
                localStorage.setItem("input",JSON.stringify(this.input));
                this.reload();
            },
            reload(){
                this.isRouteAlive = false
                this.$nextTick(function(){
                    this.isRouteAlive = true
                })
            }
        }
  }
</script>

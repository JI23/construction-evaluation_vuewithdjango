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
                //与上面相同 只是获取的data不一样
                //console.log(this.$route.path)
                //console.log(this.input)
                //console.log(JSON.stringify({
                //    searchName: this.input,
                //}));
                if(this.$route.path === "/mypj/successpj"){
                    this.reload();
                    this.$router.push({name:'successpj'});
                    //this.$router.go(0);
                    //Bus.$emit('input', this.input)
                    //setTimeout(() => {
                    //    Bus.$emit('input', this.input)
                    //}, 1)
                    localStorage.setItem("input",JSON.stringify(this.input));
                    //var input2 = JSON.parse(localStorage.getItem("input"));
                    //console.log(input2+"!");
                    this.reload();
                }
                else if(this.$route.path === "/mypj/unsuccesspj"){
                    this.$router.push({name:'unsuccesspj'});
                    setTimeout(() => {
                        Bus.$emit('input', this.input)
                    }, 10)
                }
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

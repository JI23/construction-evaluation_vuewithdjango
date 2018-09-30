<template>
    <div>
        <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
            <el-tab-pane label="基本信息" name="gen_con_info"></el-tab-pane>
            <el-tab-pane label="修复成本" name="re_cost"></el-tab-pane>
            <el-tab-pane label="修复时间" name="re_time"></el-tab-pane>
        </el-tabs>
        <router-view></router-view>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                activeName: 'gen_con_info',
            }
        },

        watch:{
            "$route": "get_url"
        },
        
        beforeMount(){
            this.get_url()
        },

        mounted: function () {
            var vm = this
            // 用$on事件来接收参数
            var label = JSON.parse(sessionStorage.getItem("label"));
            
            sessionStorage.removeItem("label");
        },

        methods: {
            handleClick(tab, event){
                if(tab.name === "gen_con_info"){
                    this.$router.push({name:'gen_con_info'});
                }
                else if(tab.name === "re_cost"){
                    this.$router.push({name:'re_cost'});
                }
                else if(tab.name === "re_time"){
                    this.$router.push({name:'re_time'});
                }
                else if(tab.name === "others"){
                    this.$router.push({name:'others'});
                }
            },

            get_url(){
                let _this = this
                console.log(_this.activeName)
                //console.log(this.$route.path)
                var path1 = this.$route.path.split("/")
                console.log(path1)
                _this.activeName = path1[4]
            },

            check(){
                this.$emit('check','');
            },
            
        }
    }
</script>


<style scoped>

</style>
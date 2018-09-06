<template>
    <div>
        <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
            <el-tab-pane label="generalInfo" name="generalinfo"></el-tab-pane>
            <el-tab-pane label="notes" name="notes"></el-tab-pane>
        </el-tabs>
        <router-view></router-view>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                activeName: ''
            }
        },

        watch:{
            "$route": "get_url"
        },

        beforeMount(){
            this.get_url()
        },
        methods: {
            check(){
                this.$emit('check','');
            },
            handleClick(tab, event) {
                //console.log(tab, event);
                if(tab.name === "generalinfo"){
                    this.$router.push({name:'generalinfo'});
                }
                else if(tab.name === "notes"){
                    this.$router.push({name:'notes'});
                }
            },
            get_url(){
                let _this = this
                console.log(_this.activeName)
                //console.log(this.$route.path)
                var path1 = this.$route.path.split("/")
                console.log(path1)
                _this.activeName = path1[4]
            }
        }
    }
</script>
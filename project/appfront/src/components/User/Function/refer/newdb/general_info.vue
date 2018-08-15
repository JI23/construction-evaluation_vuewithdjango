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
                activeName: 'generalinfo'
            }
        },

        methods: {
            handleClick(tab, event) {
                //console.log(tab, event);
                if(tab.name === "generalinfo"){
                    this.$router.push({name:'generalinfo'});
                }
                else if(tab.name === "notes"){
                    this.$router.push({name:'notes'});
                }
            }
        }
    }
</script>
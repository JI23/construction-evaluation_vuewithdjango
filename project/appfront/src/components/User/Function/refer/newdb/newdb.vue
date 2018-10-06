<template>
    <div class="box">
        <el-card style="width:30%;">
            <el-tree  :expand-on-click-node="false" :default-expand-all="true" :data="data"  @node-click="handleNodeClick" ></el-tree>
        </el-card>
        <el-card style="width:68%;">
                <router-view @check="check" v-if="isRouteAlive"></router-view>
        </el-card>
    </div>
</template>

<script>    
    export default {
        data() {
            return {
                isRouteAlive:true,
                contentHasSave: false,//用于判断是否有修改
                data: [{  
                    label: 'General Info',
                    children: [{
                        label: 'Damage State Type',
                        children: [{
                            label: 'Damage State 1',
                            children: [{
                                label: 'Consequence Functions 1'
                            }],
                        }]
                    }],
                }, {
                    label: 'Add Damage State'
                }],
                data_temp: [{
                    label: 'Damage State 1',
                    children: [{
                        label: 'Consequence Functions'
                    }],
                }]
            }
        },

        created(){
            let _this = this
            var temp = sessionStorage.getItem('temp')
            for(var i = 0; i < temp-1; i++){
                this.data[0].children[0].children[i+1] = Object.assign({},this.data_temp[0]);
                this.data[0].children[0].children[i+1].label = 'Damage State '+(i+2);
                //console.log(this.data[0].children[0].children[temp-1].children[0].label)
                //console.log('!')
                this.data[0].children[0].children[i+1].children[0].label = 'Consequence Functions '+(i+2);
                this.data = JSON.parse(JSON.stringify(this.data));
            }
            console.log(_this.data)
            console.log('!!!!')
        },

        methods: {
            reload(){
                this.isRouteAlive = false
                this.$nextTick(function(){
                    this.isRouteAlive = true
                })
            },
            check(){
                this.$emit('check','');
            },
            check(){
                var temp = sessionStorage.getItem(check)
                if(temp === 'DB_User'){
                    return false
                }
                else{
                    return true
                }
            },
            handleNodeClick(data,node) {
                //console.log(data.$treeNodeId);
                if(data.label === 'General Info'){
                    this.$router.push({name:'general_info'});
                }
                else if(data.label === 'Damage State Type'){
                    this.$router.push({name:'damage_state'});
                }
                else if(data.label.substring(0,21) === 'Consequence Functions'){
                    this.$router.push({name:'consequence'});
                    console.log(data)
                    localStorage.setItem("functionnum",JSON.stringify(data.label));
                    this.reload()
                }
                else if(data.label === 'Add Damage State'){
                    var temp = this.data[0].children[0].children.length+1;
                    this.data[0].children[0].children[temp-1] = Object.assign({},this.data_temp[0]);
                    this.data[0].children[0].children[temp-1].label = '损伤状态'+temp;
                    //console.log(this.data[0].children[0].children[temp-1].children[0].label)
                    //console.log('!')
                    this.data[0].children[0].children[temp-1].children[0].label = 'Consequence Functions '+temp;
                    this.data = JSON.parse(JSON.stringify(this.data));
                    //console.log(this.data[0].children[0].children[2]);
                    //console.log(this.data[0].children[0].children);
                }
                else{
                    //this.reload()
                    //console.log(data.label.substring(0,20))
                    localStorage.setItem("statenum",JSON.stringify(data.label));
                    this.$router.push({name:'statenum'});
                    this.reload()
                }
            },
        },

        

        beforeRouteLeave (to, from , next) {
            const answer = window.confirm('当前页面可能还未保存，确定退出？(如已保存请忽略此提示)')
            if (answer) {
                if(to.name === 'step3' | to.name === 'step4'){
                    sessionStorage.clear()
                    localStorage.setItem('new_db_ret','false')
                }
                else{
                    var temp1 = localStorage.getItem('project')
                    var temp2 = localStorage.getItem('phone')
                    localStorage.clear()
                    sessionStorage.clear()
                    localStorage.setItem('project',0)
                    localStorage.setItem('phone',temp2)
                }
                next()
            } else {
                next(false)
            }
        }
  }
</script>


<style scoped>
    .box{
        height: 530px;
        width:100%;
    }
    .clearfix:after{
        display:block;
        content:'';
        clear:both;
    }
    .el-card{
        display: inline-block;
        height: 500px;
    }

</style>




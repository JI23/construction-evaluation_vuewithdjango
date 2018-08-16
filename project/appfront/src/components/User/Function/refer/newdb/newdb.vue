<template>
    <div class="box">
        <el-card style="width:30%;">
            <el-tree  :expand-on-click-node="false" :default-expand-all="true" :data="data"  @node-click="handleNodeClick" ></el-tree>
        </el-card>
        <el-card style="width:68%;">
            <router-view></router-view>
        </el-card>
    </div>
</template>

<script>    
    export default {
        data() {
            const data2 =  [{  
                label: 'General Info',
                children: [{
                    label: 'Damage State Type',
                    children: [{
                        label: 'Damage State 1',
                        children: [{
                            label: 'Consequence Functions'
                        }],
                    },{
                        label: 'Damage State 1',
                        children: [{
                            label: 'Consequence Functions'
                        }]
                    }]
                }],
            }, {
                label: 'Add Damage State'
            }];
            return {
                contentHasSave: false,//用于判断是否有修改
                data: [{  
                    label: 'General Info',
                    children: [{
                        label: 'Damage State Type',
                        children: [{
                            label: 'Damage State 1',
                            children: [{
                                label: 'Consequence Functions'
                            }],
                        },{
                            label: 'Damage State 1',
                            children: [{
                                label: 'Consequence Functions'
                            }]
                        }]
                    }],
                }, {
                    label: 'Add Damage State'
                }],
                data6: JSON.parse(JSON.stringify(data2)), 
            }
        },

        methods: {
            handleNodeClick(data,node) {
                console.log(data.$treeNodeId);
                if(data.label === 'General Info'){
                    this.$router.push({name:'general_info'});
                }
                else if(data.label === 'Damage State Type'){
                    this.$router.push({name:'damage_state'});
                }
                else if(data.label === 'Consequence Functions'){
                    this.$router.push({name:'consequence'});
                    console.log(data)
                    localStorage.setItem("label",JSON.stringify(data.label));
                }
                else if(data.label === 'Add Damage State'){
                    var temp = this.data[0].children[0].children.length+1;
                    this.data[0].children[0].children[temp-1] = Object.assign({},this.data[0].children[0].children[0]);
                    this.data[0].children[0].children[temp-1].label = 'Damage Step'+temp;
                    this.data = JSON.parse(JSON.stringify(this.data));
                    //console.log(this.data[0].children[0].children[2]);
                    //console.log(this.data[0].children[0].children);
                }
                else{
                    this.$router.push({name:'statenum'});
                    localStorage.setItem("label",JSON.stringify(data.label));
                }
            }
        },

        beforeRouteLeave (to, from , next) {
            const answer = window.confirm('Do you really want to leave? you have unsaved changes!')
            if (answer) {
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




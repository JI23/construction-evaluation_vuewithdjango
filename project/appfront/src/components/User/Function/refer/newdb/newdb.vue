<template>
    <div class="box">
        <el-card style="width:30%;">
            <el-tree  :expand-on-click-node="false" :default-expand-all="true" :data="data"  @node-click="handleNodeClick" ></el-tree><br><br>
            <el-button @click="new_over" style="position:relative; float:right; left:-25%">建立完毕</el-button><br><br><br>
            <el-button @click="cancel_new" v-show="cancel_show" style="position:relative; float:right; left:-10%">取消新建易损性数据库</el-button>
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
                cancel_show:false,
                isRouteAlive:true,
                contentHasSave: false,//用于判断是否有修改
                data: [{  
                    label: '基本信息',
                    children: [{
                        label: '损伤状态',
                        children: [{
                            label: '损伤状态1',
                            children: [{
                                label: '结果函数1'
                            }],
                        }]
                    }],
                }, {
                    label: '添加损伤状态'
                }],
                data_temp: [{
                    label: '损伤状态1',
                    children: [{
                        label: '结果函数'
                    }],
                }]
            }
        },

        created(){
            let _this = this
            if(localStorage.getItem('new_db_ret') == 'true'){
                _this.cancel_show = true
            }
            var temp = sessionStorage.getItem('temp')
            for(var i = 0; i < temp-1; i++){
                this.data[0].children[0].children[i+1] = Object.assign({},this.data_temp[0]);
                this.data[0].children[0].children[i+1].label = '损伤状态'+(i+2);
                //console.log(this.data[0].children[0].children[temp-1].children[0].label)
                //console.log('!')
                this.data[0].children[0].children[i+1].children[0].label = '结果函数'+(i+2);
                this.data = JSON.parse(JSON.stringify(this.data));
            }
            //console.log(_this.data)
            //console.log('!!!!')
        },

        methods: {
            new_over(){
                //清缓存，返回
                if(localStorage.getItem('new_db_ret') == 'true'){
                    this.$router.push({name:'step3'});
                    localStorage.setItem('new_db_ret',false)
                }
                else{
                    this.$router.push({name:'refer'});
                }
            },
            cancel_new(){
                localStorage.setItem('new_db_ret',false)
                this.$router.push({name:'step3'});
            },
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
                if(data.label === '基本信息'){
                    this.$router.push({name:'general_info'});
                }
                else if(data.label === '损伤状态'){
                    this.$router.push({name:'damage_state'});
                }
                else if(data.label.indexOf('结果函数')>-1){
                    this.$router.push({name:'consequence'});
                    console.log(data)
                    sessionStorage.setItem("functionnum",JSON.stringify(data.label));
                    this.reload()
                }
                else if(data.label === '添加损伤状态'){
                    var temp = this.data[0].children[0].children.length+1;
                    this.data[0].children[0].children[temp-1] = Object.assign({},this.data_temp[0]);
                    this.data[0].children[0].children[temp-1].label = '损伤状态'+temp;
                    //console.log(this.data[0].children[0].children[temp-1].children[0].label)
                    //console.log('!')
                    this.data[0].children[0].children[temp-1].children[0].label = '结果函数'+temp;
                    this.data = JSON.parse(JSON.stringify(this.data));
                    //console.log(this.data[0].children[0].children[2]);
                    //console.log(this.data[0].children[0].children);
                }
                else{
                    //this.reload()
                    //console.log(data.label.substring(0,20))
                    sessionStorage.setItem("statenum",JSON.stringify(data.label));
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




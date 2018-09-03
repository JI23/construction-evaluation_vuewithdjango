<!-- 传入value4的值选择易损性数据库显示数据 -->
<template>
    <div>
        <el-main>
            <el-select @change="change_db" v-model="value4" placeholder="选择易损性数据库"><!--value4为选中内容 -->
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :value="item.label">
                </el-option>
            </el-select>
            <el-button style="float: right" round type="info" @click="write">新建易损性数据库</el-button>
            <div style="height:380px; position:relative; top:20px">
                <el-scrollbar class = "el-scrollbar">
                    <el-tree class="el-tree" :default-expand-all="true" :data="data"  @node-click="handleNodeClick" ></el-tree>
                </el-scrollbar>
            </div>
        </el-main>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                options: [{
                    value: 'DB_common',
                    label: 'DB_Common'
                }, {
                    value: 'DB_school',
                    label: 'DB_School'
                }, {
                    value: 'DB_hospital',
                    label: 'DB_Hospital'
                }, {
                    value: 'DB_user',
                    label: 'DB_User'
                }, {
                    value: 'DB_office',
                    label: 'DB_Office'
                }, {
                    value: 'DB_fEMA',
                    label: 'DB_FEMA'
                }],
                value4: 'DB_fema',
                data: []
            }
        },

        beforeMount(){
            this.change_view()
        },

        methods: {
            handleNodeClick(data,node){
                //console.log(data);
                if(node.level == 3){
                    this.$router.push({name:'generalinfo'});
                    console.log(node);
                    localStorage.setItem("label",JSON.stringify(data.label));
                     
                }
            },

            handleClose(done) {
                this.$confirm('确认关闭？')
                .then(_ => {
                    done();
                })
                .catch(_ => {});
            },

            write(){
                this.$router.push({name:'newdb'});
            },
            change_db(){
                this.change_view()
            },
            change_view(){
                let _this=this
                this.$ajax({
                    method:'get',
                    url:'step3-get-all-parts',
                    params:{
                        value: this.value4
                    },
                    headers:{"Content-Type": "application/json"}
                }).then(function(response){
                    //console.log(response)
                    //console.log('111')
                    var res=response.data
                    if(res.error_num==0){
                        //console.log(res['list'])
                        var returnData = []
                        for(var i = 0; i < res['first'].length; i++){
                            var temp = {
                                label: "",
                                children: []
                            }
                            temp.label=res['first'][i]
                            for(var j = 0; j < res['second'].length; j++){
                                if(res['first'][i] === res['second'][j][0]){
                                    var item = {
                                        label: res['second'][j][1],
                                        children: []
                                    }
                                    for(var k = 0; k < res['list'].length; k++){
                                        if(res['list'][k].fields.second === res['second'][j][1]){
                                            var item1 = {
                                                label: res['list'][k].fields.part_id + " " + res['list'][k].fields.part_name + " " + res['list'][k].fields.description,
                                                children:[]
                                            }
                                            item.children.push(item1)
                                        }
                                    }
                                    temp.children.push(item)
                                }
                            }
                            returnData.push(temp)
                        }
                        console.log(returnData)
                        _this.data=returnData
                    }
                    else {
                        _this.$message.error(res['msg'])
                        console.log(res['msg'])
                    }
                }).catch(function(err){
                    console.log(err);
                    console.log('!!')
                    console.log(_this.data)
                });
            },
        }
    }
</script>

<style scoped>
    .el-scrollbar{
        height: 100%
    }

    .el-scrollbar__wrap {
        overflow-x: hidden;
    }

    .el-tree{
        display:inline-block;
    }

</style>

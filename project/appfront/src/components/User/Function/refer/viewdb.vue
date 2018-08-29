<!-- 传入value4的值选择易损性数据库显示数据 -->
<template>
    <div>
        <el-main>
            <el-select @change="change_db" v-model="value4" clearable placeholder="选择易损性数据库"><!--value4为选中内容 -->
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :value="item.label">
                </el-option>
              </el-select>
            <el-button style="float: right" round type="info" @click="dialogVisible = true">新建易损性数据库</el-button>
            <el-dialog
                title="新建易损性数据库"
                :visible.sync="dialogVisible"
                width="30%"
                :before-close="handleClose">
                <span slot="footer" class="dialog-footer">
                    <el-button @click="upload_xml">上传xml文件</el-button>
                    <el-button type="primary" @click="write">手动填写</el-button>
                </span>
            </el-dialog>
            <div style="height:380px; overflow:scroll; position:relative; top:20px">
                <el-tree :default-expand-all="true" :data="data"  @node-click="handleNodeClick" ></el-tree>
            </div>
        </el-main>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                dialogVisible: false,
                options: [{
                    value: 'DB_Common',
                    label: 'DB_Common'
                }, {
                    value: 'DB_School',
                    label: 'DB_School'
                }, {
                    value: 'DB_Hospital',
                    label: 'DB_Hospital'
                }, {
                    value: 'DB_User',
                    label: 'DB_User'
                }, {
                    value: 'DB_Office',
                    label: 'DB_Office'
                }, {
                    value: 'DB_FEMA',
                    label: 'DB_FEMA'
                }],
                value4: '',
                data: [{
                    label: 'A - Substructure',
                    children: [{
                        label: 'A10 - Foundtions',
                        children:[{
                            label: 'A101 - Standard Foundations',
                            children: [{
                                label: 'A1011 - Wall Foundations',
                            },{
                                label: 'A1012 - Wall Foundations',
                            }]
                        },{
                            label: 'A102 - Special Foundations'
                        }]   
                    }],
                  }]
            }
        },

        beforeMount(){
            this.change_view()
        },

        methods: {
            handleNodeClick(data,node){
                //console.log(data);
                if(node.level > 3){
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

            upload_xml(){
                this.dialogVisible = false
                this.$router.push({name:'uploadXML'});
            },

            write(){
                this.dialogVisible = false;
                this.$router.push({name:'newdb'});
            },
            change_db(){
                this.change_view()
            },
            change_view(){
                //获取数据库信息并显示
            }


        }
    }
</script>
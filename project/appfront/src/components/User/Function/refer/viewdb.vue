<!-- 传入value4的值选择易损性数据库显示数据 -->
<template>
    <div>
        <el-main>
            <el-select v-model="value4" clearable placeholder="选择易损性数据库"><!--value4为选中内容 -->
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :value="item.label">
                </el-option>
              </el-select>
            <el-button style="float: right" type="info" round @click="newdb">新建易损性数据库</el-button>
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
                options: [{
                    value: '选项1',
                    label: 'DB_Common'
                }, {
                    value: '选项2',
                    label: 'DB_School'
                }, {
                    value: '选项3',
                    label: 'DB_Hospital'
                }, {
                    value: '选项4',
                    label: 'DB_User'
                }, {
                    value: '选项5',
                    label: 'DB_Office'
                }, {
                    value: '选项6',
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

      methods: {
          newdb(){
              this.$router.push({name:'newdb'});
          },
          handleNodeClick(data,node){
              //console.log(data);
              if(node.level > 3){
                  this.$router.push({name:'generalinfo'});
                  console.log(node);
                  localStorage.setItem("label",JSON.stringify(data.label));
                  
              }
          }
      }
    }
</script>
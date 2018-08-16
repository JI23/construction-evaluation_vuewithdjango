<template>
    <div>
        <el-row>
            <el-button size="small" class='btn' @click="next">下一步</el-button>
            <el-button size="small" class='btn' @click="back">上一步</el-button>
        </el-row>
        <el-col :span="8" class="step5">
            <span class="lebal">设防烈度</span>
                <el-select v-model="defense_intensity" placeholder="请选择">
                    <el-option
                    v-for="item in defense_in_option"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
            <span class="lebal">场地类别</span>
                <el-select v-model="site_type" placeholder="请选择">
                    <el-option
                    v-for="item in site_type_option"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
            <span class="lebal">地震波数</span>
            <el-input v-model="number" placeholder="请输入内容"></el-input>
            <span class="lebal">地震分组</span>
                <el-select v-model="group" placeholder="请选择">
                    <el-option
                    v-for="item in group_option"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
            <span class="lebal">峰值加速度</span>
            <el-input v-model="peak_acceleration" placeholder="请输入内容"></el-input>
            <span class="lebal">地震水准</span>
                <el-select v-model="earthquake_level" placeholder="请选择">
                    <el-option
                    v-for="item in earth_level_option"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
        </el-col>
        <el-col :span="1" style="color:transparent">''</el-col>
        <el-col :span="15">
            <el-table :data="earthquake_info" border style="width:100%" max-height="350">
                <el-table-column prop="earthquake_no" label="地震波编号">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.earthquake_no"></el-input>
                    </template>
                </el-table-column>
                <el-table-column prop="name" label="地震波名称">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.name"></el-input>
                    </template>
                </el-table-column>
                <el-table-column prop="peak" label="地震波峰值">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.peak"></el-input>
                    </template>
                </el-table-column>
                <el-table-column prop="file" label="地震波文件">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.file"></el-input>
                    </template>
                </el-table-column>
                <el-table-column
                    fixed="right"
                    label="操作"
                    width="120">
                    <template slot-scope="scope">
                        <el-button
                        @click.native.prevent="deleteRow(scope.$index, earthquake_info)"
                        type="text"
                        size="small">
                        移除
                        </el-button>
                    </template>
                </el-table-column>
            </el-table> 
            <el-button @click="newEarthquake">新增地震波</el-button>
        </el-col>
    </div>
</template>
<script>
export default {
    methods:{
        newEarthquake(){
            this.earthquake_info.push({
                earthquake_no: '',
                name: '',
                peak:'',
                file:''
            })
        
        },
        deleteRow(index, rows) {
            rows.splice(index, 1);
        },
        next(){
            this.$emit('next','');
        },
        back(){
            this.$emit('back','');
        }
    },
    data(){
        return{
            defense_intensity:'',
            defense_in_option:[{
                    value: 1,
                    label: '6度'
                }, {
                    value: 2,
                    label: '7度(0.1g)'
                }, {
                    value: 3,
                    label: '8度(0.15g)'
                }, {
                    value: 4,
                    label: '8度(0.2g)'
                }, {
                    value: 5,
                    label: '8度(0.3g)'
                },{
                    value: 6,
                    label: '9度'
                },
            ],
            site_type:null,
            site_type_option:[{
                    value: 1,
                    label: 'Ⅰ_0'
                }, {
                    value: 2,
                    label: 'Ⅰ_1'
                }, {
                    value: 3,
                    label: 'Ⅱ'
                }, {
                    value: 4,
                    label: 'Ⅲ'
                }, {
                    value: 5,
                    label: 'Ⅳ'
                }],
            number:null,
            group:null,
            group_option:[{
                    value: 1,
                    label: '第一组'
                }, {
                    value: 2,
                    label: '第二组'
                }, {
                    value: 3,
                    label: '第三组'
                }],
            peak_acceleration:null,
            earthquake_level:null,
            earth_level_option:[{
                    value: 1,
                    label: '多遇地震'
                }, {
                    value: 2,
                    label: '设防地震'
                }, {
                    value: 3,
                    label: '罕遇地震'
            }],
            earthquake_info: [{
                earthquake_no: '',
                name: '',
                peak:'',
                file:'',
            }]
        }
    }
}
</script>

<style scoped>

    .lebal{
        display: inline-block;
        padding:10px 0 5px 0;
        color: #333;
        font-size:14px;
    }
    
    .el-table{

        margin:10px 0;

    }
    .step5 .el-select{
        width:300px;
        display: block;
    }
    .step5 .el-input{
        width:300px;
        display: block;
    }
    .btn{
        margin-top:12px;
    }
    
    

</style>

<template>
    <div>
        <el-row>
            <el-button size="small" class='btn' @click="next">下一步</el-button>
            <el-button size="small" class='btn' @click="back">上一步</el-button>
            <el-button size="small" class='btn' @click="save5">保存地震信息</el-button>
        </el-row>
        <el-col :span="24" class="step5">
            <el-col :span='8'>
                <span class="lebal">设防烈度</span>
                <el-select style="width:90%" @change="change_level" v-model="defense_intensity" placeholder="请选择">
                    <el-option
                    v-for="item in defense_in_option"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
                <span class="lebal">场地类别</span>
                    <el-select style="width:90%" v-model="site_type" placeholder="请选择">
                        <el-option
                        v-for="item in site_type_option"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                        </el-option>
                    </el-select>
            </el-col>
            <el-col :span='8'>
                <span class="lebal">地震波数</span>
                <el-input style="width:90%" v-model="number" placeholder="请输入内容"></el-input>
                <span class="lebal">地震分组</span>
                <el-select style="width:90%" v-model="group" placeholder="请选择">
                    <el-option
                    v-for="item in group_option"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
                
            </el-col>
            <el-col :span='8'>
                <span class="lebal">峰值加速度</span>
                <el-input style="width:90%" :disabled="true" v-model="peak_acceleration" placeholder="请输入内容"></el-input>
                <span class="lebal">地震水准</span>
                <el-select style="width:90%" @change="change_level" v-model="earthquake_level" placeholder="请选择">
                    <el-option
                    v-for="item in earth_level_option"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
            </el-col>
            
            
        </el-col>
        <!--<el-col :span="1" style="color:transparent">''</el-col>-->
        <el-col :span="24">
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
                        <el-upload
                            class="upload-demo"
                            ref="upload"
                            action="http://localhost:8000/api/show_projects"
                            :on-preview="handlePreview"
                            :on-remove="handleRemove"
                            :file-list="fileList"
                            :auto-upload="false"
                            name="test"><!--这里是命名-->
                            <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
                            <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
                        </el-upload>
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
            <el-button @click="saveWaves">保存所有地震波</el-button>
        </el-col>
    </div>
</template>
<script>
export default {
    beforeRouteLeave(to, from, next){
        let defense_intensity = JSON.stringify(this.defense_intensity)
        sessionStorage.setItem('defense_intensity', defense_intensity)
        let site_type = JSON.stringify(this.site_type)
        sessionStorage.setItem('site_type', site_type)
        let number = JSON.stringify(this.number)
        sessionStorage.setItem('number', number)
        let group = JSON.stringify(this.group)
        sessionStorage.setItem('group', group)
        let peak_acceleration = JSON.stringify(this.peak_acceleration)
        sessionStorage.setItem('peak_acceleration', peak_acceleration)
        let earthquake_level = JSON.stringify(this.earthquake_level)
        sessionStorage.setItem('earthquake_level', earthquake_level)
        let earthquake_info = JSON.stringify(this.earthquake_info)
        sessionStorage.setItem('earthquake_info', earthquake_info)
        next()
    },
    created(){
      //从localStorage中读取条件并赋值给查询表单
        let defense_intensity = sessionStorage.getItem('defense_intensity')
        if (defense_intensity != null) {
            this.defense_intensity = JSON.parse(defense_intensity)
        }
        let site_type = sessionStorage.getItem('site_type')
        if (site_type != null) {
            this.site_type = JSON.parse(site_type)
        }
        let number = sessionStorage.getItem('number')
        if (number != null) {
            this.number = JSON.parse(number)
        }
        let group = sessionStorage.getItem('group')
        if (group != null) {
            this.group = JSON.parse(group)
        }
        let peak_acceleration = sessionStorage.getItem('peak_acceleration')
        if (peak_acceleration != null) {
            this.peak_acceleration = JSON.parse(peak_acceleration)
        }
        let earthquake_level = sessionStorage.getItem('earthquake_level')
        if (earthquake_level != null) {
            this.earthquake_level = JSON.parse(earthquake_level)
        }
        let earthquake_info = sessionStorage.getItem('earthquake_info')
        if (earthquake_info != null) {
            this.earthquake_info = JSON.parse(earthquake_info)
        }
    },
    methods:{
        newEarthquake(){
            this.earthquake_info.push({
                earthquake_no: '',
                name: '',
                peak:'',
                file:''
            })        
        },
        saveWaves(){
            let _this=this;
            var project=localStorage.getItem('project')
            console.log(this.earthquake_info)
            this.$ajax({
                method:'get',
                url:'step5-save-waves',
                params:{
                    earthquake_info:this.earthquake_info,
                    project:project,
                },
            })
            .then(function(response){
                console.log(response)
                var res = response.data
                console.log(res)
                if (res.error_num == 0) {
                    console.log(res['msg'])
                } 
                else {
                    _this.$message.error('存储地震波信息失败')
                    console.log(res['msg'])
                }
            })
            .catch(function(err){
                    console.log(err);
                    });
        },
        save5(){
            let _this=this;
            console.log(this.defense_intensity)
            var project=localStorage.getItem('project')
            this.$ajax({
                method:'get',
                url:'step5',
                params:{
                    project:project,
                    defense_intensity:this.defense_intensity,
                    site_type:this.site_type,
                    number:this.number,
                    group:this.group,
                    peak_acceleration:this.peak_acceleration,
                    earthquake_level:this.earthquake_level
                },
                headers:{"Content-Type": "application/json"}
            })
            .then(function(response){
                console.log(response)
                var res=response.data
                if(res.error_num==0){
                    localStorage.setItem('number',_this.number)
                    console.log(res['msg'])
                }
                else {
                    _this.$message.error('存储地震信息失败')
                    console.log(res['msg'])
                }
            })
            .catch(function(err){
                    console.log(err);
                    });
        },
        deleteRow(index, rows) {
            rows.splice(index, 1);
        },
        next(){
            this.$emit('next','');
        },
        back(){
            this.$emit('back','');
        },
        change_level(){
            //console.log('!')
            var array = new Array([0.18,0.5,1.25],[0.35,1,2.2],[0.5,1.5,3.1],[0.7,2,4],[1.1,3,5.1],[1.4,4,6.2])
            if(this.defense_intensity !== '' && this.earthquake_level !== null){
                console.log(this.defense_intensity)
                console.log(this.earthquake_level)
                this.peak_acceleration = array[this.defense_intensity-1][this.earthquake_level]
                console.log(this.peak_acceleration)
            }
        },
        submitUpload() {
            //console.log(this.fileList);
            this.$refs.upload.submit();
        },
        handleRemove(file, fileList) {
            console.log(file, fileList);
        },
        handlePreview(file, fileList) {
            console.log(file, fileList);
        }
    },
    data(){
        return{
            fileList: [],
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

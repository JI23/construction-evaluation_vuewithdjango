<template>
    <div>
        <el-row style="padding:10px">
            <el-button size="small" class='btn' @click="next">下一步</el-button>
            <el-button size="small" class='btn' @click="back">上一步</el-button>
            <!-- <el-button size="small" class='btn' @click="save2">保存</el-button> -->
        </el-row>
        <el-row>
            <el-col :span="24" class="step2">
                <el-form :model="buildingForm" :rules="rules" label-width="80px" ref="buildingForm" label-position="right">
                    <el-col :span="6">
                            <el-form-item label="建筑材料" prop="material" >
                                <el-input style="width:90%" size='small' v-model="buildingForm.material" auto-complete="off" placeholder="请输入内容"></el-input>
                            </el-form-item>
                            <el-form-item label="结构类型" prop="structure_type" >
                                <el-input style="width:90%" size='small' v-model="buildingForm.structure_type" auto-complete="off" placeholder="请输入内容"></el-input>
                            </el-form-item>
                    </el-col>
                    <el-col :span='6'>
                        <el-form-item label="图审时间" prop="figure_time" >
                        <el-date-picker style="width:90%" type="date" size='small' value-format="yyyy-MM-dd" :picker-options="pickerOptions1" placeholder="请选择时间"  v-model="buildingForm.figure_time"></el-date-picker>
                        </el-form-item>
                        <!-- <el-form-item label="图审时间" prop="figure_time" > -->
                        <!-- <el-input style="width:90%" size='small' v-model="buildingForm.figure_time" auto-complete="off" placeholder="请输入内容"></el-input> -->
                        <!-- </el-form-item> -->
                        <el-form-item label="结构层数" prop="floors" >
                        <el-input  style="width:90%" size='small' @blur="set_num" v-model.number="buildingForm.floors" auto-complete="off" placeholder="请输入内容"></el-input>
                        </el-form-item>
                            <!-- <span class="lebal">图审时间</span>
                            <el-input style="width:90%" size='small' v-model="figure_time" placeholder="请输入内容"></el-input> -->
                            <!-- <span class="lebal">结构层数</span>
                            <el-input style="width:90%" size='small' v-model="floors"  @blur="set_num"  placeholder="请输入内容"></el-input> -->
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="结构高度" prop="height"  >
                        <el-input style="width:90%" size='small' v-model.number="buildingForm.height" auto-complete="off" placeholder="请输入内容"></el-input>
                        </el-form-item>
                        <el-form-item label="建筑面积" prop="area" >
                        <el-input  style="width:90%" size='small' v-model.number="buildingForm.area" auto-complete="off" placeholder="请输入内容"></el-input>
                        </el-form-item>                    
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="单位造价" prop="cost_per_squaremeter" >
                                <el-input size='small' v-model.number="buildingForm.cost_per_squaremeter" auto-complete="off" placeholder="请输入内容"></el-input>
                        </el-form-item>
                    </el-col>
            </el-form>
                <!-- <span class="lebal">结构高度(m)</span>
                <el-input style="width:90%" size='small' v-model="height" placeholder="请输入内容"></el-input>
                <span class="lebal">建筑面积(m^2)</span>
                <el-input style="width:90%" size='small' v-model="area" placeholder="请输入内容"></el-input>
                <span class="lebal">单位造价(元)</span>
                <el-input style="width:90%" size='small' v-model="cost_per_squaremeter" placeholder="请输入内容"></el-input> -->
            
            </el-col>
        </el-row> 
        <el-row>
            <el-col :span="24">
                <el-table :data="Floor_info" class="tb-edit" border style="width:80%" max-height="350" highlight-current-row :header-cell-style="rowClass" >
                    <el-table-column prop="floor_no" label="楼层" width="50" align="center">
                        <template slot-scope="scope">
                            <!-- <el-input v-model="scope.row.floor_no"></el-input> -->
                            <span >{{ scope.row.floor_no }}</span> 
                        </template>
                    </el-table-column>
                    <el-table-column prop="floor_height" label="楼层高度(m)" width="150">
                        <template slot-scope="scope">
                            <el-input size="small" v-model="scope.row.floor_height"></el-input><span>{{ scope.row.floor_height }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="floor_area" label="楼层面积(m^2)" width="150">
                        <template slot-scope="scope" >
                            <el-input size="small" style="border:none" v-model="scope.row.floor_area"></el-input><span>{{ scope.row.floor_area }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="influence_coefficient" label="楼层影响系数" width="150">
                        <template slot-scope="scope">
                            <el-input size="small" v-model="scope.row.influence_coefficient"></el-input><span>{{ scope.row.influence_coefficient }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column prop="population_density" label="楼层人口密度(人/m^2)" width="200">
                        <template slot-scope="scope">
                            <el-input size="small" v-model="scope.row.population_density"></el-input><span>{{ scope.row.population_density }}</span>
                        </template>
                    </el-table-column>
                    <el-table-column
                        fixed="right"
                        label="操作"
                        width="120">
                        <template slot-scope="scope">
                            <el-button
                            @click.native.prevent="deleteRow(scope.$index, Floor_info)"
                            type="text"
                            size="small">
                            移除
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table> 
            <!-- <el-button @click="newFloor">新增楼层</el-button> -->
        </el-col>
        </el-row>
        <!-- <el-col :span="" style="color:transparent">''</el-col> -->
       
        <!-- <el-button @click="saveFloor">保存所有楼层</el-button> -->
        
        
        
    
    
    </div>
</template>
<script>
export default {
    beforeRouteLeave(to, from, next){
        //非表单
        // let material = this.material
        // let structure_type = this.structure_type
        // let figure_time = this.figure_time
        // let floors = this.floors
        // let height = this.height
        // let area = this.area
        // let cost_per_squaremeter = this.cost_per_squaremeter
        //改成表单以后
        let material = this.buildingForm.material
        let structure_type = this.buildingForm.structure_type
        let figure_time = this.buildingForm.figure_time
        let floors = this.buildingForm.floors
        let height = this.buildingForm.height
        let area = this.buildingForm.area
        let cost_per_squaremeter = this.buildingForm.cost_per_squaremeter
        let Floor_info = JSON.stringify(this.Floor_info)
        // let floor_no = JSON.stringify(this.floor_no)
        // let floor_height = JSON.stringify(this.floor_height)
        // let floor_area = JSON.stringify(this.floor_area)
        // let influence_coefficient = JSON.stringify(this.influence_coefficient)
        // let population_density = JSON.stringify(this.population_density)
        localStorage.setItem('material', material)
        localStorage.setItem('structure_type', structure_type)
        localStorage.setItem('figure_time', figure_time)
        localStorage.setItem('floors', floors)
        localStorage.setItem('height', height)
        localStorage.setItem('area', area)
        localStorage.setItem('cost_per_squaremeter', cost_per_squaremeter)
        localStorage.setItem('Floor_info', Floor_info)
        next()
    },
    created(){
      //从localStorage中读取条件并赋值给查询表单
        let material = localStorage.getItem('material')
        let structure_type = localStorage.getItem('structure_type')
        let figure_time = localStorage.getItem('figure_time')
        let floors = localStorage.getItem('floors')
        let height = localStorage.getItem('height')
        let area = localStorage.getItem('area')
        let cost_per_squaremeter = localStorage.getItem('cost_per_squaremeter')
        let Floor_info = (localStorage.getItem('Floor_info'))
        //let Floor_info_test= JSON.prase(Floor_info)
        console.log(999999999999)
        console.log(Floor_info)
        // let floor_no = localStorage.getItem('floor_no')
        // let floor_height = localStorage.getItem('floor_height')
        // let floor_area = localStorage.getItem('floor_area')
        // let influence_coefficient = localStorage.getItem('influence_coefficient')
        // let population_density = localStorage.getItem('population_density')

        console.log('step2')
        
        if (material != null) {
            this.buildingForm.material = material
        }
        if (structure_type != null) {
            this.buildingForm.structure_type = structure_type
        }
        if (figure_time != null) {
            this.buildingForm.figure_time = figure_time
        }
        if (floors != null) {
            this.buildingForm.floors = floors
        }
        if (height != null) {
            this.buildingForm.height = height
        }
        if (area != null) {
            this.buildingForm.area = area
        }
        if (cost_per_squaremeter != null) {
            this.buildingForm.cost_per_squaremeter = cost_per_squaremeter
        }
        if (Floor_info!=null) {
            this.Floor_info = JSON.parse(Floor_info)
        }
    },

    
    methods:{
        // saveFloor(){
        //     let _this=this;
        //     var floors=localStorage.getItem('floors')
        //     var area=localStorage.getItem('area')
        //     var height=localStorage.getItem('height')
        //     var project=localStorage.getItem('project')
        //     this.$ajax({
        //         method:'get',
        //         url:'step2-saveFloor',
        //         params:{
        //             floors:floors,
        //             area:area,
        //             height:height,
        //             Floor_info:this.Floor_info,
        //             project:project,
        //         },
        //     })
        //     .then(function(response){
        //         console.log(response)
        //         var res = response.data
        //         console.log(res)
        //         if (res.error_num == 0) {
        //             console.log(res['msg'])
        //             _this.$message.success(res['msg'])
        //         } 
        //         else {
        //             _this.$message.error(res['msg'])
        //             console.log(res['msg'])
        //         }
        //     })
        //     .catch(function(err){
        //             console.log(err);
        //             });
        //},
        deleteRow(index, rows) {
            rows.splice(index, 1);
        },
        next(){
            let _this=this;
            var project=localStorage.getItem('project')
            this.$ajax({
                method:'get',
                url:'step2',
                params:{
                    project:project,
                    material:this.buildingForm.material,
                    structure_type:this.buildingForm.structure_type,
                    floors:this.buildingForm.floors,
                    figure_time:this.buildingForm.figure_time,
                    height:this.buildingForm.height,
                    area:this.buildingForm.area,
                    cost_per_squaremeter:this.buildingForm.cost_per_squaremeter,
                    Floor_info:this.Floor_info,
                },
            })
            .then(function(response){
                console.log(_this.buildingForm.figure_time)
                        console.log(response)
                        var res = response.data
                        console.log(res)
                        if (res.error_num == 0) {
                            console.log(res['msg'])
                            localStorage.setItem('floors',_this.buildingForm.floors)
                            localStorage.setItem('height',_this.buildingForm.height)
                            localStorage.setItem('area',_this.buildingForm.area)
                            _this.$message.success(res['msg'])
                            console.log(localStorage.getItem('project'))
                            setTimeout(()=>{
                                _this.$emit('next','');
                            },500)
                        } 
                        else {
                            _this.$message.error(res['msg'])
                            console.log(res['msg'])
                        }
                    })
                    .catch(function(err){
                        console.log(err);
                    });

            //this.$emit('next','');
        },
        back(){
            this.$emit('back','');
        },
        set_num(){
            this.Floor_info = [{
                floor_no:1,
                floor_height: '',
                floor_area:'',
                influence_coefficient:'',
                population_density:''
            }]
            console.log("set num")
            for(var i = 0; i < this.buildingForm.floors-1; i++){
                this.Floor_info.push({
                    floor_no:i+2,
                    floor_height: '',
                    floor_area:'',
                    influence_coefficient:'',
                    population_density:''
                })    
            }
        },
        rowClass(){
            return 'background:#eee'
        }
        // save2(){
        //     let _this=this;
        //     var project=localStorage.getItem('project')
        //     this.$ajax({
        //         method:'get',
        //         url:'step2',
        //         params:{
        //             project:project,
        //             material:this.buildingForm.material,
        //             structure_type:this.buildingForm.structure_type,
        //             floors:this.buildingForm.floors,
        //             figure_time:this.buildingForm.figure_time,
        //             height:this.buildingForm.height,
        //             area:this.buildingForm.area,
        //             cost_per_squaremeter:this.buildingForm.cost_per_squaremeter,
        //             Floor_info:this.Floor_info,
        //         },
        //     })
        //     .then(function(response){
        //                 console.log(response)
        //                 var res = response.data
        //                 console.log(res)
        //                 if (res.error_num == 0) {
        //                     console.log(res['msg'])
        //                     localStorage.setItem('floors',_this.buildingForm.floors)
        //                     localStorage.setItem('height',_this.buildingForm.height)
        //                     localStorage.setItem('area',_this.buildingForm.area)
        //                     _this.$message.success(res['msg'])
        //                     console.log(localStorage.getItem('project'))
        //                 } 
        //                 else {
        //                     _this.$message.error(res['msg'])
        //                     console.log(res['msg'])
        //                 }
        //             })
        //             .catch(function(err){
        //                 console.log(err);
        //             });
        //}
    },
    data(){
        return{
            pickerOptions1: {
        //   disabledDate(time) {
        //     return time.getTime() > Date.now();
        //   },
          shortcuts: [{
            text: '今天',
            onClick(picker) {
              picker.$emit('pick', new Date());
            }
          }, {
            text: '昨天',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24);
              picker.$emit('pick', date);
            }
          }, {
            text: '一周前',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', date);
            }
          }]
        },

            project_name:'',
            buildingForm:{
            material:'',
            structure_type:'',
            floors:'',
            figure_time:'',
            height:'',
            area:'',
            cost_per_squaremeter:'',},
            Floor_info: [{
                floor_no: '',
                floor_height: '',
                floor_area:'',
                influence_coefficient:'',
                population_density:''
            }],
            rules:{
                material:[{required:true, message: '请填写建筑材料', trigger: 'blur'}],
                structure_type:[{required:true, message: '请填写结构类型', trigger: 'blur'}],
                floors:[{required:true, message: '请填写结构层数',trigger:'blur'},{ type: 'number', min:0, max:100, message: '楼层必须为0到100的整数',trigger:'blur'}],
                height:[{ type: 'number', min:0, max:99999.99, message: '结构高度在0到99999.99之间',trigger:'blur'}],
                area:[{required:true, message: '请填写建筑面积',trigger:'blur'},{ type: 'number', min:0, max:9999.99, message: '建筑面积在0到9999.99之间',trigger:'blur'}],
                cost_per_squaremeter:[{ type: 'number', min:0, max:99999.99, message: '单位造价在0到99999.99之间',trigger:'blur'}]
            }
    }
}}
</script>

<style scoped>

    body {
        font-family: Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB, Microsoft YaHei, SimSun, sans-serif;
        overflow: auto;
        font-weight: 400;
        -webkit-font-smoothing: antialiased;
    }
    .tb-edit .el-input {
        display: none
    }
    .tb-edit .current-row .el-input {
        display: block
    }
    .tb-edit .current-row .el-input+span {
        display: none
    }
    
</style>

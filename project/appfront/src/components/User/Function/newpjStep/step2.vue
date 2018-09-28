<template>
    <div>
        <el-row>
            <el-button size="small" class='btn' @click="next">下一步</el-button>
            <el-button size="small" class='btn' @click="back">上一步</el-button>
            <el-button size="small" class='btn' @click="save2">保存</el-button>
        </el-row>
        <el-col :span="24" class="step2">
            <el-col :span="8">
                <span class="lebal">建筑材料</span>
                <el-input style="width:90%" size='small' v-model="material" placeholder="请输入内容"></el-input>
                <span class="lebal">结构类型</span>
                <el-input style="width:90%" size='small' v-model="structure_type" placeholder="请输入内容"></el-input>
            </el-col>
            <el-col :span='8'>
                <span class="lebal">图审时间</span>
                <el-input style="width:90%" size='small' v-model="figure_time" placeholder="请输入内容"></el-input>
                <span class="lebal">结构层数</span>
                <el-input style="width:90%" size='small' v-model="floors" placeholder="请输入内容"></el-input>
            </el-col>
            <el-col :span="8">
                <span class="lebal">结构高度(m)</span>
                <el-input style="width:90%" size='small' v-model="height" placeholder="请输入内容"></el-input>
                <span class="lebal">建筑面积(m^2)</span>
                <el-input style="width:90%" size='small' v-model="area" placeholder="请输入内容"></el-input>
                <span class="lebal">单位造价(元)</span>
                <el-input style="width:90%" size='small' v-model="cost_per_squaremeter" placeholder="请输入内容"></el-input>
            </el-col>
        </el-col>
        <el-col :span="1" style="color:transparent">''</el-col>
        <el-col :span="24">
            <el-table :data="Floor_info" border style="width:100%" max-height="350">
                <el-table-column prop="floor_no" label="楼层">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.floor_no"></el-input>
                    </template>
                </el-table-column>
                <el-table-column prop="floor_height" label="楼层高度(m)">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.floor_height"></el-input>
                    </template>
                </el-table-column>
                <el-table-column prop="floor_area" label="楼层面积(m^2)">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.floor_area"></el-input>
                    </template>
                </el-table-column>
                <el-table-column prop="influence_coefficient" label="楼层影响系数">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.influence_coefficient"></el-input>
                    </template>
                </el-table-column>
                <el-table-column prop="population_density" label="楼层人口密度(人/m^2)">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.population_density"></el-input>
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
            <el-button @click="newFloor">新增楼层</el-button>
        </el-col>
        <el-button @click="saveFloor">保存所有楼层</el-button>
    </div>
</template>
<script>
export default {
    beforeRouteLeave(to, from, next){
    //  if (to.name == 'step2') {
        let material = this.material
        let structure_type = this.structure_type
        let figure_time = this.figure_time
        let floors = this.floors
        let height = this.height
        let area = this.area
        let cost_per_squaremeter = this.cost_per_squaremeter
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
        // localStorage.setItem('floor_no', floor_no)
        // localStorage.setItem('floor_height', floor_height)
        // localStorage.setItem('floor_area', floor_area)
        // localStorage.setItem('influence_coefficient', influence_coefficient)
        // localStorage.setItem('population_density', population_density)

    //  }
    //   else{
    //     localStorage.removeItem('project_name')
    //     localStorage.removeItem('client_name')
    //     localStorage.removeItem('project_leader')
    //     localStorage.removeItem('project_description')
    //     console.log('到其他地方');
    //   }
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
            this.material = material
        }
        if (structure_type != null) {
            this.structure_type = structure_type
        }
        if (figure_time != null) {
            this.figure_time = figure_time
        }
        if (floors != null) {
            this.floors = floors
        }
        if (height != null) {
            this.height = height
        }
        if (area != null) {
            this.area = area
        }
        if (cost_per_squaremeter != null) {
            this.cost_per_squaremeter = cost_per_squaremeter
        }
        if (Floor_info!=null) {
            this.Floor_info = JSON.parse(Floor_info)
        }
        
        // if (floor_no != null) {
        //     console.log(floor_no)
        //     this.floor_no = JSON.parse(floor_no) 
        // }
        // if (floor_height != null) {
        //     console.log(floor_height)
        //     this.floor_height = JSON.parse(floor_height) 
        // }
        // if (floor_area != null) {
        //     console.log(floor_area)
        //     this.floor_area = JSON.parse(floor_area) 
        // }
        // if (influence_coefficient != null) {
        //     console.log(influence_coefficient)
        //     this.influence_coefficient = JSON.parse(influence_coefficient) 
        // }
        // if (population_density != null) {
        //     console.log(population_density)
        //     this.population_density = JSON.parse(population_density) 
        // }
    },

    
    methods:{
        newFloor(){
            this.Floor_info.push({
                floor_no:'',
                floor_height: '',
                floor_area:'',
                influence_coefficient:'',
                population_density:''
            })
        },
        saveFloor(){
            let _this=this;
            console.log(this.Floor_info)
            var floors=localStorage.getItem('floors')
            var area=localStorage.getItem('area')
            var height=localStorage.getItem('height')
            var project=localStorage.getItem('project')
            this.$ajax({
                method:'get',
                url:'step2-saveFloor',
                params:{
                    floors:floors,
                    area:area,
                    height:height,
                    Floor_info:this.Floor_info,
                    project:project,
                },
            })
            .then(function(response){
                console.log(response)
                var res = response.data
                console.log(res)
                if (res.error_num == 0) {
                    console.log(res['msg'])
                    _this.$message.success(res['msg'])
                } 
                else {
                    _this.$message.error(res['msg'])
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
        save2(){
            let _this=this;
            var project_name=localStorage.getItem('project_name')
            var project_leader=localStorage.getItem('project_leader')
            var project_description=localStorage.getItem('project_description')
            var client_name=localStorage.getItem('client_name')
            var project=localStorage.getItem('project')
            var username=localStorage.getItem('phone')
            console.log(project_name)
            this.$ajax({
                method:'get',
                url:'step2',
                params:{
                    username:username,
                    project:project,
                    project_name:project_name,
                    project_leader:project_leader,
                    project_description:project_description,
                    client_name:client_name,
                    material:this.material,
                    structure_type:this.structure_type,
                    floors:this.floors,
                    figure_time:this.figure_time,
                    height:this.height,
                    area:this.area,
                    cost_per_squaremeter:this.cost_per_squaremeter,
                },
            })
            .then(function(response){
                        console.log(response)
                        var res = response.data
                        console.log(res)
                        if (res.error_num == 0) {
                            console.log(res['msg'])
                            console.log(res['project'])
                            localStorage.setItem('project',res['project'])
                            localStorage.setItem('floors',_this.floors)
                            localStorage.setItem('height',_this.height)
                            localStorage.setItem('area',_this.area)
                            _this.$message.success(res['msg'])
                        } 
                        else {
                            _this.$message.error(res['msg'])
                            console.log(res['msg'])
                        }
                    })
                    .catch(function(err){
                        console.log(err);
                    });
        }
    },
    data(){
        return{
            project_name:'',
            material:'',
            structure_type:'',
            floors:'',
            figure_time:'',
            height:'',
            area:'',
            cost_per_squaremeter:'',
            Floor_info: [{
                floor_no: '',
                floor_height: '',
                floor_area:'',
                influence_coefficient:'',
                population_density:''
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
    .step2input{
        display: block;
        size:'small';
        margin:0 0 0 0;
    }
    .step2 .el-input{
        width:300px;
        display: block;
    }
    .el-table{

        margin:10px 0;

    }
    .btn{
        margin-top:12px;
    }
    
    

</style>

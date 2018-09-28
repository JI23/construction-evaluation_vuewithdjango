<template> 
    <div style="top:-73px; position:relative; height:400px; margin:18px 20px;">
        <el-table
            :data="projects.slice((currentPage-1)*pagesize,currentPage*pagesize)"
            border
            style="width: 100%">
            <el-table-column
                prop="create_time"
                label="日期"
                width="150">
            </el-table-column>
            <el-table-column
                prop="project_name"
                label="项目名称"
                width="120">
            </el-table-column>
            <el-table-column
                prop="id"
                label="项目编号"
                width="120">
            </el-table-column>
            <el-table-column
                prop="client_name"
                label="客户姓名"
                width="120">
            </el-table-column>
            <el-table-column
                prop="project_leader"
                label="项目负责人"
                width="120">
            </el-table-column>
            <el-table-column
                prop="rate"
                label="定级"
                width="120">
            </el-table-column>
            <el-table-column
                prop="project_description"
                label="项目说明"
                width="270">
            </el-table-column>

            <el-table-column
                fixed="right"
                label="操作"
                width="130">
            <template slot-scope="{row,$index}">
                <el-button @click="editpj($index,row)" type="text" size="small">编辑</el-button>
                <!-- <el-button @click="deletepj(scope.row)" type="text" size="small">删除</el-button> -->
                <el-button @click="deletepj($index,row)" type="text" size="small">删除</el-button>

            </template>
            </el-table-column>
        </el-table>
        <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="currentPage"
            :page-sizes="[5, 20, 50, 100]"
            :page-size="pagesize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="projects.length"
            style="text-align: center">
        </el-pagination>
    </div>
  
</template>

<script>
    export default {
        
        beforeMount: function() {
            this.showProjects()
        },

        methods:{
        //                 dateFormat:function(row, column) {
        //        var date = row[column.property];
        //   if (date == undefined) {
        //      return "";
        //   }
        //   return moment(date).format("YYYY-MM-DD HH:mm:ss");
        //     },
            handleSizeChange: function (size) {
                this.pagesize = size;
            },
            handleCurrentChange: function(currentPage){
                this.currentPage = currentPage;
            },
            editpj: function(index,row){
                localStorage.setItem("project",JSON.stringify(row.id));
                let project = localStorage.getItem('project');
                //console.log(project_name);
                //掉用setp1进行编辑
                //console.log(pjname)
                var username=localStorage.getItem('phone')
                this.$ajax({
                    method:'get',
                    url:'step0-edit',
                    params:{
                        username:username,
                        project:project
                    }
                }).then(function(response){
                    //判断后弹窗
                    var res = response.data
                    //step1
                    let project_name = res['base_info'][0].fields.project_name
                    let client_name = res['base_info'][0].fields.client_name
                    let project_leader = res['base_info'][0].fields.project_leader
                    let project_description = res['base_info'][0].fields.project_description
                    //step2
                    let material = res['base_info'][0].fields.material
                    let structure_type = res['base_info'][0].fields.structure_type
                    let figure_time = res['base_info'][0].fields.figure_time
                    let floors = res['base_info'][0].fields.floor
                    let height = res['base_info'][0].fields.height
                    let area = res['base_info'][0].fields.area
                    let cost_per_squaremeter = res['base_info'][0].fields.cost_per_squaremeter
                    let Floor_info=res['floor_info']
                    for(var i = 0; i < res['floor_info'].length; i++){
                                delete res['floor_info'][i].fields.project //删掉返回的project属性
                                Floor_info[i]=res['floor_info'][i].fields
                    } 
                    //step3
                    let structure_element=new Array
                    let j=0
                    for(var i = 0; i < res['element_info'].length; i++){
                                if(res['element_info'][i].element_type=='s')
                                {
                                    //delete res['element_info'][i].fields.project 
                                    delete res['element_info'][i].element_type
                                    //delete res['element_info'][i].fields.element
                                    structure_element[j]=res['element_info'][i]
                                    structure_element[j].id=res['element_info'][i].element__part_id
                                    delete structure_element[j].element__part_id
                                    j++
                                }
                    } 
                    structure_element=res['element_info']
                    structure_element=JSON.stringify(structure_element)
                    console.log('step3')
                    console.log(structure_element)
                    // //step4
                    // let non_structure_element=new Array
                    // let k=0
                    // for(var i = 0; i < res['element_info'].length; i++){
                    //             if(res['element_info'][i].fields.element_type=='n')
                    //             {
                    //                 delete res['element_info'][i].fields.project 
                    //                 delete res['element_info'][i].fields.element_type
                    //                 non_structure_element[k]=res['element_info'][i].fields
                    //                 k++
                    //             }
                    // } 
                    // non_structure_element=JSON.stringify(non_structure_element)
                    // console.log('step4')
                    // console.log(non_structure_element)
                    //step5
                    var defense_intensity=''
                    var site_type=''
                    var number=''
                    var group=''
                    var earthquake_level=''
                    console.log('step5')
                    if(res['earthquake_info']!='')
                    {
                        console.log('earthquake_info!=null')
                        let defense_intensity_temp=res['earthquake_info'][0].fields.defense_intensity
                        console.log('step5')
                        console.log(defense_intensity_temp)
                        var defense_intensity
                        if(defense_intensity_temp==1.0)
                            defense_intensity=1
                        else if(defense_intensity_temp==2.0)
                            defense_intensity=2
                        else if(defense_intensity_temp==3.0)
                            defense_intensity=3
                        else if(defense_intensity_temp==4.0)
                            defense_intensity=4
                        else if(defense_intensity_temp==5.0)
                            defense_intensity=5
                        else if(defense_intensity_temp==6.0)
                            defense_intensity=6
                        site_type=res['earthquake_info'][0].fields.site_type
                        number=res['earthquake_info'][0].fields.number
                        group=res['earthquake_info'][0].fields.group
                        //let peak_acceleration=JSON.stringify(res['earthquake_info'][0].fields.peak_acceleration)
                        //console.log(res['earthquake_info'][0].fields.earthquake_level)
                        earthquake_level=res['earthquake_info'][0].fields.earthquake_level
                    }
                    
                    //step6
                    console.log('step6')
                    console.log(res['structure_response'])
                    var structure_response=''
                    if(res['structure_response']!='')
                    {
                        console.log('structure_response不为空')
                        structure_response=res['structure_response']
                        for(var i = 0; i < res['structure_response'].length; i++){
                                    delete res['structure_response'][i].fields.project //删掉返回的project属性
                                    structure_response[i]=res['structure_response'][i].fields
                        }
                    }

                    
                    localStorage.removeItem('project_name')
                    localStorage.removeItem('project_leader')
                    localStorage.removeItem('project_description')
                    localStorage.removeItem('client_name')

                    localStorage.removeItem('material')
                    localStorage.removeItem('structure_type')
                    localStorage.removeItem('figure_time')
                    localStorage.removeItem('floors')
                    localStorage.removeItem('height')
                    localStorage.removeItem('area')
                    localStorage.removeItem('cost_per_squaremeter')
                    localStorage.removeItem('Floor_info')

                    localStorage.removeItem('structure_element')

                    localStorage.removeItem('non_structure_element')

                    localStorage.removeItem('defense_intensity')
                    localStorage.removeItem('site_type')
                    localStorage.removeItem('number')
                    localStorage.removeItem('group')
                    localStorage.removeItem('peak_acceleration')
                    localStorage.removeItem('earthquake_level')

                    localStorage.removeItem('structure_response')

                    //step1的
                    localStorage.setItem('project_name', project_name)
                    console.log('step1的project_name')
                    console.log(project_name)
                    localStorage.setItem('client_name', client_name)
                    localStorage.setItem('project_leader', project_leader)
                    localStorage.setItem('project_description', project_description)
                    //step2的
                    localStorage.setItem('material', material)
                    localStorage.setItem('structure_type', structure_type)
                    localStorage.setItem('figure_time', figure_time)
                    localStorage.setItem('floors', floors)
                    localStorage.setItem('height', height)
                    localStorage.setItem('area', area)
                    localStorage.setItem('cost_per_squaremeter', cost_per_squaremeter)
                    localStorage.setItem('Floor_info', JSON.stringify(Floor_info))//亲测表格好像只有转换成字符型才能显示
                    //step3
                    localStorage.setItem('structure_element', structure_element)
                    // //step4
                    // localStorage.setItem('non_structure_element',non_structure_element)
                    //step5
                    localStorage.setItem('defense_intensity',JSON.stringify(defense_intensity))
                    localStorage.setItem('site_type',JSON.stringify(site_type))
                    localStorage.setItem('number',JSON.stringify(number))
                    localStorage.setItem('group',JSON.stringify(group))
                    //localStorage.setItem('peak_acceleration',peak_acceleration)
                    localStorage.setItem('earthquake_level',JSON.stringify(earthquake_level))
                    //step6
                    localStorage.setItem('structure_response',JSON.stringify(structure_response))
                    let a=localStorage.getItem('structure_response')
                }).catch(function(err){
                    console.log(err)
                })
                //这里延迟跳转，不知道为啥执行起来是先跳到step1再 console.log('unsucess')了
                setTimeout(()=>{
                    this.$router.push({name:'step1'})
                },300)
                 
            },
            


            /*editpj: function(row){
                //console.log(row.value)
                localStorage.setItem("project_name",JSON.stringify(row.project_name));
                //this.$router.push({name:'step1'});
                console.log('111')
                var username=localStorage.getItem('phone')
                var project=row.id
                console.log(username)
                this.$ajax({
                    method:'get',
                    url:'step0-edit',
                    params:{
                        project:project,
                        username:username,
                    },
                }).then(function(response){
                    //判断后弹窗
                    var res=response.data
                    if (res.error_num==0){
                        
                        console.log(res['msg'])
                    }
                    else{
                        console.log(res['msg'])
                    }
                }).catch(function(err){
                    console.log(err)
                })
                //console.log(localStorage.getItem('pjNum'))
                //掉用setp1进行编辑
                //console.log("!!!")
            },*/
            deletepj: function(index,row){//未连接
                console.log('111')
                var username=localStorage.getItem('phone')
                var project=row.id
                this.$ajax({
                    method:'get',
                    url:'step0-delete',
                    params:{
                        project:project,
                        username:username,
                    }
                }).then(function(response){
                    //判断后弹窗
                    //this.reload()
                    var res=response.data
                    if (res.error_num==0){
                        console.log(2222)
                        console.log(res['msg'])
                    }
                    else{
                        console.log(res['msg'])
                    }
                }).catch(function(err){
                    console.log(err)
                })
            },
            reload(){
                this.isRouteAlive = false
                this.$nextTick(function(){
                    this.isRouteAlive = true
                })
            },
            showProjects(){
                let _this = this;
                var username=localStorage.getItem('phone');
                _this.input=localStorage.getItem('input')
                this.$ajax({
                    method:'get',
                    url:'show_projects',
                    params: {
                        'username': username,
                        'is_finished': 'False', 
                        'input':_this.input
                    },
                })
                    .then(function(response){
                        console.log(response)
                        var res = response.data
                        console.log(res)
                        if (res.error_num == 0) {
                            //console.log(res['list'][0].fields)
                            //_this.projects[0] = res['list'][0].fields
                            //_this.projects[1] = res['list'][1].fields
                            //vue.set(_this.projects[0],'',res['list'][0].fields);
                            _this.projects = res['list']
                            for(var i = 0; i < res['list'].length; i++){
                                var id=res['list'][i].pk
                                console.log(id)
                                _this.projects[i] = res['list'][i].fields
                                _this.projects[i].id=id
                            }
                            //_this.projects[0] = res['list'][0].fields
                            //_this.projects[1] = res['list'][1].fields
                            console.log(_this.projects)
                        } 
                        else {
                            _this.$message.error('查询项目失败')
                            console.log(res['msg'])
                        }
                    })
                    .catch(function(err){
                        console.log(err);
                    });
                /*this.$ajax.get('http://localhost:8000/api/show_projects')
                    .then(function(response){
                        console.log(response)
                        var res = JSON.parse(response.bodyText)
                        console.log(res)
                        if (res.error_num == 0) {
                            _this.projects = res['list']
                        } 
                        else {
                            _this.$message.error('查询项目失败')
                            console.log(res['msg'])
                        }
                    })
                    .catch(function(err){
                        console.log(err);
                    });*/
            },
        },

        data () {
            return {
                projects: [{create_time: '2016-05-03',
                    project_leader: '王小虎',
                    client_name:'王小五',
                    project_name: '上海',
                    id: 12,
                    rate: '上海市',
                    project_description: 200333},],
                currentPage:1,
                pagesize:5,
                isRouteAlive: true,
                input:''
            }
        } 
    }
</script>
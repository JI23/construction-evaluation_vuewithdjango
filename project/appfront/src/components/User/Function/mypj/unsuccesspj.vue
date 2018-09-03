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
<<<<<<< HEAD
            <template slot-scope="{row,$index}">
                <el-button @click="editpj($index,row)" type="text" size="small">编辑</el-button>
                <!-- <el-button @click="deletepj(scope.row)" type="text" size="small">删除</el-button> -->
                <el-button @click="deletepj($index,row)" type="text" size="small">删除</el-button>

=======
            <template slot-scope="scope">
                <el-button @click="editpj(index,scope.row)" type="text" size="small">编辑</el-button>
                <el-button @click="deletepj(scope.row)" type="text" size="small">删除</el-button>
>>>>>>> upstream/master
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
                    let project_name = JSON.stringify(res['base_info'][0].fields.project_name)
                    let client_name = JSON.stringify(res['base_info'][0].fields.client_name)
                    let project_leader = JSON.stringify(res['base_info'][0].fields.project_leader)
                    let project_description = JSON.stringify(res['base_info'][0].fields.project_description)
                    //step2
                    let material = JSON.stringify(res['base_info'][0].fields.material)
                    let structure_type = JSON.stringify(res['base_info'][0].fields.structure_type)
                    let figure_time = JSON.stringify(res['base_info'][0].fields.figure_time)
                    let floors = JSON.stringify(res['base_info'][0].fields.floor)
                    let height = JSON.stringify(res['base_info'][0].fields.height)
                    let area = JSON.stringify(res['base_info'][0].fields.area)
                    let cost_per_squaremeter = JSON.stringify(res['base_info'][0].fields.cost_per_squaremeter)
                    let Floor_info=res['floor_info']
                    //console.log(res['floor_info'][0].fields)
                    for(var i = 0; i < res['floor_info'].length; i++){
                                delete res['floor_info'][i].fields.project //删掉返回的project属性
                                Floor_info[i]=res['floor_info'][i].fields
                    } 
                    Floor_info=JSON.stringify(Floor_info)
                    //step3
                    let structure_element=new Array
                    let j=0
                    for(var i = 0; i < res['element_info'].length; i++){
                                if(res['element_info'][i].fields.element_type=='s')
                                {
                                    delete res['element_info'][i].fields.project 
                                    delete res['element_info'][i].fields.element_type
                                    //delete res['element_info'][i].fields.element
                                    structure_element[j]=res['element_info'][i].fields
                                    j++
                                }
                    } 
                    structure_element=JSON.stringify(structure_element)
                    console.log('step3')
                    console.log(structure_element)
                    //step4
                    let non_structure_element=new Array
                    let k=0
                    for(var i = 0; i < res['element_info'].length; i++){
                                if(res['element_info'][i].fields.element_type=='n')
                                {
                                    delete res['element_info'][i].fields.project 
                                    delete res['element_info'][i].fields.element_type
                                    non_structure_element[k]=res['element_info'][i].fields
                                    k++
                                }
                    } 
                    non_structure_element=JSON.stringify(non_structure_element)
                    console.log('step4')
                    console.log(non_structure_element)
                    //step5
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
                    let site_type=JSON.stringify(res['earthquake_info'][0].fields.site_type)
                    let number=JSON.stringify(res['earthquake_info'][0].fields.number)
                    let group=JSON.stringify(res['earthquake_info'][0].fields.group)
                    //let peak_acceleration=JSON.stringify(res['earthquake_info'][0].fields.peak_acceleration)
                    //console.log(res['earthquake_info'][0].fields.earthquake_level)
                    let earthquake_level=res['earthquake_info'][0].fields.earthquake_level
                    console.log(444)
                    console.log(earthquake_level)
                    //step6
                    let structure_response=res['structure_response']
                    // structure_response[0]=JSON.stringify(res['structure_response'][0].fields)
                    // structure_response[0]=JSON.stringify(res['structure_response'][0].fields)
                    for(var i = 0; i < res['structure_response'].length; i++){
                                delete res['structure_response'][i].fields.project //删掉返回的project属性
                                structure_response[i]=res['structure_response'][i].fields
                    }
                    console.log('step6')
                    console.log(structure_response)
                    //let structure_response=JSON.stringify(res['structure_response'][0].fields)
                    //console.log(structure_response)

                    sessionStorage.clear()
                    //step1的
                    sessionStorage.setItem('project_name', project_name)
                    sessionStorage.setItem('client_name', client_name)
                    sessionStorage.setItem('project_leader', project_leader)
                    sessionStorage.setItem('project_description', project_description)
                    //step2的
                    sessionStorage.setItem('material', material)
                    sessionStorage.setItem('structure_type', structure_type)
                    sessionStorage.setItem('figure_time', figure_time)
                    sessionStorage.setItem('floors', floors)
                    sessionStorage.setItem('height', height)
                    sessionStorage.setItem('area', area)
                    sessionStorage.setItem('cost_per_squaremeter', cost_per_squaremeter)
                    sessionStorage.setItem('Floor_info', Floor_info)
                    console.log('bbbbbbbbbbbbbbbbbbbb')
                    //step3
                    sessionStorage.setItem('structure_element', structure_element)
                    //step4
                    sessionStorage.setItem('non_structure_element',non_structure_element)
                    //step5
                    sessionStorage.setItem('defense_intensity',JSON.stringify(defense_intensity))
                    sessionStorage.setItem('site_type',site_type)
                    sessionStorage.setItem('number',number)
                    sessionStorage.setItem('group',group)
                    //sessionStorage.setItem('peak_acceleration',peak_acceleration)
                    sessionStorage.setItem('earthquake_level',earthquake_level)
                    //step6
                    sessionStorage.setItem('structure_response',JSON.stringify(structure_response))

                }).catch(function(err){
                    console.log(err)
                })
                //这里延迟跳转，不知道为啥执行起来是先跳到step1再 console.log('unsucess')了
                setTimeout(()=>{
                    this.$router.push({name:'step1'})
                },100)
                 
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
<<<<<<< HEAD
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
=======
                        project:row.id,
                        username:username
                    }
                }).then(function(response){
                    //判断后弹窗
                    var res = response.data
                    console.log(res['msg'])
>>>>>>> upstream/master
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

<<<<<<< HEAD
            // editpj: function(index,row){
            //     //this.$router.push({name:'step1'})
            //     localStorage.setItem("project",JSON.stringify(row.id));
            //     let project = localStorage.getItem('project');
            //     //console.log(project_name);
            //     //掉用setp1进行编辑
            //     //console.log(pjname)
            //     var username=localStorage.getItem('phone')
            //     this.$ajax({
            //         method:'get',
            //         url:'step0-edit',
            //         params:{
            //             username:username,
            //             project:project
            //         }}).then(function(response){
            //         //判断后弹窗
            //             var res = response.data
            //             //console.log(res['base_info'])
            //             //console.log(res['base_info'][0].fields.project_name)
            //             //var project_name=res['base_info'][0].fields.project_name
            //             //sessionStorage.removeItem('project_name')
            //             let project_name = JSON.stringify(res['base_info'][0].fields.project_name)
            //             sessionStorage.clear()
            //             sessionStorage.setItem('project_name', project_name)
            //             console.log('unsucess')
            //             console.log(project_name)
            //             //this.$router.push({name:'step1'})
            //         }).catch(function(err){
            //             console.log(err)
            //             //this.$router.push({name:'step1'})
            //         })
            //         //setTimeout(this.$router.push({name:'step1'}),3000)
            //         setTimeout(()=>{
            //             this.$router.push({name:'step1'})
            //         },1000)
            //     //this.$router.push({name:'step1'})
            //     //this.$router.go('/step1');
            //     },
=======
            
>>>>>>> upstream/master
            
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
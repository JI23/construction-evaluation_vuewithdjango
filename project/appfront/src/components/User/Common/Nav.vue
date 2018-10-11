<template>
    <el-col>
    <el-menu
        :default-active=activename
        class="el-menu-vertical-demo nav"
        background-color="#66209A"
        text-color="#eee"
        @select="test"
        active-text-color="#d49178">
        <el-menu-item index="/home">
            <span slot="title">首页</span>
        </el-menu-item>
        <el-menu-item index="/newpj">
            <span slot="title">新建项目</span>
        </el-menu-item>
        <el-menu-item index="/mypj">
            <span slot="title">我的项目</span>
        </el-menu-item>
        <el-menu-item index="/refer">
            <span slot="title">查看易损性数据库</span>
        </el-menu-item>
        <el-menu-item index="/feedbk">
            <span slot="title">反馈信息</span>
        </el-menu-item>
        <el-menu-item index="/userinfo">
            <span slot="title">个人信息</span>
        </el-menu-item>
        </el-menu>
    </el-col>
</template>

<script>
export default {
    beforeMount(){
        this.get_url()
    },
    methods:{
        get_url(){
            let _this = this
            //console.log(_this.activename)
            console.log(this.$route.path)
            var path1 = this.$route.path.split("/")
            //console.log('/'+path1[1])
            _this.activename = '/'+path1[1]
        },

        test(index, indexPath){
            var temp = this.$route.path.split('/')
            temp = temp[1]
            if(index=='/newpj' & temp == 'newpj'){
                this.$confirm('当前项目可能未保存，是否保存当前项目？', '确认信息', {
                    distinguishCancelAndClose: true,
                    confirmButtonText: '保存',
                    cancelButtonText: '放弃修改'
                    }).then(() => {
                        localStorage.setItem('project','0');
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
                        this.$router.push({name:'step1'})
                        //清除缓存发送保存请求
                        this.$message({
                        type: 'info',
                        message: '保存修改'
                        });
                    }).catch(action => {
                        if(action === 'cancel'){
                            localStorage.setItem('project','0');
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
                            this.$router.push({name:'step1'})
                            //sessionStorage.clear()
                            //localStorage.clear();
                        }
                        this.$message({
                            type: 'info',
                            message: action === 'cancel'
                                ? '放弃保存并离开页面'
                                : '停留在当前页面'
                        })
                  });
            }
            else{
                console.log(this.$route.path)
                index = index.split('/')
                index = index[1]
                this.$router.push({name:index})
            }
        }
    },
    data(){
        return{
            activename:this.$route.path
        }
    },
    watch:{
        "$route": "get_url"
    }
}
</script>


<style scoped>
    .nav{
        box-shadow: 0 2px 3px rgba(0, 0, 0, 0.3);
        margin:0 2px 0 5px;
        border-radius: 5px;
        font-weight: 400;
        height: 550px;    
    }
    
</style>

<template>
    <el-col>
    <el-menu
      :default-active=activename
      class="el-menu-vertical-demo nav"
      background-color="#66209A"
      text-color="#eee"
      @select="test"
      active-text-color="#d49178" router>
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
      console.log(index,indexPath)
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
        height: 600px;
    }
    
</style>

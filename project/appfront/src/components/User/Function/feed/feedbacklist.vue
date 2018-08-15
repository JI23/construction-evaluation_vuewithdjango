<template> 
  <div style="height:390px">
    <el-table  style="height: 240px; margin-bottom:20px"
      :data="tableData" border max-height="350">
      <el-table-column
        fixed
        prop="fbDate"
        label="日期"
        width="250">
      </el-table-column>
      <el-table-column
        prop="fbTitle"
        label="标题"
        width="250">
      </el-table-column>
      <el-table-column
        prop="fbStatus"
        label="状态"
        width="250">
      </el-table-column>
      <el-table-column
        label="操作"
        width="250">
        <template slot-scope="scope">
          <el-button @click="gotoFbDetail" type="text" size="small">查看详情</el-button>
          <el-button type="text" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      background
      layout="prev, pager, next"
      :total="50"
      style="maigin:20px">
    </el-pagination>
  
     <el-button type="primary" style="float:right; margin-top:55px" @click="gotoAddFb">新增反馈信息</el-button>
  </div>

</template>

<script>
  export default {
    methods: {
      gotoFbDetail()
      {
            this.$router.push({name:'fbdetail'});
      },
      gotoAddFb(){
            this.$router.push({name:'addfeedback'});
        }
    },

    data() {
      return {
        tableData: [{
          fbDate: '2016-05-03',
          fbTitle: '页面太丑',
          fbStatus: '已读',
        }, {
          fbDate: '2016-05-03',
          fbTitle: '页面太丑',
          fbStatus: '已读',
        }, {
          fbDate: '2016-05-03',
          fbTitle: '页面太丑',
          fbStatus: '已读',
        }, {
          fbDate: '2016-05-03',
          fbTitle: '页面太丑',
          fbStatus: '已读',
        }]
      }
    }
  }
</script>


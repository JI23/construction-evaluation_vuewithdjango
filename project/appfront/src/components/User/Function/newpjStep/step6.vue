<template>
    <div class="wrapper">
        <el-row>
            <el-button size="small" class='btn' @click="next">下一步</el-button>
            <el-button size="small" class='btn' @click="back">上一步</el-button>
        </el-row>
        <div class="clearfix">
            <el-col :span='11'>
            <span class="lebal">方向</span>
            <el-input v-model="data[0].direction" :disabled="true"></el-input>
            <span class="lebal">EDP类型</span><br>
            <el-select style="width:370px" v-model="data[0].EDP_type" placeholder="请选择">
                <el-option
                    v-for="item in EDP_option"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">                    
                </el-option>
            </el-select><br>
            <span class="lebal">楼层数量</span>
            <el-input v-model="data[0].floor_no" placeholder="请输入内容"></el-input>
            <span class="lebal">地震数量</span>
            <el-input v-model="data[0].earthquake_no" placeholder="请输入内容"></el-input>
            </el-col>
            <el-col :span="1" style="color:transparent">''</el-col>
            <el-col :span='11'>
                <span class="lebal">方向</span>
                <el-input v-model="data[1].direction" :disabled="true"></el-input>
                <span class="lebal">EDP类型</span><br>
                <!--<el-input v-model="data[1].EDP_type" placeholder="请输入内容"></el-input>-->
                <el-select style="width:370px" v-model="data[1].EDP_type" placeholder="请选择">
                    <el-option
                    v-for="item in EDP_option"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select><br>
                <span class="lebal">楼层数量</span>
                <el-input v-model="data[1].floor_no" placeholder="请输入内容"></el-input>
                <span class="lebal">地震数量</span>
                <el-input v-model="data[1].earthquake_no" placeholder="请输入内容"></el-input>
            </el-col>
        </div>
        <div class="btn-group">
            <el-button>点击预览</el-button>
            <el-button>提交并生成结果</el-button>
            <el-button @click="save6">保存</el-button>
        </div>
        
    </div>
</template>

<script>
export default {
    beforeRouteLeave(to, from, next){
        let structure_response = JSON.stringify(this.data)
        sessionStorage.setItem('structure_response', structure_response)
        next()
    },
    created(){
      //从localStorage中读取条件并赋值给查询表单
        let data = sessionStorage.getItem('structure_response')
        if (data != null) {
            this.data = JSON.parse(data)
        }
    },
    methods:{
        next(){
            this.$emit('next','');
        },
        back(){
            this.$emit('back','');
        },
        save6(){
            let _this=this;
            console.log(this.Floor_info)
            var project=localStorage.getItem('project')
            this.$ajax({
                method:'get',
                url:'step6',
                params:{
                    data:this.data,
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
    },
    data(){
        return {
            data:[{
                direction:'X',
                EDP_type:null,
                floor_no:null,
                earthquake_no:null
            },{
                direction:'Y',
                EDP_type:null,
                floor_no:null,
                earthquake_no:null
            }],
            EDP_option:[{
                value:'1',
                label: 'Story Drift Ratio/层间位移角',
            }, {
                value:'2',
                label: 'Acceleration/楼层加速度',
            }]
            
        }    
    }
}
</script>


<style scoped>
    .wrapper{  
        margin:10px auto;
        max-width:800px;
    }
    .lebal{
        display: inline-block;
        padding:12px 0;
        color: #333;
    }
    .btn-group{
        margin:15px 0;
    }
    .clearfix:after{
        content:'';
        display: block;
        clear: both;
    }
    .btn{
        margin-top:12px;
    }
</style>

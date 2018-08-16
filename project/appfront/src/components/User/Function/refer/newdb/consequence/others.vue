<template>
    <div>
        <div style="height:130px" class="wrapper3" >
            <el-col>
                <el-switch @change="changed" v-model="choose1" active-text="Possible Unsafe Placard Consequers" inactive-text=""></el-switch>
                <br>
                <span class="lebal">Fraction of Total Quanttities to Trigger Ubsafe Placard</span><br>
                <span>Median:</span>
                <el-input v-if="temp" style="width:35%" size="mini" placeholder="请输入内容" v-model="input1"></el-input>
                <el-input v-if="temp" style="width:35%;float:right" size="mini" placeholder="请输入内容" v-model="input2"></el-input>
                <el-input :disabled="true" v-if="!temp" style="width:35%" size="mini" placeholder="请输入内容" v-model="input1"></el-input>
                <el-input :disabled="true" v-if="!temp" style="width:35%;float:right" size="mini" placeholder="请输入内容" v-model="input2"></el-input>
                <span style="float:right">Dispersio:</span>
                <span>This fraction should relate to the total quantity from all Performance group in this damage state</span>
            </el-col>
        </div>
        <div style="height:130px" class="wrapper3">
            <span>Potential for Non-Collapse Casualties::ality Rate in Affected Area:</span>
            <br><span>Median:</span>
            <el-input style="width:35%" size="mini" placeholder="请输入内容" v-model="input3"></el-input>
            <el-input style="width:35%;float:right" size="mini" placeholder="请输入内容" v-model="input4"></el-input>
            <span style="float:right">Dispersio:</span>
            <span>Occupied Area Affected Per Performance Group Unit(sq.</span>
            <el-input style="width:20%" size="mini" placeholder="请输入内容" v-model="input5"></el-input>
            <span>Injury Rate in Affected Area:</span><br>
            <span>Median:</span>
            <el-input style="width:35%" size="mini" placeholder="请输入内容" v-model="input7"></el-input>
            <el-input style="width:35%;float:right" size="mini" placeholder="请输入内容" v-model="input8"></el-input>
            <span style="float:right">Dispersio:</span>
        </div>
        <div style="height:40px" class="box8">
            <el-switch v-model="choose2" active-text="Use Long Lead Time Flag" inactive-text=""></el-switch>
        </div>
        <el-button style="display:block;margin:0 auto; position:relative; top: 15px" @click="save_next">保存</el-button>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                choose1: '1',
                choose2: '1',
                input1: '',
                input2: '',
                input3: '',
                input4: '',
                input5: '',
                input7: '',
                input8: '',
                temp: false
            }
        },

        methods:{
            changed(){
              //console.log('1')
              this.temp = !this.temp 
            },

            save_next(){
                var others = {
                    choose1: this.choose1, 
                    input1: this.input1,
                    input2: this.input2,
                    input3: this.input3,
                    input4: this.input4,
                    input5: this.input5,
                    input7: this.input7,
                    input8: this.input8,
                    choose2: this.choose2,
                };
                localStorage.setItem("others",JSON.stringify(others));
                //this.$router.push({name:'re_time'});
                //提交数据，成功则弹窗提示，不跳转页面，提交后删除
            },

        }
  }
</script>


<style scoped>
  .wrapper3{
    position:relative;/*相对定位:参考物*/
    float: left;;/*浮动:左浮动 与父元素的左端对齐 依次的往右端显示 一行显示不下就换行接着依次显示*/
    top:5px;
    width:90%;
    margin:18px 20px;
    
    
}
  .lebal{
    position:relative;
    display: inline-block;
    padding:9px 0;
    color: #333;
  }

</style>
<template>
    <div>
        <div style="height:130px" class="wrapper3" >
            <el-col>
                <el-switch @change="changed" v-model="UseCasualty" active-text="Possible Unsafe Placard Consequers" inactive-text=""></el-switch>
                <br>
                <span class="lebal">Fraction of Total Quanttities to Trigger Ubsafe Placard</span><br>
                <span>Median:</span>
                <el-input v-if="temp" style="width:35%" size="mini" placeholder="请输入内容" v-model="RedTagMedian"></el-input>
                <el-input v-if="temp" style="width:35%;float:right" size="mini" placeholder="请输入内容" v-model="RedTagBeta"></el-input>
                <el-input :disabled="true" v-if="!temp" style="width:35%" size="mini" placeholder="请输入内容" v-model="RedTagMedian"></el-input>
                <el-input :disabled="true" v-if="!temp" style="width:35%;float:right" size="mini" placeholder="请输入内容" v-model="RedTagBeta"></el-input>
                <span style="float:right">Dispersio:</span>
                <span>This fraction should relate to the total quantity from all Performance group in this damage state</span>
            </el-col>
        </div>
        <div style="height:130px" class="wrapper3">
            <span>Potential for Non-Collapse Casualties::ality Rate in Affected Area:</span>
            <br><span>Median:</span>
            <el-input style="width:35%" size="mini" placeholder="请输入内容" v-model="AffectedDeathRate"></el-input>
            <el-input style="width:35%;float:right" size="mini" placeholder="请输入内容" v-model="AffectedDeathRateBeta"></el-input>
            <span style="float:right">Dispersio:</span>
            <span>Occupied Area Affected Per Performance Group Unit(sq.</span>
            <el-input style="width:20%" size="mini" placeholder="请输入内容" v-model="AffectedFloorArea"></el-input>
            <span>Injury Rate in Affected Area:</span><br>
            <span>Median:</span>
            <el-input style="width:35%" size="mini" placeholder="请输入内容" v-model="AffectedInjuryRate"></el-input>
            <el-input style="width:35%;float:right" size="mini" placeholder="请输入内容" v-model="AffectedInjuryRateBeta"></el-input>
            <span style="float:right">Dispersio:</span>
        </div>
        <div style="height:40px" class="box8">
            <el-switch v-model="LongLeadFlag" active-text="Use Long Lead Time Flag" inactive-text=""></el-switch>
        </div>
        <el-button style="display:block;margin:0 auto; position:relative; top: 15px" @click="save_next">保存</el-button>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                UseCasualty: '1',
                LongLeadFlag: '1',
                RedTagMedian: '0',
                RedTagBeta: '0',
                AffectedDeathRate: '0',
                AffectedDeathRateBeta: '0',
                AffectedFloorArea: '0',
                AffectedInjuryRate: '0',
                AffectedInjuryRateBeta: '0',
                temp: false
            }
        },

        methods:{
            changed(){
              //console.log('1')
              this.temp = !this.temp 
            },

            save_next(){
                let _this=this;
                if (this.UseCasualty==false){ var UseCasualty='false'}
                else{var UseCasualty='true'}
                if (this.LongLeadFlag==false){var LongLeadFlag='false'}
                else{var LongLeadFlag='true'}
                var others = {
                    UseCasualty: UseCasualty, 
                    RedTagMedian: this.RedTagMedian,
                    RedTagBeta: this.RedTagBeta,
                    AffectedDeathRate: this.AffectedDeathRate,
                    AffectedDeathRateBeta: this.AffectedDeathRateBeta,
                    AffectedFloorArea: this.AffectedFloorArea,
                    AffectedInjuryRate: this.AffectedInjuryRate,
                    AffectedInjuryRateBeta: this.AffectedInjuryRateBeta,
                    LongLeadFlag: LongLeadFlag,
                };
                localStorage.setItem("others",JSON.stringify(others));
                //this.$router.push({name:'re_time'});
                //提交数据，成功则弹窗提示，不跳转页面，提交后删除
                this.$ajax({
                method:'get',
                url:'savegen_num',
                params:{
                    re_info:localStorage.getItem('re_info'),
                    re_cost:localStorage.getItem('re_cost'),
                    re_time:localStorage.getItem('re_time'),
                    others:localStorage.getItem('others'),
                    username:localStorage.getItem('phone'),
                    path:localStorage.getItem('path'),
                    statenum:localStorage.getItem('statenum'),
                    statenum_info:localStorage.getItem('statenum_info')
                },
            })
            .then(function(response){
                console.log(response)
                var res = response.data
                console.log(res)
                if (res.error_num == 0) {
                    console.log(res['msg'])
                    _this.$message.success(res['msg'])
                    _this.$router.push({name:'re_cost'});
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
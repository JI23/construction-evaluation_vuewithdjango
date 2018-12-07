<!-- 传入value4的值选择易损性数据库显示数据 -->
<template>
    <div>
        <keep-alive>
            <el-main>
                <el-select @change="change_db" v-model="value4" placeholder="选择易损性数据库"><!--value4为选中内容 -->
                    <el-option
                        v-for="item in options"
                        :key="item.value"
                        :value="item.label">
                    </el-option>
                </el-select>
                <el-button @click="ret_newpj" v-show="cancel_show" style="position:relative;">返回项目新建</el-button>
                <el-button style="float: right" round type="info" @click="write">新建易损性数据库</el-button>
                <div style="height:380px; position:relative; top:20px">
                    <el-scrollbar class = "el-scrollbar">
                        <el-tree class="el-tree" :default-expand-all="true" :data="data"  @node-click="handleNodeClick" ></el-tree>
                    </el-scrollbar>
                </div>
            </el-main>
        </keep-alive>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                cancel_show:false,
                options: [{
                    value: 'DB_common',
                    label: 'DB_Common'
                }, {
                    value: 'DB_school',
                    label: 'DB_School'
                }, {
                    value: 'DB_hospital',
                    label: 'DB_Hospital'
                }, {
                    value: 'DB_user',
                    label: 'DB_User'
                }, {
                    value: 'DB_office',
                    label: 'DB_Office'
                }, {
                    value: 'DB_fEMA',
                    label: 'DB_FEMA'
                }],
                value4: 'DB_common',
                data: []
            }
        },

        beforeMount(){
            if(localStorage.getItem('new_db_ret') == 'true'){
                this.cancel_show = true
            }
            this.change_view()
        },

        methods: {
            ret_newpj(){
                localStorage.setItem('new_db_ret',false)
                this.$router.push({name:'step3'});
            },
            handleNodeClick(data,node){
                //console.log(data);
                let _this = this
                var temp = data.label.split(" ")
                var value = _this.value4
                sessionStorage.setItem('check',value)
                temp = temp[0]
                localStorage.setItem('part_id',temp)
                if(node.level == 3){
                    this.$ajax({
                        method:'get',
                        url:'get_detail',
                        params:{
                            'part_id': temp
                        },
                    }).then(function(response){
                        var res = response.data
                        console.log('111')
                        console.log(res)
                        console.log('222')
                        //localStorage.setItem('type',this.value4)
                        var gen_info = {
                            name: res.detail.name, 
                            id: res.detail.id, 
                            //req_coe: this.req_coe,
                            //cus_name: this.cus_name,
                            description:res.detail.description,
                            demand_Para:res.detail.demand_Para,//?
                            value1: res.detail.value1,
                            value2: res.detail.value2,
                            choose1: res.detail.choose1,
                            choose2: res.detail.choose2,
                            typename: res.detail.typename,
                            DP_Dimension: res.detail.DP_Dimension,
                            units: res.detail.units,
                        };
                        var notes_info = {
                            data: res.detail.data, 
                            relevance: res.detail.relevance, 
                            quality: res.detail.quality,
                            rationality: res.detail.rationality,
                            author: res.detail.author,
                            notes: res.detail.notes,
                        };
                        for(var i = 0; i < res.DamageStates.length; i++){
                            var temp1 = "\"损伤状态"+(i+1) + "\""
                            var temp2 = "\"结果详情" + (i+1) + "\""
                            var statenum_info = {
                                name: res.DamageStates[i].name, 
                                median: res.DamageStates[i].median, 
                                dispersion: res.DamageStates[i].dispersion,
                                description: res.DamageStates[i].description,
                                DamageImageName:res.DamageStates[i].DamageImageName,
                            };
                            sessionStorage.setItem(temp1,JSON.stringify(statenum_info))

                            var re_info = {
                                reInfo: res.DamageStates[i].RepairMeasures, 
                            };
                            sessionStorage.setItem(temp2+"_re",JSON.stringify(re_info))

                            var re_cost = {
                                l_Quantity: res.DamageStates[i].CostConsequence.l_Quantity, 
                                aver_re_l: res.DamageStates[i].CostConsequence.aver_re_l,
                                u_Quantity: res.DamageStates[i].CostConsequence.u_Quantity,
                                aver_re_u: res.DamageStates[i].CostConsequence.aver_re_u,
                                COV:res.DamageStates[i].CostConsequence.COV,
                                CurveType:res.DamageStates[i].CostConsequence.CurveType
                            };
                            sessionStorage.setItem(temp2+"_cost",JSON.stringify(re_cost))

                            var re_time = {
                                l_Quantity: res.DamageStates[i].TimeConsequence.l_Quantity, 
                                aver_re_l: res.DamageStates[i].TimeConsequence.aver_re_l,
                                u_Quantity: res.DamageStates[i].TimeConsequence.u_Quantity,
                                aver_re_u: res.DamageStates[i].TimeConsequence.aver_re_u,
                                COV:res.DamageStates[i].TimeConsequence.COV,
                                CurveType:res.DamageStates[i].TimeConsequence.CurveType
                            };
                            sessionStorage.setItem(temp2+"_time",JSON.stringify(re_time))

                            var others = {
                                UseCasualty: res.DamageStates[i].UseCasualty, 
                                RedTagMedian: res.DamageStates[i].RedTagMedian,
                                RedTagBeta: res.DamageStates[i].RedTagBeta,
                                AffectedDeathRate: res.DamageStates[i].AffectedDeathRate,
                                AffectedDeathRateBeta: res.DamageStates[i].AffectedDeathRateBeta,
                                AffectedFloorArea: res.DamageStates[i].AffectedFloorArea,
                                AffectedInjuryRate: res.DamageStates[i].AffectedInjuryRate,
                                AffectedInjuryRateBeta: res.DamageStates[i].AffectedInjuryRateBeta,
                                LongLeadFlag: res.DamageStates[i].LongLeadFlag,
                            };
                            sessionStorage.setItem(temp2+"_others",JSON.stringify(others))
                        }
                        sessionStorage.setItem('temp',i)
                        sessionStorage.setItem('gen_info',JSON.stringify(gen_info))
                        sessionStorage.setItem('notes_info',JSON.stringify(notes_info))
                        //console.log('!！！！！！')
                        //console.log(this.value4)
                        //console.log('!！！！！！')
                    }).catch(function(response){
                        console.log(response)
                    })
                    
                    setTimeout(()=>{
                        this.$router.push({name:'generalinfo'});
                    },1000)
                    //console.log(data.label);
                    //console.log('!!')
                    //localStorage.setItem("label",JSON.stringify(data.label));
                     
                }
            },

            handleClose(done) {
                this.$confirm('确认关闭？')
                .then(_ => {
                    done();
                })
                .catch(_ => {});
            },

            write(){
                sessionStorage.setItem('check','DB_User')
                this.$router.push({name:'newdb'});
            },
            change_db(){
                this.change_view()
            },
            change_view(){
                let _this=this
                this.$ajax({
                    method:'get',
                    url:'step3-get-all-parts',
                    params:{
                        value: this.value4,
                        username: localStorage.getItem('phone')
                    },
                    headers:{"Content-Type": "application/json"}
                }).then(function(response){
                    //console.log(response)
                    //console.log('111')
                    var res=response.data
                    if(res.error_num==0){
                        //console.log(res['list'])
                        var returnData = []
                        for(var i = 0; i < res['first'].length; i++){
                            var temp = {
                                label: "",
                                children: []
                            }
                            temp.label=res['first'][i]
                            for(var j = 0; j < res['second'].length; j++){
                                if(res['first'][i] === res['second'][j][0]){
                                    var item = {
                                        label: res['second'][j][1],
                                        children: []
                                    }
                                    for(var k = 0; k < res['list'].length; k++){
                                        if(res['list'][k].fields.second === res['second'][j][1]){
                                            var item1 = {
                                                label: res['list'][k].fields.part_id + " " + res['list'][k].fields.part_name + " " + res['list'][k].fields.description,
                                                children:[]
                                            }
                                            item.children.push(item1)
                                        }
                                    }
                                    temp.children.push(item)
                                }
                            }
                            returnData.push(temp)
                        }
                        console.log(returnData)
                        _this.data=returnData
                    }
                    else {
                        _this.$message.error(res['msg'])
                        console.log(res['msg'])
                    }
                }).catch(function(err){
                    console.log(err);
                    console.log('!!')
                    console.log(_this.data)
                });
            },
        }
    }
</script>

<style scoped>
    .el-scrollbar{
        height: 100%
    }

    .el-scrollbar__wrap {
        overflow-x: hidden;
    }

    .el-tree{
        display:inline-block;
    }

</style>

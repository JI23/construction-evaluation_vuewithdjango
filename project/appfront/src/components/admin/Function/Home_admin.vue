<!-- 开始前加载项目数信息 -->
<template>
    <div>
        <schart class="wrapper" :canvasId="canvasId" :type="type" :data="data" :options="options"></schart>
        <br><br>
        <div class="box2" style= "background:#67C23A">
            <h4>总人数</h4>
            <p>10</p>
        </div>
        <div class="box2" style= "background:rgba(233,240,29,1)">
            <h4>总公司数</h4>
            <p>1</p>
        </div>
        <div class="box2">
            <h4>已完成项目总数</h4>
            <p>11</p>
        </div>
        <div class="box2">
            <h4>项目总数</h4>
            <p>11</p>
        </div>
    </div>
</template>

<script>
    import Schart from 'vue-schart';
    export default {
        data() {
            return {
                canvasId: 'myCanvas',
				type: 'bar',
				data: [
					{name: '2014', value: 1342},
					{name: '2015', value: 2123},
					{name: '2016', value: 1654},
					{name: '2017', value: 1795},
				],
				options: {
					title: 'Total sales of stores in recent years'
				},
                allpj:'',
                successpj: '',
                com_Num: '',
                user_Num: '',
            }
        },

        mounted(){
            this.show_info()
        },

        methods:{
            show_info(){//获取四个框的基本信息，以及图表的信息内容
                this.$ajax({
                    method: 'get',
                    url: '',

                }).then(function(response){
                    console.log(response)
                    //进行赋值
                })
                 
            }
        },

        components:{
			Schart
		}
    }
</script>

<style scoped>
    .box2{
        position:relative;/*相对定位:参考物*/
        float:left;/*浮动:左浮动 与父元素的左端对齐 依次的往右端显示 一行显示不下就换行接着依次显示*/
        width:20%;
        height:100px;
        margin:18px 20px;
        background:rgba(241,124,103,1);/*red红色 green绿色 blue蓝色0-255  a透明度0-1*/
        text-align: center;
        box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
        border-radius:2px;
        color:#666;
    }

    .wrapper{
        width: 40%;
        height: 40%;
    }
</style>
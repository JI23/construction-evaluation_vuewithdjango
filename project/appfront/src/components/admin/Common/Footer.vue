<template>
    <nav>
        <span>关于我们</span>
        <span>联系我们</span>
    </nav>
</template>
<style scoped>
    nav>span{
        height: 60px;
        line-height: 60px;
        font-size:16px;
    }
    nav{
        box-sizing: border-box;
        display: flex;
        justify-content: flex-end;
        transition: background .1s; 
        padding:0 40px;
        width:100%;
        height: 60px;
        color:#66209A;
        box-shadow: 0.1rem -0.1em 0.1rem rgba(0, 0, 0, 0.1);
    }
    nav>span{
        padding: 0 5px;
        cursor: pointer;
        color:#66209A
    }
    nav>span:hover,
    nav>i:hover{
        color: rgba(102, 32, 154, 0.7)
    }
    nav>i{
        cursor: pointer;
    }
</style>
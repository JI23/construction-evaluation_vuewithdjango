<template>
    <div>
        <index-nav></index-nav>
        <router-view></router-view>
    </div>
</template>
<script>
import indexNav from './indexNav'
export default {
    components:{
    "index-nav": indexNav
  }
}
</script>

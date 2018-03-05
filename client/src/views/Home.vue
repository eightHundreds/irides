<template>
    <div>
        <Header />
        <el-container>
          <el-main>
            content
          </el-main>
        </el-container>
    </div>
</template>

<script>
import Header from "../components/Header.vue";
export default {
  components: { Header },
  data: function() {
    return {};
  }
};
</script>

<style scoped>
.el-header {
  border: 1px solid blue;
}
.el-main {
  border: 1px solid red;
}
</style>
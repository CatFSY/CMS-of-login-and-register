<template>
    <div>
      <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
        点我打开
      </el-button>
  
      <el-drawer
        title="我是标题"
        :visible.sync="drawer"
        :with-header="false"
        :direction="'rtl'"
      >
        <span>我来啦!</span>
      </el-drawer>
    </div>
  </template>
  
  <script>
    export default {
      data() {
        return {
          drawer: false,
        };
      }
    };
  </script>
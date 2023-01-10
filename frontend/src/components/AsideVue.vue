<template>
  <el-menu
    class="el-menu-vertical-demo"
    :collapse="isCollapse"
    text-color="black"
    background-color="rgb(247,246,242)"
    :default-active="activeIndex"
    active-text-color="#FFFFFF"
  >
    <div class="platform">
      <img
        class="platform-logo"
        :src="require('@/assets/image/logo/80.png')"
        alt="logo"
        @click="goHome"
      >
      <div
        v-if="!isCollapse"
        id="platform-title"
      >
        <a
          class="platform-title"
          @click="goShow"
        >数据库大作业</a>
      </div>
    </div>
    <el-divider content-position="center">
      <span
        v-show="!isCollapse"
        class="divider-title"
      ></span>
    </el-divider>
    <el-menu-item
      v-for="item in routes"
      :key="item.meta.title"
      :index="item.path"
      @click="goSomeWhere(item.path)"
    >
      <i
        v-show="isCollapse"
        :class="item.meta.icon"
      />
      <h3 v-show="!isCollapse">
        <i :class="item.meta.icon" />{{ item.meta.title }}
      </h3>
    </el-menu-item>
    <el-divider content-position="center">
      <span
        v-show="!isCollapse"
        class="divider-title"
      />
    </el-divider>
  </el-menu>
</template>

<script>

import {
  goSomeWhere,goHome
} from "@/utils/goSomeWhere.js";
export default {
  props: {
    isCollapse: {
      type: Boolean,
      default: false
    },
    activeIndex: {
      type: String,
      default: '/bandlist'
    },
    routes: {
      type: Array,
      default() {
        return []
      }
    }
  },

  methods: {
    goSomeWhere,
    goHome,
    goShow() {
      this.$message.success('欢迎来到本平台')
    }
  },
};
</script>

<style lang="less">
.el-menu {
  position: relative;
  height: 100vh;
  top: 0;
  bottom: 0;
  text-align: center;
  font-family: Microsoft JhengHei UI, sans-serif;

  .el-menu-item {
    padding: 0 0;
    border-radius: 10px;
    position: relative;
    color: rgb(117, 117, 117);
    z-index: 1;
    h3 {
      padding-right: 30px;
      width: 100%;
      margin: 0 auto;
      .iconfont {
        font-weight: normal;
        margin-right: 5px;
      }
    }
  }
  .el-menu-item:hover {
    background-color: rgb(247, 246, 242);
    color: #ecf4ff !important;
  }

  .el-menu-item :hover::after {
    width: 100%;
    background: var(--theme--color);
  }
  .el-menu-item ::after {
    position: absolute;
    content: "";
    width: 0;
    height: 100%;
    top: 0;
    left: 0;
    border-radius: 10px;
    transition: 0.25s;
    z-index: -1;
  }
}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 250px;
  min-height: 400px;
}

.is-active {
  background-color: var(--theme--color);
  h3,i{
    color:rgb(247, 246, 242)!important;
  }
}

.platform {
  padding-top: 14px;
  text-align: center;
  color: var(--theme--color);
  height: 80px;
  width: auto;
  overflow: hidden;

  .platform-logo {
    color: var(--theme--color);
    width: 45px;
  }

  .platform-title {
    color: var(--theme--color);
    font-family: Microsoft JhengHei UI, sans-serif;
    font-size: 21px;
  }
}

.divider-title {
  display: block;
  line-height: 24.4px;
  overflow: hidden;
  width: 70px;
  color: rgb(140, 157, 182)
}

.el-divider__text {
  background-color: rgb(247, 246, 242) !important;
}

#platform-title {
  position: relative;
  font-size: 20px;
  font-weight: 1000;
  cursor: pointer;
}

#platform-title::after {
  content: "";
  width: 0;
  height: 3px;
  background: var(--theme--color);
  position: absolute;
  top: 100%;
  left: 50%;
  right: 50%;
  transition: all 0.5s;
}

#platform-title:hover:after {
  left: 7%;
  right: 7%;
  width: 85%;
}
</style>
 
 
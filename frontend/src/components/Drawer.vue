<template>
  <div type="primary" style="margin-left: 16px" class="aside-navigator hidden-md-and-down" @click="isNavigator = true">
    <div class="aside-navigator-title">
      <span>快速导航</span>
    </div>
    <div class="aside-navigator-icon">
      <i class="iconfont icon-feiji" />
    </div>
  </div>

  <el-drawer v-model="isNavigator" title="快速导航" :direction="direction" :size="size" >
    <el-menu class="el-menu-vertical-demo" :collapse="isCollapse" text-color="black" background-color="white"
      :default-active="activeIndex" active-text-color="#FFFFFF">
      <el-menu-item-group>
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
      </el-menu-item-group>
    </el-menu>
  </el-drawer>
</template>

<script>
import {
  goSomeWhere
} from "@/utils/goSomeWhere.js";
export default {
  name: "Drawer",
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
  data() {
    return {
      isNavigator: false,
      direction: "rtl",
      size: "15%",
    };
  },
  methods: {
    goSomeWhere
  },
};
</script>

<style lang="less" scoped>
.aside-navigator {
  position: fixed;
  z-index: 100;
  background: rgb(252, 252, 252);
  top: 200px;
  right: 0;
  width: 34px;
  height: 120px;
  padding: 0.5rem;
  border-top-left-radius: 0.2rem;
  border-bottom-left-radius: 0.2rem;
  box-shadow: -5px 0 10px 0 rgba(0, 0, 0, 0.1);
  transition: all 0.1s ease-in-out;
  cursor: pointer;
  font-family: Microsoft JhengHei UI, sans-serif;

  .aside-navigator-title {
    font-size: 17px;
    font-weight: 1000;
    -webkit-writing-mode: vertical-rl;
    writing-mode: vertical-rl;
    color: rgb(64, 158, 255);
    background: rgb(237, 242, 245);
    padding: 0.12rem;
    border-radius: 0.2rem;
    height: 80px;
    text-align: center;
    width: 33px;

    span {
      display: block;
      padding-right: 6px;
    }
  }

  .aside-navigator-icon {
    width: 37px;
    text-align: center;
    margin-top: 6px;
    color: rgb(64, 158, 255);
    background: rgb(237, 242, 245);
    border-radius: 0.2rem;
    height: 30px;

    .iconfont {
      display: block;
      padding-top: 5px;
    }
  }
}

.aside-navigator-title:hover,
.aside-navigator-icon:hover {
  background-color: rgb(228, 235, 240);
}
.el-menu {
  width: 100%;
  overflow-y: hidden;
}


</style>
<template>
  <div class="nav-bar">
    <div class="time-item">
      <span class="date hidden-sm-and-down"><i
        class="iconfont icon-shijian"
      /><span class="hms">{{ currenthour }}:{{ currentminute }}:{{
        currentsecond
      }}</span><span class="ymd">[{{ currentyear }}-{{ currentmonth }}-{{
        currentday
      }}]</span></span>
    </div>
    <div
      style="margin-left:15px"
      class="github-item"
    >
      <i
        class="iconfont icon-github"
        @click="goGithub"
      />

    </div>
    <span style="margin-left: 10px">欢迎您，{{ this.nickName}}</span>
    <div class="log-out-item">
      <el-dropdown>
        <span class="el-dropdown-link">
          <i
            class="iconfont icon-yonghu"
            style="font-size: 24px"
          />
        </span>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item @click="logOut">
              登出
            </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
import {getCurrentTime} from "@/utils/getTime.js"
import {loginOut} from "@/api/login";
import {userStore} from "@/store/user";
const store = userStore();
export default {
  data() {
    return {
      currentyear: "",
      currentday: "",
      currentmonth: "",
      currenthour: "",
      currentminute: "",
      currentsecond: "",
      getDate: "",
      nickName: store.userInfo.nickName,
    };
  },
  mounted() {
    this.getCurrentTime();
  },
  unmounted() {
    clearTimeout(this.getDate);
  },
  methods: {
    loginOut,
    getCurrentTime,
    goGithub(){
      window.open('https://github.com/terayco/database_finalwork');
    },
    logOut() {
      this.$confirm("是否确定登出?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
          .then(() => {
            this.loginOut().then((res) => {
              localStorage.setItem("token", "");
              localStorage.setItem('userInfo','');
              localStorage.setItem('routes','');
              this.$message.success("登出成功！");
              this.$router.push("Login");
            });
          })
          .catch(() => {
            this.$message({
              type: "info",
              message: "已取消操作",
            });
          });
    },
  },
};
</script>
<style scoped>
* {
    font-family: Microsoft JhengHei UI, sans-serif;
}
.date {
  font-family: Microsoft YaHei;
  font-weight: 400;
}
.hms {
  color: rgb(64,158,255);
  font-size: 18px;
}
.ymd {
  color: var(--theme--color);
  font-size: 18px;
}

.iconfont icon-yonghu {
  line-height: 70px;
  padding-top: 10px;
}
.iconfont icon-yonghu:hover {
  color: skyblue;
}
.el-dropdown-item {
  z-index: 10000;
}
.nav-bar{
  display: flex;
  flex-direction: row;
  width: 100%;
}
.log-out-item{
  position: absolute;
  margin-top: 18px;
  right: 70px;
  justify-content: right;
  align-items: center;
}
</style>

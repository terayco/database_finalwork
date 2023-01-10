<template>
  <div>
    <vue-particles
      color="#409EFF"
      :particle-opacity="0.7"
      :particles-number="60"
      shape-type="circle"
      :particle-size="6"
      lines-color="#409EFF"
      :lines-width="1"
      :line-linked="true"
      :line-opacity="0.4"
      :lines-distance="150"
      :move-speed="4"
      :hover-effect="true"
      hover-mode="grab"
      :click-effect="true"
      click-mode="push"
    />
    <img
      src="@/assets/image/other/bg1.jpg"
      class="bg"
      alt="bg"
    >
    <div
      id="container"
      class="container1"
    >
      <div class="form-container sign-up-container">
        <el-form
          ref="create"
          class="login-form band-reg"
          label-width="80px"
          :model="user"
          :rules="regRules"
          hide-required-asterisk
          @keyup.enter="createFan"
        >
          <h1>注册</h1>
          <el-form-item
            label="昵称"
            style="align-items: center"
            prop="fname"
            required
          >
            <el-input
              v-model="user.fname"
              placeholder="新用户的用户名"
            />
          </el-form-item>
          <el-form-item
            label="账户名"
            prop="username"
            style="align-items: center"
          >
            <el-input
              v-model="user.username"
              autofocus
              placeholder="请输入帐户名"
            />
          </el-form-item>
          <el-form-item
            label="密码"
            style="align-items: center"
            prop="password"
            required
          >
            <el-input
              v-model="user.password"
              type="password"
              placeholder="至少 ≥ 6 位"
            />
          </el-form-item>
          <el-form-item
            label="性别"
            style="align-items: center;width: 260px"
            prop="sex"
            required
          >
            <el-select
              v-model="user.sex"
            >
              <el-option
                v-for="item in sexList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>
          <el-form-item
            label="年龄"
            style="align-items: center;width: 260px"
            prop="age"
            required
          >
            <el-input
              v-model="user.age"
              type="number"
              placeholder="请输入年龄"
              min="12"
              max="99"
            />
          </el-form-item>
          <el-form-item
            label="职业(可选)"
            style="align-items: center"
            prop="career"
          >
            <el-input
              v-model="user.career"
              placeholder="请输入职业"
            />
          </el-form-item>
          <p
            class="forget-psw"
            @click="goBandReg"
          >
            前往乐队注册
          </p>
          <el-button
            :disabled="!canFanReg"
            @click="createFan"
          >
            创建
          </el-button>
        </el-form>
        <el-form
          ref="bandForm"
          :model="addBandInfo"
          :rules="bandRules"
          label-width="100px"
          class="fan-reg"
        >
          <el-form-item
            label="乐队名称"
            prop="bandName"
          >
            <el-input v-model="addBandInfo.bandName" />
          </el-form-item>
          <el-form-item
            label="乐队ID"
            prop="bandID"
            style="width: 270px;"
            required
          >
            <el-input
              v-model="addBandInfo.bandId"
              type="number"
              min="1"
              onkeyup="this.value=this.value.replace(/^(0+)|[^\d]+/g,'')"
            />
          </el-form-item>
          <el-form-item
            label="乐队密码"
            prop="bandPwd"
            required
            style="width: 270px;"
          >
            <el-input
              v-model="addBandInfo.bandPwd"
              type="password"
            />
          </el-form-item>
          <el-form-item
            label="队长姓名"
            prop="bandLeader"
            reuired
          >
            <el-input v-model="addBandInfo.bandLeader" />
          </el-form-item>
          <el-form-item
            label="队长性别"
            prop="bandLeaderSex"
            required
          >
            <el-select
              v-model="addBandInfo.memberData[0].memberSex"
              placeholder="请选择"
            >
              <el-option
                v-for="item in sexList"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>
          <el-form-item
            label="队长年龄"
            prop="bandLeaderAge"
            style="width: 270px;"
            required
          >
            <el-input
              v-model="addBandInfo.memberData[0].memberAge"
              type="number"
              min="12"
              max="99"
              onkeyup="this.value=this.value.replace(/^(0+)|[^\d]+/g,'')"
            />
          </el-form-item>
          <el-form-item
            label="成立时间"
            required
            style="width: 250px"
          >
            <el-col :span="11">
              <el-form-item prop="fundationTime">
                <el-date-picker
                  v-model="addBandInfo.fundationTime"
                  type="date"
                  placeholder="选择日期"
                  style="width: 100%;"
                />
              </el-form-item>
            </el-col>
          </el-form-item>
          <p
            class="forget-psw"
            @click="goFanReg"
          >
            返回粉丝注册
          </p>
          <el-button
            :disabled="!canBandReg"
            @click="createBand"
          >
            创建
          </el-button>
        </el-form>
      </div>
      <div class="form-container sign-in-container">
        <el-form
          ref="login"
          :rules="loginRules"
          hide-required-asterisk
          :model="logUser"
          class="login-table"
          @keyup.enter="gologin"
        >
          <h1 id="login-title">
            请登录
          </h1>
          <el-form-item
            label="用户名"
            prop="username"
            style="align-items: center"
          >
            <el-input
              v-model="logUser.username"
              autofocus
              placeholder="请输入用户名"
            />
          </el-form-item>

          <el-form-item
            label="密码"
            prop="password"
            style="align-items: center; padding-left: 11.5px"
          >
            <el-input
              v-model="logUser.password"
              type="password"
              placeholder="请输入密码"
            />
          </el-form-item>
            <el-radio-group v-model="logUser.role" style="padding: 10px">
              <el-radio
                label="fan"
                style="margin-right: 20px"
              >
                粉丝
              </el-radio>
              <el-radio
                label="band"
                style="margin-right: 20px"
              >
                乐队
              </el-radio>
              <el-radio
                label="admin"
                style="margin-right: 20px"
              >
                管理员
              </el-radio>
            </el-radio-group>

          <el-button
            :disabled="!canSubmit"
            @click="gologin"
          >
            登录
          </el-button>
        </el-form>
      </div>

      <div class="overlay-container">
        <div class="overlay">
          <div class="overlay-panel overlay-left">
            <h1>已有账号？去登录</h1>

            <button
              class="ghost"
              @click="goSignIn"
            >
              去登录
            </button>
          </div>
          <div class="overlay-panel overlay-right">
            <h1>没注册？去注册</h1>

            <button
              class="ghost"
              @click="goSignUp"
            >
              去注册
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { createFanApi, login,createBandApi } from "@/api/login";

import bg from "@/assets/image/other/bg1.jpg";
import {userStore} from "@/store/user";
import {buildRoute} from "@/router/permission";
import {formatTime} from "@/utils/format";

const store = userStore()
export default {
  name: "Login",
  data() {
    return {
      bg: bg,
      logUser: {
        username:'',
        password: "",
        role: "fan"
      },
      user: {
        fname: "",
        username:'',
        password: "",
        sex:'',
        age:'',
        career:''
      },
      sexList:[
        {
          value: "男",
          label: "男"
        },
        {
          value: "女",
          label: "女"
        }
      ],
      loginRules: {

        username: [{ required: true, message: "用户名必填", trigger: "blur" }],
        password: [
          { required: true, message: "密码必填", trigger: "blur" },
          { min: 6, message: "密码至少为6位", trigger: "blur" },
        ],
      },
      regRules:{
        fname: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { max: 10, message: "用户名长度不能超过10个字符", trigger: "blur" }
        ],
        username: [{ required: true, message: "账号名必填", trigger: "blur" },
            { max: 10, message: "账号名长度不能超过10个字符", trigger: "blur" }],
        password: [
          { required: true, message: "密码必填", trigger: "blur" },
          { min: 6, message: "密码至少为6位", trigger: "blur" },
        ],
        sex:[{ required: true, message: "性别必填", trigger: "blur" }],
        age:[{ required: true, message: "年龄必填", trigger: "blur" }],
      },
      addBandInfo:{
        bandId:'',
        bandName: '',
        bandPwd:'',
        bandLeader: '',
        fundationTime: '',
        bandNumber: 1,
        albumNumber: 0,
        isEdit: false,
        memberData:[
          {
            memberName: '',
            bandName: '',
            memberSex: '',
            memberAge: '',
            memberJob: '',
            memberPosition: '队长',
            joinTime: '',
            leaveTime: '',
            isEdit: false
          }
        ]
      },
      logForm:{
        username:"",
        password:"",
      },
      bandRules: {
        bandId: [
          { required: true, message: "请输入乐队ID", trigger: "blur" },
          { min: 1, message: '必须大于1', trigger: 'blur' }
        ],
        bandName: [
          { required: true, message: '请输入乐队名称', trigger: 'blur' },
        ],
        bandPwd: [
          { required: true, message: '请输入乐队密码', trigger: 'blur' },
        ],
        bandLeader: [
          { required: true, message: '请输入队长姓名', trigger: 'blur' },
        ],
        bandNumber: [
          { required: true, message: '请输入乐队人数', trigger: 'blur' },
          { min: 1, max: 99, message: '人数在1-99间', trigger: 'blur' }
        ],
        fundationTime: [
          { required: true, message: '请选择成立时间', trigger: 'change' }
        ]
      },
      passWordRules: /^\S{6,}$/,
    };
  },
  computed: {
    canSubmit() {
      const { username, password } = this.logUser;
      return Boolean(username && password);
    },
    canFanReg(){
      const { fname, username, password ,sex,age,} = this.user;
      return Boolean(fname && username && password && sex && age);
    },
    canBandReg() {
      const { bandId, bandName, bandPwd, bandLeader, fundationTime } = this.addBandInfo;
      return Boolean(bandId && bandName && bandPwd && bandLeader && fundationTime);
    },
  },
  mounted() {
    document.body.style.overflowX = "hidden";
  },
  methods: {
    formatTime,
    gologin() {
      let roleInfo = {};
      this.logForm.username = this.logUser.username;
      this.logForm.password = this.logUser.password;
      login(this.logForm)
        .then(({ data }) => {
          if (data.code === 1) {
            this.$message.error(data.msg);
          } else {
            const { accessToken } = data.data;
            const { role } = data.data;
            if(role !== this.logUser.role){
              this.$message.error("账号类型错误");
              return;
            }
            const {bandName} = data.data
            localStorage.setItem("token", accessToken);
            this.$router.push("/bandlist");
            this.$message.success("登录成功！");
            if (role === 'admin') {
              roleInfo = { name: '管理员', role: 'admin', nickName: 'admin' };
            } else if(role === 'band'){
              roleInfo = { name: '歌手', role: 'band' ,bandName:bandName , nickName: bandName};
            }else {
              roleInfo = { name: '粉丝', role: 'fan',nickName: this.logUser.username };
            }
            console.log(roleInfo)
            store.$patch({ userInfo:roleInfo })
            let allRoutes  = buildRoute(roleInfo.role)
            // 保存当前用户所有可以访问的路由到vuex中
            store.$patch({routes: allRoutes})
            // 动态添加路由配置
          }
        })
        .catch((err) => {
          this.$message.error(err.response.data.message);
        });
    },
    createFan() {
      if (!this.passWordRules.test(this.user.password)) {
        this.$message.error("格式错了哦,密码至少6位");
      } else {
        createFanApi(this.user).then((res) => {
          if (res.data.code === 1) {
            this.$message.error(res.data.msg);
            this.user = { username: "", password: "" };
          } else {
            this.goSignIn();
            this.$message.success("创建成功");
            this.user = { username: "", password: "" };
          }
        });
      }
    },
    createBand() {
      for (let item in this.addBandInfo) {
        if (this.addBandInfo[item] === '') {
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return
        }
      }
      this.addBandInfo.fundationTime = this.formatTime(this.addBandInfo.fundationTime)
      this.addBandInfo.bandId = Number(this.addBandInfo.bandId)
      this.addBandInfo.memberData[0].joinTime = this.addBandInfo.fundationTime
      this.addBandInfo.memberData[0].memberName = this.addBandInfo.bandLeader
      this.addBandInfo.memberData[0].bandName = this.addBandInfo.bandName
      this.addBandInfo.albumNumber = 0
      // console.log(this.addBandInfo)
      createBandApi(this.addBandInfo).then(res => {
        console.log(res.data.data)
        this.$message({
          message: '注册成功',
          type: 'success'
        });
      })
    },
    goSignUp() {
      let container = document.getElementById("container");
      container.classList.add("right-panel-active");
    },
    goSignIn() {
      let container = document.getElementById("container");
      container.classList.remove("right-panel-active");
    },
    goBandReg() {
      document.querySelector(".band-reg").classList.add("active-band");
      document.querySelector(".fan-reg").classList.add("active-fan");
    },
    goFanReg() {
      document.querySelector(".band-reg").classList.remove("active-band");
      document.querySelector(".fan-reg").classList.remove("active-fan");
    },
  },
};
</script>

<style scoped>
body {
  overflow-x: hidden;
}
#particles-js {
  width: 100%;
  height: calc(100% - 100px);
  position: absolute;
  top: 0;
  left: 0;
}
.bg {
  z-index: -1;
  height: 100%;
  background-size: 100%;
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;

  background-size: cover;
}
.container1 {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
  position: absolute;
  overflow: hidden;
  width: 50vw;
  height: 40vh;
  max-width: 100%;
  min-width: 500px;
  min-height: 480px;
  left: 0;
  right: 0;

  top: 21vh;
  margin: auto;
  opacity: 0.7;
}
.form-container {
  position: absolute;
  top: 0;
  height: 100%;
  transition: all 0.6s ease-in-out;
}
.sign-in-container {
  left: 0;
  width: 50%;
  z-index: 2;
}
.container1.right-panel-active .sign-in-container {
  transform: translateX(100%);
}
.sign-up-container {
  left: 0;
  width: 50%;
  opacity: 0;
  z-index: 1;
}
.container1.right-panel-active .sign-up-container {
  transform: translateX(100%);
  opacity: 1;
  z-index: 5;
  animation: show 0.41s;
}
.login-table {
  transition: all 0.7s;
}
.forget-table {
  transition: all 0.7s;
  opacity: 0;
}
.active-login {
  opacity: 0;
  z-index: -1;
}
.active-forget {
  transform: translateY(-100%);
  opacity: 1;
}
@keyframes show {
  0%,
  49.99% {
    opacity: 0;
    z-index: 1;
  }

  50%,
  100% {
    opacity: 1;
    z-index: 5;
  }
}

.overlay-container {
  position: absolute;
  top: 0;
  left: 50%;
  width: 50%;
  height: 100%;
  overflow: hidden;
  transition: transform 0.6s ease-in-out;
  z-index: 100;
}

.container1.right-panel-active .overlay-container {
  transform: translateX(-100%);
}

.overlay {
  background: skyblue;
  background: -webkit-linear-gradient(to right, skyblue, #ff416c);
  background: linear-gradient(to right, skyblue, skyblue);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: 0 0;
  color: #ffffff;
  position: relative;
  left: -100%;
  height: 100%;
  width: 200%;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}

.container1.right-panel-active .overlay {
  transform: translateX(50%);
}

.overlay-panel {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 40px;
  text-align: center;
  top: 0;
  height: 100%;
  width: 50%;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}

.overlay-left {
  transform: translateX(-20%);
}

.container1.right-panel-active .overlay-left {
  transform: translateX(0);
}

.overlay-right {
  right: 0;
  transform: translateX(0);
}
.container1.right-panel-active .overlay-right {
  transform: translateX(20%);
}

* {
  box-sizing: border-box;
  font-family: "Montserrat", sans-serif;
}
.el-button {
  transition: all 0.4s;
}
button {
  border-radius: 20px;
  border: 1px solid skyblue;
  background-color: skyblue;
  color: #ffffff;
  font-size: 18px;
  font-weight: bold;
  padding: 12px 45px;
  letter-spacing: 1px;
  text-transform: uppercase;
  margin: 0 auto;
  transition: transform 80ms ease-in;
}

button:active {
  transform: scale(0.95);
}
button:focus {
  outline: none;
}
button.ghost {
  background-color: skyblue;
  border-color: #ffffff;
  cursor: pointer;
  transition: all 0.4s;
}
.ghost:hover {
  color: skyblue;
  background-color: white;
}

form {
  background-color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 50px;
  height: 100%;
  text-align: center;
}

input {
  border: none;
  padding: 12px 15px;
  margin: 8px 0;
  width: 100%;
  background: rgb(209, 207, 208);
}
.forget-psw {
  color: skyblue;
  font-size: 15px;
  cursor: pointer;
  transition: all 0.5s;
}
.forget-psw:hover {
  color: rgb(255, 145, 0);
}
.el-button {
  font-size: 16px;
}
.band-reg {
  transition: all 0.7s;
}
.fan-reg {
  transition: all 0.7s;
  opacity: 0;
}
.active-band {
  opacity: 0;
  z-index: -1;
}
.active-fan{
  transform: translateY(-100%);
  opacity: 1;
}
</style>

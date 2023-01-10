<template>
  <div>
    <div
      v-show="currentRole==='band'"
      class="fans-look"
    >
      <div class="fan-left">
        <el-card class="cards-num">
          <img
            :src="require('@/assets/image/num.png')"
            alt="1"
            class="cards-img"
          >
          <div class="desc">
            您的歌迷有：<span class="nums">{{ fanNum }}</span>人
          </div>
        </el-card>
        <el-card class="cards-num">
          <img
            :src="require('@/assets/image/song1.png')"
            alt="1"
            class="cards-img"
          >
          <div class="desc">
            最受喜爱的歌曲是：<span class="words">{{ mostLikeSong }}</span>
          </div>
        </el-card>
      </div>
      <div class="fan-right">
        <div id="genderCharts" />
        <div id="ageCharts" />
      </div>
    </div>
    <el-card 
      style="margin-top: 20px"
    >
      <div>歌迷信息</div>
      <el-table
        :data="fanData"
        border
        :row-style="iRowStyle"
        style="width: 100%;margin-top: 20px"
      >
        <el-table-column
          v-permission="['admin']"
          prop="fanName"
          label="歌迷ID"
        >
          <template #default="scope">
            <span> {{ scope.row.fanId }}</span>
          </template>
        </el-table-column>
        <el-table-column
          prop="fanName"
          label="昵称"
        >
          <template #default="scope">
            <span v-show="!scope.row.isEdit"> {{ scope.row.fanName }}</span>
            <el-input
              v-show="scope.row.isEdit"
              v-model="scope.row.fanName"
            />
          </template>
        </el-table-column>
        <el-table-column
          property="fanSex"
          label="性别"
        >
          <template #default="scope">
            <span v-show="!scope.row.isEdit">{{ scope.row.fanSex }}</span>
            <el-select
              v-show="scope.row.isEdit"
              v-model="scope.row.fanSex"
              placeholder="请选择"
            >
              <el-option
                v-for="item in sexOptions"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </template>
        </el-table-column>
        <el-table-column
          prop="fanAge"
          label="年龄"
        >
          <template #default="scope">
            <span v-show="!scope.row.isEdit"> {{ scope.row.fanAge }}</span>
            <el-input
              v-show="scope.row.isEdit"
              v-model="scope.row.fanAge"
              type="number"
              min="12"
              max="99"
              onkeyup="this.value=this.value.replace(/^(0+)|[^\d]+/g,'')"
            />
          </template>
        </el-table-column>
        <el-table-column
          prop="fanCareer"
          label="职业"
        >
          <template #default="scope">
            <span v-show="!scope.row.isEdit"> {{ scope.row.fanCareer }}</span>
            <el-input
              v-show="scope.row.isEdit"
              v-model="scope.row.fanCareer"
            />
          </template>
        </el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="200"
          v-if="currentRole==='admin'"
        >
          <template #default="scope">
            <el-button
              v-permission="['admin','band','notBandThing']"
              type="text"
              size="small"
              @click="editFanInfo(scope.row)"
            >
              编辑
            </el-button>
            <el-button
              v-show="scope.row.isEdit"
              type="text"
              size="small"
              @click="confirmFanInfo(scope.row)"
            >
              确认
            </el-button>

            <el-button
              v-permission="['admin','band','notBandThing']"
              type="text"
              size="small"
              style="color: red"
              @click="deleteFanInfo(scope.row)"
            >
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
   <div style="display: flex;justify-content: left;align-items: center">
    <el-button
      v-if="currentRole ==='admin'"
      type="primary"
      style="margin-top: 20px;margin-right: 20px"
      @click="addFan"
    >
      添加歌迷
    </el-button>
    <div style="margin: 20px 0;padding-top: 17px">共计{{ total}}条数据</div>
   </div>
    <el-dialog
      v-model="fanVisible"
      title="添加歌迷"
      width="30%"
      center
    >
      <el-form
        ref="addFanForm"
        :model="addFanInfo"
        :rules="fanRules"
        label-width="100px"
      >
        <el-form-item
          label="姓名"
          required
          prop="姓名"
        >
          <el-input
            v-model="addFanInfo.fanName"
          />
        </el-form-item>
        <el-form-item
          label="性别"
          required
          prop="性别"
        >
          <el-select
            v-model="addFanInfo.fanSex"
            placeholder="请选择"
          >
            <el-option
              v-for="item in sexOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item
          label="年龄"
          required
          prop="年龄"
        >
          <el-input
            v-model="addFanInfo.fanAge"
            type="number"
            min="12"
            max="99"
            onkeyup="this.value=this.value.replace(/^(0+)|[^\d]+/g,'')"
          />
        </el-form-item>
        <el-form-item
          label="职业"
          prop="职业"
        >
          <el-input
            v-model="addFanInfo.fanCareer"
          />
        </el-form-item>
        <el-form-item>
          <el-button
            type="primary"
            @click="submitAddFanForm"
          >
            立即创建
          </el-button>
          <el-button @click="resetForm('addFanForm')">
            重置
          </el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <el-pagination
      background
      :page-size="10"
      layout="prev, pager, next, jumper"
      :total="total"
      :current-page="currentPage"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      @next-click="goNextPage"
      @prev-click="goPrePage"
    />
  </div>
</template>

<script>
import * as echarts from "echarts";
import {getList} from "@/api/info";
import {addFanApi, deleteFanApi, editFanApi, getFanOverLookApi} from "@/api/fan";

export default {
  name: "FanList",
  data(){
    return{
      currentPage: 1,
      total: 0,
      currentRole:'',
      currentBandName: "",
      role: localStorage.getItem("role"),
      fanVisible: false,
      isFanEdit:false,
      sexOptions:[
        {
          value: '男',
          label: '男'
        },
        {
          value: '女',
          label: '女'
        }   
      ],
      fanData:[
      ],
      formFanInfo:{
        fanName:"",
        fanSex:"",
        fanAge:'',
        fanCareer:'',
        isEdit:false
      },
      addFanInfo:{
        fanName:"",
        fanSex:"",
        fanAge:'',
        fanCareer:'',
        isEdit:false
      },
      fanGenderData:[
      ],
      fanAgeData:[
      ],
      fanRules:{
        姓名:[
          { required: true, message: '请输入歌迷姓名', trigger: 'blur' },
        ],
        性别:[
          { required: true, message: '请选择歌迷性别', trigger: 'change' }
        ],
        年龄:[
          { required: true, message: '请输入歌迷年龄', trigger: 'blur' },
          { min: 12, max: 99, message: '年龄在12到99间', trigger: 'blur' }
        ]
      },
      genderCharts:null,
      ageCharts:null,
      fanNum:0,
      mostLikeSong:'',
    }
  },
  created() {
    let {userInfo} = JSON.parse(localStorage.getItem('userInfo'))
    this.selectBandName = this.currentBandName= userInfo.role==='band'? userInfo.bandName : ''
    this.currentRole = userInfo.role
    this.getFanData()
  },
  mounted() {
    if(this.currentRole === 'band'){
      getFanOverLookApi().then(res=>{
        let {data} = res.data
        this.fanNum = data.fanNum
        this.mostLikeSong = data.mostLikeSong
        this.fanGenderData= data.fanGenderData
        this.fanAgeData = data.fanAgeData
        this.drawGenderPic('genderCharts');
        this.drawAgePic('ageCharts');
      })
    }
  },
  beforeUnmount() {
    if (this.currentRole === 'band') {
      this.genderCharts.dispose();
      this.ageCharts.dispose();
    }
  },
  methods:{
    editFanInfo(row){
      if(this.isFanEdit){
        this.$message({
          message: '请先完成当前编辑',
          type: 'warning'
        });
        return
      }
      row.isEdit = true;
      this.isFanEdit = true
    },
    cancelEditFanInfo(row){
      row.isEdit = false;
      this.isFanEdit = false
    },
    confirmFanInfo(row){
      for(let item in row){
        if(row[item] === '' && item!=='fanCareer'){
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return
        }
      }
      row.isEdit = false;
      this.isFanEdit = false
      this.formFanInfo = row;
      editFanApi(this.formFanInfo).then(res=>{
        this.$message({
          message: '修改成功',
          type: 'success'
        });
        this.getFanData()
      }).catch(()=>{})
    },
    deleteFanInfo(row){
      this.$confirm('此操作将永久删除该粉丝信息, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
       deleteFanApi(row.fanId).then(res=>{
         this.$message({
           message: '删除成功',
           type: 'success'
         });
         this.getFanData()
       }).catch(()=>{})
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });
    },
    iRowStyle({row, rowIndex}) {
      return 'height:65px';
    },
    addFan(){
      if(this.isFanEdit){
        this.$message({
          message: '请先完成当前编辑',
          type: 'warning'
        });
        return
      }
      this.fanVisible = true;

    },
    submitAddFanForm(){
      for(let item in this.addFanInfo){
        if(this.addFanInfo[item] === '' && item!=='fanCareer'){
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return
        }
      }
      console.log(this.addFanInfo)
      this.fanVisible = false;
      this.isFanEdit = false
      addFanApi(this.addFanInfo).then(res=>{
        this.$message({
          message: '添加成功',
          type: 'success'
        });
        this.getFanData()
      }).catch(()=>{})
    },
    drawGenderPic(id) {
      this.genderCharts = echarts.init(document.getElementById(id));
      this.genderCharts.setOption({
        title: {
          text: "男女比例",
        },
        tooltip: {
          trigger: "item",
        },
        legend: {
          top: "5%",
          left: "center",
        },
        series: [
          {
            name: "男女比例",
            type: "pie",
            radius: ["40%", "70%"],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: "center",
            },
            emphasis: {
              label: {
                show: true,
                fontSize: "40",
                fontWeight: "bold",
              },
            },
            labelLine: {
              show: false,
            },
            data: this.fanGenderData
          },
        ],
      });
    },
    drawAgePic(id) {
      this.ageCharts = echarts.init(document.getElementById(id));
      this.ageCharts.setOption({
        title: {
          text: "年龄比例",
        },
        tooltip: {
          trigger: "item",
        },
        legend: {
          top: "5%",
          left: "center",
        },
        series: [
          {
            name: "年龄比例",
            type: "pie",
            // radius: ["40%", "70%"],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: "center",
            },
            emphasis: {
              label: {
                show: true,
                fontSize: "40",
                fontWeight: "bold",
              },
            },
            labelLine: {
              show: false,
            },
            data: this.fanAgeData
          },
        ],
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    getFanData(){
      getList(this.currentPage,10,5).then(res=>{
        let {data} =res.data
        this.fanData = data.fanData
        this.total = data.total
      })
    },
    handleSelectionChange(val) {
      this.bandData = val;
    },
    handleSizeChange(val) {
      this.pageSize = val;
      this.getFanData()
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      this.getFanData()
    },
    goPrePage(){
      this.getFanData()
    },
    goNextPage(){
      this.getFanData()
    },
  }
}
</script>

<style scoped lang="less">
.fans-look{
  padding-top: 20px;
  width: 100%;
  height: 400px;
  display: flex;
  flex-direction: row;
  .fan-left{
    margin-right: 20px;
    width: 25vw;
    display: flex;
    flex-direction: column;
    .cards-num{
      width: 100%;
      height: 200px;
      position: relative;
      overflow: hidden;
      margin-bottom: 20px;
      .desc{
        width: 70%;
        letter-spacing: 2px;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%,-50%);
        font-size: 25px;
        font-weight: 600;
      }
      .cards-img{
        width: 100%;
        position: absolute;
      }
    }
  }
  .fan-right{
    display: flex;
    flex-direction: row;
   justify-content: space-around;
    flex-wrap: wrap;
  }
}
.nums{
  font-family: Yu Gothic Medium;
  font-style: oblique;
  font-size: 60px;
  z-index: 20;
  color:var(--theme--color)
}
.words{
  font-family: Yu Gothic Medium;
  font-style: oblique;
  font-size: 35px;
  z-index: 20;
  color:white;
}
#genderCharts{
  width: 25vw;
  height: 380px;
  box-shadow: 0 0 2rem 0 rgba(41, 48, 66, 0.1);
  margin-right: 20px;
}
#ageCharts{
  width: 25vw;
  height: 380px;
  box-shadow: 0 0 2rem 0 rgba(41, 48, 66, 0.1);
}
</style>
<template>
  <div>
    搜索：
    <el-input
      v-model="searchText"
      placeholder="请输入乐队名称"
      style="width: 200px;margin-top: 20px;margin-right: 20px"

    />
    <span v-permission="['fan']">
    筛选条件：
    <el-select
      v-model="searchType"
      placeholder="请选择"
      style="width: 100px;margin-top: 20px;margin-right: 30px"
      @change="goSearch"
    >
      <el-option
        v-for="item in searchTypeList"
        :key="item.value"
        :label="item.label"
        :value="item.value"
      />
    </el-select>
      </span>
    <el-button
      type="primary"
      @click="goSearch"
    >
      搜索
    </el-button>
    <el-button
      type="danger"
      @click="toggleSearchResult"
    >
      隐藏/显示结果
    </el-button>
    <el-checkbox @change="onlyMyConcert(Number(checked))" v-model="checked" v-permission="['band','notBandThing']" style="margin-left: 10px">只显示自己的</el-checkbox>
    <div class="search-words" v-show="isOnSearch">共计{{searchTotal}}条结果</div>
    <el-table
      v-show="isOnSearch"
      :data="searchConcertData"
      border
      :row-style="iRowStyle"
      style="width: 100%;margin-top: 20px"
    >
      <el-table-column
        prop="bandName"
        label="演出乐队"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.bandName }}</span>
          <el-input
            v-if="scope.row.isEdit && currentRole === 'admin'"
            v-model="scope.row.bandName"
          />
        </template>
      </el-table-column>

      <el-table-column
        prop="holdingTime"
        label="举办时间"
      >
        <template #default="scope">
          <span v-if="!scope.row.isEdit"> {{ scope.row.holdingTime }}</span>
          <el-date-picker
            v-if="scope.row.isEdit"
            v-model="scope.row.holdingTime"
            style="width: 150px;"
            type="datetime"
            placeholder="选择日期"
          />
        </template>
      </el-table-column>
      <el-table-column
        prop="holdingPlace"
        label="举办地点"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.holdingPlace }}</span>
          <el-input
            v-show="scope.row.isEdit"
            v-model="scope.row.holdingPlace"
          />
        </template>
      </el-table-column>
      <el-table-column
        prop="duration"
        label="持续时间"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.duration }}</span>
          <el-input
            v-show="scope.row.isEdit"
            v-model="scope.row.duration"
          />
        </template>
      </el-table-column>
      <el-table-column
        fixed="right"
        label="操作"
        width="200"
      >
        <template #default="scope">
          <el-button
            type="text"
            size="small"
            @click="checkPerformDetail(scope.row)"
          >
            查看详情
          </el-button>
          <el-button
            v-show="currentRole ==='admin' || currentBandName === scope.row.bandName "
            type="text"
            size="small"
            @click="editPerformanceInfo(scope.row)"
          >
            编辑
          </el-button>
          <el-button
            v-show="scope.row.isEdit"
            type="text"
            size="small"
            @click="confirmPerformanceInfo(scope.row)"
          >
            确认
          </el-button>

          <el-button
            v-show="currentRole ==='admin' || currentBandName === scope.row.bandName "
            type="text"
            size="small"
            style="color: red;"
            @click="deletePerformanceInfo(scope.row)"
          >
            删除
          </el-button>
          <div @click="joinPerformance(scope.row)">
            <el-button
              v-show="!scope.row.isLike"
              v-permission="['fan']"
              type="text"
              size="small"
            >
              参加
            </el-button>
            <el-button
              v-show="scope.row.isLike"
              v-permission="['fan']"
              type="text"
              size="small"
              style="color: red;"
            >
              取消参加
            </el-button>
          </div>
        </template>
      </el-table-column>
    </el-table>
    <el-table
      :data="performData"
      border
      :row-style="iRowStyle"
      style="width: 100%;margin-top: 20px"
    >
      <el-table-column
        prop="bandName"
        label="演出乐队"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.bandName }}</span>
          <el-input
            v-if="scope.row.isEdit && currentRole === 'admin'"
            v-model="scope.row.bandName"
          />
        </template>
      </el-table-column>

      <el-table-column
        prop="holdingTime"
        label="举办时间"
      >
        <template #default="scope">
          <span v-if="!scope.row.isEdit"> {{ scope.row.holdingTime }}</span>
          <el-date-picker
            v-if="scope.row.isEdit"
            v-model="scope.row.holdingTime"
            style="width: 150px;"
            type="datetime"
            placeholder="选择日期"
          />
        </template>
      </el-table-column>
      <el-table-column
        prop="holdingPlace"
        label="举办地点"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.holdingPlace }}</span>
          <el-input
            v-show="scope.row.isEdit"
            v-model="scope.row.holdingPlace"
          />
        </template>
      </el-table-column>
      <el-table-column
        prop="duration"
        label="持续时间"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.duration }}</span>
          <el-input
            v-show="scope.row.isEdit"
            v-model="scope.row.duration"
          />
        </template>
      </el-table-column>
      <el-table-column
        fixed="right"
        label="操作"
        width="200"
      >
        <template #default="scope">
          <el-button
            type="text"
            size="small"
            @click="checkPerformDetail(scope.row)"
          >
            查看详情
          </el-button>
          <el-button
            v-show="currentRole ==='admin' || currentBandName === scope.row.bandName "
            type="text"
            size="small"
            @click="editPerformanceInfo(scope.row)"
          >
            编辑
          </el-button>
          <el-button
            v-show="scope.row.isEdit"
            type="text"
            size="small"
            @click="confirmPerformanceInfo(scope.row)"
          >
            确认
          </el-button>

          <el-button
            v-show="currentRole ==='admin' || currentBandName === scope.row.bandName "
            type="text"
            size="small"
            style="color: red;"
            @click="deletePerformanceInfo(scope.row)"
          >
            删除
          </el-button>
          <div @click="joinPerformance(scope.row)">
            <el-button
              v-show="!scope.row.isLike"
              v-permission="['fan']"
              type="text"
              size="small"
            >
              参加
            </el-button>
            <el-button
              v-show="scope.row.isLike"
              v-permission="['fan']"
              type="text"
              size="small"
              style="color: red;"
            >
              取消参加
            </el-button>
          </div>
        </template>
      </el-table-column>
    </el-table>
    <div style="display: flex;justify-content: left;align-items: center">
    <el-button
      v-if="currentRole!== 'fan'"
      type="primary"
      style="margin-top: 20px;margin-right: 20px"
      @click="addPerformance"
    >
      添加演唱会
    </el-button>
      <div style="margin: 20px 0;padding-top: 17px">共计{{ total}}条数据</div>
    </div>
    <el-dialog
      v-model="actingSongVisible"
      title="演出歌单"
      width="40vw"
      center
    >
      <template #title>
        <span>演出详情</span>
      </template>
      <el-button
        v-if="currentBandName === selectBandName"
        type="primary"
        @click="addActingSong"
      >
        添加歌曲
      </el-button>
      <el-table
        :data="actingSongData"
        border
        :row-style="iRowStyle"
        style="width: 100%;margin-top: 20px"
      >
        <el-table-column
          prop="songOrder"
          label="歌曲序号"
        >
          <template #default="scope">
            <span v-show="!scope.row.isEdit"> {{ scope.row.songOrder }}</span>
            <el-input
                v-show="scope.row.isEdit"
                v-model="scope.row.songOrder"
            >
            </el-input>
          </template>
        </el-table-column>
        <el-table-column
          prop="表演时间（分钟）"
          label="表演时间（分钟）"
        >
          <template #default="scope">
            <span v-show="!scope.row.isEdit"> {{ scope.row.duration }}</span>
            <el-input
                v-show="scope.row.isEdit"
                v-model="scope.row.duration"
                type="number"
                min="1"
                onkeyup="this.value=this.value.replace(/^(0+)|[^\d]+/g,'')"
            >
            </el-input>
          </template>
        </el-table-column>
        <el-table-column
          prop="songName"
          label="歌曲名称"
        >
          <template #default="scope">
            <span v-show="!scope.row.isEdit"> {{ scope.row.songName }}</span>
            <el-input
              v-show="scope.row.isEdit"
              v-model="scope.row.songName"
            />
          </template>
        </el-table-column>
        <el-table-column
          v-if="selectBandName===currentBandName && currentBandName!=='fan'"
          fixed="right"
          label="操作"
        >
          <template #default="scope">
            <el-button
              type="text"
              size="small"
              @click="editActingSong(scope.row)"
            >
              编辑
            </el-button>
            <el-button
              v-show="scope.row.isEdit"
              type="text"
              size="small"
              @click="confirmActingSong(scope.row)"
            >
              确认
            </el-button>

            <el-button
              type="text"
              size="small"
              style="color: red;"
              @click="deleteActingSong(scope.row)"
            >
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
    <el-dialog
      v-model="performVisible"
      title="演出详情"
      width="30%"
      center
    >
      <el-form
        ref="performanceForm"
        :model="addPerformInfo"
        :rules="performanceRules"
        label-width="100px"
        class="demo-ruleForm"
      >
        <el-form-item
          label="演出乐队"
          prop="bandName"
          required
          v-if="currentRole === 'admin'"
        >
          <el-input v-model="addPerformInfo.bandName" />
        </el-form-item>
        <el-form-item
          label="举办时间"
          prop="举办时间"
          required
        >
          <el-date-picker
            v-model="addPerformInfo.holdingTime"
            style="width: 150px;"
            type="datetime"
            placeholder="选择日期"
          />
        </el-form-item>
        <el-form-item
          label="举办地点"
          required
          prop="holdingPlace"
        >
          <el-input v-model="addPerformInfo.holdingPlace" />
        </el-form-item>
        <el-form-item
          label="持续时间"
          required
          prop="duration"
        >
          <el-input v-model="addPerformInfo.duration" />
        </el-form-item>
        <el-form-item>
          <el-button
            type="primary"
            @click="submitPerformanceForm"
          >
            立即创建
          </el-button>
          <el-button @click="resetForm('performanceForm')">
            重置
          </el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <el-dialog
      v-model="addActingSongVisible"
      title="歌曲详情"
      width="30%"
      center
    >
      <el-form
        ref="actingSongForm"
        :model="addActingSongInfo"
        :rules="actingSongRules"
        label-width="100px"
        class="demo-ruleForm"
      >

        <el-form-item
          label="歌曲名称"
          prop="songName"
          required
        >
          <el-input v-model="addActingSongInfo.songName" />
        </el-form-item>
        <el-form-item
            label="表演时间（分钟）"
            prop="duration"
            required
        >
          <el-input v-model="addActingSongInfo.duration"
                    type="number"
                    min="1"
                    onkeyup="this.value=this.value.replace(/^(0+)|[^\d]+/g,'')"
          />
        </el-form-item>
        <el-form-item>
          <el-button
            type="primary"
            @click="submitActingSongForm"
          >
            立即创建
          </el-button>
          <el-button @click="resetForm('actingSongForm')">
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
import {formatDateTime} from "@/utils/format";
import {changePerformanceJoin} from "@/utils/like";
import {getList, searchBandApi, searchConcertApi} from "@/api/info";
import {
  addPerformApi,
  addSongPerformApi,
  deletePerformApi,
  deleteSongPerformApi,
  editPerformApi,
  editSongPerformApi
} from "@/api/perform";

export default {
  name: "PerformanceList",
  data(){
    return{
      checked: false,
      searchTotal: 0,
      searchConcertData: [],
      isOnSearch: false,
      searchType: '全部',
      searchTypeList:[
        {
          value: '未关注',
          label: '未关注'
        },
        {
          value: '已关注',
          label: '已关注'
        },
        {
          value: '全部',
          label: '全部'
        }
      ],
      searchText: '',
      currentPage: 1,
      total: 0,
      addBandName: '',
      currentRole: '',
      selectBandName: '',
      currentBandName: '',
      performVisible: false,
      actingSongVisible: false,
      addActingSongVisible: false,
      isPerformEdit:false,
      isActingSongEdit:false,
      performData:[
      ],
      actingSongData:[
      ],
      editPerformInfo:{
        concertId: '',
        bandName: "",
        holdingTime: "",
        holdingPlace: "",
        duration: "",
        isEdit: false
      },
      addPerformInfo:{
        bandName: "",
        holdingTime: "",
        holdingPlace: "",
        duration: "",
        isEdit: false,
        isLike:false
      },
      editActingSongInfo:{
        sheetId: '',
        concertId: '',
        songOrder: "",
        bandName: "",
        songName: "",
        holdingTime: "",
        isEdit: false
      },
      addActingSongInfo:{
        concertId: '',
        duration: "",
        bandName: '',
        songName: "",
        holdingTime: "",
        isEdit: false
      },
      performanceRules: {
        performBand: [
          { required: true, message: "请输入演出乐队", trigger: "blur" }
        ],
        holdingTime: [
          { required: true, message: "请选择举办时间", trigger: "change" }
        ],
        holdingPlace: [
          { required: true, message: "请输入举办地点", trigger: "blur" }
        ]
      },
      actingSongRules: {
        songName: [
          { required: true, message: "请输入歌曲名称", trigger: "blur" }
        ]
      },
      joinInfo:{
        fanName: "",
        fanId: "",
        holdingTime: "",
      },
      currentConcertId: '',
    }
  },
  created() {
    let {userInfo} = JSON.parse(localStorage.getItem('userInfo'))
    this.selectBandName = this.currentBandName = userInfo.role==='band' ? userInfo.bandName : ''
    this.currentRole = userInfo.role
    this.getPerformData()
  },
  methods:{
    formatDateTime,
    changePerformanceJoin,
    checkPerformDetail(row){
      if(this.isPerformEdit){
        this.$message({
          message: '请先保存当前编辑的演出信息',
          type: 'warning'
        });
        return
      }
      this.actingSongVisible = true;
      this.actingSongData = row.actingSongData;
      this.editActingSongInfo.concertId = row.concertId;
      this.currentConcertId = row.concertId;
      if(this.currentRole ==='admin'){
      }else{
        this.selectBandName = row.bandName;
      }
      this.addBandName = row.bandName;
    },
    editPerformanceInfo(row){
      if(this.isPerformEdit){
        this.$message({
          message: '请先完成当前编辑',
          type: 'warning'
        });
        return
      }
      this.isPerformEdit = true
      row.isEdit = true
    },
    cancelEditPerformanceInfo(row){
      row.isEdit = false;
      this.isPerformEdit = false
    },
    confirmPerformanceInfo(row){
      for(let item in row){
        if(item ==='holdingTime' && row['holdingTime'] === null){
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return;
        }
        if(row[item] === ''){
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return
        }
      }
      row.isEdit = false;
      this.isPerformEdit = false
      this.editPerformInfo = row;
      this.editPerformInfo.holdingTime = this.formatDateTime(this.editPerformInfo.holdingTime)
      editPerformApi(this.editPerformInfo).then(res=>{
        this.$message({
          message: '修改成功',
          type: 'success'
        });

        this.getPerformData()
      }).catch(()=>{})
    },
    addPerformance(){
      if(this.isPerformEdit){
        this.$message({
          message: '请先完成当前编辑',
          type: 'warning'
        });
        return
      }
      this.addPerformInfo.bandName = this.currentBandName
      this.performVisible = true
    },
    deletePerformanceInfo(row){
      this.$confirm('此操作将永久删除该演出信息, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deletePerformApi(row.concertId).then(res=>{
          this.$message({
            message: '删除成功',
            type: 'success'
          });
          this.getPerformData()
        }).catch(()=>{})
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });
    },
    editActingSong(row) {
      if(this.isActingSongEdit){
        this.$message({
          message: '请先完成当前编辑',
          type: 'warning'
        });
        return
      }

      this.isActingSongEdit = true
      row.isEdit = true
    },
    cancelEditActingSong(row) {
      row.isEdit = false;
      this.isActingSongEdit = false
    },
    confirmActingSong(row) {
      for(let item in row){
        if(row[item] === ''){
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return
        }
      }
      row.isEdit = false;
      this.isActingSongEdit = false
      this.editActingSongInfo = row;
      this.editActingSongInfo.holdingTime = this.formatDateTime(this.editActingSongInfo.holdingTime)
      editSongPerformApi(this.editActingSongInfo).then(res=>{
        this.$message({
          message: '修改成功',
          type: 'success'
        });
        this.getPerformData()
      }).catch(()=>{
        this.getPerformData()
      })
    },
    addActingSong(){
      if(this.isPerformEdit){
        this.$message({
          message: '请先完成当前编辑',
          type: 'warning'
        });
        return
      }
      if(this.currentBandName!==this.selectBandName){
        this.$message({
          message: '您没有权限添加该乐队的演出信息',
          type: 'error'
        });
        return
      }
      this.addActingSongVisible = true

    },
    deleteActingSong(row){
      this.$confirm('此操作将永久删除该歌单信息, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        console.log(row)
        deleteSongPerformApi(row.sheetId,this.currentConcertId).then(res=>{
          this.$message({
            message: '删除成功',
            type: 'success'
          });
          this.getPerformData()
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
    submitPerformanceForm(){
      console.log(this.addPerformInfo)
      for (let item in this.addPerformInfo) {
        if (item === 'holdingTime' && this.addPerformInfo['holdingTime'] === null) {
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return;
        }
        if (this.addPerformInfo[item] === '') {
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return
        }
      }
      this.performVisible = false
      this.isPerformEdit = false
      this.addPerformInfo.holdingTime = this.formatDateTime(this.addPerformInfo.holdingTime)
      addPerformApi(this.addPerformInfo).then(res=>{
        this.$message({
          message: '添加成功',
          type: 'success'
        });
        this.getPerformData()
      }).catch(()=>{})
    },
    submitActingSongForm(){
      this.addActingSongInfo.concertId = this.currentConcertId
      this.addActingSongInfo.bandName = this.addBandName;
      this.addActingSongInfo.holdingTime = this.formatDateTime(this.addActingSongInfo.holdingTime)
      for (let item in this.addActingSongInfo) {
        if (this.addActingSongInfo[item] === "") {
          console.log(item)
          this.$message({
            message: "请填写完整信息",
            type: "warning"
          });
          return;
        }
      }
      this.addActingSongVisible = false
      this.isActingSongEdit = false
      addSongPerformApi(this.addActingSongInfo).then(res=>{
        this.$message({
          message: '添加成功',
          type: 'success'
        });
        this.getPerformData()
      }).catch(()=>{})
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    joinPerformance(row){
      this.joinInfo.holdingTime = row.holdingTime
      this.changePerformanceJoin(row)
      console.log(this.joinInfo)
    },
    onlyMyConcert(checked){
      this.getPerformData(checked)
    },
    getPerformData(param=0){
      getList(this.currentPage,10,4,param).then(res=>{
        let {data} = res.data
        this.performData = data.performData
        this.total = data.total
        this.actingSongVisible = false;
      })
    },
    handleSelectionChange(val) {
      this.bandData = val;
    },
    handleSizeChange(val) {
      this.pageSize = val;
      this.getPerformData()
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      this.getPerformData()
    },
    goPrePage(){
      this.getPerformData()
    },
    goNextPage(){
      this.getPerformData()
    },
    goSearch(){
      this.isOnSearch = true
      let searchText = this.searchText;
      let searchType = this.searchType;
      searchConcertApi({searchText,searchType}).then(res=>{
        let {data} = res.data
        this.searchConcertData = data.searchConcertData
        this.searchTotal = data.total
      })
    },
    toggleSearchResult(){
      this.isOnSearch = !this.isOnSearch
    },
  }
}
</script>

<style scoped>
.search-words{
  margin: 20px 0;
  letter-spacing: 3px;
}
</style>
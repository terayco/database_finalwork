<template>
  <div>
    搜索：
    <el-input
      v-model="searchText"
      placeholder="请输入专辑名称"
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
    <el-checkbox @change="onlyMyAlbum(Number(checked))" v-model="checked" v-permission="['band','notBandThing']" style="margin-left: 10px">只显示自己的</el-checkbox>
    <div class="search-words" v-show="isOnSearch">共计{{searchTotal}}条结果</div>
    <el-table
      v-show="isOnSearch"
      :data="searchAlbumData"
      border
      :row-style="iRowStyle"
      style="width: 100%;margin-top: 20px"
    >
      <el-table-column
        prop="bandName"
        label="专辑名称"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.albumName }}</span>
          <el-input
            v-show="scope.row.isEdit"
            v-model="scope.row.albumName"
          />
        </template>
      </el-table-column>
      <el-table-column
        prop="performBand"
        label="乐队名称"
      >
        <template #default="scope">
          <span v-if="!scope.row.isEdit"> {{ scope.row.performBand }}</span>
          <el-input
            v-if="scope.row.isEdit && currentRole === 'admin'"
            v-model="scope.row.performBand"
          />
        </template>
      </el-table-column>
      <el-table-column
        prop="releaseTime"
        label="发行时间"
      >
        <template #default="scope">
          <span v-if="!scope.row.isEdit"> {{ scope.row.releaseTime }}</span>
          <el-date-picker
            v-if="scope.row.isEdit"
            v-model="scope.row.releaseTime"
            style="width: 150px;"
            type="date"
            placeholder="选择日期"
          />
        </template>
      </el-table-column>
      <el-table-column
        prop="releaseCompany"
        label="发行公司"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.releaseCompany }}</span>
          <el-input
            v-show="scope.row.isEdit"
            v-model="scope.row.releaseCompany"
          />
        </template>
      </el-table-column>
      <el-table-column
        v-show="searchType === '未关注' && currentRole === 'band'"
        fixed="right"
        label="操作"
        width="200"
      >
        <template #default="scope">
          <el-button
            v-show="currentRole === 'admin' || currentBandName === scope.row.performBand"
            type="text"
            size="small"
            @click="editAlbum(scope.row)"
          >
            编辑
          </el-button>
          <el-button
            v-show="scope.row.isEdit"
            type="text"
            size="small"
            @click="confirmAlbumInfo(scope.row)"
          >
            确认
          </el-button>
          <el-button
            v-show="currentRole === 'admin' || currentBandName === scope.row.performBand"
            type="text"
            size="small"
            style="color: red"
            @click="deleteAlbum(scope.row)"
          >
            删除
          </el-button>
          <div
            v-permission="['band','fan']"
            @click="changeAlbumLike(scope.row)"
          >
            <i
              v-show="!scope.row.isLike"
              class="iconfont icon-jurassic_love"
            />
            <i
              v-show="scope.row.isLike"
              class="iconfont icon-jurassic_love1"
            />
          </div>
        </template>
      </el-table-column>
    </el-table>
    <el-table
      :data="albumData"
      border
      :row-style="iRowStyle"
      style="width: 100%;margin-top: 20px"
    >
      <el-table-column
        prop="bandName"
        label="专辑名称"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.albumName }}</span>
          <el-input
            v-show="scope.row.isEdit"
            v-model="scope.row.albumName"
          />
        </template>
      </el-table-column>

      <el-table-column
        prop="performBand"
        label="乐队名称"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.performBand }}</span>
          <el-input
            v-if="scope.row.isEdit && currentRole === 'admin'"
            v-model="scope.row.performBand"
          />
        </template>
      </el-table-column>
      <el-table-column
        prop="releaseTime"
        label="发行时间"
      >
        <template #default="scope">
          <span v-if="!scope.row.isEdit"> {{ scope.row.releaseTime }}</span>
          <el-date-picker
            v-if="scope.row.isEdit"
            v-model="scope.row.releaseTime"
            style="width: 150px;"
            type="date"
            placeholder="选择日期"
          />
        </template>
      </el-table-column>
      <el-table-column
        prop="releaseCompany"
        label="发行公司"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.releaseCompany }}</span>
          <el-input
            v-show="scope.row.isEdit"
            v-model="scope.row.releaseCompany"
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
            v-show="currentRole === 'admin' || currentBandName === scope.row.performBand"
            type="text"
            size="small"
            @click="editAlbum(scope.row)"
          >
            编辑
          </el-button>
          <el-button
            v-show="scope.row.isEdit"
            type="text"
            size="small"
            @click="confirmAlbumInfo(scope.row)"
          >
            确认
          </el-button>
          <el-button
            v-show="currentRole === 'admin' || currentBandName === scope.row.performBand"
            type="text"
            size="small"
            style="color: red"
            @click="deleteAlbum(scope.row)"
          >
            删除
          </el-button>
          <div
            v-permission="['band','fan']"
            @click="changeAlbumLike(scope.row)"
          >
            <i
              v-show="!scope.row.isLike"
              class="iconfont icon-jurassic_love"
            />
            <i
              v-show="scope.row.isLike"
              class="iconfont icon-jurassic_love1"
            />
          </div>
        </template>
      </el-table-column>
    </el-table>
    <div style="display: flex;justify-content: left;align-items: center">
    <el-button
      v-if="currentRole!=='fan'"
      type="primary"
      style="margin-top: 20px;margin-right: 20px"
      @click="addAlbum"
    >
      添加专辑
    </el-button>
      <div style="margin: 20px 0;padding-top: 17px">共计{{ total}}条数据</div>
    </div>
    <el-dialog
      v-model="albumVisible"
      title="提示"
      width="30vw"
      center
    >
      <el-form
        ref="addAlbumForm"
        :model="addAlbumInfo"
        :rules="albumRules"
        label-width="100px"
        class="demo-ruleForm"
      >
        <el-form-item
          label="专辑名称"
          prop="bandName"
          required
        >
          <el-input v-model="addAlbumInfo.albumName" />
        </el-form-item>
        <el-form-item
          v-if="currentRole==='admin'"
          label="乐队名称"
          prop="performBand"
        >
          <el-input v-model="addAlbumInfo.performBand" />
        </el-form-item>
        <el-form-item
          label="发行时间"
          required
        >
          <el-col :span="11">
            <el-form-item prop="releaseTime">
              <el-date-picker
                v-model="addAlbumInfo.releaseTime"
                type="date"
                placeholder="选择日期"
                style="width: 100%;"
              />
            </el-form-item>
          </el-col>
        </el-form-item>
        <el-form-item
          label="发行公司"
          prop="releaseCompany"
        >
          <el-input v-model="addAlbumInfo.releaseCompany" />
        </el-form-item>
        <el-form-item>
          <el-button
            type="primary"
            @click="submitAddAlbumForm"
          >
            立即创建
          </el-button>
          <el-button @click="resetForm('addAlbumForm')">
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
import {formatTime} from "@/utils/format";
import {changeAlbumLike} from "@/utils/like";
import {getList, searchAlbumApi, searchBandApi} from "@/api/info";
import {addAlbumApi, deleteAlbumApi, editAlbumApi} from "@/api/album";

export default {
  name: "AlbumList",
  data(){
    return{
      checked: false,
      searchTotal: 0,
      searchAlbumData:[],
      isOnSearch: false,
      searchText: '',
      searchTypeList:[
        {
          value:'已关注',
          label:'已关注'
        },
        {
          value:'未关注',
          label:'未关注'
        },
        {
          value:'全部',
          label:'全部'
        }
      ],
      searchType:'全部',
      currentPage: 1,
      total: 0,
      currentRole:'',
      currentBandName: '',
      albumVisible: false,
      isAlbumEdit:false,
      albumData:[
      ],
      addAlbumInfo:{
        albumName:"",
        performBand:"",
        releaseTime:"",
        releaseCompany:"",
        isEdit:false,
        isLike:false
      },
      editAlbumInfo:
        {
          albumId:"",
          albumName:"",
          performBand:"",
          releaseTime:"",
          releaseCompany:"",
          isEdit:false,
          isLike: false
        },
      albumRules:{
        albumName:[
          {required:true,message:"请输入专辑名称",trigger:"blur"}
        ],
        performBand:[
          {required:true,message:"请输入表演乐队",trigger:"blur"}
        ],
        releaseTime:[
          {required:true,message:"请输入发行时间",trigger:"blur"}
        ],
        releaseCompany:[
          {required:true,message:"请输入发行公司",trigger:"blur"}
        ]
      }
    }
  },
  created() {
    let {userInfo} = JSON.parse(localStorage.getItem('userInfo'))
    this.currentBandName= userInfo.role==='band'? userInfo.bandName : ''
    this.currentRole = userInfo.role
    this.getAlbumData()
  },
  methods:{
    formatTime,
    changeAlbumLike,
    editAlbum(row){
      if(this.isAlbumEdit){
        this.$message({
          message: '请先完成当前编辑',
          type: 'warning'
        });
        return
      }
      row.isEdit = true;
      this.isAlbumEdit = true
    },
    cancelEditAlbumInfo(row){
      row.isEdit = false;
      this.isAlbumEdit = false
    },
    confirmAlbumInfo(row){
      for(let item in row){
        if(item ==='releaseTime' && row['releaseTime'] === null){
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return;
        }
        if( row[item] === ''){
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return
        }
      }
      row.isEdit = false;
      this.isAlbumEdit = false
      this.editAlbumInfo = row;
      editAlbumApi(this.editAlbumInfo).then(res=>{
        console.log(res)
        this.$message({
          message: '修改成功',
          type: 'success'
        });
        this.getAlbumData()
      }).catch(()=>{})
    },
    iRowStyle({row, rowIndex}) {
      return 'height:65px';
    },
    addAlbum(){
      this.albumVisible = true
    },
    deleteAlbum(row){
      this.$confirm('此操作将永久删除该专辑, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteAlbumApi(row.albumId).then(res=>{
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
          this.getAlbumData()
        }).catch(()=>{})
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });
    },
    submitAddAlbumForm() {
      if(this.currentRole==='admin'){
      }else{
        this.addAlbumInfo.performBand = this.currentBandName
      }
      for (let item in this.addAlbumInfo) {
        if (item === 'releaseTime' && this.addAlbumInfo['releaseTime'] === null) {
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return;
        }
        if (this.addAlbumInfo[item] === '') {
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return
        }
      }
      this.albumVisible = false;
      this.addAlbumInfo.releaseTime = this.formatTime(this.addAlbumInfo.releaseTime)
      addAlbumApi(this.addAlbumInfo).then(res=>{
        console.log(res)
        this.$message({
          message: '添加成功',
          type: 'success'
        });
        this.getAlbumData()
      }).catch(()=>{})
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    onlyMyAlbum(checked){
      this.getAlbumData(checked)
    },
    getAlbumData(params=0){
      getList(this.currentPage,10,2,params).then(res=>{
        let {data} = res.data
        this.albumData = data.albumData
        this.total = data.total
      })
    },
    handleSelectionChange(val) {
      this.albumData = val;
    },
    handleSizeChange(val) {
      this.pageSize = val;
      this.getAlbumData()
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      this.getAlbumData()
    },
    goPrePage(){
      this.getAlbumData()
    },
    goNextPage(){
      this.getAlbumData()
    },
    goSearch(){
      this.isOnSearch = true
      let searchText = this.searchText;
      let searchType = this.searchType;
      searchAlbumApi({searchText,searchType}).then(res=>{
        let {data} = res.data
        this.searchAlbumData = data.searchAlbumData
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
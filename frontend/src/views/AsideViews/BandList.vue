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
    <el-checkbox @change="onlyMyBand(Number(checked))" v-model="checked" v-permission="['band','notBandThing']" style="margin-left: 10px">只显示自己的</el-checkbox>
    <div class="search-words" v-show="isOnSearch">共计{{searchTotal}}条结果</div>
    <el-table
      v-show="isOnSearch"
      :data="searchBandData"
      border
      :row-style="iRowStyle"
      style="width: 100%;margin-top: 20px"
    >
      <el-table-column
        prop="name"
        label="乐队ID"
        v-permission="['admin']"
      >
        <template #default="scope">
         {{scope.row.bandId}}
        </template>
      </el-table-column>
      <el-table-column
        prop="bandName"
        label="乐队名称"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.bandName }}</span>
          <el-input
            v-show="scope.row.isEdit"
            v-model="scope.row.bandName"
          />
        </template>
      </el-table-column>
      <el-table-column
        prop="bandLeader"
        label="队长"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.bandLeader }}</span>
          <el-input
            v-show="scope.row.isEdit"
            v-model="scope.row.bandLeader"
          />
        </template>
      </el-table-column>
      <el-table-column
        prop="fundationTime"
        label="成立时间"
      >
        <template #default="scope">
          <span v-if="!scope.row.isEdit"> {{ scope.row.fundationTime }}</span>
          <el-date-picker
            v-if="scope.row.isEdit"
            v-model="scope.row.fundationTime"
            style="width: 150px;"
            type="date"
            placeholder="选择日期"
          />
        </template>
      </el-table-column>
      <el-table-column
        prop="bandNumber"
        label="乐队人数"
      >
        <template #default="scope">
          <span> {{ scope.row.bandNumber }}</span>
        </template>
      </el-table-column>
      <el-table-column
        prop="albumNumber"
        label="发行专辑数量"
      >
        <template #default="scope">
          <span> {{ scope.row.albumNumber }}</span>
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
            @click="checkMember(scope.row)"
          >
            查看成员信息
          </el-button>
          <el-button
            v-show="currentRole ==='admin' || currentBandName === scope.row.bandName"
            type="text"
            size="small"
            @click="editBandInfo(scope.row)"
          >
            编辑
          </el-button>
          <el-button
            v-show="scope.row.isEdit"
            type="text"
            size="small"
            @click="confirmBandInfo(scope.row)"
          >
            确认
          </el-button>
          <el-button
            v-permission="['admin']"
            type="text"
            size="small"
            style="color: red"
            @click="deleteBandInfo(scope.row)"
          >
            删除
          </el-button>
          <div
            v-permission="['fan','band']"
            @click="changeBandLike(scope.row)"
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
      :data="bandData"
      border
      :row-style="iRowStyle"
      style="width: 100%;margin-top: 20px"
      @selection-change="handleSelectionChange"
    >
      <el-table-column
          prop="name"
          label="乐队ID"
          v-permission="['admin']"
      >
        <template #default="scope">
          {{scope.row.bandId}}
        </template>
      </el-table-column>
      <el-table-column
        prop="bandName"
        label="乐队名称"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.bandName }}</span>
          <el-input
            v-show="scope.row.isEdit"
            v-model="scope.row.bandName"
          />
        </template>
      </el-table-column>

      <el-table-column
        prop="bandLeader"
        label="队长"
      >
        <template #default="scope">
          <span v-show="!scope.row.isEdit"> {{ scope.row.bandLeader }}</span>
          <el-input
            v-show="scope.row.isEdit"
            v-model="scope.row.bandLeader"
          />
        </template>
      </el-table-column>
      <el-table-column
        prop="fundationTime"
        label="成立时间"
      >
        <template #default="scope">
          <span v-if="!scope.row.isEdit"> {{ scope.row.fundationTime }}</span>
          <el-date-picker
            v-if="scope.row.isEdit"
            v-model="scope.row.fundationTime"
            style="width: 150px;"
            type="date"
            placeholder="选择日期"
          />
        </template>
      </el-table-column>
      <el-table-column
        prop="bandNumber"
        label="乐队人数"
      >
        <template #default="scope">
          <span> {{ scope.row.bandNumber }}</span>
        </template>
      </el-table-column>
      <el-table-column
        prop="albumNumber"
        label="发行专辑数量"
      >
        <template #default="scope">
          <span> {{ scope.row.albumNumber }}</span>
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
            @click="checkMember(scope.row)"
          >
            查看成员信息
          </el-button>
          <el-button
            v-show="currentRole ==='admin' || currentBandName === scope.row.bandName"
            type="text"
            size="small"
            @click="editBandInfo(scope.row)"
          >
            编辑
          </el-button>
          <el-button
            v-show="scope.row.isEdit"
            type="text"
            size="small"
            @click="confirmBandInfo(scope.row)"
          >
            确认
          </el-button>
          <el-button
            v-permission="['admin']"
            type="text"
            size="small"
            style="color: red"
            @click="deleteBandInfo(scope.row)"
          >
            删除
          </el-button>
          <div
            v-permission="['fan','band']"
            @click="changeBandLike(scope.row)"
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
      v-permission="['admin']"
      type="primary"
      style="margin-top: 20px;margin-right: 20px"
      @click="addBand"
    >
      添加乐队
    </el-button>
    <div style="margin: 20px 0;padding-top: 17px">共计{{ total}}条数据</div>
    </div>
    <el-dialog
      v-model="showBandMember"
      title="乐队成员"
      width="85vw"
      center
    >
      <el-button 
        v-if="currentBandName === selectBandName"
        type="primary"
        @click="addMember"
      >
        添加成员
      </el-button>
      <el-table
        :data="memberData"
        border
        :row-style="iRowStyle"
        style="width: 100%;"
      >
        <el-table-column
          property="memberId"
          label="成员ID"
        >
          <template #default="scope">
            <span>{{ scope.row.memberId }}</span>
          </template>
        </el-table-column>
        <el-table-column
          property="memberName"
          label="姓名"
        >
          <template #default="scope">
            <span v-show="!scope.row.isEdit">{{ scope.row.memberName }}</span>
            <el-input
              v-show="scope.row.isEdit"
              v-model="scope.row.memberName"
            />
          </template>
        </el-table-column>
        <el-table-column
          property="bandName"
          label="所属乐队"
        >
          <template #default="scope">
            <span>{{ scope.row.bandName }}</span>
          </template>
        </el-table-column>
        <el-table-column
          property="memberSex"
          label="性别"
        >
          <template #default="scope">
            <span v-show="!scope.row.isEdit">{{ scope.row.memberSex }}</span>
            <el-select
              v-show="scope.row.isEdit"
              v-model="scope.row.memberSex"
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
          property="memberAge"
          label="年龄"
        >
          <template #default="scope">
            <span v-show="!scope.row.isEdit">{{ scope.row.memberAge }}</span>
            <el-input
              v-show="scope.row.isEdit"
              v-model="scope.row.memberAge"
              type="number"
              min="12"
              max="99"
              onkeyup="this.value=this.value.replace(/^(0+)|[^\d]+/g,'')"
            />
          </template>
        </el-table-column>
        <el-table-column
          property="memberJob"
          label="乐队分工"
        >
          <template #default="scope">
            <span v-show="!scope.row.isEdit">{{ scope.row.memberJob }}</span>
            <el-input
              v-show="scope.row.isEdit"
              v-model="scope.row.memberJob"
            />
          </template>
        </el-table-column>
        <el-table-column
          property="memberPosition"
          label="职位"
        >
          <template #default="scope">
            <span v-show="!scope.row.isEdit">{{ scope.row.memberPosition }}</span>
            <el-select
              v-show="scope.row.isEdit"
              v-model="scope.row.memberPosition"
              placeholder="请选择"
            >
              <el-option
                v-for="item in positionOptions"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </template>
        </el-table-column>
        <el-table-column
          property="joinTime"
          label="加入时间"
          width="150"
        >
          <template #default="scope">
            <span v-if="!scope.row.isEdit"> {{ scope.row.joinTime }}</span>
            <el-date-picker
              v-if="scope.row.isEdit"
              v-model="scope.row.joinTime"
              style="width: 120px;"
              type="date"
              placeholder="选择日期"
              format="YYYY-MM-DD"
            />
          </template>
        </el-table-column>
        <el-table-column
          property="leaveTime"
          label="离开时间"
          width="150"
        >
          <template #default="scope">
            <span v-if="!scope.row.isEdit">{{ scope.row.leaveTime }}</span>
            <el-date-picker
              v-if="scope.row.isEdit"
              v-model="scope.row.leaveTime"
              style="width: 120px;"
              type="date"
              placeholder="选择日期"
              format="YYYY-MM-DD"
            />
          </template>
        </el-table-column>
        <el-table-column
          v-if="selectBandName===currentBandName && currentBandName!=='fan'"
          fixed="right"
          label="操作"
          width="160"
        >
          <template #default="scope">
            <el-button
              type="text"
              size="small"
              @click="editMemberInfo(scope.row)"
            >
              编辑
            </el-button>
            <el-button
              v-show="scope.row.isEdit"
              type="text"
              size="small"
              @click="confirmMemberInfo(scope.row)"
            >
              确认
            </el-button>
            <el-button
              type="text"
              size="small"
              style="color:red"
              @click="deleteMemberInfo(scope.row)"
            >
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
    <el-dialog
      v-model="addBandDialog"
      width="32vw"
      title="乐队信息"
      center
    >
      <el-form
        ref="bandForm"
        :model="addBandInfo"
        :rules="bandRules"
        label-width="100px"
        class="demo-ruleForm"
      >
        <el-form-item
          label="乐队名称"
          prop="bandName"
        >
          <el-input v-model="addBandInfo.bandName" />
        </el-form-item>
        <el-form-item
          label="乐队ID"
          prop="bandId"
        >
          <el-input
            v-model="addBandInfo.bandId"
          />
        </el-form-item>
        <el-form-item
          label="乐队密码"
          prop="bandPwd"
          required
        >
          <el-input
            v-model="addBandInfo.bandPwd"
            type="password"
          />
        </el-form-item>
        <el-form-item
          label="队长"
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
              v-for="item in sexOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item
          label="队长年龄"
          prop="bandLeaderAge"
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
          label="队长分工"
          prop="bandLeaderJob"
        >
          <el-input v-model="addBandInfo.memberData[0].memberJob" />
        </el-form-item>
        
        <el-form-item
          label="乐队人数"
          prop="bandNumber"
        >
          {{ addBandInfo.bandNumber }}
        </el-form-item>
        <el-form-item
          label="成立时间"
          required
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
        <el-form-item>
          <el-button
            type="primary"
            @click="submitBandForm"
          >
            立即创建
          </el-button>
          <el-button @click="resetForm('bandForm')">
            重置
          </el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <el-dialog
      v-model="addMemberDialog"
      width="32vw"
      title="成员信息"
      center
    >
      <el-form
        ref="MemberForm"
        :model="addMemberInfo"
        :rules="memberRules"
        label-width="100px"
        class="demo-ruleForm"
      >
        <el-form-item
          label="成员姓名"
          prop="memberName"
          required
        >
          <el-input v-model="addMemberInfo.memberName" />
        </el-form-item>
        <el-form-item
          prop="memberSex"
          label="性别"
          required
        >
          <el-select
            v-model="addMemberInfo.memberSex"
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
          prop="memberAge"
          required
        >
          <el-input
            v-model="addMemberInfo.memberAge"
            type="number"
            min="12"
            max="99"
            onkeyup="this.value=this.value.replace(/^(0+)|[^\d]+/g,'')"
          />
        </el-form-item>
        <el-form-item
          label="乐队分工"
          prop="memberJob"
        >
          <el-input v-model="addMemberInfo.memberJob" />
        </el-form-item>
        <el-form-item
          label="职位"
          prop="memberPosition"
        >
          <el-select
            v-model="addMemberInfo.memberPosition"
            placeholder="请选择"
          >
            <el-option
              v-for="item in positionOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item
          label="加入时间"
          required
        >
          <el-col :span="11">
            <el-form-item prop="joinTime">
              <el-date-picker
                v-model="addMemberInfo.joinTime"
                type="date"
                placeholder="选择日期"
                style="width: 100%;"
                format="YYYY-MM-DD"
              />
            </el-form-item>
          </el-col>
        </el-form-item>
        <el-form-item
          label="离开时间"
        >
          <el-col :span="11">
            <el-form-item prop="leaveTime">
              <el-date-picker
                v-model="addMemberInfo.leaveTime"
                type="date"
                placeholder="选择日期"
                style="width: 100%;"
                format="YYYY-MM-DD"
              />
            </el-form-item>
          </el-col>
        </el-form-item>
        <el-form-item>
          <el-button
            type="primary"
            @click="submitMemberForm"
          >
            立即创建
          </el-button>
          <el-button @click="resetForm('MemberForm')">
            重置
          </el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
    <el-row justify="center">
      <el-col
        :xs="24"
        :sm="24"
        :md="10"
        :lg="11"
        :xl="10"
        style="margin-right: 40px"
      >
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

      </el-col>
    </el-row>
  </div>
</template>

<script>
import {bandStore} from '@/store/band'
import {getList, searchBandApi} from "@/api/info";
import {formatTime,compareTime} from "@/utils/format";
import {changeBandLike} from "@/utils/like";
import {addBandApi, addMemberApi, deleteBandApi, deleteMemberApi, editBandApi, editMemberApi} from "@/api/band";

const store = bandStore()
export default {
  name: "BandList",
  data(){
    return{
      checked: false,
      searchTotal:0,
      searchBandData:[],
      isOnSearch:false,
      searchType: '全部',
      searchTypeList:[
        {value:'已关注',label:'已关注'},
        {value:'未关注',label:'未关注'},
        {value:'全部',label:'全部'},
      ],
      searchText:'',
      type:1,
      pageSize: 10,
      total: 0,
      currentPage: 1,

      addBandName:'',
      currentRole:'',
      currentBandName: '',
      selectBandName: '',
      addBandDialog: false,
      addMemberDialog: false,
      sexOptions: [
        {
          value: '男',
          label: '男'
        },
        {
          value: '女',
          label: '女'
        }
      ],
      positionOptions: [
        {
          value: '队长',
          label: '队长'
        },
        {
          value: '队员',
          label: '队员'
        },
      ],
      isBandEdit: false,
      isMemberEdit: false,
      showBandMember: false,
      bandData: [
      ],
      memberData:[
      ],
      formBandInfo: {
        bandId: '',
        bandName: '',
        bandLeader: '',
        fundationTime: '',
        bandNumber: '',
        albumNumber: '',
        isEdit: false,
      },
      formMemberInfo:{
        memberId: '',
        memberName: '',
        bandName: '',
        memberSex: '',
        memberAge: '',
        memberJob: '',
        memberPosition: '',
        joinTime: '',
        leaveTime: '',
        isEdit: false
      },
      addBandInfo:{
        bandName: '',
        bandId: '',
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
      bandRules: {
        bandName: [
          { required: true, message: '请输入乐队名称', trigger: 'blur' },
        ],
        bandId: [
          { required: true, message: '请输入乐队ID', trigger: 'blur' },
          { min: 1,  message: '至少大于1', trigger: 'blur' }
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
      addMemberInfo:{
        memberName: '',
        bandName: '',
        memberSex: '',
        memberAge: 18,
        memberJob: '',
        memberPosition: '',
        joinTime: '',
        leaveTime: '',
        isEdit: false
      },
      memberRules:{
        bandName: [
          { required: true, message: '请选择乐队', trigger: 'change' },
        ],
        memberName: [
          { required: true, message: '请输入成员姓名', trigger: 'blur' },
        ],
        memberSex: [
          { required: true, message: '请选择成员性别', trigger: 'change' },
        ],
        memberAge: [
          { required: true, message: '请输入成员年龄', trigger: 'blur' },
          { min: 12, max: 99, message: '年龄在12-99间', trigger: 'blur' }
        ],
        memberPosition: [
          { required: true, message: '请选择成员职位', trigger: 'blur' },
        ],
        joinTime: [
          { required: true, message: '请选择加入时间', trigger: 'change' }
        ],

      },
    }
  },

  created() {
    let {userInfo} = JSON.parse(localStorage.getItem('userInfo'))
    this.selectBandName = this.currentBandName = userInfo.role==='band' ? userInfo.bandName : ''
    this.currentRole = userInfo.role
    this.getBandData()
},
  methods:{
    formatTime,compareTime,
    changeBandLike,
    checkMember(row){
      if(this.isBandEdit){
        this.$message({
          message: '请先保存乐队信息',
          type: 'warning'
        });
        return
      }
      this.showBandMember= true;
      this.memberData = row.memberData
      if(this.currentRole ==='admin'){
      }else{
        this.selectBandName = row.bandName
      }
      this.addMemberInfo.bandName = row.bandName
    },
    editBandInfo(row){
      if(this.isBandEdit){
        this.$message({
          message: '请先完成当前编辑',
          type: 'warning'
        });
        return
      }
      this.isBandEdit = true;
      row.isEdit = true;
    },
    cancelEditBandInfo(row){
      row.isEdit = false;
      this.isBandEdit = false;
      let {initBandInfo} = localStorage.getItem('bandInfo')
      row = initBandInfo
    },
    confirmBandInfo(row){
      if(row.bandNumber < 1){
        this.$message({
          message: '乐队人数不能小于1，不能为空',
          type: 'warning'
        });
        return
      }
      this.isBandEdit = false;
      for(let item in row){
        if(item === 'fundationTime' && row[item] === null){
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return
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
      this.formBandInfo = row;
      this.formBandInfo.fundationTime = this.formatTime(this.formBandInfo.fundationTime)
      // console.log(this.formBandInfo)
      editBandApi(this.formBandInfo).then(res=>{
        this.$message({
          message: '修改成功',
          type: 'success'
        });
        this.getBandData()
      })
    },
    addBand(){
      if(this.isBandEdit){
        this.$message({
          message: '请先完成当前编辑',
          type: 'warning'
        });
        return
      }
      this.addBandDialog = true;

    },
    deleteBandInfo(row){
      this.$confirm('此操作将永久删除该乐队, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteBandApi(row.bandId).then(res=>{
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
          this.getBandData()
        }).catch(()=>{})
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });
    },
    editMemberInfo(row){
      if(this.isMemberEdit){
        this.$message({
          message: '请先完成当前编辑',
          type: 'warning'
        });
        return
      }
      this.formMemberInfo.joinTime = row.joinTime
      this.formMemberInfo.leaveTime = row.leaveTime
      this.isMemberEdit = true;
      row.isEdit = true;
    },
    cancelEditMemberInfo(row){
      row.isEdit = false;
      this.isMemberEdit = false;

    },
    confirmMemberInfo(row){
      for(let item in row){
        if(item ==='joinTime' && row['joinTime'] === null){
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return;
        }
        if(row[item] === '' && item !=='memberJob' && item !== 'leaveTime'){
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return
        }
      }
      this.formMemberInfo = row;
      let {leaveTime} = row
      this.formMemberInfo.joinTime = this.formatTime(this.formMemberInfo.joinTime)
      this.formMemberInfo.leaveTime = this.formatTime(this.formMemberInfo.leaveTime)
      if(leaveTime === ''){}else if(this.compareTime(this.formMemberInfo.joinTime,this.formMemberInfo.leaveTime)){
        this.$message({
          message: '请填写正确的时间',
          type: 'warning'
        });
        return
      }
      row.isEdit = false;
      this.isMemberEdit = false;
      // console.log(this.formMemberInfo)
      editMemberApi(this.formMemberInfo).then(res=>{
        this.$message({
          message: '修改成功',
          type: 'success'
        });
        this.getBandData()
      })
    },
    addMember(){
      if(this.isMemberEdit){
        this.$message({
          message: '请先完成当前编辑',
          type: 'warning'
        });
        return
      }
      this.addMemberDialog = true;
    },
    deleteMemberInfo(row){
      this.$confirm('此操作将永久删除该成员, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteMemberApi(row.memberId).then(res=>{
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
          this.getBandData()
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
    submitBandForm() {
      for (let item in this.addBandInfo) {
        if (this.addBandInfo[item] === '') {
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return
        }
      }
      this.addBandDialog = false;
      this.addBandInfo.fundationTime = this.formatTime(this.addBandInfo.fundationTime)
      this.addBandInfo.memberData[0].joinTime = this.addBandInfo.fundationTime
      this.addBandInfo.memberData[0].memberName = this.addBandInfo.bandLeader
      this.addBandInfo.memberData[0].bandName = this.addBandInfo.bandName
      this.addBandInfo.albumNumber = 0
      // console.log(this.addBandInfo)
      addBandApi(this.addBandInfo).then(res => {
        console.log(res.data.data)
        this.$message({
          message: '添加成功',
          type: 'success'
        });
        this.getBandData()
      })
    },
    submitMemberForm() {
      for (let item in this.addMemberInfo) {
        if (item === 'joinTime' && this.addMemberInfo[item] === null) {
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return;
        }
        if (this.addMemberInfo[item] === '' && item !== 'memberJob' && item !== 'leaveTime') {
          console.log(item)
          this.$message({
            message: '请填写完整信息',
            type: 'warning'
          });
          return
        }
      }
      let {leaveTime} = this.addMemberInfo
      this.addMemberInfo.joinTime = this.formatTime(this.addMemberInfo.joinTime)
      if(this.addMemberInfo.leaveTime.length !== 0){
        this.addMemberInfo.leaveTime = this.formatTime(this.addMemberInfo.leaveTime)
      }
      else this.addMemberInfo.leaveTime = ''
      if(leaveTime===''){}else if(this.compareTime(this.addMemberInfo.joinTime,this.addMemberInfo.leaveTime)){
        this.$message({
          message: '请填写正确的时间',
          type: 'warning'
        });
        this.addMemberInfo.joinTime = ''
        this.addMemberInfo.leaveTime = ''
        return
      }
      this.addMemberDialog = false;
      addMemberApi(this.addMemberInfo).then(res => {
        this.$message({
          message: '添加成功',
          type: 'success'
        });
        this.showBandMember = false
        this.getBandData()
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    onlyMyBand(checked){
      this.getBandData(checked)
    },
    getBandData(params=0){
      getList(this.currentPage,10,this.type,params).then((res)=>{
        let {data} = res.data
         this.bandData = data.bandData
         this.total = data.total
      })
    },
    handleSelectionChange(val) {
      this.bandData = val;
    },
    handleSizeChange(val) {
      this.pageSize = val;
      this.getBandData()
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      this.getBandData()
    },
    goPrePage(){
      this.getBandData()
    },
    goNextPage(){
      this.getBandData()
    },
    goSearch(){
      this.isOnSearch = true
      let searchText = this.searchText;
      let searchType = this.searchType;
      searchBandApi({searchText,searchType}).then(res=>{
        let {data} = res.data
        this.searchBandData = data.searchBandData
        this.searchTotal = data.total
      })
    },
    toggleSearchResult(){
      this.isOnSearch = !this.isOnSearch
    },
  },

}


</script>

<style scoped>
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
.search-words{
  margin: 20px 0;
  letter-spacing: 3px;
}
</style>
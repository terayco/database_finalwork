<template>
  <div>
    <el-card
      v-permission="['fan']"
      style="margin-top: 20px"
    >
      <div>我的信息</div>
      <el-table
        :data="aboutMeData"
        border
        :row-style="iRowStyle"
        style="width: 100%;margin-top: 20px"
      >
        <el-table-column
          prop="fanId"
          label="我的ID"
        >
          <template #default="scope">
            {{ scope.row.fanId }}
          </template>
        </el-table-column>

        <el-table-column
          prop="fanName"
          label="姓名"
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
        >
          <template #default="scope">
            <el-button
              v-permission="['band','fan']"
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
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    <div class="like-box">
      <div class="like-top">
        <el-card>
          <div>喜欢的歌曲</div>
          <el-table
            height="220"
            :data="likeMusicData"
            border
            :row-style="iRowStyle"
            style="width: 100%;margin-top: 20px"
          >
            <el-table-column
              prop="songName"
              label="歌曲名称"
            >
              <template #default="scope">
                {{ scope.row.songName }}
              </template>
            </el-table-column>
            <el-table-column
              prop="musicSinger"
              label="创作乐队"
            >
              <template #default="scope">
                {{ scope.row.creator }}
              </template>
            </el-table-column>
            <el-table-column
              prop="albumBelong"
              label="所属专辑"
            >
              <template #default="scope">
                {{ scope.row.albumBelong }}
              </template>
            </el-table-column>
            <el-table-column
              fixed="right"
              label="操作"
            >
              <template #default="scope">
                <div @click="disLikeSong(scope.row)">
                  <i
                    v-show="scope.row.isLike"
                    class="iconfont icon-jurassic_love1"
                  />
                </div>
              </template>
            </el-table-column>
          </el-table>
        </el-card>
        <el-card>
          <div>喜欢的专辑</div>
          <el-table
            height="220"
            :data="likeAlbumData"
            border
            :row-style="iRowStyle"
            style="width: 100%;margin-top: 20px"
          >
            <el-table-column
              prop="albumName"
              label="专辑名称"
            >
              <template #default="scope">
                {{ scope.row.albumName }}
              </template>
            </el-table-column>
            <el-table-column
              prop="performBand"
              label="表演乐队"
            >
              <template #default="scope">
                {{ scope.row.performBand }}
              </template>
            </el-table-column>
            <el-table-column
              prop="releaseTime"
              label="发行时间"
            >
              <template #default="scope">
                {{ scope.row.releaseTime }}
              </template>
            </el-table-column>
            <el-table-column
              prop="releaseCompany"
              label="发行公司"
            >
              <template #default="scope">
                {{ scope.row.releaseCompany }}
              </template>
            </el-table-column>
            <el-table-column
              fixed="right"
              label="操作"
            >
              <template #default="scope">
                <div @click="disLikeAlbum(scope.row)">
                  <i
                    v-show="scope.row.isLike"
                    class="iconfont icon-jurassic_love1"
                  />
                </div>
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </div>
      <div
        v-permission="['fan']"
        class="like-btm"
      >
        <el-card>
          <div>参加的演唱会</div>
          <el-table
            height="220"
            :data="concertData"
            border
            :row-style="iRowStyle"
            style="width: 100%;margin-top: 20px"
          >
            <el-table-column
              prop="bandName"
              label="表演乐队"
            >
              <template #default="scope">
                {{ scope.row.bandName }}
              </template>
            </el-table-column>
            <el-table-column
              prop="holdingTime"
              label="举办时间"
            >
              <template #default="scope">
                {{ scope.row.holdingTime }}
              </template>
            </el-table-column>
            <el-table-column
              prop="holdingPlace"
              label="举办地点"
            >
              <template #default="scope">
                {{ scope.row.holdingPlace }}
              </template>
            </el-table-column>
            <el-table-column
              prop="duration"
              label="持续时间"
            >
              <template #default="scope">
                {{ scope.row.duration }}
              </template>
            </el-table-column>
            <el-table-column
              fixed="right"
              label="操作"
            >
              <template #default="scope">
                <div @click="disJoinConcert(scope.row)">
                  <span v-show="scope.row.isLike" class="words">取消参加</span>
                </div>
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </div>
      <div class="like-btm">
        <el-card>
          <div>喜欢的乐队</div>
          <el-table
            :data="likeBandData"
            border
            :row-style="iRowStyle"
            style="width: 100%;margin-top: 20px"
          >
            <el-table-column
              prop="bandName"
              label="乐队名称"
            >
              <template #default="scope">
                {{ scope.row.bandName }}
              </template>
            </el-table-column>
            <el-table-column
              prop="bandLeader"
              label="队长"
            >
              <template #default="scope">
                {{ scope.row.bandLeader }}
              </template>
            </el-table-column>
            <el-table-column
              prop="fundationTime"
              label="成立时间"
            >
              <template #default="scope">
                {{ scope.row.fundationTime }}
              </template>
            </el-table-column>
            <el-table-column
              prop="bandNumber"
              label="乐队人数"
            >
              <template #default="scope">
                {{ scope.row.bandNumber }}
              </template>
            </el-table-column>
            <el-table-column
              prop="albumNumber"
              label="发行专辑数量"
            >
              <template #default="scope">
                {{ scope.row.albumNumber }}
              </template>
            </el-table-column>
            <el-table-column
              fixed="right"
              label="操作"
            >
              <template #default="scope">
                <div @click="disLikeBand(scope.row)">
                  <i
                    v-show="scope.row.isLike"
                    class="iconfont icon-jurassic_love1"
                  />
                </div>
              </template>
            </el-table-column>
          </el-table>
        </el-card>
      </div>
    </div>
  </div>
</template>

<script>
import {
  disLikeApi,
  disMyAttendingApi,
  editMyInfoApi,
  getMyAttendingApi,
  getMyInfoApi,
  getMyLikeApi
} from "@/api/aboutMe";

export default {
  name: "AboutMe",
  data(){
    return{
      sexOptions:[
        {
          value:'男',
          label:'男'
        },
        {
          value:'女',
          label:'女'
        }
      ],
      aboutMeData:[
      ],
      likeMusicData:[
      ],
      likeAlbumData:[
      ],
      likeBandData:[
      ],
      concertData:[
      ],
      editAboutMeForm:{
        fanId:'',
        fanName:"",
        fanSex:"",
        fanAge:'',
        fanCareer:'',
        isEdit:false
      },
      currentRole:''
    }
  },
  created() {
    let {userInfo} = JSON.parse(localStorage.getItem('userInfo'))
    this.currentBandName= userInfo.role==='band'? userInfo.bandName : ''
    this.currentRole = userInfo.role
    getMyInfoApi().then(res=>{
      let {data} = res.data
      this.aboutMeData = data.aboutMeData
    });
    getMyLikeApi('band').then(res=>{
      let {data} = res.data
      this.likeBandData = data.likeBandData
    })
    getMyLikeApi('song').then(res=>{
      let {data} = res.data
      this.likeMusicData = data.likeMusicData
    })
    getMyLikeApi('album').then(res=>{
      let {data} = res.data
      this.likeAlbumData = data.likeAlbumData
    })
    getMyAttendingApi().then(res=>{
      let {data} = res.data
      this.concertData = data.concertData
    })

  },
  methods:{
    editFanInfo(row){
      row.isEdit = true
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
      this.editAboutMeForm = row
      editMyInfoApi(this.editAboutMeForm).then(res=>{
        this.$message.success('修改成功')
        getMyInfoApi().then(res=>{
          let {data} = res.data
          this.aboutMeData = data.aboutMeData
        });
      }).catch(()=>{})
      row.isEdit = false
    },
    cancelEditFanInfo(row){
      row.isEdit = false
    },
    disLikeSong(row){
      disLikeApi('songs',row.songName,row.bandName).then(res=>{
        this.$message.success('取消喜欢成功')
        getMyLikeApi('song').then(res=>{
          let {data} = res.data
          this.likeMusicData = data.likeMusicData
        })
      }).catch(()=>{})
    },
    disLikeAlbum(row){
      disLikeApi('albums',row.albumName).then(res=>{
        this.$message.success('取消喜欢成功')
        getMyLikeApi('album').then(res=>{
          let {data} = res.data
          this.likeAlbumData = data.likeAlbumData
        })
      }).catch(()=>{})
    },
    disLikeBand(row){
      disLikeApi('bands',row.bandName).then(res=>{
        this.$message.success('取消喜欢成功')
        getMyLikeApi('band').then(res=>{
          let {data} = res.data
          this.likeBandData = data.likeBandData
        })
      }).catch(()=>{})
    },
    disJoinConcert(row){
      disMyAttendingApi('concerts',row.bandName,row.holdingTime).then(res=>{
        this.$message.success('取消参加成功')
        getMyAttendingApi().then(res=>{
          let {data} = res.data
          this.concertData = data.concertData
        })
      }).catch(()=>{})
    },
    iRowStyle({row, rowIndex}) {
      return 'height:65px';
    },
  }
}
</script>

<style scoped lang="less">
.like-box{
  width: 100%;
  height: 400px;
  margin-top: 20px;
  .like-top{
    width: 100%;
    height: 300px;
    display: flex;
    justify-content: space-between;
    .el-card{
      width: 49%;
      height: 100%;
    }
  }
  .like-btm{
    margin-top: 20px;
    width: 100%;
    height: 300px;
    .el-card{
      width: 100%;
      height: 100%;
      background-color: #fff;
    }
  }
}
.words{
  color: var(--theme--color);
}
</style>
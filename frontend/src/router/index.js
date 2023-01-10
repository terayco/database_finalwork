import { createRouter, createWebHistory } from 'vue-router'

const Home = () => import('@/views/Home.vue')
const BandList = () => import('@/views/AsideViews/BandList')
const AlbumList = () => import('@/views/AsideViews/AlbumList')
const SongList = () => import('@/views/AsideViews/SongList')
const PerformanceList = () => import('@/views/AsideViews/PerformanceList')
const FanList = () => import('@/views/AsideViews/FanList')
const AboutMe = () => import('@/views/AsideViews/AboutMe')


const LogReg = ()=> import('@/views/LogReg')

const NotFound = () => import('@/views/NotFound.vue')
export const publicRoutes = [
  {
    path: '/',
    redirect: '/bandlist',
      meta: {
            title: '首页',
            roles: ['admin','band', 'fan'],
      }
  },
  {
    path: '/login',
    name: 'Login',
    component:LogReg,
      meta: {
            title: '登录',
            roles: ['admin','band', 'fan'],
      }
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
    meta: {
        title: '首页',
        roles: ['admin','band', 'fan'],
    },
    children:[{
      path:'/bandlist',
      name:'BandList',
      component:BandList,
        meta: {
            title: '乐队信息',
            roles: ['admin','band', 'fan'],
            icon:'el-icon-s-home'
        }
    },{
      path:'/albumlist',
      name:'AlbumList',
      component:AlbumList,
        meta: {
            title: '专辑信息',
            roles: ['admin','band', 'fan'],
            icon:'el-icon-s-home'
        }
    },{
      path:'/songlist',
      name:'SongList',
      component:SongList,
        meta: {
            title: '歌曲信息',
            roles: ['admin','band', 'fan'],
            icon:'el-icon-s-home'
        }
    },{
      path:'/performancelist',
      name:'PerformanceList',
      component:PerformanceList,
        meta: {
            title: '演唱会信息',
            roles: ['admin','band', 'fan'],
            icon:'el-icon-s-home'
        }
    },
        {
          path: '/fanlist',
            name: 'FanList',
            component: FanList,
            meta: {
                title: '粉丝信息',
                roles: ['band', 'admin' ],
                icon: 'el-icon-s-home'
            }
        },
        {
            path: '/aboutme',
            name: 'AboutMe',
            component: AboutMe,
            meta: {
                title: '关于我的',
                roles: [ 'fan'],
                icon: 'el-icon-s-home'
            }
        },
    ]
  },
    {
        path: "/:pathMatch(.*)*",
        name: 'Notfound',
        component: NotFound,
        meta: {
            title: '404',
            roles: ['admin','band', 'fan'],
        }
    }
]

export const AsideRoutes = [
    {
        path:'/bandlist',
        name:'BandList',
        component:BandList,
        meta: {
            title: '乐队信息',
            roles: ['admin','band', 'fan'],
            icon:'iconfont icon-ledui'
        }
    },{
        path:'/albumlist',
        name:'AlbumList',
        component:AlbumList,
        meta: {
            title: '专辑信息',
            roles: ['admin','band', 'fan'],
            icon: 'iconfont icon-zhuanji1'
        }
    },{
        path:'/songlist',
        name:'SongList',
        component:SongList,
        meta: {
            title: '歌曲信息',
            roles: ['admin','band', 'fan'],
            icon: 'iconfont icon-gequ'
        }
    },{
        path:'/performancelist',
        name:'PerformanceList',
        component:PerformanceList,
        meta: {
            title: '演唱会信息',
            roles: ['admin','band', 'fan'],
            icon: 'iconfont icon-huatong'
        }
    },
    {
        path: '/fanlist',
        name: 'FanList',
        component: FanList,
        meta: {
            title: '粉丝信息',
            roles: ['band', 'admin'],
            icon: 'iconfont icon-29my'
        }
    },
    {
        path: '/aboutme',
        name: 'AboutMe',
        component: AboutMe,
        meta: {
            title: '我的',
            roles: [ 'fan'],
            icon: 'iconfont icon-wodeguanzhu'
        }
    },
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: publicRoutes,
})

router.beforeEach(async (to, from, next) => {
    const isLogin = localStorage.getItem('token') || false
    const {userInfo} = JSON.parse(localStorage.getItem('userInfo') || '{}')
    if (to.path === '/login') {
        next()
    } else {
        //先判断是否登录
        if (isLogin) {
            to.meta.roles.includes(userInfo.role) ? next() : next({ name: 'Notfound' })
        } else if (!isLogin) {
            next('/login')
        }
    }
})

export default router

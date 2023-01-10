import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router'

import '@/assets/font/iconfont.css'
import './assets/css/normalize.css'
import '@/assets/css/app.css'
import '@/assets/css/font.css'
import 'element-plus/theme-chalk/display.css'
import store from '@/store'
import zhCn from 'element-plus/es/locale/lang/zh-cn'

import VueParticles from 'vue-particles'
const app = createApp(App)
app.use(router).use(ElementPlus,{locale: zhCn}).use(VueParticles).use(store).mount('#app')

import {userStore} from "@/store/user";
const store1 = userStore()
app.directive('permission', {
    mounted: function (el, binding) {
        const routes = binding.value
        if (routes && Array.isArray(routes) && routes.length) {
            const role = store1.userInfo.role
            if (role && routes.includes(role)) {
                if(role === 'band'){
                    let roleLength = binding.value.length
                    if(binding.value[roleLength-1]!=='notBandThing' && binding.value[roleLength-1] !== binding.instance.$data.currentBandName){
                        el.parentNode.removeChild(el)
                    }
                }
            } else {
                // 如果角色不在允许范围，则移除dom
                el.parentNode.removeChild(el)
            }

        }
    },
})
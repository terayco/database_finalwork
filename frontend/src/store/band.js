// useStore 可以是 useUser、useCart 之类的任何东西
// 第一个参数是应用程序中 store 的唯一 id
import {defineStore} from "pinia";

export const bandStore = defineStore('main', {
    // 推荐使用 完整类型推断的箭头函数
    state: () => {
        return {
            // 所有这些属性都将自动推断其类型
            bandInfo:{
                bandName: '',
                bandLeader: '',
                fundationTime: '',
                bandNumber: '',
                albumNumber: '',
                isEdit: false,
                members:[]
            }
        };
    },
    persist: {
        //这里存储默认使用的是session
        enabled: true,
        strategies: [
            {
                //key的名称
                key: 'bandInfo',
                //更改默认存储，我更改为localStorage
                storage: localStorage,
                // 可以选择哪些进入local存储，这样就不用全部都进去存储了
                // 默认是全部进去存储
                // paths: ['userInfo']
            },
        ]
    }
})
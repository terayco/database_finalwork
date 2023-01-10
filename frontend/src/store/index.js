import { createPinia } from 'pinia'
import piniaPluginPersist from 'pinia-plugin-persist'
const store = createPinia()
// 使用该插件
store.use(piniaPluginPersist)
//导出
export default store


// 导入 路由配置
import { AsideRoutes } from './index'

/**
 * 根据角色不同，获取对应能够访问到的路由页面配置
 * @param {*} role 角色 cjgly
 */
export const buildRoute = function (role) {
    const routes = []
    // 在需要权限才能访问的路由asyncRoutes中，找出当前角色能够访问的
    // 路由 遍历当前角色可以访问的路由
    AsideRoutes.forEach(route => {
        if (route.meta.roles && route.meta.roles.includes(role)) {
            routes.push(route)
        }
    })
    return routes
}


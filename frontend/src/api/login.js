import {request} from "@/api/request";

export function login(data){
    return request({
        method:'POST',
        url:'/api/user/login',
        data
    })
}

export function createFanApi(data) {
    return request({
        method: 'POST',
        url: '/api/user/register/fan',
        data,
    })
}

export function createBandApi(data) {
    return request({
        method: 'POST',
        url: '/api/user/register/band',
        data,
    })
}


export function loginOut(){
    return request({
        method:'POST',
        url:'/api/user/logout'
    })
}

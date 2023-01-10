import {request} from "@/api/request";

export function getMyInfoApi(){
    return request({
        method:'GET',
        url:'/api/aboutMe/info'
    })
}

export function editMyInfoApi(data){
    return request({
        method:'PUT',
        url:'/api/aboutMe/editMyInfo',
        data:data
    })
}

export function getMyLikeApi(likeThing){
    return request({
        method:'GET',
        url:'/api/aboutMe/getMyLike',
        params:{
            likeThing:likeThing
        }
    })
}

export function addMyLikeApi(table,mainKey,plusKey){
    return request({
        method:'POST',
        url:'/api/aboutMe/addMyLike',
        data:{
            table,
            mainKey,
            plusKey
        }
    })
}

export function disLikeApi(table,mainKey,plusKey){
    return request({
        method:'DELETE',
        url:'/api/aboutMe/disLike',
        data: {table,mainKey,plusKey}
    })
}

export function getMyAttendingApi(){
    return request({
        method:'GET',
        url:'/api/aboutMe/getMyAttending'
    })
}

export function addMyAttendingApi(table,mainKey,plusKey){
    return request({
        method:'POST',
        url:'/api/aboutMe/addMyAttending',
        data:{table,
            mainKey,plusKey
        }
    })
}

export function disMyAttendingApi(table,mainKey,plusKey){
    return request({
        method:'DELETE',
        url:'/api/aboutMe/disMyAttending',
        data:{table,
            mainKey,plusKey
        }
    })
}
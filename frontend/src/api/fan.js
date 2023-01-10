import {request} from "@/api/request";

export function addFanApi(fanInfo){
    return request({
        method:'POST',
        url:'/api/fan/addFan',
        data:fanInfo
    })
}

export function editFanApi(data){
    return request({
        method:'PUT',
        url:'/api/fan/editFan',
        data:data
    })
}

export function deleteFanApi(fanId){
    return request({
        method:'DELETE',
        url:'/api/fan/deleteFan',
        data:{
            fanId
        }
    })
}

export function getFanOverLookApi(){
    return request({
        method:'GET',
        url:'api/band/getFanOverLook'
    })
}
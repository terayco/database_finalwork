import {request} from "@/api/request";

export function addPerformApi(performInfo){
    return request({
        method:'POST',
        url:'/api/perform/addPerform',
        data:performInfo
    })
}

export function editPerformApi(data){
    return request({
        method:'PUT',
        url:'/api/perform/editPerform',
        data:data
    })
}

export function deletePerformApi(concertId){
    return request({
        method:'DELETE',
        url:'/api/perform/deletePerform',
        data:{
            concertId
        }
    })
}

export function addSongPerformApi(data){
    return request({
        method:'POST',
        url:'/api/perform/addSongPerform',
        data:data
    })
}

export function editSongPerformApi(data){
    return request({
        method:'PUT',
        url:'/api/perform/editSongPerform',
        data:data
    })
}

export function deleteSongPerformApi(sheetId,concertId){
    return request({
        method:'DELETE',
        url:'/api/perform/deleteSongPerform',
        data:{
            sheetId,
            concertId
        }
    })
}
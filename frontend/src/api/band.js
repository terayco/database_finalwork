import {request} from "@/api/request";

export function addBandApi(bandInfo){
    return request({
        method:'POST',
        url:'/api/band/addBand',
        data:bandInfo
    })
}

export function editBandApi(data){
    return request({
        method:'PUT',
        url:'/api/band/editBand',
        data:data
    })
}

export function deleteBandApi(bandId){
    return request({
        method:'DELETE',
        url:'/api/band/deleteBand',
        data:{
            bandId
        }
    })
}

export function addMemberApi(data){
    return request({
        method:'POST',
        url:'/api/band/addMember',
        data:data
    })
}

export function editMemberApi(data){
    return request({
        method:'PUT',
        url:'/api/band/editMember',
        data:data
    })
}

export function deleteMemberApi(memberId){
    return request({
        method:'DELETE',
        url:'/api/band/deleteMember',
        data:{
            memberId
        }
    })
}
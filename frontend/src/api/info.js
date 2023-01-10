import {request} from "@/api/request";

export function getList(page,limit,type,info){
    return request({
        method:'GET',
        url:'/api/list',
        params:{
            page:page,
            limit:limit,
            type:type,
            info:info
        }
    })
}

export function searchBandApi(data){
    return request({
        method:'POST',
        url:'/api/search/band',
        data
    })
}

export function searchSongApi(data){
    return request({
        method:'POST',
        url:'/api/search/song',
        data
    })
}

export function searchAlbumApi(data){
    return request({
        method:'POST',
        url:'/api/search/album',
        data
    })
}

export function searchConcertApi(data){
    return request({
        method:'POST',
        url:'/api/search/concert',
        data
    })
}
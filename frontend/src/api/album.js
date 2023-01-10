import {request} from "@/api/request";

export function addAlbumApi(albumInfo){
    return request({
        method:'POST',
        url:'/api/album/addAlbum',
        data:albumInfo
    })
}

export function editAlbumApi(data){
    return request({
        method:'PUT',
        url:'/api/album/editAlbum',
        data:data
    })
}

export function deleteAlbumApi(id){
    return request({
        method:'DELETE',
        url:'/api/album/deleteAlbum',
        data:{
            albumId:id
        }
    })
}
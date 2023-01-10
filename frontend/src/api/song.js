import {request} from "@/api/request";

export function addSongApi(songInfo){
    return request({
        method:'POST',
        url:'/api/song/addSong',
        data:songInfo
    })
}

export function editSongApi(data){
    return request({
        method:'PUT',
        url:'/api/song/editSong',
        data:data
    })
}

export function deleteSongApi(songId){
    return request({
        method:'DELETE',
        url:'/api/song/deleteSong',
        data:{
            songId
        }
    })
}
import {userStore} from "@/store/user";
import {addMyAttendingApi, addMyLikeApi, disLikeApi, disMyAttendingApi} from "@/api/aboutMe";
const store = userStore()
let myFavourite ={
    myFavouriteBand: [],
    myFavouriteAlbum: [],
    myFavouriteSong: [],
    toPerformance: [],
}
export function changeBandLike(row){
    row.isLike = !row.isLike
    let {myFavouriteBand} = JSON.parse(localStorage.getItem('myFavourite') ?? JSON.stringify(myFavourite))
    if (row.isLike) {
        addMyLikeApi('bands',row.bandName).then(res => {
            this.$message.success({
                message: '添加至我的喜欢',
            })
        })
        myFavouriteBand.push(row.bandName)
        myFavouriteBand = [...new Set(myFavouriteBand)]
    } else {
        myFavouriteBand = myFavouriteBand.filter(item => item !== row.bandName)
        disLikeApi('bands',row.bandName).then(res => {
            this.$message.success({
                message: '取消喜欢',
            })
        })
    }
    store.$patch({
        myFavouriteBand: myFavouriteBand
    })

}

export function changeAlbumLike(row){
    row.isLike = !row.isLike
    let {myFavouriteAlbum} = JSON.parse(localStorage.getItem('myFavourite') ?? JSON.stringify(myFavourite))
    if (row.isLike) {
        addMyLikeApi('albums',row.albumName).then(res => {
            this.$message.success({
                message: '添加至我的喜欢',
            })
        })
        myFavouriteAlbum.push(row.albumName)
        myFavouriteAlbum = [...new Set(myFavouriteAlbum)]

    } else {
        myFavouriteAlbum = myFavouriteAlbum.filter(item => item !== row.albumName)
        disLikeApi('albums',row.albumName).then(res => {
            this.$message.success({
                message: '已取消喜欢',
            })
        })
    }
    store.$patch({
        myFavouriteAlbum: myFavouriteAlbum
    })
}

export function changeSongLike(row){
    row.isLike = !row.isLike
    let {myFavouriteSong} = JSON.parse(localStorage.getItem('myFavourite') ?? JSON.stringify(myFavourite))
    if (row.isLike) {
        addMyLikeApi('songs',row.songName,row.bandName).then(res => {
            this.$message.success({
                message: '添加至我的喜欢',
            })
        })
        myFavouriteSong.push(row.songName)
        myFavouriteSong = [...new Set(myFavouriteSong)]
    } else {
        myFavouriteSong = myFavouriteSong.filter(item => item !== row.songName)
        disLikeApi('songs',row.songName,row.bandName).then(res => {
            this.$message.success({
                message: '已取消喜欢',
            })
        })
    }
    store.$patch({
        myFavouriteSong: myFavouriteSong
    })
}

export function changePerformanceJoin(row){
    row.isLike = !row.isLike
    let {toPerformance} = JSON.parse(localStorage.getItem('myFavourite') ?? JSON.stringify(myFavourite))
    if (row.isLike) {
        addMyAttendingApi('concerts',row.bandName,row.holdingTime).then(res => {
            this.$message.success({
                message: '参加成功',
            })
        })
        toPerformance.push(row.holdingTime)
        toPerformance = [...new Set(toPerformance)]
    } else {
        toPerformance = toPerformance.filter(item => item !== row.holdingTime)
        disMyAttendingApi('concerts',row.bandName,row.holdingTime).then(res => {
            this.$message.success({
                message: '已取消参加',
            })
        })
    }
    store.$patch({
        toPerformance: toPerformance
    })
}
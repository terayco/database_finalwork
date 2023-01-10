export function formatTime(time){
    if(time === ''){
        return
    }
    try{ let year = time.getFullYear(),
        month = time.getMonth() + 1 < 10 ? '0' + (time.getMonth() + 1) : time.getMonth() + 1,
        day = time.getDate() < 10 ? '0' + time.getDate() : time.getDate()
        return year + '-' + month + '-' + day}
    catch(e){
        return time
    }
}
export function formatDateTime(time){
    if(time === ''){
        return
    }
    try{ let year = time.getFullYear(),
        month = time.getMonth() + 1 < 10 ? '0' + (time.getMonth() + 1) : time.getMonth() + 1,
        day = time.getDate() < 10 ? '0' + time.getDate() : time.getDate(),
        hour = time.getHours() < 10 ? '0' + time.getHours() : time.getHours(),
        minute = time.getMinutes() < 10 ? '0' + time.getMinutes() : time.getMinutes(),
        second = time.getSeconds() < 10 ? '0' + time.getSeconds() : time.getSeconds()
        return year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second}
    catch(e){
        return time
    }
}
export function compareTime(time1,time2){
    try {
        time1 = time1.split('-')
        time2 = time2.split('-')
        if (time1[0] > time2[0]) {
            return true
        } else if (time1[0] === time2[0]) {
            if (time1[1] > time2[1]) {
                return true
            } else if (time1[1] === time2[1]) {
                if (time1[2] > time2[2]) {
                    return true
                } else {
                    return false
                }
            } else {
                return false
            }
        } else {
            return false
        }
    }
    catch(e){
        return
    }

}
function goSomeWhere(path) {
    this.isNavigator = false
    if (this.$route.path === path) {
        this.$message.success('您已经在该界面了哦')
    } else this.$router.push(path);
}
function goHome() {
  this.$message.success('您已经在该界面了哦')
}
export { goSomeWhere,goHome}

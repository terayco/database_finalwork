const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    port: 3000, // 端口
  },
  
  // transpileDependencies: ['@arcgis']
  //设置跨域4000端口
  //   devServer: {
  //       proxy: {
  //           '/api': {
  //               target: 'http://localhost:4000',
  //               changeOrigin: true,
  //               pathRewrite: {
  //                   '^/api': ''
  //               }
  //           }
  //       }
  //   }
})


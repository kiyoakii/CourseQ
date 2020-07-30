module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://27.102.70.185:8080',
        // target: 'http://127.0.0.1:3000',
        changeOrigin: true,
        secure: false,
        pathRewrite: {
          '^/api': ''
        }
      }
    },
  }
};
module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/admin/' : '/',
  devServer: {
    proxy: {
      '/api': {
        target: process.env.API_ENDPOINT,
        changeOrigin: true,
        secure: false,
      }
    }
  }
}
module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://27.102.70.185:8080',
        changeOrigin: true,
        secure: false,
        pathRewrite: {
          '^/api': '',
        },
      },
    },
  },
};

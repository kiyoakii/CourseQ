module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://42.120.20.54:8080',
        changeOrigin: true,
        secure: false,
        pathRewrite: {
          '^/api': '',
        },
      },
    },
  },
};

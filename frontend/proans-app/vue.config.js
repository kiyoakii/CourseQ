module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/proans/' : '/',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://42.120.20.54:80',
        changeOrigin: true,
        secure: false,
      },
    },
  },
};

const axios = require('axios');
const { Message } = require('element-ui');

const instance = axios.create({
  timeout: 10000,
});

function errorHandler({ err, response }) {
  if (err) {
    Message.error(`请求失败：${err.message}`);
  }
  if (response) {
    Message.error(`请求失败：${response.data.msg}`);
  }
}

function successHandler() {
  Message.success('请求成功！');
}

instance.interceptors.request.use(
  (config) => {
    // console.log(config);
    return config;
  },
  (err) => {
    errorHandler({ err });
    return Promise.reject(err);
  },
);

instance.interceptors.response.use(
  (response) => {
    if ((response.config.method === 'delete' && response.status !== 204)
      || (response.config.method !== 'delete' && response.status !== 200)) {
      errorHandler({ response });
    }
    successHandler();
    return response;
  },
  (err) => {
    errorHandler({ err });
    return Promise.reject(err);
  },
);

module.exports = {
  instance,
};

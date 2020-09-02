import store from '../store';

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
    config.headers.Authorization = `Bearer ${store.state.token}`;
    console.log(config, store.state);
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
    if (err.response.status) {
      switch (err.response.status) {
        case 403:
          Message.error('您无权进行此操作!');
          break;
        case 401:
          if (err.response.data.msg === 'Token expired') {
            Message.error('登录已失效，请重新登录！');
          }
          break;
        default:
          errorHandler({ err });
      }
    }
    return Promise.reject(err);
  },
);

export {
  instance,
};

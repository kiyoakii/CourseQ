function debounce(fn) {
  let timer = null;
  return (...args) => {
    window.clearTimeout(timer);
    timer = window.setTimeout(() => {
      fn.apply(this, args);
    }, 1000);
  };
}

module.exports = {
  debounce,
};

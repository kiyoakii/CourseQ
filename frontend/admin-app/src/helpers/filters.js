module.exports = {
  memberFilter(data) {
    const res = [];
    data.forEach((item) => {
      res.push({
        name: item.name || item.nickname,
        id: item.gid,
        email: item.email,
        phone: item.phone || '暂无电话信息',
        school: item.school || '暂无学院信息',
      });
    });
    return res;
  },
};

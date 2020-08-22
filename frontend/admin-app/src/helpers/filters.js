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
  courseFilter(data) {
    const res = [];
    data.forEach((item) => {
      res.push({
        id: item.cid,
        name: item.name_zh || item.name_en,
        intro: item.intro,
        pre_course: item.pre_course,
        textbooks: item.textbooks,
        semester: item.semester,
        series: item.series,
        teachers: item.teachers.reduce((teachersText, teacher) => {
          return `${teachersText}, ${teacher.name || teacher.nickname}`;
        }, '').slice(2),
      });
    });
    return res;
  },
  teacherOptionsFilter(data) {
    const res = [];
    data.forEach((item) => {
      res.push({
        label: `${item.name || item.nickname} - ${item.gid}`,
        value: item.gid,
      });
    });
    return res;
  },
  distinctCoursesFilter(data) {
    const res = [];
    data.forEach((item) => {
      if (res.findIndex((v) => v.name === (item.name_zh || item.name_en)) === -1) {
        res.push({
          name: item.name_zh || item.name_en,
        });
      }
    });
    return res;
  },
  schedulesFilter(data) {
    const res = [];
    const map = {};
    data.forEach((item) => {
      if (map[item.week] === undefined) {
        res.push({
          week: item.week,
          lectures: [item],
        });
        map[item.week] = res.length - 1;
      } else {
        res[map[item.week]].lectures.push(item);
      }
    });
    res.sort((a, b) => { return a.week - b.week; });
    const sortedSchedule = [];
    res.forEach((item) => {
      item.lectures.sort();
      item.lectures.forEach((lec) => {
        sortedSchedule.push(lec);
      });
    });
    return {
      weekInfo: res,
      schedules: sortedSchedule,
    };
  },
};

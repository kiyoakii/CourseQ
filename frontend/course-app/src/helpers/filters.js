module.exports = {
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
    res.sort((a, b) => a.week - b.week);
    const sortedSchedule = [];
    res.forEach((item) => {
      item.lectures.sort((a, b) => {
        if (a.datetime > b.datetime) {
          return 1;
        }
        if (a.datetime < b.datetime) {
          return -1;
        }
        return 0;
      });
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

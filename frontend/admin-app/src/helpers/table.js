module.exports = {
  memberTable: [
    { label: 'ID', prop: 'id', minWidth: 140 },
    { label: '姓名', prop: 'name', minWidth: 100 },
    { label: '邮箱', prop: 'email', minWidth: 200 },
    { label: '电话', prop: 'phone', minWidth: 140 },
    { label: '所属院系', prop: 'school', minWidth: 140 },
  ],
  courseTable: [
    { label: 'ID', prop: 'id', minWidth: 100 },
    { label: '课程名', prop: 'name', minWidth: 120 },
    // { label: '课程介绍', prop: 'intro', minWidth: 140 },
    { label: '预修课', prop: 'pre_course', minWidth: 120 },
    { label: '教科书', prop: 'textbooks', minWidth: 120 },
    { label: '学期', prop: 'semester', minWidth: 120 },
    { label: '系列', prop: 'series', minWidth: 120 },
    { label: '授课教师', prop: 'teachers', minWidth: 120 },
  ],
};

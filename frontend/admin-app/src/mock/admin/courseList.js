import Mock from 'mockjs';

const courses = {
  'courses|2-7': [
    {
      'courseName|+1': ['计算方法', '体系结构', '信息安全', '微积分', '算法基础', '代数结构', '图论'],
      'teacherName|1': () => Mock.Random.cname(),
      id: () => Mock.Random.id(),
    },
  ],
};

export default courses;

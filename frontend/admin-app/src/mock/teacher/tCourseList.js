import Mock from 'mockjs';


const courses = {
  'courses|2-4': [
    {
      id: () => Mock.Random.id(),
      'name|+1': ['数学分析A1', '数学分析B1', '数学分析A2', '数学分析B2'],
    },
  ],
};

export default courses;

import Mock from 'mockjs';

const semesters = {
  'semesters|1-4': [
    {
      id: () => Mock.Random.id(),
      'name|+1': ['2019春季学期', '2019秋季学期', '2020春季学期', '2020秋季学期'],
    },
  ],
};

export default semesters;

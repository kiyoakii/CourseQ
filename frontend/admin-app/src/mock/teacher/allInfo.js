import Mock from 'mockjs';


const allInfo = {
  allInfo: {
    name: () => Mock.Random.ctitle(),
    intro: () => Mock.Random.cparagraph(),
    'teachers|1-2': [
      {
        id: () => Mock.Random.id(),
        name: () => Mock.Random.cname(),
        email: () => Mock.Random.email(),
        phone: /^1[385][1-9]\d{8}/,
      },
    ],
    'assistants|2-5': [
      {
        id: /^(PB|SA)1[567]111\d{3}/,
        name: () => Mock.Random.cname(),
        email: () => Mock.Random.email(),
        phone: /^1[3785][1-9]\d{8}/,
      },
    ],
    'students|5-10': [
      {
        id: /^PB17111\d{3}/,
        name: () => Mock.Random.cname(),
        email: () => Mock.Random.email(),
        phone: /^1[3785][1-9]\d{8}/,
      },
    ],
    'announces|1-3': [
      {
        'title|+1': ['公告1', '公告2', '公告3'],
        publisher: () => Mock.Random.cname(),
        date: () => Mock.Random.date(),
        content: () => Mock.Random.cparagraph(),
      },
    ],
    'schedule|1-5': [
      {
        'weekId|+1': ['1', '2', '3', '4', '5'],
        'courses|1-2': [
          {
            'topic|+1': ['前端开发', '后端开发'],
            reference: '',
          },
        ],
        'assignments|1-2': [
          {
            'title|+1': ['作业1', '作业2'],
            due: () => Mock.Random.date(),
          },
        ],
      },
    ],
    'resources|1-5': [
      {
        title: () => Mock.Random.ctitle(),
        date: () => Mock.Random.date(),
        content: () => Mock.Random.cparagraph(),
        'attachments|1-2': [
          {
            'name|+1': ['1.txt', '2.txt'],
            downloadLink: () => Mock.Random.url(),
          },
        ],
      },
    ],
  },
};


export default allInfo;

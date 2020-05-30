const allinfo = {
  code: 0,
  msg: '...',
  data: {
    name: 'CourseName',
    semester: '2020Spring',
    intro: 'Introduction ......',
    teachers: [
      {
        name: 'Teacher1',
        email: 't1@mail.com',
        phone: '12312341234',
      },
    ],
    assistants: [
      {
        name: 'TA1',
        email: 'ta1@mail.com',
        phone: '12312341234',
      },
    ],
    announces: [
      {
        title: 'title',
        publisher: 'ta1',
        date: '2019-01-01',
        content: 'homework ddl: 2020-12-12',
      },
    ],
    resources: [
      {
        title: 'title',
        date: '2019-01-01',
        content: 'balabala',
        attachments: [
          {
            name: 'att1',
            downloadLink: 'http://jinzhe.xin',
          },
        ],
      },
    ],
  },
};

export default allinfo;

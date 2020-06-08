const teacherAnswer = {
  code: 0,
  msg: '...',
  data: {
    answer: {
      id: '1',
      content: `动态规划(dynamic programming)是运筹学的一个分支，
      是求解决策过程(decision process)最优化的数学方法。
      20世纪50年代初美国数学家R.E.Bellman等人在研究
      多阶段决策过程(multistep decision process)的优化问题时，
      提出了著名的最优化原理(principle of optimality)，
      把多阶段过程转化为一系列单阶段问题，利用各阶段之间的关系，
      逐个求解，创立了解决这类过程优化问题的新方法——动态规划。`,
      stared: false,
    },
  },
};
const studentAnswer = {
  code: 0,
  msg: '...',
  data: {
    answer: {
      id: '1',
      content: '我寻思动态规划就是反向递归，保存中间变量以便化简运算',
      stared: false,
    },
  },
};
const answer = {
  teacher: teacherAnswer,
  student: studentAnswer,
};
export default answer;

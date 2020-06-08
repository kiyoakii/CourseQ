import Mock from 'mockjs';
import problems from './problems';
import categories from './categories';
import problem from './problem';
import answer from './answer';
import discussions from './discussions';

Mock.mock('/v1/proans/problems?id=1', 'get', problems);
Mock.mock('/v1/proans/problems?id=1&category=2', 'get', problems);
Mock.mock('/v1/proans/categories?id=1', 'get', categories);
Mock.mock('/v1/proans/problem/detail?id=1&problem=1', 'get', problem);
Mock.mock('/v1/proans/answer/teacher?id=1&problem=1', 'get', answer.teacher);
Mock.mock('/v1/proans/answer/student?id=1&problem=1', 'get', answer.student);
Mock.mock('/v1/proans/discussions?id=1&problem=1', 'get', discussions);

import Mock from 'mockjs';
import problems from './problems';

Mock.mock('/v1/proans/problems?id=1', 'get', problems);
Mock.mock('/v1/proans/problems?id=1&category=2', 'get', problems);

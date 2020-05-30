import Mock from 'mockjs';
import allinfo from './allinfo';

Mock.mock('/v1/course/allinfo?id=1', 'get', allinfo);

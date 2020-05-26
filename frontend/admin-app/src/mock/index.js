import Mock from 'mockjs';
import courses from './admin/courseList';

Mock.mock('/v1/admin/admin/course-list', 'get', courses.courses);

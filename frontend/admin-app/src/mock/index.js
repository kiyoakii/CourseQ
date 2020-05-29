import Mock from 'mockjs';
import courseList from './admin/courseList';
import teacherList from './admin/teacherList';
import studentList from './admin/studentList';

Mock.mock('/v1/admin/admin/course-list', 'get', courseList);
Mock.mock('/v1/admin/admin/teacher-list', 'get', teacherList);
Mock.mock('/v1/admin/admin/student-list', 'get', studentList);

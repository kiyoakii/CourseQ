import Mock from 'mockjs';
import courseList from './admin/courseList';
import teacherList from './admin/teacherList';
import studentList from './admin/studentList';
import tCourseList from './teacher/tCourseList';
import semesterList from './teacher/semesterList';
import allInfo from './teacher/allInfo';


Mock.mock('/v1/admin/admin/course-list', 'get', courseList);
Mock.mock('/v1/admin/admin/teacher-list', 'get', teacherList);
Mock.mock('/v1/admin/admin/student-list', 'get', studentList);
Mock.mock('/v1/admin/teacher/course-list', 'get', tCourseList);
Mock.mock('/v1/admin/teacher/semester-list?course=1', 'get', semesterList);
Mock.mock('/v1/admin/teacher/course/allinfo?course=1&semester=1', 'get', allInfo);

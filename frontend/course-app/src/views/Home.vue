<template>
  <div id="info">
    <course-info :courseInfo="courseInfo"></course-info>
    <teacher-info :teacherInfo="teacherInfo"></teacher-info>
    <course-announce :announcements="announcements"></course-announce>
    <course-schedule :schedule="schedule"></course-schedule>
  </div>
</template>

<script>
import CourseInfo from '@/components/CourseInfo.vue';
import TeacherInfo from '@/components/TeacherInfo.vue';
import CourseAnnounce from '@/components/CourseAnnounce.vue';
import CourseSchedule from '@/components/CourseSchedule.vue';

export default {
  name: 'Home',
  data() {
    return {
      courseInfo: {
        name: 'CourseName',
        semester: '2020Spring',
        intro: 'Introduction...',
      },
      teacherInfo: {
        teacher: 'TeacherName',
        teacherEmail: 'teacher@mail.com',
        teacherPhone: '12312341234',
        assistant: ['Assistant1', 'Assistant2'],
        assistantEmail: ['ta1@mail.com', 'ta2@mail.com'],
        assistantPhone: ['12312341234', '12312341234'],
      },
      announcements: [
        {
          title: 'Announcement 1',
          publisher: 'teacher 1',
          time: '2020.04.25 20:00',
          content: 'Announcement 1 content ...',
        },
        {
          title: 'Announcement 2',
          publisher: 'teacher 2',
          time: '2020:04:25 20:00',
          content: 'Announcement 2 content ...',
        },
        {
          title: 'Announcement 3',
          publisher: 'teacher 3',
          time: '2020:04:25 20:00',
          content: 'Announcement 3 content ...',
        },
      ],
      schedule: [
        {
          week: 'Week1',
          courseOne: null,
          courseTwo: {
            lecture: 'Lec1',
            describe: 'Introduction',
            reference: 'Chapter 1',
          },
          assignments: 'Homework 1',
        },
        {
          week: 'Week2',
          courseOne: {
            lecture: 'Lec2',
            topic: 'Langrange Formula',
            reference: 'Chapter2',
            link: 'https://www.wolframalpha.com/',
          },
          courseTwo: {
            lecture: 'Lec3',
            topic: 'Newton Formula',
            describe: 'Several means to find the root',
            reference: 'Chapter3',
          },
          assignments: 'Homework 2, Lab 1',
        },
        {
          week: 'Week3',
          courseOne: {
            notification: 'Class suspended due to holiday',
          },
          courseTwo: {
            lecture: 'Lec4',
            describe: 'exercise lesson',
          },
          assignments: null,
        },
      ],
    };
  },
  components: {
    CourseInfo,
    TeacherInfo,
    CourseAnnounce,
    CourseSchedule,
  },
};
</script>

<style scoped>
#info > * {
  margin-bottom: 30px;
}
</style>

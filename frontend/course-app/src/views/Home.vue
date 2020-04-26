<template>
  <div>
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
      schedule: [],
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

<style>

</style>

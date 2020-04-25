<template>
  <div>
    <course-info :courseInfo="courseInfo"></course-info>
    <teacher-info></teacher-info>
    <course-announce></course-announce>
    <course-schedule></course-schedule>
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

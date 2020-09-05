<template>
  <div id="info">
    <course-info :allinfo="allinfo"></course-info>
    <teacher-info :allinfo="allinfo"></teacher-info>
    <course-announce :allinfo="allinfo"></course-announce>
    <course-schedule :allinfo="allinfo"></course-schedule>
  </div>
</template>

<script>
import CourseInfo from '@/components/CourseInfo.vue';
import TeacherInfo from '@/components/TeacherInfo.vue';
import CourseAnnounce from '@/components/CourseAnnounce.vue';
import CourseSchedule from '@/components/CourseSchedule.vue';

export default {
  name: 'Home',
  props: {
    allinfo: {},
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
  margin-top: 10px;
}
</style>

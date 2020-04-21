<template>
  <div>
    This is Home view.
    <course-info></course-info>
    <teacher-info></teacher-info>
    <course-announce></course-announce>
    <course-assigns></course-assigns>
  </div>
</template>

<script>
import CourseInfo from '@/components/CourseInfo.vue';
import TeacherInfo from '@/components/TeacherInfo.vue';
import CourseAnnounce from '@/components/CourseAnnounce.vue';
import CourseAssigns from '@/components/CourseAssigns.vue';

export default {
  name: 'Home',
  components: {
    CourseInfo,
    TeacherInfo,
    CourseAnnounce,
    CourseAssigns,
  },
};
</script>

<style>

</style>

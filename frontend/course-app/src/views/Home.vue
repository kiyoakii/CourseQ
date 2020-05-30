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
  props: {
    allinfo: {},
  },
  computed: {
    courseInfo() {
      return {
        name: this.allinfo.name,
        semester: this.allinfo.semester,
        intro: this.allinfo.intro,
      };
    },
    teacherInfo() {
      return {
        teachers: this.allinfo.teachers,
        assistants: this.allinfo.assistants,
      };
    },
    announcements() {
      return this.allinfo.announces;
    },
    schedule() {
      return [];
    },
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

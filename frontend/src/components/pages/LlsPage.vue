<template>
  <div>
    <h1 className="text-center text-red-darken-4 my-2 ">Лицевой Летописный Свод</h1>
    <v-divider></v-divider>
    <div>
      <h2 className="text-center text-red-darken-3 my-2">Библейская история</h2>
      <v-divider></v-divider>
      <TimelineLls :llsManuscripts="llsBibleManuscripts" />
      <v-divider></v-divider>
      <h2 className="text-center text-red-darken-3 my-2">Всемирная история</h2>
      <v-divider></v-divider>
      <TimelineLls :llsManuscripts="llsOtherManuscripts" />
      <v-divider></v-divider>
      <h2 className="text-center text-red-darken-3 my-2">Русская летописная история</h2>
      <TimelineLls :llsManuscripts="llsRusManuscripts" />
      <v-divider></v-divider>
    </div>
  </div>
</template>

<script>


import TimelineLls from "@/components/book/timeline/TimelineLls.vue";

export default {
  components: { TimelineLls },
  props: {
    llsManuscripts: {
      type: Object,
      required: true
    }
  },
  computed: {
    llsBibleManuscripts() {
      return Object.values(this.llsManuscripts).filter(manuscript => manuscript.title?.includes("Библейская история"));
    },
    llsOtherManuscripts() {
      return Object.values(this.llsManuscripts).filter(manuscript => !manuscript.title?.includes("Библейская история") & !manuscript.code?.includes("rus"));
    },
    llsRusManuscripts() {
      return Object.values(this.llsManuscripts).filter(manuscript => manuscript.code?.includes("rus"));
    }
  }
};
</script>

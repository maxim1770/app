<template>
  <component
    :is="manuscriptContentFactory"
    :manuscript="manuscript"
  />
</template>

<script>


import ManuscriptContentDate from "@/components/manuscript/manuscript_content/ManuscriptContentDate.vue";
import ManuscriptContentChapter from "@/components/manuscript/manuscript_content/ManuscriptContentChapter.vue";
import ManuscriptContentHead from "@/components/manuscript/manuscript_content/ManuscriptContentHead.vue";

export default {
  components: {
    ManuscriptContentDate, ManuscriptContentChapter, ManuscriptContentHead
  },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  },
  computed: {
    manuscriptContentFactory() {
      if (Array.isArray(this.manuscript?.bookmarks_)) {
        return ManuscriptContentChapter;
      } else if (this.__isDictWithArrayValues(this.manuscript?.bookmarks_)) {
        return ManuscriptContentHead;
      } else if (this.__isNestedDict(this.manuscript?.bookmarks_)) {
        return ManuscriptContentDate;
      }
    }
  },
  methods: {
    __isDictWithArrayValues: (obj) => {
      if (typeof obj !== "object" || obj === null) {
        return false;
      }
      for (const key in obj) {
        if (Array.isArray(obj[key]) === false) {
          return false;
        }
      }
      return true;
    },
    __isNestedDict: (obj) => {
      if (typeof obj !== "object" || obj === null) {
        return false;
      }

      for (let key in obj) {
        if (typeof obj[key] !== "object" || obj[key] === null) {
          return false;
        }
      }

      return true;
    }
  }
};

</script>


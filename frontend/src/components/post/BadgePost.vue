<template>
  <v-badge
    :content="postTitle"
    color="blue"
  />
</template>

<script>


export default {
  props: {
    post: {
      type: Object,
      required: true
    },
    date: {
      type: Object,
      required: false,
      default: null
    }
  },
  computed: {
    postTitle() {
      if (this.post?.title) {
        return this.post.title;
      } else if (this.date?.has_post_in_wed_or_fri) {
        return "Пост в Среду или Пятницу";
      } else {
        return "Поста нет";
      }
    }
  }
};

</script>

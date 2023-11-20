<template>
  <v-chip
    v-if="book.type"
    color="pink-darken-1"
    class="ma-1"
  >
    {{ book.type }}
  </v-chip>
  <BookAuthor :saint="book.author" />
  <v-chip
    v-if="book.topic_book.source"
    color="amber"
    class="ma-1"
  >
    {{ book.topic_book.source }}
  </v-chip>
  <span v-if="book.topic_book.topics.length">
    <template
      v-for="topic in book.topic_book.topics"
      :key="topic.id"
    >
      <v-chip
        :to="{ name: 'books' , query : {topics__title__in: [topic.title]}}"
        color="blue"
        class="ma-1"
      >
        {{ topic.title }}
      </v-chip>
      <v-chip
        v-if="book.topic_book.topics.lastIndexOf(topic) + 1 !== book.topic_book.topics.length"
        color="blue-lighten-2"
        class="ma-1"
      >
        и
      </v-chip>
    </template>
  </span>
</template>

<script>


import BookAuthor from "@/components/book/book_full_title/__BookAuthor.vue";

export default {
  components: { BookAuthor },
  props: {
    book: {
      type: Object,
      required: true
    }
  }
};

</script>




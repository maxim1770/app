<template>
  <v-chip v-if="book.type">
    {{ book.type }}
  </v-chip>
  <v-chip
    v-if="book.author"
    :to="{ name: 'saint', params: { saintSlug: book.author.slug } }"
  >
    <template v-if="book.author.name_in_genitive">
      {{ book.author.name_in_genitive }}
    </template>
    <template v-else>
      Автор: {{ book.author.name }}
    </template>
  </v-chip>
  <v-chip v-if="book.topic_book.source">
    {{ book.topic_book.source }}
  </v-chip>
  <template
    v-if="book.topic_book.topics.length"
    v-for="topic in book.topic_book.topics"
    :key="topic"
  >
    <v-chip>
      {{ topic }}
    </v-chip>
    <v-chip v-if="book.topic_book.topics.lastIndexOf(topic) + 1 !== book.topic_book.topics.length">
      и
    </v-chip>
  </template>
</template>

<script>


export default {
  props: {
    book: {
      type: Object,
      required: true
    }
  }
};

</script>




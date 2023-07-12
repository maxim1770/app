<template>
  <v-chip v-if="book.type">
    {{ book.type }}
  </v-chip>
  <v-chip
    v-if="book.author"
    :to="{ name: 'saint', params: { saintSlug: book.author.slug } }"
    class="ml-1"
  >
    <template v-if="book.author.name_in_genitive">
      {{ book.author.name_in_genitive }}
    </template>
    <template v-else>
      Автор: {{ book.author.name }}
    </template>
  </v-chip>
  <v-chip v-if="book.topic_book.source" class="ml-1">
    {{ book.topic_book.source }}
  </v-chip>
  <span v-if="book.topic_book.topics.length" class="ml-1">
    <template
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
  </span>
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




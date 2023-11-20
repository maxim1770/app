<template>
  <ExpansionPanelSearch @getItems="$emit('getItems')">
    <v-row>
      <v-col>
        <v-autocomplete
          @update:modelValue="$emit('update:topics__title__in', $event)"
          :model-value="topics__title__in"
          :items="booksSearchData.book_topics"
          label="Темы"
          multiple
          chips
          closable-chips
        />
        <v-chip-group
          @update:modelValue="updateTopicsTitleInIndexes"
          :model-value="topics__title__in_indexes"
          selected-class="text-blue"
          multiple
          filter
        >
          <v-chip
            v-for="book_topic in booksSearchData.book_topics"
            :key="book_topic"
          >
            {{ book_topic }}
          </v-chip>
        </v-chip-group>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="6"
      >
        <v-autocomplete
          @update:modelValue="$emit('update:type', $event)"
          :model-value="type"
          :items="booksSearchData.book_types"
          label="Тип"
        />
      </v-col>
      <v-col
        cols="12"
        md="6"
      >
        <v-autocomplete
          @update:modelValue="$emit('update:topic_book__source', $event)"
          :model-value="topic_book__source"
          :items="booksSearchData.book_sources"
          label="Источник"
        />
      </v-col>
    </v-row>
  </ExpansionPanelSearch>
</template>


<script>


import TextFieldSearch from "@/components/search/TextFieldSearch.vue";
import ExpansionPanelSearch from "@/components/search/ExpansionPanelSearch.vue";
import YearsRangeSearch from "@/components/manuscript/manuscripts_search/YearsRangeSearch.vue";

export default {
  components: { YearsRangeSearch, ExpansionPanelSearch, TextFieldSearch },
  props: {
    booksSearchData: {
      type: Object,
      required: true
    },
    type: {
      type: String,
      required: true
    },
    topic_book__source: {
      type: String,
      required: true
    },
    topics__title__in: {
      type: Array,
      required: true
    }
  },
  emits: [
    "update:type",
    "update:topic_book__source",
    "update:topics__title__in",
    "getItems"
  ],
  computed: {
    topics__title__in_indexes() {
      let topics__title__in_indexes = [];
      for (let topicsTitleInElement of this.topics__title__in || []) {
        topics__title__in_indexes.push(this.booksSearchData.book_topics?.indexOf(topicsTitleInElement));
      }
      return topics__title__in_indexes;
    }
  },
  methods: {
    updateTopicsTitleInIndexes(event) {
      let topics__title__in = [];
      for (let topics__title__in_index of event) {
        topics__title__in.push(this.booksSearchData.book_topics[topics__title__in_index]);
      }
      this.$emit("update:topics__title__in", topics__title__in);
    }
  }
};

</script>


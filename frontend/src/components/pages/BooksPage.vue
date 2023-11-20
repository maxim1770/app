<template>
  <div>
    <FormBooksSearch
      @getItems="getBooks"
      :booksSearchData="booksSearchData"
      :type="$route.query.type"
      :topic_book__source="$route.query.topic_book__source"
      :topics__title__in="$route.query.topics__title__in"
      @update:type="replaceRouterQuery( {type: $event} )"
      @update:topic_book__source="replaceRouterQuery( {topic_book__source: $event} )"
      @update:topics__title__in="replaceRouterQuery( {topics__title__in: $event})"
    />
    <NumItems :numItems="books.total" />
    <ContainerBooks :books="books.items" />
  </div>
</template>

<script>


import { api } from "@/services/api";
import { replaceRouterQuery, scroll } from "@/utils/common";
import ContainerBooks from "@/components/book/books/ContainerBooks.vue";
import NumItems from "@/components/common/NumItems.vue";
import FormBooksSearch from "@/components/book/books_search/FormBooksSearch.vue";


export default {
  components: { FormBooksSearch, NumItems, ContainerBooks },
  props: {
    booksSearchData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      books: {
        type: Object,
        required: true
      },
      page: {
        type: Number,
        required: true
      }
    };
  },
  computed: {
    apiGetBooks() {
      return api.getBooks({
          page: this.page,
          type: this.$route.query.type,
          topic_book__source: this.$route.query.topic_book__source,
          topics__title__in: Array.isArray(this.$route.query.topics__title__in) ? this.$route.query.topics__title__in?.join() : this.$route.query.topics__title__in
        }
      );
    }
  },
  watch: {
    "$route.query": function(newVal, oldVal) {
      this.getBooks();
    }
  },
  beforeMount() {
    this.getBooks();
  },
  mounted() {
    scroll(this.getBooksPage);
  },
  methods: {
    replaceRouterQuery,
    getBooksPage() {
      this.page += 1;
      this.apiGetBooks.then((response) => (this.books.items = this.books.items?.concat(response.data.items)));
    },
    getBooks() {
      this.page = 1;
      this.apiGetBooks.then((response) => (this.books = response.data));
    }
  }
};
</script>


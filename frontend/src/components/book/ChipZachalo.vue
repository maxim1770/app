<template>
  <v-chip
    v-if="zachalo"
    :to="{ name: 'book', params: { bookId: zachalo?.id } }"
    :color="color"
    :prepend-icon="mdAndUp || hasAlwaysSeeOptional ? 'mdi-book-open-page-variant' : undefined"
    class="ma-1"
  >
    <router-link
      v-if="hasBibleBookLink"
      :to="{ name: 'bible-book', params: { bibleBookAbbr: zachalo.bible_book.abbr } }"
      class="text-decoration-none text-blue-accent-4 font-weight-bold"
      :class="{'mr-1': hasZachaloAbbr}"
    >
      {{ zachalo.bible_book.abbr_ru }}
    </router-link>
    <span
      v-else
      :class="{'mr-1': hasZachaloAbbr}"
      class="font-weight-bold"
    >
      {{ zachalo.bible_book.abbr_ru }}
    </span>
    <template
      v-if="hasZachaloAbbr"
    >
      зач.
    </template>
    <BadgeNum :num="zachalo?.num" :color="color" class="ml-1" />
  </v-chip>
</template>

<script>


import { useDisplay } from "vuetify";
import BadgeNum from "@/components/common/BadgeNum.vue";

export default {
  components: { BadgeNum },
  props: {
    zachalo: {
      type: Object,
      required: true
    },
    color: {
      type: String,
      required: false,
      default: "success"
    },
    hasBibleBookLink: {
      type: Boolean,
      required: false,
      default: false
    },
    isPsaltyrBook: {
      type: Boolean,
      required: false,
      default: false
    },
    hasAlwaysSeeOptional: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  computed: {
    hasZachaloAbbr() {
      return (this.hasAlwaysSeeOptional || !this.smAndDown) && !this.isPsaltyrBook;
    }
  },
  setup() {
    const { mdAndUp, smAndDown } = useDisplay();
    return { mdAndUp, smAndDown };
  }
};

</script>



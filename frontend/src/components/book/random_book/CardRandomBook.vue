<template>
  <v-card
    v-once
    class="text-center my-5"
  >
    <v-container>
      <v-row>
        <v-col>
          <v-btn
            @click="getRandomBookId()"
            size="x-large"
            rounded="lg"
            elevation="3"
            variant="text"
            color="blue"
            prepend-icon="mdi-book-open-variant"
            stacked
            class="mb-2"
          >
            <v-badge content="Случайное" class="mb-1" color="blue" />
            Слово, Поучение
          </v-btn>
        </v-col>
      </v-row>
      <v-row
        no-gutters
      >
        <v-col>
          <v-btn-toggle
            variant="text"
            color="blue"
            rounded="lg"
          >
            <v-btn
              @click="getRandomBookId('holiday_book')"
              class="text-blue-lighten-2"
            >
              Житие
            </v-btn>
            <v-btn
              @click="getRandomBookId('movable_date_book')"
              class="text-blue-lighten-2"
              v-if="lgAndUp"
            >
              Чтение по времени
            </v-btn>
            <v-btn
              @click="getRandomBookId('zachalo')"
              class="text-blue-lighten-2"
            >
              Библия
            </v-btn>
            <v-btn
              @click="getRandomBookId('psaltyr_book')"
              class="text-blue-lighten-2"
            >
              Псалом
            </v-btn>
            <v-btn
              @click="getRandomBookId('cathedral_book')"
              class="text-blue-lighten-2"
              v-if="lgAndUp"
            >
              Правило
            </v-btn>
            <v-btn
              @click="getRandomBookId('lls_book')"
              class="text-blue-lighten-2"
              v-if="lgAndUp"
            >
              ЛЛС
            </v-btn>
          </v-btn-toggle>
        </v-col>
      </v-row>
      <v-row
        v-if="!lgAndUp"
        no-gutters
      >
        <v-col>
          <v-btn-toggle
            variant="text"
            color="blue"
            rounded="lg"
          >
            <v-btn
              @click="getRandomBookId('movable_date_book')"
              class="text-blue-lighten-2"
            >
              {{ !smAndDown ? "Чтение по времени" : "По времени" }}
            </v-btn>
            <v-btn
              @click="getRandomBookId('cathedral_book')"
              class="text-blue-lighten-2"
            >
              Правило
            </v-btn>
            <v-btn
              @click="getRandomBookId('lls_book')"
              class="text-blue-lighten-2"
            >
              ЛЛС
            </v-btn>
          </v-btn-toggle>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>

import { api } from "@/services/api";
import { useDisplay } from "vuetify";

export default {

  data() {
    return {
      book_id: {
        type: Number
      }
    };
  },
  setup() {
    const { smAndDown, lgAndUp } = useDisplay();
    return { smAndDown, lgAndUp };
  },
  watch: {
    book_id() {
      this.$router.push({ name: "book", params: { bookId: this.book_id } });
    }
  },
  methods: {
    getRandomBookId(some_book_slug) {
      api.getRandomBookId({
        some_book_slug: some_book_slug
      })
        .then((response) => (this.book_id = response.data.book_id));
    }
  }
};

</script>


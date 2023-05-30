<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" location="right" temporary>
      <template v-slot:prepend>
        <v-list-item
          lines="two"
          title="Иван Иванович"
          subtitle="Logged in"
        ></v-list-item>
      </template>
      <v-divider></v-divider>
      <v-list>
        <v-list-item
          v-for="item in mainPages.slice(0, -1)"
          :key="item.title"
          :to="{ name: item.value }"
          :title="item.title"
          :prepend-icon="item.prependIcon"
        ></v-list-item>
        <v-list-item
          :to="{ name: booksPage.value }"
          :title="booksPage.title"
          :prepend-icon="booksPage.prependIcon"
        >
          <v-menu activator="parent" location="start" open-on-hover transition="scale-transition">
            <v-list density="compact" nav>
              <v-list-item
                v-for="item in const_data.book_topics"
                :key="item"
                :value="item"
                :title="item"
                rounded="xl"
              ></v-list-item>
            </v-list>
          </v-menu>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar :elevation="5">
      <v-app-bar-title>
        <v-btn
          :to="{ name: 'home' }"
          rounded="xl"
          variant="text"
          prepend-icon="mdi-heart-outline"
        >
          Православие в Рукописях
        </v-btn>
      </v-app-bar-title>
      <template v-slot:append>
        <v-btn
          @click="$router.push({ name: 'date', params: { date: todayWithCorrectYear.toISOString().split('T')[0] } })"
        >
          {{ todayWithCorrectYear.toISOString().split("T")[0] }}
        </v-btn>
        <v-combobox
          label="Поиск..."
          clearable
          hide-details
          prepend-icon="mdi-magnify"
          single-line
          style="min-width: 150px"
          @click:prepend=""
        ></v-combobox>
        <v-btn @click="toggleTheme" variant="text" icon="mdi-theme-light-dark"></v-btn>
        <v-divider
          class="mx-1"
          vertical
        ></v-divider>
        <v-btn variant="text" icon="mdi-filter"></v-btn>
        <v-btn icon="mdi-heart"></v-btn>
        <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer">
        </v-app-bar-nav-icon>
      </template>
    </v-app-bar>
    <v-main>
      <v-container
        class="d-flex justify-center align-center"
        style="min-height: 300px"
      >
        <router-view class="mx-md-16"></router-view>
      </v-container>
      <div class="h-75"></div>
      <v-footer class="bg-grey-lighten-1 text-center d-flex flex-column">
        <p>{{ new Date().getFullYear() + 8 }} — Православие в Рукописях</p>
      </v-footer>
    </v-main>
  </v-app>
</template>

<script>
import { api } from "@/services/api";
import { useTheme } from "vuetify";

export default {
  data() {
    return {
      const_data: {
        type: Object,
        required: true
      },
      drawer: null
    };
  },
  computed: {
    booksPage() {
      return this.mainPages.at(-1);
    },
    todayWithCorrectYear() {
      let date = new Date();
      date.setFullYear(date.getFullYear() + 9);
      return date;
    }
  },
  created() {
    this.mainPages = [
      {
        title: "Праздники",
        value: "holidays",
        prependIcon: "mdi-candelabra-fire"
      },
      {
        title: "Святые",
        value: "saints",
        prependIcon: "mdi-account-group"
      },
      {
        title: "Календарь",
        value: "dates",
        prependIcon: "mdi-calendar-blank-outline"
      },
      {
        title: "Рукописи",
        value: "manuscripts",
        prependIcon: "mdi-bookshelf"
      },
      {
        title: "Книги",
        value: "books",
        prependIcon: "mdi-book-open-page-variant"
      }
    ];
  },
  setup() {
    const theme = useTheme();

    return {
      theme,
      toggleTheme: () => theme.global.name.value = theme.global.current.value.dark ? "myCustomLightTheme" : "dark"
    };
  },
  mounted() {
    api
      .getMainConstData()
      .then((response) => (this.const_data = response.data));
  }
};
</script>







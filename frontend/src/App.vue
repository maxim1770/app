<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" location="start" temporary>
      <v-list>
        <v-list-item
            v-for="item in items"
            :key="item.title"
            :title="item.title"
            :to="{ name: item.value }"
        ></v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar color="grey-lighten-2">
      <template v-slot:prepend>
        <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer">
        </v-app-bar-nav-icon>
      </template>

      <v-app-bar-title>
        <v-btn :to="{ name: 'home' }" rounded="xl">Сайт</v-btn>
      </v-app-bar-title>

      <template v-slot:append>
        <v-btn icon="mdi-dots-vertical"></v-btn>
      </template>
    </v-app-bar>

    <v-main>
      <v-container
          class="d-flex justify-center align-center"
          style="min-height: 300px"
      >
        <router-view class="mx-md-16"></router-view>
        >
      </v-container>

      <div class="h-100"></div>
      <v-footer class="bg-indigo-lighten-1 text-center d-flex flex-column">
        <div>{{ new Date().getFullYear() + 8 }} — <strong>Сайт</strong></div>
      </v-footer>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      items: [
        {
          title: "Праздники",
          value: "holidays",
        },
      ],
    };
  },
};
</script>

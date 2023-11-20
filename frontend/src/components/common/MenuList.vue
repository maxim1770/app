<template>
  <v-menu
    activator="parent"
    location="start"
    transition="scale-transition"
    open-on-hover
  >
    <v-list
      density="compact"
      nav
    >
      <v-list-item
        v-for="item in mainData.book_topics"
        :key="item"
        :value="item"
        :title="item"
      ></v-list-item>
    </v-list>
  </v-menu>
</template>

<script>

export default {};
</script>


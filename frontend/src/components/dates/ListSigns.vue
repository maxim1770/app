<template>
  <v-list
    density="compact"
  >
    <v-list-item>
      <template v-slot:prepend>
        <v-icon color="red-accent-4" icon="mdi-numeric-3-circle"></v-icon>
      </template>
      Великий Праздник
      <v-divider class="mt-1" />
    </v-list-item>
    <v-list-item>
      <template v-slot:prepend>
        <v-icon class="bg-red rounded-xl" color="black" icon="mdi-numeric-3"></v-icon>
      </template>
      Средний Праздник, Предпразднство и Попразднство
      <v-divider class="mt-1" />
    </v-list-item>
    <v-list-item>
      <template v-slot:prepend>
        <v-icon color="red-accent-4" icon="mdi-circle-small"></v-icon>
      </template>
      Малый Праздник
      <v-divider class="mt-1" />
    </v-list-item>
    <v-list-item>
      <template v-slot:prepend>
        <v-icon color="red" icon="mdi-numeric-3-circle-outline"></v-icon>
      </template>
      Отдание Праздника
      <v-divider class="mt-1" />
    </v-list-item>
    <v-list-item>
      <template v-slot:prepend>
        <v-icon class="bg-light-blue-accent-4 rounded-xl" color="black" icon="mdi-numeric-3"></v-icon>
      </template>
      Рождественский Пост, Петров Пост, Успенский Пост, Пост в Среду и Пятницу
      <v-divider class="mt-1" />
    </v-list-item>
    <v-list-item>
      <template v-slot:prepend>
        <v-icon class="bg-purple-lighten-2 rounded-xl" color="black" icon="mdi-numeric-3"></v-icon>
      </template>
      Великий Пост
      <v-divider class="mt-1" />
    </v-list-item>
    <v-list-item>
      <template v-slot:prepend>
        <v-icon class="bg-indigo-darken-1 rounded-xl" color="black" icon="mdi-numeric-3"></v-icon>
      </template>
      Страстная Седмица
      <v-divider class="mt-1" />
    </v-list-item>
  </v-list>
</template>

<script>


export default {};

</script>




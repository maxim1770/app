<template>
  <div class="mt-2">
    <h3>Другие {{ holiday.holiday_category.title }}:</h3>
    <v-list lines="one">
      <v-list-item
        prepend-icon="mdi-candelabra-fire"
      >
        <v-chip
          :to="{ name: 'saint', params: { saintSlug: holiday.saints[0].slug } }"
          class="ml-1"
          color="red-darken-3"
        >
          Подробнее
        </v-chip>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>


export default {
  props: {
    holiday: {
      type: Object,
      required: true
    }
  }
};

</script>




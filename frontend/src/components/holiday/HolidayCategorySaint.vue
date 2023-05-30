<template>
  <div class="mt-2">
    <h3>Подробнее:</h3>
    <v-list lines="one">
      <v-list-item
        prepend-icon="mdi-account-heart-outline"
      >
        <v-chip
          :to="{ name: 'saint', params: { saintSlug: holiday.saints[0].slug } }"
          class="ml-1"
        >
          {{ holiday.saints[0].name }}
          <v-chip
            v-if="holiday.saints[0].face_sanctity"
            variant="tonal"
            color="green"
            class="ml-1"
          >
            {{ holiday.saints[0].face_sanctity.title }}
          </v-chip>
          <v-chip
            v-if="holiday.saints[0].dignity"
            variant="tonal"
            class="ml-1"
            color="blue">
            {{ holiday.saints[0].dignity.title }}
          </v-chip>
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




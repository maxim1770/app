<template>
  <div class="d-flex flex-column mb-4 align-content-center" width="400px">
    <div class="mb-2 pa-2">
      <p class="text-h4 font-weight-bold mr-1">
        {{ holiday.title }}
        <v-chip color="green">
          {{ holiday.holiday_category?.title }}
        </v-chip>
        <v-chip v-if="holiday.year" variant="outlined">
          {{ holiday.year.title }}
        </v-chip>
      </p>
    </div>
    <v-btn
        @click="$router.push({ name: 'date', params: { date: holiday.day?.month_day } })"
    >
      {{ holidayDate }}
    </v-btn>

    <v-list class="mb-2 pa-2">
      <v-list-item
          v-for="saint in holiday.saints"
          :key="saint.id"
          :title="saint.name"
          :to="{ name: 'saint', params: { saintSlug: saint.slug } }"
      >
        {{ saint.slug }}
        <v-chip v-if="saint.face_sanctity" class="ma-2" color="green">
          {{ saint.face_sanctity.title }}
        </v-chip>
        <v-chip v-if="saint.dignity" class="ma-2" color="blue">
          {{ saint.dignity.title }}
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
      required: true,
    },
  },

  computed: {
    holidayDate() {
      return `${this.holiday.day?.month}-${this.holiday.day?.day}`;
    },
  },
};
</script>

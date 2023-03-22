<template>
  <div class="75">
    <div class="d-flex justify-space-around mb-5 mt-2 align-center">
      <v-btn
          color="blue"
          @click="$router.push({ name: 'date', params: { date: preDate } })"
      >
        <v-icon icon="mdi-arrow-left"></v-icon>
      </v-btn>
      <p class="text-h2">{{ date.day?.title }}</p>
      <v-btn
          color="blue"
          @click="$router.push({ name: 'date', params: { date: nextDate } })"
      >
        <v-icon icon="mdi-arrow-right"></v-icon>
      </v-btn>
    </div>
    <v-table>
      <thead>
      <tr>
        <th class="text-left">Slug</th>
        <th class="text-left">Название Праздника</th>
        <th class="text-left">Год</th>
        <th class="text-left">Святые</th>
        <th class="text-left">Добавлено</th>
      </tr>
      </thead>
      <tbody>
      <tr
          v-for="holiday in date.day?.holidays"
          :key="holiday.id"
          :class="{ 'bg-yellow': holiday.saints?.length > 1 }"
      >
        <td class="w-0 font-italic">
          {{ holiday.slug }}
          <v-btn @click="copyText(holiday.slug)"> Скопировать</v-btn>
        </td>
        <td class="w-25 text-h6 text-center">{{ holiday.title }}</td>
        <td>
          <v-chip v-if="holiday.year" variant="outlined">
            {{ holiday.year.title }}
          </v-chip>
        </td>
        <td>
          <v-list
              lines="one"
              :class="{ 'bg-yellow': holiday.saints?.length > 1 }"
          >
            <v-list-item
                v-for="saint in holiday.saints"
                :key="saint.id"
                :title="saint.name"
            >
              <v-chip v-if="saint.face_sanctity" class="ma-2" color="green">
                {{ saint.face_sanctity.title }}
              </v-chip>
              <v-chip v-if="saint.dignity" class="ma-2" color="blue">
                {{ saint.dignity.title }}
              </v-chip>
              <br/>
              <p class="font-italic">{{ saint.slug }}</p>
            </v-list-item>
          </v-list>
        </td>
        <td>
          <v-checkbox color="success" hide-details></v-checkbox>
        </td>
      </tr>
      </tbody>
    </v-table>

    <div class="mt-7">
      <hr/>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    date: {
      type: Object,
      required: true,
    },
  },
  computed: {
    preDate() {
      let _preDate = new Date(this.date.day?.month_day)
      _preDate.setDate(_preDate.getDate() - 1)
      return this.date2str(_preDate)
    },
    nextDate() {
      let _nextDate = new Date(this.date.day?.month_day)
      _nextDate.setDate(_nextDate.getDate() + 1)
      return this.date2str(_nextDate)
    },
  },
  methods: {
    date2str(dateObject) {
      return dateObject.toISOString().split('T')[0]
    },
    copyText(text) {
      navigator.clipboard.writeText(text);
    },
  },
};
</script>

<template>
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
      v-for="holiday in allHolidays"
      :key="holiday.id"
      :class="{
                        'bg-green-lighten-3': holiday.title?.includes('NEW'),
                        'bg-yellow': holiday.saints?.length > 1,
                    }"
    >
      <td class="w-0 font-italic">
        {{ holiday?.slug }}
        <div class="d-flex mb-1">
          <v-btn @click="copyText(holiday?.slug)" class="mr-1" color="blue-lighten-3">Скопировать</v-btn>
          <v-btn @click="copyText(holiday?.slug + ' Упоминание')">Упом</v-btn>
        </div>
        <div class="d-flex">
          <v-btn @click="copyText('Тропарь глас ' + glasNumNotNull + ' ' + holiday?.slug)" class="mx-1">
            Тропарь
          </v-btn>
          <v-btn @click="copyText('Кондак глас ' + glasNumNotNull + ' ' +holiday?.slug)">
            Кондак
          </v-btn>
        </div>
        <v-text-field
          v-model.number="glasNum"
          label="Глас"
        >
        </v-text-field>
      </td>
      <td class="w-25 text-h6 text-center"
          :class="{
                        'bg-green-lighten-3': holiday.title?.includes('NEW'),
                  }"
      >
        {{ holiday?.title }}
      </td>
      <td>
        <v-chip
          v-if="holiday?.year"
          :class="{
                    'bg-red': holiday?.year.year < 5500 + 1600,
                    'bg-yellow-accent-2': holiday?.year.year < 5500 + 1500,
                    'bg-light-blue': holiday?.year.year < 5500 + 1400,
                    'bg-grey-lighten-5': holiday?.year.year < 5500 + 1000,
                  }"
        >
          {{ holiday?.year.title }}
        </v-chip>
      </td>
      <td>
        <v-list
          :class="{
                        'bg-green-lighten-4': holiday.title?.includes('NEW') && holiday.saints?.length > 1,
                        'bg-green-lighten-3': holiday.title?.includes('NEW'),
                        'bg-yellow': holiday.saints?.length > 1,
                            }"
        >
          <v-list-item
            v-for="saint in holiday?.saints"
            :key="saint.id"
            :title="saint.name"
          >
            <v-chip
              v-if="saint.face_sanctity"
              class="ma-2"
              :class="{
                    'text-red': saint.face_sanctity.title.toLowerCase().indexOf('мучени') !== -1,
                    'text-green': saint.face_sanctity.title.toLowerCase().indexOf('мучени') === -1
                     }"
            >
              {{ saint.face_sanctity.title }}
            </v-chip>
            <v-chip
              v-if="saint.dignity"
              class="ma-2 text-blue"
            >
              {{ saint.dignity.title }}
            </v-chip>
            <br />
            <p class="font-italic mt-1 mb-2">{{ saint.slug }}</p>
            <p class="font-italic mb-4">{{ saint.url }}</p>
            <p class="font-italic">{{ azbykaURL }}</p>
          </v-list-item>
        </v-list>
      </td>
      <td>
        <v-checkbox color="success" hide-details></v-checkbox>
      </td>
    </tr>
    </tbody>
  </v-table>
  <v-divider />
</template>

<script>


import { date2dateSlug } from "@/utils/date";

export default {
  props: {
    date: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      glasNum: 0
    };
  },
  computed: {
    glasNumNotNull() {
      if (this.glasNum === null) { // FIXME: не работает
        return "0";
      }
      return this.glasNum;
    },
    azbykaDate() {
      let _azbykaDate = new Date(this.date.day?.date_slug);
      _azbykaDate.setDate(_azbykaDate.getDate() + 13);
      return date2dateSlug(_azbykaDate);
    },
    azbykaURL() {
      return "https://azbyka.ru/days/" + this.azbykaDate;
    },
    allHolidays() {
      let allHolidays = [];
      if (this.date.day?.holidays) {
        allHolidays = allHolidays.concat(this.date.day.holidays);
      }
      if (this.date.movable_day?.holidays) {
        allHolidays = allHolidays.concat(this.date.movable_day.holidays);
      }
      if (this.date.day?.before_after_holidays.length) {
        allHolidays.push(this.date.day.before_after_holidays[0].before_after_holiday.holiday);
      }
      if (this.date.movable_day?.before_after_holidays.length) {
        allHolidays.push(this.date.movable_day.before_after_holidays[0].before_after_holiday.holiday);
      }
      return allHolidays;
    }
  },
  methods: {
    copyText(text) {
      navigator.clipboard.writeText(text);
    }
  }
};
</script>


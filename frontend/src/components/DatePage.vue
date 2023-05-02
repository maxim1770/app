<template>
  <div class="75">
    <div class="d-flex justify-center mb-5 mt-2 align-center">
      <v-btn
          color="blue"
          @click="$router.push({ name: 'date', params: { date: preDate } })"
          class="mr-12"
      >
        <v-icon icon="mdi-arrow-left"></v-icon>
      </v-btn>
      <p class="text-h2">{{ date.day?.title }}</p>
      <v-btn
          color="blue"
          @click="$router.push({ name: 'date', params: { date: nextDate } })"
          class="ml-12"
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
          :class="{
                        'bg-green-lighten-3': holiday.title.includes('NEW G_M_2'),
                        'bg-yellow': holiday.saints?.length > 1,
                    }"
      >
        <td class="w-0 font-italic">
          {{ holiday.slug }}
          <div class="d-flex mb-1">
            <v-btn @click="copyText(holiday.slug)" class="mr-1" color="blue-lighten-3">Скопировать</v-btn>
            <v-btn @click="copyText(holiday.slug + ' Упоминание')">Упом</v-btn>
          </div>
          <div class="d-flex">
            <v-btn @click="copyText('Тропарь глас ' + foo_num_not_null + ' ' + holiday.slug)" class="mx-1">
              Тропарь
            </v-btn>
            <v-btn @click="copyText('Кондак глас ' + foo_num_not_null + ' ' +holiday.slug)">
              Кондак
            </v-btn>
          </div>
          <v-text-field
              v-model.number="foo_num"
              label="Глас"
          >
          </v-text-field>
        </td>
        <td class="w-25 text-h6 text-center"
            :class="{
                        'bg-green-lighten-3': holiday.title.includes('NEW G_M_2'),
                  }"
        >
          {{ holiday.title }}
        </td>
        <td>
          <v-chip
              v-if="holiday.year"
              :class="{
                    'bg-red': holiday.year.year < 5500 + 1600,
                    'bg-yellow-accent-2': holiday.year.year < 5500 + 1500,
                    'bg-light-blue': holiday.year.year < 5500 + 1400,
                    'bg-grey-lighten-5': holiday.year.year < 5500 + 1000,
                  }"
              variant="outlined"
          >
            {{ holiday.year.title }}
          </v-chip>
        </td>
        <td>
          <v-list
              lines="one"
              :class="{
                        'bg-green-lighten-4': holiday.title.includes('NEW G_M_2') && holiday.saints?.length > 1,
                        'bg-green-lighten-3': holiday.title.includes('NEW G_M_2'),
                        'bg-yellow': holiday.saints?.length > 1,
                            }"
          >
            <v-list-item
                v-for="saint in holiday.saints"
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
              <br/>
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
  data() {
    return {
      foo_num: 0
    };
  },
  computed: {
    foo_num_not_null() {
      if (this.foo_num === null) { // FIXME: не работает
        return '0'
      }
      return this.foo_num
    },
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
    azbykaDate() {
      let _azbykaDate = new Date(this.date.day?.month_day)
      _azbykaDate.setDate(_azbykaDate.getDate() + 13)
      return this.date2str(_azbykaDate)
    },
    azbykaURL() {
      return 'https://azbyka.ru/days/' + this.azbykaDate
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

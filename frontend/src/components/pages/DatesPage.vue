<template>
  <div>
    <v-sheet>
      <v-calendar
        v-model="selectedDate"
        :date-formatter="customDateFormatter"
        :initial-page="{ month: 9, year: 2023 }"
        :attributes="dates.attributes"
        :rows="4"
        :columns="3"
        first-day-of-week="1"
        @dayclick="toSelectedDay"
        @transition-start="Foo"
      >
        <template #popover="{ event: { popover } }">{{ popover.description }}</template>
      </v-calendar>
    </v-sheet>
    <v-list
      density="compact"
      lines="one"
    >
      <v-list-item>
        <template v-slot:prepend>
          <v-icon color="red-accent-4" icon="mdi-numeric-3-circle"></v-icon>
        </template>
        Великий Праздник
      </v-list-item>
      <v-list-item>
        <template v-slot:prepend>
          <v-icon class="bg-red rounded-xl" color="black" icon="mdi-numeric-3"></v-icon>
        </template>
        Средний Праздник, Предпразднство и Попразднство
      </v-list-item>
      <v-list-item>
        <template v-slot:prepend>
          <v-icon color="red-accent-4" icon="mdi-circle-small"></v-icon>
        </template>
        Малый Праздник
      </v-list-item>
      <v-list-item>
        <template v-slot:prepend>
          <v-icon color="red" icon="mdi-numeric-3-circle-outline"></v-icon>
        </template>
        Отдание Праздника
      </v-list-item>
      <v-list-item>
        <template v-slot:prepend>
          <v-icon class="bg-light-blue-accent-4 rounded-xl" color="black" icon="mdi-numeric-3"></v-icon>
        </template>
        Рождественский Пост, Петров Пост, Успенский Пост, Пост в Среду и Пятницу
      </v-list-item>
      <v-list-item>
        <template v-slot:prepend>
          <v-icon class="bg-purple-lighten-2 rounded-xl" color="black" icon="mdi-numeric-3"></v-icon>
        </template>
        Великий Пост
      </v-list-item>
      <v-list-item>
        <template v-slot:prepend>
          <v-icon class="bg-indigo-darken-1 rounded-xl" color="black" icon="mdi-numeric-3"></v-icon>
        </template>
        Страстная Седмица
      </v-list-item>
    </v-list>
  </div>
</template>

<script>


export default {
  props: {
    dates: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      selectedDate: new Date()
    };
  },
  methods: {
    toSelectedDay(CalendarDay) {
      let year = CalendarDay.year + 8;
      if ((9 <= CalendarDay.month) && (CalendarDay.month <= 12)) {
        year += 1;
      }
      this.$router.push({ name: "date", params: { date: CalendarDay.id.replace(CalendarDay.year, year) } });
    },
    Foo() {
      console.log("test");
    },
    customDateFormatter(date, format, type) {
      if (type === "calendar") {
        return this.$moment.utc(date).format("D MMMM");
      }
      return this.$moment.utc(date).format("YYYY-MM-DD");
    }
  }
};
</script>

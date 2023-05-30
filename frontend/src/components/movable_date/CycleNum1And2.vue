<template>
  <div>
    <v-container
        v-for='week in cycle.weeks'
        :key='week.id'
        class='mb-2 rounded-lg border text-center'
    >
      <v-row class='bg-red-lighten-3 border-b'>
        <v-col
            cols='12'
            class='text-h6 text-red-accent-4 font-weight-bold'
        >
          Нд {{ week.sunday_num }}<template v-if='week.sunday_title'>, {{ week.sunday_title }}</template>
        </v-col>
      </v-row>
      <v-row
          v-if='sundayMatins(week)'
          class='bg-red-lighten-3'
      >
        <v-col cols='2'>
          <p v-if='sundayMatins(week).divine_service.title === "matins"'>
            На Утрене
          </p>
          <p v-else>
            На Вечерне
          </p>
        </v-col>
        <v-col offset='1' cols='4'>
          <p class='text-red-accent-3'>
            {{ sundayMatins(week).zachalos[0].title }}
          </p>
        </v-col>
        <v-col cols='5'>
          <v-chip variant="tonal" color='red-accent-3'>
            {{ sundayMatins(week).zachalos[0].bible_book.abbr_ru }} зач.
            {{ sundayMatins(week).zachalos[0].num }}
          </v-chip>
        </v-col>
      </v-row>
      <v-row class='bg-red-lighten-3 border-b-md'>
        <v-col cols='2'>
          На Литургии
        </v-col>
        <v-col
            v-for='zachalo in sundayLiturgyZachalos(week)'
            :key='zachalo.id'
            cols='5'
        >
          <v-chip color='red-accent-3'>
            {{ zachalo.bible_book.abbr_ru }} зач. {{ zachalo.num }}
          </v-chip>
        </v-col>
      </v-row>
      <v-row
          v-for='movable_day in week.movable_days.slice(1)'
          :key='movable_day.id'
      >
        <v-col cols='2' class='text-capitalize'>
          {{ movable_day.abbr_ru }}
        </v-col>
        <v-col
            v-for='zachalo in movable_day.movable_dates[0].zachalos'
            v-if='movable_day.movable_dates[0]'
            :key='zachalo.id'
            cols='5'
        >
          <v-chip color='success'>
            {{ zachalo.bible_book.abbr_ru }} зач. {{ zachalo.num }}
          </v-chip>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>

export default {
  props: {
    cycle: {
      type: Object,
      required: true,
    },
  },
  methods: {
    sundayMatins(week) {
      return week.movable_days[0].movable_dates.filter(movable_date => movable_date.divine_service.title !== 'liturgy')[0]
    },
    sundayLiturgyZachalos(week) {
      return week.movable_days[0].movable_dates.filter(movable_date => movable_date.divine_service.title === "liturgy")[0].zachalos
    },
  },
}
</script>


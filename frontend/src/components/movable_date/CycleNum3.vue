<template>
    <div>
        <v-container
                v-for='week in cycle.weeks.slice(0, -2)'
                :key='week.id'
                class='mb-2 rounded-lg border text-center'
        >
            <v-row
                    v-for='movable_day in week.movable_days.slice(5)'
                    :key='movable_day.id'
            >
                <v-col cols='2'>
                    {{ movable_day.abbr_ru.replace('вс', 'нд') }} {{ week.sunday_num }}
                </v-col>
                <v-col
                        v-for='zachalo in movable_day.movable_dates[0].zachalos'
                        :key='zachalo.id'
                        cols='5'
                >
                    <v-chip color='success'>
                        {{ zachalo.bible_book.abbr_ru }} зач. {{ zachalo.num }}
                    </v-chip>
                </v-col>
            </v-row>
        </v-container>
        <v-container
                class='mb-2 rounded-lg border text-center'
        >
            <v-row>
                <v-col cols='2'>
                    {{ satWeek6.abbr_ru }} {{ week6.sunday_num }}, {{ satWeek6.title }}
                </v-col>
                <v-col
                        v-for='zachalo in satLiturgyWeek6'
                        :key='zachalo.id'
                        cols='5'
                >
                    <v-chip color='success'>
                        {{ zachalo.bible_book.abbr_ru }} зач. {{ zachalo.num }}
                    </v-chip>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols='2'>
                    {{ sunWeek6.abbr_ru }} {{ week6.sunday_num }}, {{ sunWeek6.title }}
                </v-col>
                <v-col offset='1' cols='4'>
                    Евангелие на Утрене
                </v-col>
                <v-col cols='5'>
                    <v-chip color='success'>
                        {{ sunMatinsWeek6.bible_book.abbr_ru }} зач. {{ sunMatinsWeek6.num }}
                    </v-chip>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols='2'>
                    На Литургии
                </v-col>
                <v-col
                        v-for='zachalo in sunLiturgyWeek6'
                        :key='zachalo.id'
                        cols='5'
                >
                    <v-chip color='success'>
                        {{ zachalo.bible_book.abbr_ru }} зач. {{ zachalo.num }}
                    </v-chip>
                </v-col>
            </v-row>
        </v-container>
        <v-container
                class='rounded-lg border text-center text-red-accent-3'
        >
            <template
                    v-for='movable_day in strastnajaSedmitsa.movable_days.slice(0, 4)'
                    :key='movable_day.id'
            >
                <v-row>
                    <v-col cols='12' class='text-red-accent-4 bg-red-lighten-3'>
                        {{ movable_day.title }}
                    </v-col>
                </v-row>
                <v-row>
                    <v-col offset='1' cols='6'>
                        На Литургии
                    </v-col>
                    <v-col cols='5'>
                        <v-chip>
                            {{ dayLiturgyStrastnajaSedmitsa(movable_day).bible_book.abbr_ru }} зач.
                            {{ dayLiturgyStrastnajaSedmitsa(movable_day).num }}
                        </v-chip>
                    </v-col>
                </v-row>
            </template>
            <v-row
                    no-gutters
                    class='mt-2'
            >
                <v-col offset='1' cols='6'>
                    На умовение ногам
                </v-col>
                <v-col cols='5'>
                    <v-chip>
                        {{ thuUmyveniyeStrastnajaSedmitsa[0].bible_book.abbr_ru }} зач.
                        {{ thuUmyveniyeStrastnajaSedmitsa[0].num }}
                    </v-chip>
                </v-col>
            </v-row>
            <v-row
                    no-gutters
                    class='mt-1'
            >
                <v-col offset='1' cols='6'>
                    По умовению
                </v-col>
                <v-col cols='5'>
                    <v-chip>
                        {{ thuUmyveniyeStrastnajaSedmitsa[1].bible_book.abbr_ru }} зач.
                        {{ thuUmyveniyeStrastnajaSedmitsa[1].num }}
                    </v-chip>
                </v-col>
            </v-row>
            <v-row
                    no-gutters
                    class='mt-2'
            >
                <v-col offset='1' cols='6'>
                    Апостол на Вечерне
                </v-col>
                <v-col cols='5'>
                    <v-chip>
                        {{ thuVespersStrastnajaSedmitsa.bible_book.abbr_ru }} зач.
                        {{ thuVespersStrastnajaSedmitsa.num }}
                    </v-chip>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols='12' class='text-red-accent-4 bg-red-lighten-3 mb-3'>
                    Евангелия 12 Святых Страстей Господа Бога и Спаса нашего Исуса Христа
                </v-col>
            </v-row>
            <v-row
                    v-for='zachalo in friCommonStrastnajaSedmitsa.slice(0, 12)'
                    :key='zachalo.id'
                    no-gutters
                    class='mt-3'
            >
                <v-col cols='12'>
                    <v-chip style='width: 100px;'>
                        {{ zachalo.bible_book.abbr_ru }} зач. {{ zachalo.num }}
                    </v-chip>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols='12' class='text-red-accent-4 bg-red-lighten-3'>
                    Последование часов Святой и Великой Пятницы
                </v-col>
            </v-row>
            <v-row
                    v-for='i in 4'
            >
                <v-col cols='2'>
                    На Часе
                    <template v-if='(i - 1) * 3 === 0'>1</template>
                    <template v-else>{{ (i - 1) * 3}}</template>
                </v-col>
                <v-col cols='5'>
                    <v-chip>
                        {{ friCommonStrastnajaSedmitsa[11 + i].bible_book.abbr_ru }} зач.
                        {{ friCommonStrastnajaSedmitsa[11 + i].num }}
                    </v-chip>
                </v-col>
                <v-col cols='5'>
                    <v-chip>
                        {{ friCommonStrastnajaSedmitsa[15 + i].bible_book.abbr_ru }} зач.
                        {{ friCommonStrastnajaSedmitsa[15 + i].num }}
                    </v-chip>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols='2'>
                    На Вечерне
                </v-col>
                <v-col
                        v-for='zachalo in friVespersStrastnajaSedmitsa'
                        :key='zachalo.id'
                        cols='5'
                >
                    <v-chip>
                        {{ zachalo.bible_book.abbr_ru }} зач. {{ zachalo.num }}
                    </v-chip>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols='12' class='text-red-accent-4 bg-red-lighten-3'>
                    {{ satStrastnajaSedmitsa.title }}
                </v-col>
            </v-row>
            <v-row>
                <v-col cols='2'>
                    На Утрене
                </v-col>
                <v-col
                        v-for='zachalo in satMatinsStrastnajaSedmitsa'
                        :key='zachalo.id'
                        cols='5'
                >
                    <v-chip>
                        {{ zachalo.bible_book.abbr_ru }} зач. {{ zachalo.num }}
                    </v-chip>
                </v-col>
            </v-row>
            <v-row>
                <v-col cols='2'>
                    Вечер на Литургии (или Вечерня) (не знаю)
                </v-col>
                <v-col
                        v-for='zachalo in satLiturgyStrastnajaSedmitsa'
                        :key='zachalo.id'
                        cols='5'
                >
                    <v-chip>
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
  computed: {
    week6() {
      return this.cycle.weeks[5]
    },
    strastnajaSedmitsa() {
      return this.cycle.weeks[6]
    },
    satWeek6() {
      return this.week6.movable_days[5]
    },
    sunWeek6() {
      return this.week6.movable_days[6]
    },
    thuStrastnajaSedmitsa() {
      return this.strastnajaSedmitsa.movable_days[3]
    },
    friStrastnajaSedmitsa() {
      return this.strastnajaSedmitsa.movable_days[4]
    },
    satStrastnajaSedmitsa() {
      return this.strastnajaSedmitsa.movable_days[5]
    },
    satLiturgyWeek6() {
      return this.satWeek6.movable_dates.filter(movable_date => movable_date.divine_service.title === 'liturgy')[0].zachalos
    },
    sunMatinsWeek6() {
      return this.sunWeek6.movable_dates.filter(movable_date => movable_date.divine_service.title === 'matins')[0].zachalos[0]
    },
    sunLiturgyWeek6() {
      return this.sunWeek6.movable_dates.filter(movable_date => movable_date.divine_service.title === 'liturgy')[0].zachalos
    },
    thuUmyveniyeStrastnajaSedmitsa() {
      return this.thuStrastnajaSedmitsa.movable_dates.filter(movable_date => movable_date.divine_service === null)[0].zachalos
    },
    thuVespersStrastnajaSedmitsa() {
      return this.thuStrastnajaSedmitsa.movable_dates.filter(movable_date => movable_date.divine_service?.title === 'vespers')[0].zachalos[0]
    },
    friCommonStrastnajaSedmitsa() {
      return this.friStrastnajaSedmitsa.movable_dates.filter(movable_date => movable_date.divine_service === null)[0].zachalos
    },
    friVespersStrastnajaSedmitsa() {
      return this.friStrastnajaSedmitsa.movable_dates.filter(movable_date => movable_date.divine_service?.title === 'vespers')[0].zachalos
    },
    satMatinsStrastnajaSedmitsa() {
      return this.satStrastnajaSedmitsa.movable_dates.filter(movable_date => movable_date.divine_service.title === 'matins')[0].zachalos
    },
    satLiturgyStrastnajaSedmitsa() {
      return this.satStrastnajaSedmitsa.movable_dates.filter(movable_date => movable_date.divine_service.title === 'liturgy')[0].zachalos
    }
  },
  methods: {
    dayLiturgyStrastnajaSedmitsa(movable_day) {
      return movable_day.movable_dates.filter(movable_date => movable_date.divine_service?.title === 'liturgy')[0].zachalos[0]
    },
  },
}
</script>


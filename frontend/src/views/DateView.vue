<template>
    <div class="d-block">
        <v-btn
                @click=foo
                class="d-flex w-100 justify-center mb-5 mt-2 align-center text-center"
                :class="{
                        'bg-green-lighten-3': date.day?.has_new_holidays
                    }"
        >
            test
        </v-btn>
        <DatePage :date="date"/>
    </div>
</template>

<script>
import {api} from "@/api";
import DatePage from "@/components/DatePage.vue";

export default {
  components: {DatePage},

  data() {
    return {
      date: {
        type: Object,
        required: true,
      },
    };
  },
  watch: {
    $route(to, from) {
      this.getDate()
    }
  },
  mounted() {
      this.getDate()

      // this.sleep(3600)
      // console.log(this.date)

  },
  methods: {
      getDate() {
          api
              .getDate(this.$route.params.date)
              .then((response) => (this.date = response.data));
      },
      foo() {
          console.log(this.date.day?.has_new_holidays)
          if (this.date.day?.has_new_holidays === false) {
              console.log(this.nextDate())
              this.$router.push({name: 'date', params: {date: this.nextDate()}})

              // api
              //   .getDate(this.nextDate())
              //   .then((response) => (this.date = response.data));

          }
      },
      sleep(ms) {
          return new Promise(resolve => setTimeout(resolve, ms));
      },
      nextDate() {
          let _nextDate = new Date(this.date.day?.month_day)
          _nextDate.setDate(_nextDate.getDate() + 1)
          return this.date2str(_nextDate)
      },
      date2str(dateObject) {
          return dateObject.toISOString().split('T')[0]
      },
  },
};
</script>

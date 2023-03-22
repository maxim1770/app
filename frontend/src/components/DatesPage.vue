<template>
  <div class='d-flex w-100 h-100'>
    <div class='flex-grow-1 p-3'>
      <FullCalendar
          class='text-subtitle-2 text-sm-body-2 text-lg-h5'
          :options='calendarOptions'
      >
        <template v-slot:eventContent='arg'>
          <b>{{ arg.timeText }}</b>
          <i>{{ arg.event.title }}</i>
        </template>
      </FullCalendar>
    </div>
  </div>
</template>

<script>
import {defineComponent} from 'vue'
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'


export default defineComponent({
  components: {
    FullCalendar,
  },
  props: {
    dates: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      calendarOptions: {
        plugins: [
          dayGridPlugin,
          timeGridPlugin,
          interactionPlugin // needed for dateClick
        ],
        headerToolbar: {
          left: 'prev,next today',
          center: 'title',
          right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        locale: 'ru',
        initialView: 'dayGridMonth',
        initialEvents: this.getInitialEvents(),
        editable: true,
        selectable: true,
        selectMirror: true,
        dayMaxEvents: true,
        weekends: true,
        weekNumbers: true,
        weekNumberCalculation: this.weekNumberCalculation,
        select: this.handleDateSelect,
        eventClick: this.handleEventClick,
      },
    }
  },
  methods: {
    getInitialEvents() {
      console.log(this.dates?.[0])
      const initialEvents = [
        {
          id: 'test',
          title: 'All-day esdfsdfdsvent',
          start: '2023-03-21'
        }
      ]
      return initialEvents;
    },
    handleDateSelect(selectInfo) {
      let date = new Date(selectInfo.startStr)
      date.setFullYear(date.getFullYear() + 9)
      this.$router.push({
        name: 'date',
        params: {date: date.toISOString().split('T')[0]},
      })
    },
    weekNumberCalculation(weekMoment) {
      let weekDate = new Date(weekMoment.startStr)
      weekDate.setFullYear(weekDate.getFullYear() + 9)
      // console.log(this.dates?.[1])
      // this.dates.forEach((date) => {
      //   console.log(date.year);
      // });
      // const date = this.dates.filter(dates => date.day?.month_day == weekDate.toISOString().split('T')[0])[0];
      return 0;
    },
    handleEventClick(clickInfo) {
      this.$router.push({
        name: 'holiday',
        params: {holidaySlug: clickInfo.event.id},
      })
    },
  }
})

</script>

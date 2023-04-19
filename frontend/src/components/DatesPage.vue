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
      type: Array,
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
      let initialEvents = [];
      // for (let date of this.dates) {
      //   for (let holiday of date.day?.holidays) {
      //     let dateStr = new Date(date.day?.month_day);
      //     dateStr.setFullYear(dateStr.getFullYear() - 9);
      //     const event = {
      //       id: holiday?.slug,
      //       title: holiday?.title,
      //       start: this.date2str(dateStr)
      //     };
      //     initialEvents.push(event);
      //   }
      // }
      return initialEvents;
    },
    handleDateSelect(selectInfo) {
      let date = new Date(selectInfo.startStr)
      date.setFullYear(date.getFullYear() + 9)
      this.$router.push({
        name: 'date',
        params: {date: this.date2str(date)},
      })
    },
    weekNumberCalculation(weekMoment) {
      weekMoment.setFullYear(weekMoment.getFullYear() + 9)
      let result = this.dates?.find(function (item) {
        console.log(item)
      });
      console.log(result)
      return result; //date.day?.month_day === this.date2str(weekMoment)
    },
    handleEventClick(clickInfo) {
      this.$router.push({
        name: 'holiday',
        params: {holidaySlug: clickInfo.event.id},
      })
    },
    date2str(dateObject) {
      return dateObject.toISOString().split('T')[0]
    },
  }
})

</script>

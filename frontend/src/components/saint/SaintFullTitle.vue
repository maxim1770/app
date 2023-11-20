<template>
  <span
    :class="choiceHolidayTextColor(holiday)"
    class="ma-1"
  >
    {{ saint.name }}
  </span>
  <BadgeFaceSanctity :face_sanctity="saint.face_sanctity" class="ma-1" />
  <BadgeDignity :dignity="saint.dignity" class="ma-1" />
</template>

<script>


import BadgeDignity from "@/components/saint/dignity/BadgeDignity.vue";
import BadgeFaceSanctity from "@/components/saint/face_sanctity/BadgeFaceSanctity.vue";
import { choiceHolidayTextColor } from "@/utils/holidays";


export default {
  components: { BadgeFaceSanctity, BadgeDignity },
  props: {
    saint: {
      type: Object,
      required: true
    },
    holiday: {
      type: Object,
      required: false,
      default: null
    }
  },
  methods: { choiceHolidayTextColor }
};

</script>




<template>
  <v-card>
    <v-card-item>
      <v-list>
        <v-list-item
          v-if="saint"
          :to="{ name: 'saint', params: { saintSlug: saint.slug } }"
        >
          <template v-slot:prepend>
            <v-icon
              icon="mdi-account-heart-outline"
              :color="choiceHolidayColor(holiday)"
            />
          </template>
          <SaintFullTitle :saint="saint" :holiday="holiday" />
        </v-list-item>
      </v-list>
    </v-card-item>
  </v-card>
</template>

<script>


import SaintFullTitle from "@/components/saint/SaintFullTitle.vue";
import { choiceHolidayColor } from "@/utils/holidays";


export default {
  components: { SaintFullTitle },
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
  methods: { choiceHolidayColor }

};

</script>


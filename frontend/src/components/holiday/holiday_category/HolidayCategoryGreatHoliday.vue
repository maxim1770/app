<template>
  <ChapterWithHead
    :headTitle="`Другие ${ holiday.holiday_category ? holiday.holiday_category.title : 'Праздники' }`"
  >
    <v-card>
      <v-card-item>
        <v-list>
          <v-list-item
            :to="{ name: 'saint', params: { saintSlug: holiday.saints[0].slug } }"
          >
            <template v-slot:prepend>
              <v-icon
                icon="mdi-candelabra-fire"
                :color="choiceHolidayColor(holiday)"
                size="large"
              />
            </template>
            <SaintFullTitle
              :saint="holiday.saints[0]"
              :holiday="holiday"
            />
          </v-list-item>
        </v-list>
      </v-card-item>
    </v-card>
  </ChapterWithHead>
</template>

<script>


import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import { choiceHolidayColor } from "@/utils/holidays";
import SaintFullTitle from "@/components/saint/SaintFullTitle.vue";

export default {
  components: { SaintFullTitle, ChapterWithHead },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  },
  methods: {
    choiceHolidayColor
  }
};

</script>




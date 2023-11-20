<template>
  <div class="my-2">
    <v-sheet class="bg-blue-lighten-2 pa-12" rounded>
      <v-card class="mx-auto px-6 py-8" max-width="500">
        <div>
          <v-select
            v-model="tipikon__title"
            :items="holidaysSearchData.tipikons"
            class="mb-2"
            clearable
            label="Выберите Типикон Праздника"
            variant="underlined"
          ></v-select>
          <br>
          <v-btn
            @click="putHoliday"
            block
            color="success"
            size="large"
            type="submit"
            variant="elevated"
          >
            Обновить
          </v-btn>
          <ListItemTipikon :tipikon="holiday.tipikon" />
        </div>
      </v-card>
    </v-sheet>
    <v-divider />
  </div>
</template>

<script>


import ListItemTipikon from "@/components/holiday/tipikon/ListItemTipikon.vue";
import { api } from "@/services/api";

export default {
  components: { ListItemTipikon },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      tipikon__title: null,
      holidaysSearchData: {
        type: Object,
        required: true
      }
    };
  },
  mounted() {
    api
      .getHolidaysSearchData()
      .then((response) => (this.holidaysSearchData = response.data));
  },
  methods: {
    putHoliday() {
      api
        .putHoliday({ "holidaySlug": this.$route.params.holidaySlug, "tipikon__title": this.tipikon__title })
        .then((response) => (this.holiday = response.data));
    }
  }
};

</script>




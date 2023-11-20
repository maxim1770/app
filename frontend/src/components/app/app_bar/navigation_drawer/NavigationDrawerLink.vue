<template v-slot:append>
  <v-list>
    <v-list-item
      @click="toUrl(TG_CHANNEL_LINK)"
      class="text-center"
    >
      <v-icon
        icon="custom:tg"
        size="x-large"
      />
      <p
        :style="{ 'font-size': 'smaller' }"
      >
        Присоединяйтесь к нам в телеграм!
      </p>
    </v-list-item>
  </v-list>
</template>

<script>


import { toUrl } from "@/utils/common";
import { TG_CHANNEL_LINK } from "@/env";

export default {
  computed: {
    TG_CHANNEL_LINK() {
      return TG_CHANNEL_LINK;
    }
  },
  methods: {
    toUrl
  }
};

</script>




<template>
  <span v-if="saint">
    <v-chip
      v-if="!saint.name_in_genitive"
      prepend-icon="mdi-account-heart-outline"
      color="cyan-darken-1"
      class="ma-1"
    >
      Автор
    </v-chip>
    <router-link
      :to="{ name: 'saint', params: { saintSlug: saint.slug } }"
      class="text-decoration-none text-black ma-1"
    >
      <template v-if="saint.name_in_genitive">
        {{ saint.name_in_genitive }}
      </template>
      <template v-else>
        {{ saint.name }}
      </template>
    </router-link>
    <BadgeFaceSanctity
      :face_sanctity="saint?.face_sanctity"
      class="ma-1"
    />
    <BadgeDignity
      :dignity="saint?.dignity"
      class="ma-1"
    />
  </span>
</template>

<script>


import BadgeDignity from "@/components/saint/dignity/BadgeDignity.vue";
import BadgeFaceSanctity from "@/components/saint/face_sanctity/BadgeFaceSanctity.vue";

export default {
  components: { BadgeFaceSanctity, BadgeDignity },
  props: {
    saint: {
      type: Object,
      required: true
    }
  }
};

</script>




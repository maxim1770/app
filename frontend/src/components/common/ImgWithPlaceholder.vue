<template>
  <v-img :src="src">
    <template v-slot:placeholder>
      <div class="d-flex align-center justify-center fill-height">
        <v-progress-circular
          color="grey-lighten-4"
          indeterminate
        ></v-progress-circular>
      </div>
    </template>
  </v-img>
</template>

<script>

export default {
  props: {
    src: {
      type: String,
      required: true
    }
  }
};

</script>


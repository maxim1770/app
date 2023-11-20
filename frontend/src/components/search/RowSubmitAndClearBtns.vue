<template>
  <v-row>
    <v-col
      cols="12"
      md="6"
    >
      <v-btn
        class="text-none"
        color="grey-lighten-3"
        size="x-large"
        variant="flat"
        @click="clear"
        block
      >
        Очистить
      </v-btn>
    </v-col>
    <v-col
      cols="12"
      md="6"
    >
      <v-btn
        :disabled="loading"
        :loading="loading"
        class="text-none"
        color="blue-darken-2"
        size="x-large"
        variant="flat"
        @click="submit"
        block
      >
        Искать
      </v-btn>
    </v-col>
  </v-row>

</template>


<script>

export default {
  emits: ["getItems"],
  data() {
    return {
      loading: false
    };
  },
  methods: {
    clear() {
      this.$router.replace({
        query: { "notEmptyQuery": null }
      });
    },
    submit() {
      this.loading = true;
      this.$emit("getItems");
      this.loading = false;
    }
  }
};

</script>


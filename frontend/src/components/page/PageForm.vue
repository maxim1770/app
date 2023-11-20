<template>
  <v-combobox
    v-model="page_num"
    label="Num"
    variant="underlined"
    clearable
    class="mb-2"
  ></v-combobox>
  <br>
  <v-select
    v-model="page_position"
    :items="[0, 1]"
    label="Position"
    variant="underlined"
    clearable
    class="mb-2"
  ></v-select>

</template>

<script>


export default {
  props: {
    page: {
      type: Object,
      required: true
    }
  },
  emits: ["update:page"],
  data() {
    return {
      page_num: null,
      page_position: null
    };
  },
  computed: {
    page_() {
      return { "num": Number(this.page_num), "position": Number(this.page_position) };
    }
  },
  watch: {
    page_() {
      this.$emit("update:page", this.page_);
    }
  }
};

</script>




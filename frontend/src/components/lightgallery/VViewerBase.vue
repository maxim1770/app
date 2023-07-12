<template>
  <div>
    <viewer :options="options" :images="imgsWithHost"
            @inited="inited"
            class="viewer" ref="viewer"
    >
      <template #default="scope">
        <img v-for="src in scope.imgsWithHost" :src="src" :key="src">
        {{scope.options}}
      </template>
    </viewer>
    <button type="button" @click="show">Show</button>
  </div>
</template>

<script>


import 'viewerjs/dist/viewer.css'
import { component as Viewer } from "v-viewer"
export default {
  components: { Viewer },
  props: {
    imgs: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      index: null
    };
  },
  computed: {
    imgsWithHost() {
      const imgsWithHost_ = [];
      for (let i = 0; i < this.imgs?.length; i++) {
        imgsWithHost_.push(
          "http://localhost:81/assets/img//manuscripts//lls//lls-book-rus-1//40.webp"
        );
      }
      return imgsWithHost_;
    }
  },
  methods: {
    inited (viewer) {
      this.$viewer = viewer
    },
    show () {
      this.$viewer.show()
    }
  }
};
</script>


<style lang="css" scoped>
@import "viewerjs/dist/viewer.css";
</style>


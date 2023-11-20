<template>
  <div style="width: 500px; height: 1000px">
    <viewer
      :options="{'inline': true}"
      :images="images"
      @inited="inited"
      class="viewer"
      ref="viewer"
    >
      <template #default="scope">
        <img
          v-for="src in scope.images"
          :src="src"
          :key="src"
          style="width: 500px; height: 1000px"
        >
        {{ scope.options }}
      </template>
    </viewer>
    <button type="button" @click="show">Show</button>
  </div>
</template>

<script>
import "viewerjs/dist/viewer.css";
import { component as Viewer } from "v-viewer";

export default {
  components: {
    Viewer
  },
  data() {
    return {
      images: [
        "https://w.forfun.com/fetch/39/399f74771a37da97630f86e85696f882.jpeg",
        "https://w.forfun.com/fetch/39/399f74771a37da97630f86e85696f882.jpeg",
        "https://w.forfun.com/fetch/39/399f74771a37da97630f86e85696f882.jpeg"
      ]
    };
  },
  methods: {
    inited(viewer) {
      this.$viewer = viewer;
    },
    show() {
      this.$viewer.show();
    }
  }
};
</script>
<template>
  <VueScrollUp
    tag="div"
    :scroll-duration="1000"
    :scroll-y="2250"
    custom-class="my-scroll-up scroll-animation"
  />

  <!--  <VueScrollUp-->
  <!--    v-slot="{ isTop }"-->
  <!--    tag="div"-->
  <!--    :scroll-duration="1000"-->
  <!--    :scroll-y="250"-->
  <!--    :always-show="true"-->
  <!--    custom-class="my-scroll-up demo-is-top "-->
  <!--  >-->
  <!--    {{ isTop ? "👇" : "👆" }}-->
  <!--  </VueScrollUp>-->

  <!--    <VueScrollUp-->
  <!--      v-slot="{ pointer }"-->
  <!--      tag="div"-->
  <!--      :scroll-duration="1000"-->
  <!--      :scroll-y="250"-->
  <!--      :always-show="true"-->
  <!--      custom-class="my-scroll-up demo-pointer"-->
  <!--    >-->
  <!--      {{ pointer }}-->
  <!--    </VueScrollUp>-->
</template>

<script>


import VueScrollUp from "vue-scroll-up";

export default {
  components: { VueScrollUp }
};
</script>


<style lang="css" scoped>

.my-scroll-up {
  align-items: center;
  background-color: rgba(0, 0, 0, 0.658);
  border: rgba(0, 0, 0, 0.658);
  border-radius: 100px;
  bottom: 100px;
  color: white;
  cursor: pointer;
  display: flex;
  height: 55px;
  justify-content: center;
  position: fixed;
  right: 10px;
  width: 55px;
  z-index: 99;
}

.my-scroll-up::after {
  border: 2px solid white;
  border-radius: 10px;
  content: '';
  display: block;
  height: 25px;
  margin: 0 auto;
  width: 10px;
}

.my-scroll-up::before {
  animation: 2s top infinite;
  border: 1px solid white;
  border-radius: 10px;
  content: '';
  display: block;
  height: 10px;
  left: 49%;
  position: absolute;
  width: 0;
}

.scroll-animation::after {
  content: '';
  height: 25px;
  width: 10px;
  display: block;
  margin: 0 auto;
  border: 2px solid white;
  border-radius: 10px;
}

.scroll-animation::before {
  content: '';
  display: block;
  height: 10px;
  width: 0;
  left: 49%;
  animation: 2s top infinite;
  border: 1px solid white;
  border-radius: 10px;
  position: absolute;
}

@keyframes top {
  0% {
    opacity: 0;
    transform: translateY(10px);
  }

  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

@media screen and (max-width: 450px) {
  .vue-scroll-up {
    bottom: 10px;
    transform: translateX(5px) scale(0.7);
  }
}

.demo-is-top {
  left: 25vw;
  top: 50vh;
}

.demo-pointer {
  left: 50vw;
  top: 50vh;
}

</style>





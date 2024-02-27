<template v-slot:append>
  <v-list>
    <v-list-item
      class="text-center"
    >
      <div
        class="ya-share2"
        data-color-scheme="whiteblack"
        data-curtain
        data-shape="round"
        data-services="vkontakte,odnoklassniki,telegram,viber,whatsapp"
      ></div>
      <p
        :style="{ 'font-size': 'smaller' }"
      >
        Поделиться в соц. сетях!
      </p>
    </v-list-item>
  </v-list>
</template>

<script>

export default {};

</script>

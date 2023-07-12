<template>
  <!--  <div>-->
  <!--    <div class="d-block d-sm-inline pa-2 bg-deep-purple">-->
  <!--      d-inline-->
  <!--    </div>-->
  <!--    <div class="d-block d-sm-inline pa-2 bg-black">-->
  <!--      d-inline-->
  <!--    </div>-->
  <!--  </div>-->
  <!--  <v-card-->
  <!--      class="pa-md-4 mx-lg-auto"-->
  <!--      color="secondary"-->
  <!--      width="250px"-->
  <!--  >-->
  <!--    <v-card-text>-->
  <!--      Adjust screen size to_cyrillic see spacing changes-->
  <!--    </v-card-text>-->
  <!--  </v-card>-->

  <v-btn-group>
    <v-btn
      @click="$router.push({ name: 'lls'})"
    >
      lls
    </v-btn>
    <v-btn
      @click="$router.push({ name: 'bible-books'})"
    >
      bible-books
    </v-btn>
    <v-btn
      @click="$router.push({ name: 'cathedrals'})"
    >
      cathedrals
    </v-btn>
  </v-btn-group>


</template>

<script>

export default {
  data: () => ({
    open: ["Users"],
    admins: [
      ["Management", "mdi-account-multiple-outline"],
      ["Settings", "mdi-cog-outline"]
    ],
    cruds: [
      ["Create", "mdi-plus-outline"],
      ["Read", "mdi-file-outline"],
      ["Update", "mdi-update"],
      ["Delete", "mdi-delete"]
    ]
  })
};
</script>

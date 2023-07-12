<template>
  <div>
    <h4 class="text-h4 font-weight-bold ma-2">
      Соборы, Правила Святых Отцов
    </h4>
    <v-divider></v-divider>
    <v-timeline side="end" align="start">
      <v-timeline-item
        v-for="cathedral in cathedrals"
        :key="cathedral.id"
        :dot-color="cathedralDotColor(cathedral)"
        size="small"
      >
        <template v-slot:opposite>
          <div v-if="cathedral.year"
               class="pt-1 headline font-weight-bold"
               v-text="cathedral.year.title"
          ></div>
        </template>
        <div class="d-flex">
          <div>
            <strong>{{ cathedral.title }}</strong>
            <div class="text-caption">
              (Кол. Правил
              <v-chip
                variant="tonal"
                color="blue"
              >
                {{ cathedral.num_rules }}
              </v-chip>
              )
            </div>
            <v-menu activator="parent" transition="scale-transition" location="end" open-on-hover>
              <v-sheet elevation="8" rounded="lg">
                <v-chip-group class="ma-1">
                  <v-chip
                    v-for="cathedral_book in cathedral.cathedral_books"
                    :key="cathedral_book.id"
                    :to="{ name: 'book', params: { bookId: cathedral_book.id } }"
                  > {{ cathedral_book.rule_num }}
                  </v-chip>
                </v-chip-group>
              </v-sheet>
            </v-menu>
          </div>
        </div>
      </v-timeline-item>
    </v-timeline>
    <v-divider></v-divider>
  </div>
</template>

<script>


import ChipYear from "@/components/year/ChipYear.vue";

export default {
  components: { ChipYear },
  props: {
    cathedrals: {
      type: Object,
      required: true
    }
  },
  methods: {
    cathedralDotColor(cathedral) {
      if (cathedral.slug?.startsWith("vselenskij_sobor")) {
        return "red-darken-3";
      }
      return "blue";
    }
  }
};
</script>

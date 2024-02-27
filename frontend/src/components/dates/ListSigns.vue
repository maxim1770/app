<template>
  <ChapterWithHead
    headTitle="Обозначения"
  >
    <v-card>
      <v-card-item>
        <v-list
          v-once
          density="compact"
        >
          <v-list-item>
            <template v-slot:prepend>
              <v-icon color="red-accent-4" icon="mdi-numeric-3-circle"></v-icon>
            </template>
            <ChipTipikon
              :tipikon='{title: "Великий Праздник", title_en: "Velikij_Prazdnik"}'
              class="ma-1"
            />
            <v-badge
              content="Воскресенье"
              color="red-lighten-1"
              class="ma-1"
            />
          </v-list-item>
          <v-list-item>
            <template v-slot:prepend>
              <v-icon class="bg-red rounded-xl" color="black" icon="mdi-numeric-3"></v-icon>
            </template>
            <ChipTipikon
              :tipikon='{title: "Средний Праздник (Всенощное Бдение)", title_en: "Srednij_Prazdnik_Vsenoschnoe_Bdenie"}'
              class="ma-1"
            />
            <ChipTipikon
              :tipikon='{title: "Средний Праздник", title_en: "Srednij_Prazdnik"}'
              class="ma-1"
            />
            <BadgeHolidayCategory
              :holiday_category='{title: "Предпразднство"}'
              class="ma-1"
            />
            <BadgeHolidayCategory
              :holiday_category='{title: "Попразднство"}'
            />
          </v-list-item>
          <v-list-item>
            <template v-slot:prepend>
              <v-icon color="red-accent-4" icon="mdi-circle-small"></v-icon>
            </template>
            <ChipTipikon
              :tipikon='{title: "Малый Праздник (Славословная Служба)", title_en: "Malyj_Prazdnik_Slavoslovnaja_Sluzhba"}'
              class="ma-1"
            />
            <ChipTipikon
              :tipikon='{title: "Малый Праздник", title_en: "Malyj_Prazdnik"}'
              class="ma-1"
            />
          </v-list-item>
          <v-list-item>
            <template v-slot:prepend>
              <v-icon color="red" icon="mdi-numeric-3-circle-outline"></v-icon>
            </template>
            <BadgeHolidayCategory
              :holiday_category='{title: "Отдание Праздника"}'
            />
          </v-list-item>
          <v-list-item>
            <template v-slot:prepend>
              <v-icon class="bg-light-blue-accent-4 rounded-xl" color="black" icon="mdi-numeric-3"></v-icon>
            </template>
            <BadgePost
              :post='{title: "Рождественский Пост"}'
            />
            <BadgePost
              :post='{title: "Петров Пост"}'
            />
            <BadgePost
              :post='{title: "Успенский Пост"}'
            />
            <BadgePost
              :post='{title: "Пост в Среду или Пятницу"}'
            />
          </v-list-item>
          <v-list-item>
            <template v-slot:prepend>
              <v-icon class="bg-purple-lighten-2 rounded-xl" color="black" icon="mdi-numeric-3"></v-icon>
            </template>
            <BadgePost
              :post='{title: "Великий Пост"}'
            />
          </v-list-item>
          <v-list-item>
            <template v-slot:prepend>
              <v-icon class="bg-indigo-darken-1 rounded-xl" color="black" icon="mdi-numeric-3"></v-icon>
            </template>
            <BadgePost
              :post='{title: "Страстная Седмица"}'
            />
          </v-list-item>
          <v-list-item>
            <template v-slot:prepend>
              <v-icon class="bg-yellow-darken-1 rounded-xl" color="black" icon="mdi-numeric-3"></v-icon>
            </template>
            <ChipSolidWeek :is_solid_week="true" />
          </v-list-item>
        </v-list>
      </v-card-item>
    </v-card>
  </ChapterWithHead>
</template>

<script>


import ChipTipikon from "@/components/holiday/tipikon/ChipTipikon.vue";
import BadgeHolidayCategory from "@/components/holiday/holiday_category_title/BadgeHolidayCategory.vue";
import BadgePost from "@/components/post/BadgePost.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import ChipSolidWeek from "@/components/date/ChipSolidWeek.vue";

export default {
  components: { ChipSolidWeek, ChapterWithHead, BadgePost, BadgeHolidayCategory, ChipTipikon }
};

</script>




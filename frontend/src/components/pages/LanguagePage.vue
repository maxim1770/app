<template>
  <div
    v-once
  >
    <ImgMainTitle mainPageValue="language" />
    <div>
      <v-divider />
      <MainTitle title="Учебники, пособия" textColor="red-darken-4" :hasDivider="true" />
      <TimelineLanguage :materials="books" timelineItemIcon="mdi-text-box" />
      <v-divider />
      <MainTitle title="Видеообучения" textColor="red-darken-4" :hasDivider="true" />
      <TimelineLanguage :materials="videos" timelineItemIcon="mdi-video" />
      <v-divider />
      <MainTitle title="Словари" textColor="red-darken-4" :hasDivider="true" />
      <TimelineLanguage :materials="dictionaries" timelineItemIcon="mdi-alphabet-cyrillic" />
      <v-divider />
      <MainTitle title="Числа" textColor="red-darken-4" :hasDivider="true" />
      <TimelineLanguage :materials="numbers" timelineItemIcon="mdi-numeric" />
      <v-divider />
      <MainTitle title="Слова под титлами" textColor="red-darken-4" :hasDivider="true" />
      <TimelineLanguage :materials="words_under_titles" timelineItemIcon="mdi-format-title" />
      <v-divider />
    </div>
  </div>

</template>

<script>


import ImgMainTitle from "@/components/common/ImgMainTitle.vue";
import TimelineLanguage from "@/components/book/timeline/TimelineLanguage.vue";
import MainTitle from "@/components/common/title/MainTitle.vue";

export default {
  components: { MainTitle, TimelineLanguage, ImgMainTitle },
  computed: {
    dictionaries() {
      return [
        {
          "title": "Словарь древнерусского языка И.И.Срезневского",
          "link": "//oldrusdict.ru/dict.html",
          "highlight": true
        },
        {
          "title": "Древнеславянский on-line словарь",
          "link": "//drevlit.ru/drevslav_slovar.html"
        },
        {
          "title": "Церковно-славянский словарь, содержит около 9500 слов и выражений",
          "link": "//drevlit.ru/slovar_cerkov.html"
        },
        {
          "title": "Словарь древнерусского языка (XI-XIV вв.)",
          "link": "//rus-old-russian-dict.slovaronline.com"
        }
      ];
    },
    books() {
      return [
        {
          "title": "Учебник по древнерусскому",
          "link": "//олдп.рус/uchebnik",
          "highlight": true
        },
        {
          "title": "Грамматика церковнославянского языка",
          "link": "//www.ponomar.net/files/gama2/toc.html#p004?utm_source=yafavorites"
        },
        {
          "title": "Буква в духе. Церковнославянская грамота",
          "link": "//paerok.ru/gramota"
        }
      ];
    },
    videos() {
      return [
        {
          "title": "Евангелие от Матфея на древнерусском",
          "link": "//youtube.com/playlist?list=PLopvhxoMSfbzT9SXfwS0ZnUWuyBIx6-y-&si=nC-oADgoXNYoXS54",
          "highlight": true
        },
        {
          "title": "Библейская история, Септуагинта на древнерусском",
          "link": "//youtube.com/playlist?list=PLopvhxoMSfbzHHCP4fEgcnPOOJU8DD4Ch&si=21Wdz6ps_xMupmaV"
        },
        {
          "title": "Апостол на древнерусском",
          "link": "//youtube.com/playlist?list=PLopvhxoMSfbwXATgpE_-0glGuMHSyw7Jb&si=7gy2LOKo_zEb1bkZ"
        },
        {
          "title": "Уроки древнерусского языка",
          "link": "//youtube.com/playlist?list=PLXggOC5piOfxUUit4jDRqhMUQ_QbS2bJD&si=6ATrxKQA9fzF33rP"
        },
        {
          "title": "Как пользоваться словарём Срезневского",
          "link": "//youtu.be/yVIuGQog9_c?si=_Hj8mBz5vxyukx5b",
          "highlight": true
        }
      ];
    },
    numbers() {
      return [
        {
          "title": "Тренажеры для запоминания древнерусских чисел и слов",
          "link": "//dobroazbyka.ru/clock",
          "highlight": true
        },
        {
          "title": "Конвертер древнерусских чисел",
          "link": "//azbyka.ru/converter",
          "highlight": true
        },
        {
          "title": "Числа",
          "link": "//optim.tildacdn.com/tild6437-3163-4234-a164-303963656439/-/format/webp/noroot.jpg"
        }
      ];
    },
    words_under_titles() {
      return [
        {
          "title": "Словарь церковнославянских слов под титлами",
          "link": "//azbyka.ru/otechnik/Spravochniki/slovar-tserkovnoslavjanskih-slov-pod-titlami",
          "highlight": true
        },
        {
          "title": "Надстрочные знаки",
          "link": "//www.ponomar.net/files/gama2/p003.htm?utm_source=yafavorites"
        }
      ];
    }
  }
};
</script>

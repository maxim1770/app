import { OBJECT_STORAGE_BASE_URL } from "@/env";

function imgUrl(imgPath) {
  return `${OBJECT_STORAGE_BASE_URL}/${imgPath}`;
}

function scroll(someFun) {
  window.onscroll = () => {
    let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;
    if (bottomOfWindow) {
      someFun();
    }
  };
}

function replaceRouterQuery(queries) {
  this.$router.replace({
    query: { ...this.$route.query, ...queries }
  });
}

function computeCustomIcon(title_en) {
  return `custom:${title_en.replace(/_/g, "")}`;
}


function numObjectKeys(object) {
  return Object.keys(object ? object : {}).length;
}

function toUrl(url) {
  window.location.href = url;
}


function isVselenskijSobor(cathedral) {
  return cathedral?.slug?.startsWith("vselenskij_sobor");
}


const MONTH_TITLE = {
  9: "Сентябрь",
  10: "Октябрь",
  11: "Ноябрь",
  12: "Декабрь",
  1: "Январь",
  2: "Февраль",
  3: "Март",
  4: "Апрель",
  5: "Май",
  6: "Июнь",
  7: "Июль",
  8: "Август"
};

const mainPages = [{
  title: "Календарь",
  value: "dates",
  prependIcon: "mdi-calendar-range-outline",
  img: "img/manuscripts/rsl/f_173i/f-173i-11/196.webp"
}, {
  title: "Библия",
  value: "bible-books",
  prependIcon: "mdi-notebook-heart-outline",
  img: "img/manuscripts/lls/lls-book-1/31.webp"
}, {
  title: "Соборы, Правила Святых Отцов",
  value: "cathedrals",
  prependIcon: "mdi-menorah-fire",
  img: "img/manuscripts/lls/lls-book-8/565.webp"
}, {
  title: "Лицевой Летописный Свод",
  value: "lls",
  prependIcon: "mdi-book-open-variant",
  img: "img/manuscripts/lls/lls-book-rus-11/4.webp"
}, {
  title: "Чтения по времени",
  value: "movable-dates",
  prependIcon: "mdi-clipboard-text-clock-outline",
  img: "img/manuscripts/rsl/f_178i/f-178i-9500/607.webp"
}, {
  title: "Книги",
  value: "books",
  prependIcon: "mdi-book-open-page-variant",
  img: "img/manuscripts/rsl/f_98/f-98-80/15.webp"
}, {
  title: "Рукописи", value: "manuscripts", prependIcon: "mdi-bookshelf", img: "img/manuscripts/lls/lls-book-1/1.webp"
}, {
  title: "Праздники",
  value: "holidays",
  prependIcon: "mdi-candelabra-fire",
  img: "img/manuscripts/rsl/f_98/f-98-80/831.webp"
}, {
  title: "Святые", value: "saints", prependIcon: "mdi-account-group", img: "img/manuscripts/lls/lls-book-10/5.webp"
}];

export {
  imgUrl, scroll, MONTH_TITLE, mainPages, replaceRouterQuery, computeCustomIcon, toUrl, numObjectKeys, isVselenskijSobor
};

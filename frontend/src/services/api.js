import axios from "axios";
import { API_BASE_URL } from "@/env";

const instance = axios.create({
  baseURL: API_BASE_URL
});

instance.interceptors.request.use(config => {
  NProgress.start();
  return config;
});

instance.interceptors.response.use(response => {
  NProgress.done();
  return response;
});


export const api = {
  async getMainData() {
    return instance.get("/");
  }, async getDates({ year } = {}) {
    return instance.get(`/dates/`, {
      params: {
        "year": year
      }
    });
  }, async getDate(dateSlug) {
    return instance.get(`/dates/${dateSlug}`);
  }, async getMovableDates() {
    return instance.get(`/movable-dates/`);
  }, async getHolidays({ page, search, tipikon__title, holiday_category__title, day__month, day__day } = {}) {
    return instance.get(`/holidays/`, {
      params: {
        "search": search,
        "tipikon__title": tipikon__title,
        "holiday_category__title": holiday_category__title,
        "day__month": day__month,
        "day__day": day__day,
        "page": page,
        "size": 15
      }
    });
  }, async getHolidaysSearchData() {
    return instance.get(`/holidays/search-data/`);
  }, async getHoliday(holidaySlug) {
    return instance.get(`/holidays/${holidaySlug}`);
  }, async putHoliday({ holidaySlug, tipikon__title } = {}) {
    return instance.put(`/holidays/${holidaySlug}`, { "tipikon__title": tipikon__title });
  }, async getSaints({ page, search, face_sanctity__title, dignity__title, order_by } = {}) {
    return instance.get(`/saints/`, {
      params: {
        "search": search,
        "face_sanctity__title": face_sanctity__title,
        "dignity__title": dignity__title,
        "order_by": order_by,
        "page": page,
        "size": 15
      }
    });
  }, async getSaintsSearchData() {
    return instance.get(`/saints/search-data/`);
  }, async getSaint(saintSlug) {
    return instance.get(`/saints/${saintSlug}`);
  }, async getManuscripts({ page, search, fund__title, fund__library, y__year__gte, y__year__lt } = {}) {
    return instance.get(`/manuscripts/`, {
      params: {
        "search": search,
        "fund__title": fund__title,
        "fund__library": fund__library,
        "y__year__gte": y__year__gte,
        "y__year__lt": y__year__lt,
        "page": page,
        "size": 6
      }
    });
  }, async getManuscriptsSearchData() {
    return instance.get(`/manuscripts/search-data/`);
  }, async getManuscript(manuscriptCode) {
    return instance.get(`/manuscripts/${manuscriptCode}`);
  }, async putManuscript({ manuscriptCode, preview_page_in } = {}) {
    return instance.put(`/manuscripts/${manuscriptCode}`, { "preview_page_in": preview_page_in });
  }, async getLls() {
    return instance.get(`/manuscripts/lls/`);
  }, async getBooks({ page, type, topic_book__source, topics__title__in } = {}) {
    return instance.get(`/books/`, {
      params: {
        "type": type,
        "topic_book__source": topic_book__source,
        "topics__title__in": topics__title__in,
        "page": page,
        "size": 6
      }
    });
  }, async getBooksSearchData() {
    return instance.get(`/books/search-data/`);
  }, async getBook(bookId) {
    return instance.get(`/books/${bookId}`);
  }, async getRandomBookId({ some_book_slug } = {}) {
    return instance.get(`/books/random_id/`, {
      params: {
        "some_book_slug": some_book_slug
      }
    });
  }, async putBookmarkPages({ bookId, manuscriptCode, pages_in } = {}) {
    return instance.put(`/books/${bookId}/bookmarks/${manuscriptCode}`, pages_in);
  }, async getCathedrals() {
    return instance.get(`/books/cathedrals/`);
  }, async getCathedral(cathedralSlug) {
    return instance.get(`/books/cathedrals/${cathedralSlug}`);
  }, async getBibleBooks() {
    return instance.get(`/books/bible-books/`);
  }, async getBibleBook(bibleBookAbbr) {
    return instance.get(`/books/bible-books/${bibleBookAbbr}`);
  }, async getIcon(iconId) {
    return instance.get(`/icons/${iconId}`);
  }
};

import axios from "axios";
import { apiUrl } from "@/env";

const instance = axios.create({
  baseURL: apiUrl
});

axios.interceptors.request.use(config => {
  NProgress.start();
  return config;
});

axios.interceptors.response.use(response => {
  NProgress.done();
  return response;
});


export const api = {
  async getAsset(assetPath) {
    return instance.get(`/assets/${assetPath}`);
  }, async getMainConstData() {
    return instance.get("/");
  }, async getDates() {
    return instance.get(`/dates/?limit=2`);
  }, async getDate(date) {
    return instance.get(`/dates/${date}`);
  }, async getMovableDates() {
    return instance.get(`/movable-dates/`);
  }, async getHolidays() {
    return instance.get(`/holidays/`);
  }, async getHoliday(holidaySlug) {
    return instance.get(`/holidays/${holidaySlug}`);
  }, async getSaints({ search, face_sanctity__title, dignity__title, order_by } = {}) {
    return instance.get(`/saints/`, {
      params: {
        "search": search,
        "face_sanctity__title": face_sanctity__title,
        "dignity__title": dignity__title,
        "order_by": order_by
      }
    });
  }, async getSaint(saintSlug) {
    return instance.get(`/saints/${saintSlug}`);
  }, async getManuscripts({ search, fund__title, year__year__gte, year__year__lt, order_by } = {}) {
    return instance.get(`/manuscripts/`, {
      params: {
        "search": search,
        "fund__title": fund__title,
        "year__year__gte": year__year__gte,
        "year__year__lt": year__year__lt,
        "order_by": order_by
      }
    });
  }, async getBooks() {
    return instance.get(`/books/`);
  }, async getBook(bookId) {
    return instance.get(`/books/${bookId}`);
  }, async getManuscript(manuscriptCode) {
    return instance.get(`/manuscripts/${manuscriptCode}`);
  }
};

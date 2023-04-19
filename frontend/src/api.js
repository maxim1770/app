import axios from "axios";
import {apiUrl} from "@/env";

export const api = {
  async getDates() {
    return axios.get(`${apiUrl}/dates/?limit=2`);
  }, async getDate(date) {
    return axios.get(`${apiUrl}/dates/${date}`);
  }, async getCycle(cycleNum) {
    return axios.get(`${apiUrl}/movable-dates/cycle-${cycleNum}`);
  }, async getHolidays() {
    return axios.get(`${apiUrl}/holidays/`);
  }, async getHoliday(holidaySlug) {
    return axios.get(`${apiUrl}/holidays/${holidaySlug}`);
  }, async getSaint(saintSlug) {
    return axios.get(`${apiUrl}/saints/${saintSlug}`);
  }, async getManuscripts({search, fund__title, year__year__gte, year__year__lt, order_by} = {}) {
    return axios.get(`${apiUrl}/manuscripts/`, {
      params: {
        'search': search,
        'fund__title': fund__title,
        'year__year__gte': year__year__gte,
        'year__year__lt': year__year__lt,
        'order_by': order_by
      }
    });
  }, async getFile(filePath) {
    return axios.get(`${apiUrl}/files/${filePath}`);
  },
};

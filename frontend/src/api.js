import axios from "axios";
import {apiUrl} from "@/env";

export const api = {
  async getDates() {
    return axios.get(`${apiUrl}/dates/?limit=2`);
  },
  async getDate(date) {
    return axios.get(`${apiUrl}/dates/${date}`);
  },
  async getHolidays() {
    return axios.get(`${apiUrl}/holidays`);
  },
  async getHoliday(holidaySlug) {
    return axios.get(`${apiUrl}/holidays/${holidaySlug}`);
  },
  async getSaint(saintSlug) {
    return axios.get(`${apiUrl}/saints/${saintSlug}`);
  },
  async getFile(filePath) {
    return axios.get(`${apiUrl}/files/${filePath}`);
  },
};

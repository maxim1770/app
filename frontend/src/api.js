import axios from "axios";
import {apiUrl} from "@/env";

export const api = {
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
};

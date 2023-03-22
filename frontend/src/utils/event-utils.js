import {api} from "@/api";


function test_() {
  return api
    .getDates()
    .then((response) => {
      return response.data;
    });
}

test_().then(main);

function main(dates) {
  let INITIAL_EVENTS = [];
  let i, j;
  for (i = dates?.length - 1; i >= 0; --i) {
    for (j = dates[i].day.holidays?.length - 1; j >= 0; --j) {
      let date = new Date(dates[i].day?.month_day);
      date.setFullYear(date.getFullYear() - 9);
      const event = {
        id: dates[i].day.holidays[j]?.slug,
        title: dates[i].day.holidays[j]?.title,
        start: date.toISOString().split('T')[0]
      }
      INITIAL_EVENTS.push(event);
    }
  }
  return INITIAL_EVENTS;
}


export const INITIAL_EVENTS = main()


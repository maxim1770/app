import { numObjectKeys } from "@/utils/common";

const GREAT_HOLIDAYS = ["Праздники Христовы", "Праздники Богородичны", "Праздники Предтечевы"];


function isGreatHoliday(holidayCategoryTitle) {
  return GREAT_HOLIDAYS.includes(holidayCategoryTitle);
}

function __prepareBeforeAfterHoliday(date) {
  let before_after_holiday = null;
  if (date?.day?.before_after_holidays?.[0]?.before_after_holiday) {
    before_after_holiday = date?.day?.before_after_holidays[0].before_after_holiday;
  } else if (date?.movable_day?.before_after_holidays?.[0]?.before_after_holiday) {
    before_after_holiday = date?.movable_day?.before_after_holidays[0].before_after_holiday;
  }
  return before_after_holiday;
}


function _joinAllHolidays(date) {
  let allHolidays = [];
  const __before_after_holiday = __prepareBeforeAfterHoliday(date);
  if (__before_after_holiday) {
    allHolidays.push(__before_after_holiday?.holiday);
  }
  if (date?.day?.holidays) {
    allHolidays = allHolidays.concat(date.day.holidays);
  }
  if (date?.movable_day?.holidays) {
    allHolidays = allHolidays.concat(date.movable_day.holidays);
  }
  return allHolidays;
}

function sortHolidays(holidays) {
  return Object.assign([], holidays).sort(function(holiday_1, holiday_2) {
    if (holiday_2.tipikon) {
      if (holiday_1.tipikon) {
        return holiday_1.tipikon.priority < holiday_2.tipikon?.priority ? -1 : 1;
      } else {
        return 1;
      }
    } else {
      if (holiday_1.tipikon) {
        return -1;
      } else {
        return numObjectKeys(holiday_1.molitva_books_by_manuscript) > numObjectKeys(holiday_2.molitva_books_by_manuscript) || holiday_1?.holiday_books?.length > holiday_2?.holiday_books?.length ? -1 : 1;
      }
    }
  });
}


function prepareDateAllSortedHolidays(date) {
  return sortHolidays(_joinAllHolidays(date));
}


function prepareAllHolidaysBooks(holidays) {
  let allHolidaysBooks = [];
  for (let holiday of holidays) {
    if (holiday.holiday_books?.length) {
      for (let holiday_book of holiday.holiday_books) {
        holiday_book.holiday = holiday;
      }
      allHolidaysBooks = allHolidaysBooks.concat(holiday.holiday_books);
    }
  }
  return allHolidaysBooks;
}


function prepareAllIcons(holidays) {
  let allIcons = [];
  for (let holiday of holidays) {
    if (holiday.icons?.length) {
      allIcons = allIcons.concat(holiday.icons);
    }
  }
  return allIcons;
}


function choiceHolidayColor(holiday) {
  switch (holiday?.tipikon?.title_en) {
    case "Velikij_Prazdnik":
      return "red-darken-4";
    case "Srednij_Prazdnik_Vsenoschnoe_Bdenie":
    case "Srednij_Prazdnik":
      return "red-darken-2";
    case "Malyj_Prazdnik_Slavoslovnaja_Sluzhba":
    case "Malyj_Prazdnik":
      return "red-darken-1";
    default:
      return "black";
  }
}

function choiceHolidayTextColor(holiday) {
  return `text-${choiceHolidayColor(holiday)}`;
}


export {
  isGreatHoliday,
  prepareDateAllSortedHolidays,
  prepareAllHolidaysBooks,
  prepareAllIcons,
  choiceHolidayColor,
  choiceHolidayTextColor,
  sortHolidays
};
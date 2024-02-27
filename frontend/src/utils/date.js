function preDateSlug(dateSlug) {
  let _preDate = new Date(dateSlug);
  if ((getMonth(_preDate) === 9) && (_preDate.getDay() === 1)) {
    _preDate.setFullYear(_preDate.getFullYear() - 1);
  }
  _preDate.setDate(_preDate.getDate() - 1);
  return date2dateSlug(_preDate);
}

function nextDateSlug(dateSlug) {
  let _nextDate = new Date(dateSlug);
  if ((getMonth(_nextDate) === 8) && (_nextDate.getDay() === 31)) {
    _nextDate.setFullYear(_nextDate.getFullYear() + 1);
  }
  _nextDate.setDate(_nextDate.getDate() + 1);
  return date2dateSlug(_nextDate);
}

function date2dateSlug(dateObject) {
  return dateObject.toISOString().split("T")[0];
}

function getMonth(dateObject) {
  return dateObject.getMonth() + 1;
}

function year2offsetYear(year, month) {
  let offsetYear = year - 8;
  if ((9 <= month) && (month <= 12)) {
    offsetYear -= 1;
  }
  return offsetYear;
}

function offsetYear2year(offsetYear, month) {
  let year = offsetYear + 8;
  if ((9 <= month) && (month <= 12)) {
    year += 1;
  }
  return year;
}


function isSunDate(date) {
  return date?.movable_day?.abbr === "sun";
}

const YEAR_CHRISTMAS = 5500;

const CALENDAR_MASKS = {
  title: "MMMM",
  weekdays: "W",
  navMonths: "MMM",
  hours: "h A",
  input: ["L", "MM-DD", "MM/DD"],
  inputDateTime: ["L h:mm A", "MM-DD h:mm A", "MM/DD h:mm A"],
  inputDateTime24hr: ["L HH:mm", "MM-DD HH:mm", "MM/DD HH:mm"],
  inputTime: ["h:mm A"],
  inputTime24hr: ["HH:mm"],
  dayPopover: "WWW, MMM D",
  data: ["L", "MM-DD", "MM/DD"],
  model: "iso",
  iso: "MM-DDTHH:mm:ss.SSSZ"
};


export {
  preDateSlug,
  nextDateSlug,
  date2dateSlug,
  offsetYear2year,
  year2offsetYear,
  isSunDate,
  YEAR_CHRISTMAS,
  getMonth,
  CALENDAR_MASKS
};

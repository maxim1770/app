function preDate(dateStr) {
  let _preDate = new Date(dateStr);
  _preDate.setDate(_preDate.getDate() - 1);
  return date2str(_preDate);
}

function nextDate(dateStr) {
  let _nextDate = new Date(dateStr);
  _nextDate.setDate(_nextDate.getDate() + 1);
  return date2str(_nextDate);
}

function date2str(dateObject) {
  return dateObject.toISOString().split("T")[0];
}

export { preDate, nextDate, date2str};

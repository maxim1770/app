function preDate(dateStr) {
  let _preDate = new Date(dateStr);
  if ((_preDate.getMonth() === 9) && (_preDate.getDay() === 1)) {
    _preDate.setFullYear(_preDate.getFullYear() - 1);
  }
  _preDate.setDate(_preDate.getDate() - 1);
  return date2str(_preDate);
}

function nextDate(dateStr) {
  let _nextDate = new Date(dateStr);
  if ((_nextDate.getMonth() === 8) && (_nextDate.getDay() === 31)) {
    _nextDate.setFullYear(_nextDate.getFullYear() + 1);
  }
  _nextDate.setDate(_nextDate.getDate() + 1);
  return date2str(_nextDate);
}

function date2str(dateObject) {
  return dateObject.toISOString().split("T")[0];
}

export { preDate, nextDate, date2str };

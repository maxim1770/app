const GREAT_HOLIDAYS = ["Праздники Христовы", "Праздники Богородичны", "Праздники Предтечевы"];


function isGreatHoliday(holidayCategoryTitle) {
  return GREAT_HOLIDAYS.includes(holidayCategoryTitle);
}

export { isGreatHoliday };
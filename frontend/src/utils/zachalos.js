function chooseEvangelAndApostleZachalos(zachalos) {
  return [zachalos.find(zachalo => ["mt", "mk", "lk", "jn"].includes(zachalo.bible_book.abbr)), zachalos.find(zachalo => !["mt", "mk", "lk", "jn"].includes(zachalo.bible_book.abbr))];
}


export {
  chooseEvangelAndApostleZachalos
};

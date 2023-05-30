from pydantic import BaseModel

from .bible_book import BibleBook, BibleBookCreate, BibleBookNewTestamentCreate, BibleBookEvangelCreate, \
    BibleBookApostleCreate
from .bible_book import Zachalo, ZachaloCreate, ZachaloInDB
from .book import BookDataType, BookDataGetType, Book, BookCreate, BookUpdate, BookDataCreate, HolidayBookDataCreate, \
    MolitvaBookDataCreate, MovableDateBookDataCreate, TopicBookDataCreate, ZachaloBookDataGet, BookInDB, \
    BookInDBToManuscript, BookInDBToAuthor
from .book import HolidayBook, HolidayBookCreate, HolidayBookInDB
from .book import MolitvaBook, MolitvaBook, MolitvaBookCreate, MolitvaBookInDB
from .book import MovableDateBook, MovableDateBookCreate, MovableDateBookInDB
from .book import TopicBook, TopicBookCreate, TopicBookInDB
from .city import City, CityCreate
from .date import Date, DateCreate, DateUpdate
from .day import Day, DayCreate, DayInDB
from .holiday import Holiday, HolidayCreate, HolidayUpdate, HolidayDataCreate, HolidayInDB, HolidayInDBToDay, \
    HolidayInDBToSaint
from .holiday import HolidayCategory, HolidayCategoryCreate
from .holiday import MovableSaintHolidayCreateWithoutData
from .holiday import SaintHolidayCreate, SaintHolidayCreateWithoutYear, MovableSaintHolidayCreate
from .holiday import SaintsHolidayCreate
from .icon import Icon, IconCreate, IconUpdate, IconDataCreate, IconDataUpdate
from .manuscript import Bookmark, BookmarkInDB
from .manuscript import Fund, FundCreate
from .manuscript import Manuscript, ManuscriptWithNear, ManuscriptCreateAny, ManuscriptCreate, \
    ManuscriptUpdate
from .manuscript import ManuscriptDataCreateAny, ManuscriptDataCreate, ManuscriptDataUpdate
from .manuscript import NotNumberedPages, NotNumberedPage
from .manuscript import Page, PagesCreate, PageCreate
from .movable_date import Cycle, CycleCreate
from .movable_date import DivineService, DivineServiceCreate
from .movable_date import MovableDate, MovableDateCreate
from .movable_date import MovableDay, MovableDayCreate, MovableDayGet, MovableDayInDB, MovableDayInDBForWeek
from .movable_date import Week, WeekCreate, WeekInDB
from .saint import Dignity, DignityCreate
from .saint import FaceSanctity, FaceSanctityCreate
from .saint import Saints, Saint, SaintCreate, SaintUpdate, SaintDataCreate, SaintDataUpdate, SaintInDB, \
    SaintInDBToHoliday
from .year import Year, YearCreate

MovableDate.update_forward_refs(MovableDayInDB=MovableDayInDB)
WeekInDB.update_forward_refs(MovableDayInDBForWeek=MovableDayInDBForWeek)
Cycle.update_forward_refs(WeekInDB=WeekInDB)

Saint.update_forward_refs(BookInDBToAuthor=BookInDBToAuthor, HolidayInDBToSaint=HolidayInDBToSaint)
SaintInDB.update_forward_refs(HolidayInDBToSaint=HolidayInDBToSaint)

Holiday.update_forward_refs(DayInDB=DayInDB, MovableDayInDB=MovableDayInDB)
HolidayInDBToSaint.update_forward_refs(DayInDB=DayInDB)
HolidayInDB.update_forward_refs(DayInDB=DayInDB)
MovableSaintHolidayCreate.update_forward_refs(MovableDayGet=MovableDayGet)
MovableSaintHolidayCreateWithoutData.update_forward_refs(MovableDayGet=MovableDayGet)
HolidayDataCreate.update_forward_refs(DayCreate=DayCreate)
SaintHolidayCreate.update_forward_refs(DayCreate=DayCreate)
SaintHolidayCreateWithoutYear.update_forward_refs(DayCreate=DayCreate)
SaintsHolidayCreate.update_forward_refs(DayCreate=DayCreate)

__book_refs: list[[BaseModel]] = [TopicBookInDB, HolidayBookInDB, MolitvaBookInDB, MovableDateBookInDB, ZachaloInDB]
__book_refs_kwargs: dict[str, [BaseModel]] = {
    str(book_ref).split('.')[-1].replace("'>", ''): book_ref for book_ref in __book_refs
}
BookInDBToManuscript.update_forward_refs(**__book_refs_kwargs)
BookInDBToAuthor.update_forward_refs(**__book_refs_kwargs)
Book.update_forward_refs(**__book_refs_kwargs)
TopicBookDataCreate.update_forward_refs(TopicBookCreate=TopicBookCreate)
HolidayBookDataCreate.update_forward_refs(HolidayBookCreate=HolidayBookCreate)
MolitvaBookDataCreate.update_forward_refs(MolitvaBookCreate=MolitvaBookCreate)
MovableDateBookDataCreate.update_forward_refs(MovableDayGet=MovableDayGet, MovableDateBookCreate=MovableDateBookCreate)
ZachaloBookDataGet.update_forward_refs(ZachaloCreate=ZachaloCreate)

BookmarkInDB.update_forward_refs(BookInDBToManuscript=BookInDBToManuscript)

Manuscript.update_forward_refs(BookmarkInDB=BookmarkInDB)

HolidayBook.update_forward_refs(HolidayInDB=HolidayInDB)
HolidayBookInDB.update_forward_refs(HolidayInDB=HolidayInDB)

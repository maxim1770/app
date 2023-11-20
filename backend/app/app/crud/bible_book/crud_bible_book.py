from app.filters import BibleBookFilter
from app.models import BibleBook
from app.schemas import BibleBookCreate, BibleBookUpdate
from ..base import CRUDBase


class CRUDBibleBook(CRUDBase[BibleBook, BibleBookCreate, BibleBookUpdate, BibleBookFilter]):
    pass


bible_book = CRUDBibleBook(BibleBook)

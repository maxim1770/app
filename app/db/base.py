# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models import BibleBook  # noqa
from app.models import Book  # noqa
from app.models import Cycle  # noqa
from app.models import Date  # noqa
from app.models import Day  # noqa
from app.models import Dignity  # noqa
from app.models import DivineService  # noqa
from app.models import FaceSanctity  # noqa
from app.models import Holiday  # noqa
from app.models import HolidayCategory  # noqa
from app.models import MovableDate  # noqa
from app.models import MovableDay  # noqa
from app.models import Reading  # noqa
from app.models import Saint  # noqa
from app.models import SaintLive  # noqa
from app.models import Week  # noqa
from app.models import Year  # noqa
from app.models import Zachalo  # noqa
from app.models.saint.saint import SaintsHolidays  # noqa

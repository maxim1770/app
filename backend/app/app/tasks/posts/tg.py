import asyncio
from datetime import date as date_type
from pathlib import Path

from sqlalchemy.orm import Session
from telegram import Bot, InputMediaPhoto

from app import models, enums, crud, utils, schemas
from app.api import deps
from app.api.api_v1.endpoints.main import get_valid_current_date
from app.core.config import settings
from app.tasks.celery import celery


async def __send_random_book(db: Session) -> None:
    book_id = crud.book.get_random_book_id(db, some_book_slug=enums.SomeBookSlug.topic_book)
    book = crud.book.get(db, id=book_id)

    bookmark = book.bookmarks[0]
    __first_page_num, __end_page_num = utils.pages_in2pages_nums(
        bookmark.first_page,
        bookmark.end_page,
        not_numbered_pages=schemas.NotNumberedPages.model_validate(bookmark.manuscript.not_numbered_pages),
        has_left_and_right=utils.manuscript_has_left_and_right(
            bookmark.manuscript.neb_slug,
            manuscript_code=bookmark.manuscript.code
        ),
        first_page_position=bookmark.manuscript.first_page_position
    )
    manuscript_path: Path = utils.assemble_manuscript_path(manuscript=bookmark.manuscript)
    pages_paths: list[Path] = [
        manuscript_path / f'{page_num}.webp'
        for page_num in range(__first_page_num, __end_page_num + 1)
    ]
    bot = Bot(
        token=settings.TG_BOT_TOKEN
    )
    await bot.send_media_group(
        chat_id=settings.TG_CHANNEL_ID,
        media=[
            InputMediaPhoto(
                'http://storage.yandexcloud.net/pravoslavie16.ru/img/manuscripts/nlr/sof/50d07a48-b72e-4372-b020-ad5baf59f797/344.webp'),
            InputMediaPhoto(
                'http://storage.yandexcloud.net/pravoslavie16.ru/img/manuscripts/nlr/sof/50d07a48-b72e-4372-b020-ad5baf59f797/345.webp')
        ],
        caption=f'{book.type} {book.topic_book.source}',
        # parse_mode='MarkdownV2'
    )


async def __send_message(db: Session) -> None:
    date: models.Date = get_valid_current_date(db=db)
    bot = Bot(
        token=settings.TG_BOT_TOKEN
    )
    __date_slug = str(date_type(date.year, date.day.month, date.day.day))
    text = f"""
    <a :href=http://localhost:5173/dates/{__date_slug}>Читать подробнее на сайте...</a>
    <p>{date.day.holidays[0].title}</p>
    """
    await bot.send_photo(
        chat_id=settings.TG_CHANNEL_ID,
        photo='https://storage.yandexcloud.net/pravoslavie16.ru/img/manuscripts/lls/lls-book-1/31.webp',
        caption="""
             *bold \*text*   
            _italic \*text_
            __underline__
            ~strikethrough~
            ||spoiler||
            *bold _italic bold ~italic bold strikethrough ||italic bold strikethrough spoiler||~ __underline italic bold___ bold*
            [inline URL](http://www.example.com/)
            [inline mention of a user](tg://user?id=123456789)
            ![👍](tg://emoji?id=5368324170671202286)
            `inline fixed-width code`
            ```
            pre-formatted fixed-width code block
            ```
            ```python
            pre-formatted fixed-width code block written in the Python programming language
            ```
        """,
        parse_mode='MarkdownV2'
    )


@celery.task
def post_to_tg() -> None:
    db: Session = next(deps.get_db())
    asyncio.run(__send_message(db))


if __name__ == '__main__':
    db: Session = next(deps.get_db())
    asyncio.run(__send_random_book(db))
    # asyncio.run(__send_message(db))
    # asyncio.run(get_main_data(db=db))

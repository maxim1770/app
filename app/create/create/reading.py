from typing import Final

from sqlalchemy.orm import Session

from app import schemas, crud


def create_readings(
        db: Session,
        cycle_num: schemas.CycleEnum,
        sundays_nums: list[int],
        days_abbrs: list[schemas.DayAbbrEnum],
        # sundays_matins: list[int | None],
        bible_books_abbrs: list[schemas.AbbrEnum],
        zachalos_nums: list[int],
        number_readings: Final[int]
) -> bool:
    num_creatures: int = 0

    for i, sunday_num in enumerate(sundays_nums):
        i_14: int = i * 7 * 2

        print(f'Неделя {sunday_num}')

        for j in (i_14, i_14 + 1):
            if crud.get_reading(  # Создание вс Литургии
                    db,
                    cycle_num=cycle_num,
                    sunday_num=sunday_num,
                    day_abbr=schemas.DayAbbrEnum.sun,
                    divine_service_title=schemas.DivineServiceEnum.liturgy,
                    bible_book_abbr=bible_books_abbrs[j],
                    zachalo_num=zachalos_nums[j]
            ):
                raise ValueError(f"""
                    Reading: cycle_num={cycle_num}, sunday_num={sunday_num}, day_abbr={schemas.DayAbbrEnum.sun}, 
                    divine_service_title={schemas.DivineServiceEnum.liturgy}, 
                    bible_book_abbr={bible_books_abbrs[j]}, zachalo_num={zachalos_nums[j]} уже была создана"""
                                 )

            crud.create_reading(
                db,
                cycle_num=cycle_num,
                sunday_num=sunday_num,
                day_abbr=schemas.DayAbbrEnum.sun,
                divine_service_title=schemas.DivineServiceEnum.liturgy,
                bible_book_abbr=bible_books_abbrs[j],
                zachalo_num=zachalos_nums[j]
            )
            num_creatures += 1

            if j % 2 == 0:
                print(f'{schemas.DayAbbrEnum.sun} | {bible_books_abbrs[j]} - {zachalos_nums[j]}')

        # Создание пн, вт, ср, чт, пт, сб - Литургии
        for d, day_abbr in enumerate(days_abbrs[i * 6: (i + 1) * 6]):

            for j in (i_14 + d * 2 + 2, i_14 + d * 2 + 2 + 1):
                if crud.get_reading(
                        db,
                        cycle_num=cycle_num,
                        sunday_num=sunday_num,
                        day_abbr=day_abbr,
                        divine_service_title=schemas.DivineServiceEnum.liturgy,
                        bible_book_abbr=bible_books_abbrs[j],
                        zachalo_num=zachalos_nums[j]
                ):
                    raise ValueError(f"""
                        Reading: cycle_num={cycle_num}, sunday_num={sunday_num}, day_abbr={day_abbr}, 
                        divine_service_title={schemas.DivineServiceEnum.liturgy}, 
                        bible_book_abbr={bible_books_abbrs[j]}, zachalo_num={zachalos_nums[j]} уже была создана"""
                                     )

                crud.create_reading(
                    db,
                    cycle_num=cycle_num,
                    sunday_num=sunday_num,
                    day_abbr=day_abbr,
                    divine_service_title=schemas.DivineServiceEnum.liturgy,
                    bible_book_abbr=bible_books_abbrs[j],
                    zachalo_num=zachalos_nums[j]
                )
                num_creatures += 1

                if j % 2 == 0:
                    print(f'{day_abbr} | {bible_books_abbrs[j]} - {zachalos_nums[j]}')

    if number_readings != num_creatures:
        raise ValueError(
            f'Не создались {number_readings} записи о чтениях в таблице `readings`.')
    return True

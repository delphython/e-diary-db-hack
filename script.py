import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

import random
import sys
import argparse
from datacenter.models import Commendation
from datacenter.models import Lesson
from datacenter.models import Chastisement
from datacenter.models import Mark
from datacenter.models import Schoolkid
from datacenter.models import Subject


def fix_marks(schoolkid):
    marks_for_changes = [2, 3]
    changed_mark = 5

    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=marks_for_changes)
    for mark in marks:
        mark.points = changed_mark
        mark.save()


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(schoolkid, lesson):
    commendations = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!",
    ]

    Commendation.objects.create(
        schoolkid=schoolkid,
        teacher=lesson.teacher,
        subject=lesson.subject,
        created=lesson.date,
        text=random.choice(commendations)
    )


def get_lesson(schoolkid, subject_title):
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject_title
    ).order_by("?").first()

    return lesson


def get_parsed_args():
    parser = argparse.ArgumentParser(
        description="""Введите ФИО ученика и наименование предмета.
        Пример: python main.py "Иванов Иван Иванович" Математика """
    )

    parser.add_argument("schoolkid_full_name", type=str, help="ФИО ученика в кавычках")
    parser.add_argument("subject", type=str, help="Наименвоание предмета")
    return parser.parse_args()


def main():
    schoolkid_full_name = get_parsed_args().schoolkid_full_name
    subject_title = get_parsed_args().subject

    try:
        subject = Subject.objects.filter(title=subject_title)[:1].get()
    except Subject.DoesNotExist:
        print(f"В базе данных нет предмета с названием {subject_title}!")
        sys.exit()

    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_full_name)
    except Schoolkid.DoesNotExist:
        print(f"В базе данных нет ученика с именем {schoolkid_full_name}!")
        sys.exit()
    except Schoolkid.MultipleObjectsReturned:
        print(f"В базе данных несколько учеников в ФИО которых содержится {schoolkid_full_name}!")
        sys.exit()

    fix_marks(schoolkid)
    remove_chastisements(schoolkid)
    create_commendation(schoolkid, get_lesson(schoolkid, subject_title))


if __name__ == "__main__":
    main()

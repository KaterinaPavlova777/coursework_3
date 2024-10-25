from typing import Any

import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy_1() -> Any:
    return {
        "name": "Junior Python",
        "alternate_url": "https://hh.ru/vacancy/105338726",
        "salary": {"from": 0},
        "snippet": {"responsibility": "Создание скриптов"},
        "area": {
            "name": "Могилев",
        },
    }


@pytest.fixture
def vacancy_2() -> Any:
    return {
        "name": "Junior Python",
        "alternate_url": "https://hh.ru/vacancy/105338726",
        "salary": {"from": 10000},
        "snippet": {"responsibility": "Приглашаем Инженера"},
        "area": {
            "name": "Москва",
        },
    }


@pytest.fixture
def vac_list_1(vacancy_1: Any, vacancy_2: Any) -> Any:
    return [Vacancy(vacancy_1), Vacancy(vacancy_2)]


def test_vacancy_init(vacancy_1: Any) -> None:
    vacancy_1 = Vacancy(vacancy_1)
    assert vacancy_1.name == "Junior Python"
    assert vacancy_1.link == "https://hh.ru/vacancy/105338726"
    assert vacancy_1.salary == 0
    assert vacancy_1.description == "Создание скриптов"
    assert vacancy_1.city == "Могилев"

    assert (
        str(vacancy_1) == " Вакансия: Junior Python, Ссылка: https://hh.ru/vacancy/105338726, Зарплата: 0, Описание:"
        " Создание скриптов, Место: Могилев"
    )


def test_comparison(vacancy_1: Any, vacancy_2: Any) -> None:
    vacancy_1 = Vacancy(vacancy_1)
    vacancy_2 = Vacancy(vacancy_2)
    assert vacancy_1 < vacancy_2

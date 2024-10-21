from typing import Any


class Vacancy:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, vacancy: dict) -> None:
        self.__name = vacancy["name"]
        self.__link = vacancy["alternate_url"]
        self.__salary = vacancy["salary"]["from"]
        self.__description = vacancy["snippet"]["responsibility"]
        self.__validator()

    @property
    def name(self) -> Any:
        return self.__name

    @property
    def link(self) -> Any:
        return self.__link

    @property
    def salary(self) -> Any:
        return self.__salary

    @property
    def description(self) -> Any:
        return self.__description

    def __validator(self) -> None:
        if self.__salary is None:
            self.__salary = 0.0

    def __lt__(self, other: Any) -> Any:
        return self.__salary < other.__salary

    def __le__(self, other: Any) -> Any:
        return self.__salary <= other.__salary

    def __gt__(self, other: Any) -> Any:
        return self.__salary > other.__salary

    def __ge__(self, other: Any) -> Any:
        return self.__salary >= other.__salary

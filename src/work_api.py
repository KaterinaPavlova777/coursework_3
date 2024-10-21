from abc import ABC, abstractmethod
from typing import Any

import requests


class Parser(ABC):
    """
    Абстрактный класс для подключения по API.
    """

    @abstractmethod
    def load_vacancies(self, keyword: str) -> None:
        pass

    @abstractmethod
    def get_vacancies(self) -> None:
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self) -> None:
        self.__url: str = "https://api.hh.ru/vacancies"
        self.__headers: dict = {"User-Agent": "HH-User-Agent"}
        self.__params: dict = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies: list = []

    def load_vacancies(self, keyword: str) -> Any:
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

    def get_vacancies(self) -> Any:
        return self.__vacancies

    @property
    def url(self) -> str:
        return self.__url

    @property
    def headers(self) -> dict:
        return self.__headers

    @property
    def params(self) -> dict:
        return self.__params

    @property
    def vacancies(self) -> list:
        return self.__vacancies

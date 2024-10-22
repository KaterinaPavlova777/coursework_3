import json
from abc import ABC, abstractmethod
from typing import Any

from src.vacancy import Vacancy


class Worker(ABC):
    """
    Абстрактный родительский класс для чтения и записи файла
    """

    @abstractmethod
    def add_vacancy(self, vacancy: Any) -> None:
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy: Any) -> None:
        pass


class JSONSaver:

    def __init__(self, filename: str) -> None:
        self.__filename = filename
        with open(f"{filename}.json", "w", encoding="utf8") as file:
            json.dump([], file)

    @property
    def filename(self) -> Any:
        return self.__filename

    def add_vacancy(self, vacancy: Vacancy) -> None:
        data = {
            "name": vacancy.name,
            "link": vacancy.link,
            "salary": vacancy.salary,
            "description": vacancy.description,
        }

        with open(f"{self.__filename}.json", "r", encoding="utf8") as file:
            info = json.load(file)
        info.append(data)

        with open(f"{self.__filename}.json", "w", encoding="utf8") as file:
            json.dump(info, file)

    def remove_vacancy(self, vacancy: Vacancy) -> None:
        data = {
            "name": vacancy.name,
            "link": vacancy.link,
            "salary": vacancy.salary,
            "description": vacancy.description,
        }

        with open(f"{self.__filename}.json", "r", encoding="utf8") as file:
            info = json.load(file)
        info.remove(data)

        with open(f"{self.__filename}.json", "w", encoding="utf8") as file:
            json.dump(info, file)

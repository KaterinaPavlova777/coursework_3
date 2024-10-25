import json
import os
from abc import ABC, abstractmethod
from typing import Any

from config import DATA_DIR
from src.vacancy import Vacancy


class Worker(ABC):
    """
    Абстрактный класс для чтения и записи файла.
    """

    @abstractmethod
    def read_file(self) -> None:
        pass

    @abstractmethod
    def write_file(self, ser_vacs: Any) -> None:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Any) -> None:
        pass

    @abstractmethod
    def del_vacancy(self) -> None:
        pass


class JSONSaver(Worker):
    """
    Класс для чтения из файла, записи в файл списка вакансий.
    """

    filename_value = "vacancies.json"

    def __init__(self, filename: str = filename_value) -> None:
        self.vacs_list = []
        self.__filename = os.path.join(DATA_DIR, filename)

    @property
    def filename(self) -> str:
        return self.__filename

    def read_file(self) -> Any:
        """
        Функция для чтения файла, если есть, сохраняет список объектов.
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="UTF-8") as f:
                vacs = json.load(f)
            self.vacs_list = [Vacancy(i) for i in vacs]
        return self.vacs_list

    def write_file(self, vacs_obj: Any) -> None:
        """
        Функция для записи списка вакансий в файл. Принимает список объектов класса Vacancy.
        """
        vacs_list = []
        for i in vacs_obj:
            vacs_list.append(
                {
                    "name": Vacancy(i).name,
                    "alternate_url": Vacancy(i).link,
                    "salary": {"from": Vacancy(i).salary},
                    "snippet": {"responsibility": Vacancy(i).description},
                    "area": {"name": Vacancy(i).city},
                }
            )
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(vacs_list, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Any) -> None:
        pass

    def del_vacancy(self) -> None:
        with open(self.filename, "w") as f:
            pass

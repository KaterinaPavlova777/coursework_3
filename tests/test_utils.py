from src.utils import FilterSortVacancies


def test_filter_init() -> None:
    test = FilterSortVacancies(filter_word="python", filter_area="москва", filter_salary=0, top_n=5)
    assert test.filter_word == "python"
    assert test.filter_area == "москва"
    assert test.filter_salary == 0
    assert test.top_n == 5

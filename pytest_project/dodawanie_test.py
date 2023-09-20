import pytest

@pytest.mark.parametrize("skladnik, suma", [(5,10), (2,4)])
def test_dodawanie(skladnik,suma):
    assert skladnik+suma==suma, "Suma dwoch takich samych skladnikow powinna byc rowna: " + str(skladnik+skladnik)


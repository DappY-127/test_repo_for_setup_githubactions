import pytest


@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_title(self):
        self.driver.get('https://phptravels.net/')
        assert self.driver.title == "PHPTRAVELS | Travel Technology Partner"

    def test_title_blog(self):
        self.driver.get('https://phptravels.net/blog')
        print(self.driver.title)
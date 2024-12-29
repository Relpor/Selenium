from tests.conftest import browser


class mapleLandSearchPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://mapleland.gg/"

    def load(self):
        self.browser.get(self.url)

    def search(self, phrase):
        pass
import selenium.webdriver
import pytest

@pytest.fixture
def browser():
    # initialize the Chrome Driver instance
    b = selenium.webdriver.Chrome()
    # Make its calls wait up to 10 seconds for elementto appear
    b.implicitly_wait(10)
    # Return the WebDriver instance for the setup
    yield b
    # Quit the WebDriver instance for the setup
    b.quit()
import pytest
from steps.steps_amazon_loginPage import Amazon_login_validations

@pytest.fixture(scope="session")
def amazonlogin():
    return Amazon_login_validations()

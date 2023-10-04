from pytest_bdd import given, when, then, scenario, parsers

feauture_file_path = "../../features/login_validation.feature"

@scenario(feauture_file_path,"verification of positive flow for amazon login")
def test_validate_positive_flow_amzlogin():
    print('verification of positive flow for amazon login')

@scenario(feauture_file_path,"verification of negative flow for amazon login using invalid email or phone number")
def test_validate_negative_flow1_amzlogin():
    print("verification of negative flow for amazon login using invalid email or phone number")

@scenario(feauture_file_path,"verification of negative flow for amazon login using invalid password")
def test_validate_negative_flow2_amzlogin():
    print('verification of negative flow for amazon login using invalid password')

@given(parsers.parse("user launches the browser and enter this {url} in search box"))
def launch_browser(amazonlogin,url):
    amazonlogin.launch_crbrowser(url)
    print('user launches the browser and enter this <url> in search box')

@when("user click on Sign in option from Account & Lists")
def sign_in():
    print('user click on Sign in option from Account & Lists')

@when('user enters the valid <Email or mobile phone number> in the text box and click on "Continue" button')
def valid_email_phone():
    print('user enters the valid <Email or mobile phone number> in the text box and click on "Continue" button')

@when('user enters valid <Password> in the text box and click on "Sign in" button')
def password():
    print('user enters valid <Password> in the text box and click on "Sign in" button')

@then('validate the user is in Amazon home page using <Title>')
def validate_homepage():
    print('validate the user is in Amazon home page using <Title>')



@When('user enters the invalid <Email or mobile phone number> in the text box and click on "Continue" button')
def invalid_email_phone():
    print('user enters the invalid <Email or mobile phone number> in the text box and click on "Continue" button')

@Then('validate the <Error Message> stating "Please enter the valid Email or mobile phone number"')
def validate_error_msg():
    print('validate the <Error Message> stating "Please enter the valid Email or mobile phone number"')





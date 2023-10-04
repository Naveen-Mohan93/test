Feature: amazon login validation
  @test
  Scenario Outline: verification of positive flow for amazon login
    Given user launches the browser and enter this <url> in search box
    When user click on Sign in option from Account & Lists
    When user enters the valid <Email or mobile phone number> in the text box and click on "Continue" button
    When user enters valid <Password> in the text box and click on "Sign in" button
    Then validate the user is in Amazon home page using <Title>
    Examples:
      |url|Email or mobile phone number|Password|Title|
      |https://www.amazon.in/|naveen.mohan93@gmail.com|MynameisNaveen|Amazon|

Scenario Outline: verification of negative flow for amazon login using invalid email or phone number
    Given user launches the browser and enter this <url> in search box
    When user click on Sign in option from Account & Lists
    When user enters the invalid <Email or mobile phone number> in the text box and click on "Continue" button
    Then validate the <Error Message> stating "Please enter the valid Email or mobile phone number"
    Examples:
      |url|Email or mobile phone number|Error Message|
      |https://www.amazon.in/|naveen.mohan@gmail.com|Please enter the valid Email or mobile phone number|

  Scenario Outline:
    Given user launches the browser and enter this <url> in search box
    When user click on Sign in option from Account & Lists
    When user enters valid <Email or mobile phone number> in the text box and click on "Continue" button
    When user enters invalid "Password" in the text box and click on "Sign in" button
    Then validate the <Error Message> stating "Please enter the valid Password"
    Examples:
      |url|Email or mobile phone number|Error Message|
      |https://www.amazon.in/|naveen.mohan@gmail.com|Please enter the valid Password|
Feature: AdditionTwoNumbers

  Scenario: Adding two numbers
    Given I have clicked number '9'
    And I pressed '+' button on calculator app
    And I have clicked number '4'
    And I pressed '=' button on calculator app
    Then I get the result '13'
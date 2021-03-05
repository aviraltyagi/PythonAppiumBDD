from behave import *
from nose.tools import assert_equal
import config
from features.Utility.WaitUtility import *


@given("I have clicked number '{number}'")
def step_impl(context, number):
    digit = explicit_wait_clickable_element_by_id(context, config.Digit_ID + f"{number}", 30)
    digit.click()


@given("I pressed '{operator}' button on calculator app")
def step_impl(context, operator):
    if operator == "+":
        explicit_wait_clickable_element_by_id(context, config.Operator_ADD_ID, 30).click()
    if operator == "=":
        explicit_wait_clickable_element_by_id(context, config.Operator_Equal_ID, 30).click()


@then("I get the result '{expectedResult}'")
def step_impl(context, expectedResult):
    actualResult = explicit_wait_clickable_element_by_id(context, config.Result_ID, 30).text
    assert_equal(expectedResult, actualResult, msg=f"Expected {expectedResult} but was {actualResult}")

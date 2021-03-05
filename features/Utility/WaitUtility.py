from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def explicit_wait_clickable_element_by_id(context, value, timeout):
    wait = WebDriverWait(context.driver, timeout)
    element = wait.until(EC.element_to_be_clickable((By.ID, value)))
    return element

from appium import webdriver

import config


def before_all(context):
    start_driver(context=context)


def after_all(context):
    close_driver(context=context)


def start_driver(context):
    context.driver = webdriver.Remote(command_executor=config.Host,
                                      desired_capabilities=config.Desired_Capabilities)
    context.driver.implicitly_wait(30)


def close_driver(context):
    if context.driver:
        context.driver.__exit__()

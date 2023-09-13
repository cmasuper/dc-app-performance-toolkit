import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def selenium_launch_report_page(webdriver):
    page = BasePage(webdriver)
    @print_timing("selenium_launch_report_page")
    def measure():
        @print_timing("selenium_launch_report_page:load_page")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/projects/KPROA?projectKey=KPROA&selectedItem=com.go2group.jira.plugin.synapse:report-project-page")
            page.wait_until_visible((By.CSS_SELECTOR, ("a[title='Execution Date wise Report']")))  # Wait for you app-specific UI element by ID selector
        sub_measure()
    measure()


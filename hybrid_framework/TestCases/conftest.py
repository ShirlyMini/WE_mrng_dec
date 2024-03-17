from datetime import datetime

import pytest
from selenium import webdriver

from hybrid_framework.Utilities.ReadProperty import Read_Property


@pytest.fixture()
def launch_browser(request):
    if request.config.getoption("--browser") == "chrome":
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif request.config.getoption("--browser") == "edge":
        from selenium.webdriver.edge.service import Service
        service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    elif request.config.getoption("--browser") == "ff":
        # from selenium.webdriver.firefox.service import Service
        # service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Firefox()
    else:
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    driver.get(Read_Property.GetURL())
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")

def pytest_configure(config):
    # <markers: <name: desc>>
    config.addinivalue_line("markers", "functionality: functional testing")
    config.addinivalue_line("markers", "sanity: sanity testing")


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     now = datetime.now()
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call':
#         feature_request = item.funcargs['request']
#         driver = feature_request.getfuncargvalue('launch_browser')
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             driver.save_screenshot(r'.\ScreenShots\test123.png')
#             # file_name = report.nodeid.replace("::", "_") + ".png"
#             file_name = r'.\ScreenShots\test123.png'
#             # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
#             # _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra

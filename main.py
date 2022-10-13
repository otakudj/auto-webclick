from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import logging

from config import DRIVER_PATH
from secret import HOME_PAGE, USERNAME, PASSWORD


err_filter = logging.Filter()
err_filter.filter = lambda record: record.levelno >= logging.INFO

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='record.log', level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    options = EdgeOptions()

    # # 手动指定使用的浏览器位置
    # options.binary_location = PATH_TO_EDGE  # 浏览器的位置

    # 不加载图片, 提升速度
    options.add_argument('blink-settings=imagesEnabled=false')

    # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    options.add_argument('--headless')

    # 取消DevTools listening on ws://127.0.0.1...提示的方法
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Edge(DRIVER_PATH, options=options)

    driver.get(HOME_PAGE)

    while 1:
        # 刷新页面
        driver.refresh()

        time.sleep(5)

        # 找按钮
        btns = driver.find_elements(By.TAG_NAME, 'button')

        flag = -1
        for ind, btn in enumerate(btns):
            if btn.text == '登 录':
                flag = ind

        if flag == -1:
            logger.info('logged')
        else:
            btn = btns[flag]
            logger.warning('relogging ... ')

            # 模拟按键输入
            driver.find_element(By.ID, 'username').send_keys(USERNAME)
            driver.find_element(By.ID, 'password').send_keys(PASSWORD)

            # 对定位到的元素执行鼠标点击操作
            ActionChains(driver).click(btn).perform()
            logger.warning('done !')

        time.sleep(55)

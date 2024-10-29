import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_footer(url):
    driver = webdriver.Chrome()

    try:
        driver.get(url)
        time.sleep(3)
        footer = driver.find_element(By.TAG_NAME, "footer")
        assert footer, "footer not found"
        print("footer found")
    except Exception as e:
        print(e)
    finally:
        driver.quit()


if __name__ == "__main__":
    test_footer('https://only.digital/')
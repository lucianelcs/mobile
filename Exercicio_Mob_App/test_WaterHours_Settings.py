import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        caps = {
            'platformName': 'Android',
            'appium:automationName': 'UiAutomator2',
            'appium:appPackage': 'com.remind.drink.water.hourly',
            'appium:appActivity': '.SplashActivity',
            'appium:ensureWebviewsHavePages': True,
            'appium:nativeWebScreenshot': True,
            'appium:newCommandTimeout': 3600,
            'appium:connectHardwareKeyboard': True
        }

        options = UiAutomator2Options()
        options.load_capabilities(caps)
        self.driver = webdriver.Remote("http://127.0.0.1:4723",  options=options)
        return super().setUp()

    def my_find_element(self, by, value):
        return WebDriverWait(self.driver, 20).until(lambda x: x.find_element(by=by, value=value))
    
    def test_setup_to_access_settings(self):
        driver = self.driver
        el1 = self.my_find_element(AppiumBy.ID, "com.remind.drink.water.hourly:id/ia")
        el1.click()
        el2 = self.my_find_element(AppiumBy.ID, "com.remind.drink.water.hourly:id/btn_next")
        el2.click()
        el3 = self.my_find_element(AppiumBy.ID, "com.remind.drink.water.hourly:id/btn_next")
        el3.click()
        el4 = self.my_find_element(AppiumBy.ID, "com.remind.drink.water.hourly:id/btn_next")
        el4.click()
        el5 = self.my_find_element(AppiumBy.ID, "com.remind.drink.water.hourly:id/btn_next")
        el5.click()
        el6 = self.my_find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[1]")
        el6.click()
        el7 = self.my_find_element(AppiumBy.ID, "com.remind.drink.water.hourly:id/kj")
        el7.click()
        time.sleep(5)
        el9 = driver.find_element(by=AppiumBy.XPATH, value="//b.a.k.a.c[@content-desc=\"Settings\"]/android.widget.LinearLayout/android.widget.TextView")
        el9.click()
        el10 = driver.find_element(by=AppiumBy.ID, value="com.remind.drink.water.hourly:id/text_language")
        el10.click()
        time.sleep(5)
        el11 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[9]")
        el11.click()
        time.sleep(5)
        el12 = driver.find_element(by=AppiumBy.ID, value="com.remind.drink.water.hourly:id/text_mode")
        current_text = el12.text
        expected_text = "Configuración del dispositivo"
        self.assertEqual(expected_text, current_text, "Os textos não são iguais")

        driver.quit()

    def test_setup_to_access_settings_reminder_scheduler(self):
        driver = self.driver
        el1 = self.my_find_element(AppiumBy.ID, "com.remind.drink.water.hourly:id/ia")
        el1.click()
        el2 = self.my_find_element(AppiumBy.ID, "com.remind.drink.water.hourly:id/btn_next")
        el2.click()
        el3 = self.my_find_element(AppiumBy.ID, "com.remind.drink.water.hourly:id/btn_next")
        el3.click()
        el4 = self.my_find_element(AppiumBy.ID, "com.remind.drink.water.hourly:id/btn_next")
        el4.click()
        el5 = self.my_find_element(AppiumBy.ID, "com.remind.drink.water.hourly:id/btn_next")
        el5.click()
        el6 = self.my_find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[1]")
        el6.click()
        el7 = self.my_find_element(AppiumBy.ID, "com.remind.drink.water.hourly:id/kj")
        el7.click()
        time.sleep(5)
        el9 = driver.find_element(by=AppiumBy.XPATH, value="//b.a.k.a.c[@content-desc=\"Settings\"]/android.widget.LinearLayout/android.widget.TextView")
        el9.click()
        el10 = driver.find_element(by=AppiumBy.ID, value="com.remind.drink.water.hourly:id/reminder_schedule")
        el10.click()
        time.sleep(5)
        el11 = driver.find_element(by=AppiumBy.ID, value="com.remind.drink.water.hourly:id/fab_schedule")
        el11.click()
        time.sleep(3)
        el12 = driver.find_element(by=AppiumBy.ID, value="android:id/button1")
        el12.click()     
        time.sleep(5)
        el12 = driver.find_element(by=AppiumBy.ID, value="com.remind.drink.water.hourly:id/fh")
        current_text = el12.text
        expected_text = "Delete"
        self.assertEqual(expected_text, current_text, "Os textos não são iguais")

        driver.quit()    

if __name__ == '__main__':
    unittest.main()

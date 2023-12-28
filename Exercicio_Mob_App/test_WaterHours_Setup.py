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
    
    def test_setup_inicial(self):
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
        el8 = self.my_find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView")
        label_already_account = "Start drinking first cup of water!"
        assert label_already_account == "Start drinking first cup of water!"

        driver.quit()

    def test_setup_inicial_for_women(self):
         driver = self.driver
         el9 = driver.find_element(by=AppiumBy.ID, value="com.remind.drink.water.hourly:id/ia")
         el9.click()
         el10 = driver.find_element(by=AppiumBy.ID, value="com.remind.drink.water.hourly:id/j_")
         el10.click()
         el11 = driver.find_element(by=AppiumBy.ID, value="com.remind.drink.water.hourly:id/btn_next")
         el11.click()
         el12 = driver.find_element(by=AppiumBy.ID, value="com.remind.drink.water.hourly:id/btn_next")
         el12.click()
         el13 = driver.find_element(by=AppiumBy.ID, value="com.remind.drink.water.hourly:id/btn_next")
         el13.click()
         el14 = self.my_find_element(AppiumBy.ID, "com.remind.drink.water.hourly:id/btn_next")
         el14.click()
         el15 = self.my_find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[1]")
         el15.click()
         el16 = self.my_find_element(AppiumBy.ID, "com.remind.drink.water.hourly:id/kj")
         el16.click()
         el17 = self.my_find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView")
         label_already_account = "Start drinking first cup of water!"
         assert label_already_account == "Start drinking first cup of water!"   

         driver.quit()

if __name__ == '__main__':
    unittest.main()
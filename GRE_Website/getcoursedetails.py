from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = r"C:\Yash\Software Downloads\chromedriver.exe"


class CourseDetails():

    @staticmethod
    def getcoursedetails(course_url):
        try:
            driver = webdriver.Chrome(PATH)  # ,options=opts)
        except:
            print("Webdriver could not be loaded. Check path/version of the selenium webdriver.")
        # Get the homepage
        about = {}
        expenses = {}
        exams = {}
        try:
            driver.get(course_url)
            # Wait for it to load
            wait = WebDriverWait(driver, 10)
            # Obtain search bar
            try:
                row_count = 1
                while True:
                    try:
                        a = driver.find_element_by_xpath(
                            '//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div['
                            '1]/table/tbody/tr[{0}]/td[1]'.format(
                                row_count)).text
                        a = a.split()
                        a_string = ""
                        for word in a:
                            if word == "&":
                                a_string += "And"
                            else:
                                a_string += word
                        b = driver.find_element_by_xpath(
                            '//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/table/tbody/tr['
                            '{0}]/td[2]'.format(
                                row_count)).text
                        about[a_string] = b
                        row_count = row_count + 1
                    except:
                        break
                print(about)
                try:
                    # Tuition fees for 1 year
                    try:
                        a = driver.find_element_by_xpath(
                            '//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[4]/div[2]/div[1]/div['
                            '2]/table/tbody/tr/td[1]').text
                        a = a.split()
                        a_string = ""
                        for word in a:
                            if word == "&":
                                a_string += "And"
                            else:
                                a_string += word
                        b = driver.find_element_by_xpath(
                            '//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[4]/div[2]/div[1]/div['
                            '2]/table/tbody/tr/td[2]').text
                        expenses[a_string] = b
                    except:
                        print("Tuition fees couldn't be accessed")
                    # Other expenses
                    row_count = 1
                    while True:
                        try:
                            a = driver.find_element_by_xpath(
                                '//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[4]/div[2]/div[2]/div['
                                '2]/table/tbody/tr[{0}]/td[1]'.format(
                                    row_count)).text
                            a = a.split()
                            a_string = ""
                            for word in a:
                                if word == "&":
                                    a_string += "And"
                                else:
                                    a_string += word
                            b = driver.find_element_by_xpath(
                                '//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[4]/div[2]/div[2]/div['
                                '2]/table/tbody/tr[{0}]/td[2]'.format(
                                    row_count)).text
                            expenses[a_string] = b
                            row_count = row_count + 1
                        except:
                            break
                    print(expenses)
                    try:
                        row_count = 1
                        while True:
                            try:
                                a = driver.find_element_by_xpath(
                                    '//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[5]/div[2]/div['
                                    '1]/table/tbody/tr[3]/td[2]/div[{0}]/label'.format(
                                        row_count)).text
                                a = a.split()
                                a_string = ""
                                for word in a:
                                    if word == ":":
                                        continue
                                    elif word == "&":
                                        a_string += "And"
                                    else:
                                        a_string += word
                                b = driver.find_element_by_xpath(
                                    '//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[5]/div[2]/div['
                                    '1]/table/tbody/tr[3]/td[2]/div[{0}]/span'.format(
                                        row_count)).text
                                exams[a_string] = b
                                row_count = row_count + 1
                            except:
                                break
                        print(exams)
                    except:
                        print("Exams details not obtained")
                except:
                    print("Expenses details not obtained")
            except:
                print("Basic details not obtained")
        except:
            # Send this error message to admin homepage
            print("Homepage loading failed")
        finally:
            driver.close()
        return about, expenses, exams

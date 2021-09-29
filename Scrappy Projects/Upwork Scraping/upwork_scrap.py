from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


print("Enter Work")
work = input()
work.replace(' ', '%20')
url1 = f'https://www.upwork.com/search/profiles/?q={work}'

driver = webdriver.Chrome(executable_path='C:\\Programming\\Chrome WebDriver\\app\\chromedriver')

file = open(f"Upwork-{work}.csv", "w", encoding='utf-8')
writer = csv.writer(file)

writer.writerow(["Sr. no.", "Work", "Freelancer Name", "Profession", "Location", "Rate", "Earned", "Job Success", "Description"])

def getInfo():
    try:
        driver.get(url1)

        mainDiv = driver.find_element_by_class_name('mt-md-0')
        items = mainDiv.find_elements_by_class_name('up-card-section')

        for i, item in enumerate(items):
            i = i + 1
            try:
                person_name = item.find_element_by_class_name('identity-name').text
            except:
                person_name = "None"
            profession = item.find_element(by=By.CLASS_NAME, value='freelancer-title').text
            location = item.find_element(by=By.CLASS_NAME, value='vertical-align-middle').text
            r = item.find_element_by_class_name('profile-stats')
            rate = r.find_element(by=By.TAG_NAME, value='strong').text+'/hr'
            try:
                e = item.find_element(by=By.CLASS_NAME, value='grid-col-2')
                earned = e.find_element_by_tag_name('p').text
            except:
                earned = "None"
            try:
                success = item.find_element_by_class_name('up-job-success-text').text.split(' ')[0]
            except:
                success = "None"
            description = item.find_element(by=By.CLASS_NAME, value='clamped').text

            writer.writerow([i, work, person_name, profession, location, rate, earned, success, description])

        print("\nFile Saved Successfully!!")
    except:
        print("An Error Occurred ")

    finally:
        driver.close()

getInfo()

file.close()
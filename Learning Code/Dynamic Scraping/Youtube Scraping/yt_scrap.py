from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Programming\\Chrome WebDriver\\app\\chromedriver')
url = 'https://www.youtube.com/c/JohnWatsonRooney/videos'

driver.get(url)

videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')

video_list = []

for video in videos:
    title = video.find_element_by_id('video-title').text
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    when = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    vid_items = {
        'title': title,
        'views': views,
        'posted': when
    }

    video_list.append(vid_items)
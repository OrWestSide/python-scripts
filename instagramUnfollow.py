###########################################################################
#                                                                         #
#	Instagram Unfollower Tool                                             #
#                                                                         #
#	This tool tries to add followers in an IG account by following and    #
#	unfollowing famous IG accounts. By following a really famous account  #
#	you get 0-3 random followers. This tool tries to exploit that. There  #
#	are limitations as to how many unfollows one can do per hour, so use  #
#	at your own risk.													  #
#                                                                         #
#	Developed by OrWestSide												  #
#																		  #
###########################################################################

# Ιmport modules
from time import sleep 				# Module to make programm wait

from selenium import webdriver 							# Module used to initiate a browser
from selenium.webdriver.common.keys import Keys         # Module needed to send keyboard keys to browser
from selenium.webdriver.common.by import By 			# Module for searching an element

from selenium.webdriver.support.ui import WebDriverWait 		# Module to make driver wait until an element is available
from selenium.webdriver.support import expected_conditions		# Module used in combination with WebDriverWait

from selenium.webdriver.chrome.options import Options           # Module imported to make chrome run headless-ly

from selenium.common.exceptions import StaleElementReferenceException		# Module used to import certain exception

# Define strings
url = 'https://instagram.com'
username = 'orestisz93'
password = 'KJDr6LH8t4AhhqV'
path = r'C:\Users\OrWestSide\Desktop\Side projects\Python\Instagram Unfollow Tool\chromedriver_win32\chromedriver.exe'
celebrities = ['instagram', 'cristiano', 'beyonce', 'therock', 'justinbieber', 'jlo']

# Open *headless* chrome and go to instagram website
print('Opening chrome...')													
#c_options = Options()														#
#c_options.add_argument('--headless')										# Uncomment for headless mode
#c_options.add_argument('--disable-gpu')									#
#driver = webdriver.Chrome(executable_path=path, options = c_options)		#
driver = webdriver.Chrome(executable_path=path)
print('Getting \"https://instagram.com\"...')
driver.get(url)

# Click the login button
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a').click()

# Enter username
print('Entering username...')
usrField = driver.find_element_by_name('username')
try:
    usrField.click()
    usrField.send_keys(username)
except StaleElementReferenceException:
    print('Caught exception. Wait 2 second for page to be fully loaded...')
    sleep(2)
    usrField = driver.find_element_by_name('username')
    usrField.click()
    usrField.send_keys(username)

# Enter password
print('Entering password...')
passField = driver.find_element_by_name('password')
try:
    passField.click()
    passField.send_keys(password)
except StaleElementReferenceException:
    print('Caught exception. Wait 2 seconds for page to be fully loaded...')
    sleep(2)
    passField = driver.find_element_by_name('password')
    passField.click()
    passField.send_keys(password)

# Click the log in button
print('Logging in...')
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/button').click()

# Close the notifications window
sleep(5)
driver.find_element_by_css_selector('.aOOlW.HoLwm').click()		# Comment for headless mode
print('\n**Successfully logged in to \"'+ username + '\" account**\n')

# Get current followers number
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'followers')))
previousFollowers = driver.find_element_by_partial_link_text('followers')
previousFollowing = driver.find_element_by_partial_link_text('following')
prevFollowers = int(previousFollowers.text[0])*100 + int(previousFollowers.text[1])*10 + int(previousFollowers.text[2])
prevFollowing = int(previousFollowing.text[0])*100 + int(previousFollowing.text[1])*10 + int(previousFollowing.text[2])
print('Currently, there are ' + str(prevFollowers) + ' followers and ' + str(prevFollowing) + ' following. Let\'s follow some celebrities.\n')

# Let's follow some celebrities!
for name in celebrities:
	searchField = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
	searchField.send_keys(name)
	sleep(4)
	sel = 'a[href*=\'/'+name+ '/\']'
	driver.find_element_by_css_selector(sel).click()
	WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '._5f5mN.jIbKX._6VtSN.yZn4P')))
	driver.find_element_by_css_selector('._5f5mN.jIbKX._6VtSN.yZn4P').click()

# Get number of followers and following after following some celebs
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'followers')))
midFollowers = driver.find_element_by_partial_link_text('followers')
midFollowing = driver.find_element_by_partial_link_text('following')
mFollowers = int(midFollowers.text[0])*100 + int(midFollowers.text[1])*10 + int(midFollowers.text[2])
mFollowing = int(midFollowing.text[0])*100 + int(midFollowing.text[1])*10 + int(midFollowing.text[2])
print('After following the celebrities, we have ' + str(mFollowers) + ' followers and ' + str(mFollowing) + ' following.')

# Let's wait for about 2 minutes
print('\nWaiting 20 seconds', end =" ")
for i in range(1,10):
	print('.',end = " ")
	sleep(2)
print('\nUnfollow the celebrities!!')

# Unfollow the celebrities followed in previous step
for name in celebrities:
	searchField = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
	searchField.send_keys(name)
	sleep(4)
	sel = 'a[href*=\'/'+name+ '/\']'
	driver.find_element_by_css_selector(sel).click()
	WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '._5f5mN.-fzfL._6VtSN.yZn4P')))
	driver.find_element_by_css_selector('._5f5mN.-fzfL._6VtSN.yZn4P').click()

# Get final number of followers and following
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click()
WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'followers')))
driver.refresh()
WebDriverWait(driver, 15).until(expected_conditions.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'followers')))
finalFollowers = driver.find_element_by_partial_link_text('followers')
finalFollowing = driver.find_element_by_partial_link_text('following')
fFollowers = int(finalFollowers.text[0])*100 + int(finalFollowers.text[1])*10 + int(finalFollowers.text[2])
fFollowing = int(finalFollowing.text[0])*100 + int(finalFollowing.text[1])*10 + int(finalFollowing.text[2])
print('Finally, there are ' + str(fFollowers) + ' followers and ' + str(fFollowing) + ' following.')

print('\n**' + str(int(fFollowers - prevFollowers)) + ' new followers were added**\n')

# Close chrome
print('Closing chrome...\n')
driver.quit()

print('Terminated successfully')
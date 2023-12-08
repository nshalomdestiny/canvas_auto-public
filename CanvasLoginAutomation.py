from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml
from selenium.webdriver.chrome.options import Options

# Set Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

# Initialize Chrome driver
driver = webdriver.Chrome(options=chrome_options)


#Function to perform login action
def login(url, usernameID, username, passwordId, password, submit):
  driver.get(url)
  print('URL opened') #logging Status
  driver.find_element(By.ID, usernameID).send_keys(username)
  print('username sent') #logging Status
  driver.find_element(By.ID, passwordId).send_keys(password)
  print('password sent') #logging Status
  driver.find_element(By.ID, submit).click()
  print('submision sent') #logging Status

#Function to find Today's posts/assingments
def assingment():
  #Search Html file for Today section
  today = driver.find_element(By.CLASS_NAME, 'planner-today')
  print("Today Section Found") #log status

  #Find parent Elements containing datas in today Element
  planner = today.find_elements(By.CLASS_NAME, 'css-qch21e-view-link')

  for elem in planner:  
    #Error handling in case one of the Parent Elements doesn't contain child Element    
    try:
      #Get Assingments: Find element within Todays section planner that has keyword "assingment"
      is_assingment = elem.find_element(By.XPATH, 'span[@class="css-1sr5vj2-screenReaderContent" and contains(text(), "Assignment")]')
      due = is_assingment.find_element(By.XPATH, './../../../div[2]/div[2]/div/span/span').text
      assingment = is_assingment.find_element(By.XPATH, './../span[2]').text
      print(f"Today's Assingments:\n|->{assingment} Due at {due}\n")
      return assingment, due

    except:
      False

    try:
      is_announcement = elem.find_element(By.XPATH, 'span[@class="css-1sr5vj2-screenReaderContent" and contains(text(), "Announcement")]')
      anouncement = is_announcement.find_element(By.XPATH, './../span[2]').text
      posted = is_announcement.find_element(By.XPATH, './../../../div[2]/div[2]/div/span/span').text
      print(f"Today's Announcenments:\n|->{anouncement} Posted at{posted}\n")
      return anouncement, posted

    except:
      False

#get Username and password from yaml file
with open('C:/projects/canvas_alerts/canvas_login/loginDetails.yml', 'r') as file:
  confidential = yaml.safe_load(file)

my_username = confidential['login_data']['canvas_username']
my_password = confidential['login_data']['canvas_password']

canvas_website = 'https://pgcps.instructure.com'

login(canvas_website, "userNameInput", my_username, "passwordInput", my_password, "submitButton")

assingment()
from selenium import webdriver

driver =  webdriver.Chrome('./chromedriver.exe') 
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("https://www.doctolib.fr/account/appointments/1868784635")

print (session_id)
print (executor_url)


driver2 = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
driver2.session_id = session_id
print (driver2.current_url)
from lib2to3.pgen2 import driver
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

from zmq import proxy

proxy_ip_port = '92.240.206.207'

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.FIREFOX
proxy.add_to_capabilities(capabilities)

#Driver related to automate browser
# GECODRIVER 
Path = "geckodriver.exe"
driver = webdriver.Firefox(executable_path = Path, desired_capabilities=capabilities)

'''WRITE THIS FOR RUNNING GECKODRIVER IN HEADLESS MODE'''

# options = FirefoxOptions()
# options.add_argument("--headless")
# driver = webdriver.Firefox(options=options)

'''HEADLESS CODE ENDS HERE'''

target_url = 'https://whatismyipaddress.com/'
driver.get(target_url)
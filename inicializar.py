from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Inicializar:
    def __init__(self):

        self._chrome_options = Options()
        
        self._arguments = [
            '--lang=pt-BR',
            '--window-size=800,600',
            '--incognito',
            '--disable-notifications'
        ]

        for argument in self._arguments:
            self._chrome_options.add_argument(argument)

        self._chrome_options.add_experimental_option('prefs',{
            'download.prompt_for_download': False,
            'profile.default_content_setting_values.notifications': 2,
            'profile.default_content_setting_values.automatic_downloads': 1
        })

        self._driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version='114.0.5735.90').install()), options=self._chrome_options)


    def get_driver(self):
        return self._driver
    
    def get_arguments(self):
        return self._arguments
    
    def include_argument(self, argument):
        self._arguments.append(argument)

    def exclude_argument(self, argument):
        if argument in self._arguments:
            self._arguments.remove(argument)
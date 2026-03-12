from aiAccessInterface import AiAccessInterface
class AiAccessBrowser(AiAccessInterface):
    # This class is responsible for managing the connection to the AI through a web browser using Playwright.
    def __init__(self) -> None:
        self.playwright = None
        self.context = None
        self.page = None

    def sayHello(self) -> None:
        # This method can be used to greet the user.
        print("Hello! This is the AiAccessBrowser class.")

    def ask(self, prompt : str, model: str = "mixtral-8x7b-instruct") -> str:
        # This method should be implemented to send a prompt to the AI and receive a response.
        # You can use the self.page object to interact with the web page and extract the response.
        return "method not implemented yet!"

    def connect(self) -> bool:
        # This method establishes a connection to the AI through the web browser. It uses Playwright to automate the login process and navigate to the AI chat page.
        import os
        from dotenv import load_dotenv
        from pathlib import Path
        env_path = Path(__file__).resolve().parent.parent / ".env"  # aiWorkflow/.env
        load_dotenv(dotenv_path=env_path)

        unimail = os.getenv("ACADEMIC_EMAIL")#todo: make this dynamic
        institution_name = os.getenv("INSTITUTION_NAME")#
        uni_username = os.getenv("UNI_USERNAME")#
        uni_password = os.getenv("UNI_PASSWORD")#
        """ import getpass
        uni_password = getpass.getpass("Please enter your university password: ")#todo: make this dynamic; so load these data from a file
        """

        from playwright.sync_api import sync_playwright
        user_data_dir = ".playwright_academiccloud_profile"

        self.playwright = sync_playwright().start()
        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=False,
            slow_mo=0,
        )

        self.page = self.context.pages[0] if self.context.pages else self.context.new_page()
        self.page.goto("https://chat-ai.academiccloud.de/chat")
        self.page.wait_for_load_state("domcontentloaded")

        # STEP 1: Fill in email on Academic Cloud login page
        self.page.fill('input[name="login"]', unimail)
        self.page.click('button[type="submit"]')  # Click "Weiter"
        self.page.wait_for_load_state("domcontentloaded")

        self.page.click(".dselect-wrapper")
        self.page.wait_for_selector(".dropdown-menu.show")

        # Search for institution by name
        self.page.fill('.dropdown-menu.show input[placeholder="Search"]', institution_name)
        self.page.wait_for_timeout(timeout=500)

        # Click matching institution entry
        self.page.locator(".dropdown-menu.show .dropdown-item").filter(has_text=institution_name).first.click()

        # Submit selected institution
        self.page.get_by_role("button", name="Weiter").click()
        self.page.wait_for_load_state("domcontentloaded")

        # University login
        self.page.wait_for_selector('input[name="j_username"]')
        self.page.fill('input[name="j_username"]', uni_username)
        self.page.fill('input[name="j_password"]', uni_password)
        self.page.get_by_role("button", name="Anmelden").click()

        self.page.wait_for_load_state("domcontentloaded")
        skip_tour_button = self.page.get_by_role("button", name="Tour überspringen")
        try:
            skip_tour_button.wait_for(timeout=500)
            skip_tour_button.click()
        except:
            pass
        print(f"Welcome to {self.page.url}")
        return True
    
    def disconnect(self) -> None:
        # This method is responsible for closing the browser and cleaning up any resources used for the connection.
        print("Disconnecting browser...")
        if self.context:
            self.context.close()
            self.context = None

        if self.playwright:
            self.playwright.stop()
            self.playwright = None

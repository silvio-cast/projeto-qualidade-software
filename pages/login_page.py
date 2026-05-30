BASE_URL = "https://local-eats-unisenac.vercel.app/static"


class LoginPage:
    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto(f"{BASE_URL}/login.html")
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector("#loginEmail", state="visible", timeout=10000)

    def preencher_login(self, email, senha):
        self.page.locator("#loginEmail").fill(email)
        self.page.locator("#loginPassword").fill(senha)

    def submeter_login(self):
        self.page.locator("#loginForm button[type='submit']").click()

    def preencher_cadastro(self, nome, email, senha):
        self.page.locator("#showRegisterBtn").click()
        self.page.locator("#regName").fill(nome)
        self.page.locator("#regEmail").fill(email)
        self.page.locator("#regPassword").fill(senha)

    def submeter_cadastro(self):
        self.page.locator("#registerForm button[type='submit']").click()

    def mensagem_erro(self):
        return self.page.locator("#errorMsg")

    def badge_usuario(self):
        return self.page.locator("#userBadge")

    def esta_autenticado(self):
        return self.page.locator("#logoutBtn").is_visible()

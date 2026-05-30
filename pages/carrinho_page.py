BASE_URL = "https://local-eats-unisenac.vercel.app/static"


class CarrinhoPage:
    def __init__(self, page):
        self.page = page

    def acessar_home(self):
        self.page.goto(f"{BASE_URL}/index.html")
        self.page.wait_for_selector(".rest-card", timeout=15000)

    def autenticar(self, nome="Teste PBL", user_id="999"):
        # Navega para o domínio primeiro para poder escrever no localStorage
        self.page.goto(f"{BASE_URL}/login.html")
        self.page.wait_for_load_state("networkidle")
        self.page.evaluate(
            f"""() => {{
                localStorage.setItem('userId', '{user_id}');
                localStorage.setItem('userName', '{nome}');
            }}"""
        )
        # Navega para a home agora autenticado
        self.acessar_home()

    def clicar_primeiro_restaurante(self):
        self.page.locator(".rest-card").first.click()

    def aguardar_cardapio(self):
        self.page.wait_for_selector("#menuList .menu-item", timeout=10000)

    def adicionar_primeiro_item(self):
        self.page.locator(".add-cart-btn").first.click()

    def badge_contagem_carrinho(self):
        return self.page.locator("#cartCountBadge")

    def total_carrinho(self):
        return self.page.locator("#cartTotalValue")

    def carrinho_visivel(self):
        return self.page.locator(".floating-cart").is_visible()

    def finalizar_pedido(self):
        self.page.locator("#checkoutBtn").click()

    def modal_sucesso_visivel(self):
        return self.page.locator("#orderSuccessModal").is_visible()

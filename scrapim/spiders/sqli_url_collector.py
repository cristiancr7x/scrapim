from scrapy import Spider, Request
from urllib.parse import urljoin, quote

class SQLiURLCollectorSpider(Spider):
    name = "sqli_url_collector"

    # Palabras clave para filtrar URLs
    keywords = [
        "/api/login", "access_token",
        "/login.php", "username", "password",
        "/signin", "intitle:Login",
        "/admin/login", "panel",
        "/wp-login.php", "site:.org",
        "/user/login", "intitle:Drupal",
        "index.php?page=login",
        "/auth", "intext:token",
        "/account/signin", "site:.co",
        "login", "AND intext:remember me"
    ]

    def start_requests(self):
        # Usamos Google para buscar URLs que contengan nuestras palabras clave
        for keyword in self.keywords:
            google_search_url = f"https://www.google.com/search?q={quote(keyword)}"
            yield Request(google_search_url, callback=self.parse_google_results)

    def parse_google_results(self, response):
        # Extraemos los enlaces de los resultados de búsqueda de Google
        links = response.css(".tF2Cxc a::attr(href)").getall()
        for link in links:
            # Verificamos si el enlace es absoluto
            if link.startswith("http"):
                yield {"url": link}
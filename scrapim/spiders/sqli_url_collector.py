from scrapy import Spider
from urllib.parse import urljoin


class SQLiURLCollectorSpider(Spider):
    name = "sqli_url_collector"
    start_urls = [
        "https://www.disneyplus.com/identity/login"
    ]

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

    def parse(self, response):
        # Extraer todos los enlaces de la página
        links = response.css("a::attr(href)").getall()
        for link in links:
            absolute_url = urljoin(response.url, link)
            # Filtrar URLs que contengan alguna de las palabras clave
            if any(keyword in absolute_url for keyword in self.keywords):
                yield {"url": absolute_url}

        # Seguir a la siguiente página si existe
        next_page = response.css(".next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
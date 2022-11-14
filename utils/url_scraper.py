import os
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from multiprocessing import get_context
class Scraper:
    root_url = "https://www.immoweb.be/en"
    search_apartment_url = root_url + "/search/apartment/for-sale" 
    search_house_url = root_url + "/search/house/for-sale"
    search_property_type_url = [search_apartment_url, search_house_url]

    def _get_properties_url(page_num):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        items = []
        for property_type in Scraper.search_property_type_url:
            print(f"PAGE N°{page_num} of {property_type}")
            driver.get(property_type + f"?countries=BE&isAPublicSale=false&page={page_num}&orderBy=relevance")
            elements = driver.find_elements(By.XPATH, '//h2[@class="card__title card--result__title"]')
            for item in elements:
                items.append(item.find_element(By.CLASS_NAME, "card__title-link").get_attribute("href"))
        driver.close()
        return items

    def write_property_urls():
        path = os.path.join(pathlib.Path(__file__).parent.resolve(), "../data")
        try:
            os.mkdir("data")
        except OSError as error: 
            pass
        file_location = os.path.join(path, "realestate_urls.csv")
        with open(file_location, "a+", encoding="utf-8") as cache:
            existing = [l.rstrip("\n") for l in cache.readlines()]
        with get_context("fork").Pool() as pool:
            gen = list(tuple(pool.map(Scraper._get_properties_url, range(1, 300))))
        with open(file_location, "a+", encoding="utf-8") as realestate_file:
            for apt_url in gen:
                for url in apt_url:
                    if url not in existing:
                        realestate_file.write(url + "\n")
        print("Done writing")
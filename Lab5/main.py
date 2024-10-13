from html_renderer import HTMLRenderer
from json_renderer import JSONRenderer
from xml_renderer import XMLRenderer
from simple_page import SimplePage
from product_page import ProductPage
from product import Product

def main():
    html_renderer = HTMLRenderer()
    json_renderer = JSONRenderer()
    xml_renderer = XMLRenderer()

    simple_page = SimplePage(html_renderer, "Main Page", "Welcome!")
    simple_page.view()

    simple_page = SimplePage(json_renderer, "Main Page", "Welcome!")
    simple_page.view()

    simple_page = SimplePage(xml_renderer, "Main Page", "Welcome!")
    simple_page.view()


    

    product = Product("Car", "Cool car", "car.png", 101)

    product_page = ProductPage(html_renderer, product)
    product_page.view()

    product_page = ProductPage(json_renderer, product)
    product_page.view()

    product_page = ProductPage(xml_renderer, product)
    product_page.view()

if __name__ == "__main__":
    main()

import os
from datetime import datetime
from xml.etree import ElementTree as ET
from xml.dom import minidom

def generate_sitemap():
    # Cấu hình cơ bản
    domain = "monkeymart.one"
    base_url = f"https://{domain}"
    
    # Tạo root element
    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    urlset.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    urlset.set("xsi:schemaLocation", "http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd")

    # Danh sách các trang chính
    main_pages = {
        "/": {"priority": "1.0", "changefreq": "daily"},
        "/index.html": {"priority": "0.9", "changefreq": "daily"},
    }

    # Danh sách các category
    categories = [
        "new", "sports", "running", "racing", "car", "puzzle",
        "skill", "stickman", "adventure", "shooting", "fighting", "2-player"
    ]

    # Danh sách các game Papa's
    papas_games = [
        "freezeria", "burgeria", "pizzeria", "wingeria", "sushiria",
        "pastaria", "cheeseria", "cupcakeria", "donuteria", "taco-mia",
        "bakeria", "hot-doggeria", "pancakeria", "scooperia"
    ]

    # Danh sách các game khác
    other_games = [
        "monkey-mart", "slope", "geometry-dash", "friday-night-funkin",
        "papa-louie-when-pizzas-attack", "papa-louie-2-when-burgers-attack",
        "papa-louie-3-when-sundaes-attack", "jacksmith",
        "cactus-mccoy-1", "cactus-mccoy-2"
    ]

    # Thêm trang chính
    for path, settings in main_pages.items():
        add_url(urlset, base_url + path, settings["priority"], settings["changefreq"])

    # Thêm trang category
    for category in categories:
        add_url(urlset, f"{base_url}/category/{category}.html", "0.8", "weekly")

    # Thêm trang Papa's Games
    for game in papas_games:
        add_url(urlset, f"{base_url}/papas-{game}.html", "0.8", "weekly")

    # Thêm các game khác
    for game in other_games:
        if game.startswith("papa-louie"):
            add_url(urlset, f"{base_url}/{game}.html", "0.8", "weekly")
        else:
            add_url(urlset, f"{base_url}/go/{game}.html", "0.8", "weekly")

    # Tạo XML string với format đẹp
    xml_str = minidom.parseString(ET.tostring(urlset)).toprettyxml(indent="  ")
    
    # Lưu file
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml_str)

    # Tạo sitemap index
    create_sitemap_index(domain)

def add_url(urlset, loc, priority, changefreq):
    url = ET.SubElement(urlset, "url")
    
    # Location
    ET.SubElement(url, "loc").text = loc
    
    # Last modified
    ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
    
    # Change frequency
    ET.SubElement(url, "changefreq").text = changefreq
    
    # Priority
    ET.SubElement(url, "priority").text = priority

def create_sitemap_index(domain):
    sitemapindex = ET.Element("sitemapindex")
    sitemapindex.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    # Add main sitemap
    sitemap = ET.SubElement(sitemapindex, "sitemap")
    ET.SubElement(sitemap, "loc").text = f"https://{domain}/sitemap.xml"
    ET.SubElement(sitemap, "lastmod").text = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")

    # Create pretty XML string
    xml_str = minidom.parseString(ET.tostring(sitemapindex)).toprettyxml(indent="  ")
    
    # Save file
    with open("sitemapindex.xml", "w", encoding="utf-8") as f:
        f.write(xml_str)

if __name__ == "__main__":
    generate_sitemap()
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

    # Các trang ưu tiên cao
    priority_pages = {
        "/": {"priority": "1.0", "changefreq": "daily"},
        "/index.html": {"priority": "0.9", "changefreq": "daily"},
    }

    # Thêm trang ưu tiên cao
    for path, settings in priority_pages.items():
        add_url(urlset, base_url + path, settings["priority"], settings["changefreq"])

    # Quét tất cả file HTML trong thư mục
    excluded_paths = [
        'privacy-policy.html', 
        'terms.html', 
        'contact.html',
        '404.html',
        'index.html'  # Đã thêm ở trên
    ]

    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html') and file not in excluded_paths:
                # Lấy đường dẫn tương đối
                rel_path = os.path.join(root, file)[2:].replace('\\', '/')
                
                # Xác định priority và changefreq dựa trên loại trang
                priority = "0.8"
                changefreq = "weekly"
                
                if "category/" in rel_path:
                    priority = "0.7"
                    changefreq = "weekly"
                elif "go/" in rel_path:
                    priority = "0.8"
                    changefreq = "weekly"
                elif "papas-" in rel_path:
                    priority = "0.8"
                    changefreq = "weekly"
                
                # Thêm URL vào sitemap
                add_url(urlset, f"{base_url}/{rel_path}", priority, changefreq)

    # Tạo XML string với format đẹp
    xml_str = minidom.parseString(ET.tostring(urlset)).toprettyxml(indent="  ")
    
    # Xóa các dòng trống
    xml_str = '\n'.join([line for line in xml_str.split('\n') if line.strip()])
    
    # Lưu file sitemap.xml
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml_str)

    # Tạo sitemap index
    create_sitemap_index(domain)

    # In thống kê
    url_count = len(urlset.findall('url'))
    print(f"Đã tạo sitemap với {url_count} URLs")

def add_url(urlset, loc, priority, changefreq):
    url = ET.SubElement(urlset, "url")
    
    # Location
    ET.SubElement(url, "loc").text = loc
    
    # Last modified - sử dụng thời gian thực của file nếu có
    try:
        file_path = loc.replace('https://monkeymart.one/', '')
        if os.path.exists(file_path):
            mtime = os.path.getmtime(file_path)
            lastmod = datetime.fromtimestamp(mtime).strftime("%Y-%m-%dT%H:%M:%S+00:00")
        else:
            lastmod = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
    except:
        lastmod = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
    
    ET.SubElement(url, "lastmod").text = lastmod
    
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
    xml_str = '\n'.join([line for line in xml_str.split('\n') if line.strip()])
    
    # Save file
    with open("sitemapindex.xml", "w", encoding="utf-8") as f:
        f.write(xml_str)

if __name__ == "__main__":
    generate_sitemap() 
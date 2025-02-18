import os
import re

def modify_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Thêm link CSS
    css_links = '''<!-- Game Pages Stylesheet -->
    <link href="css/game-pages.css" rel="stylesheet">
    <!-- Papa Pages Stylesheet -->
    <link href="css/papa-pages.css" rel="stylesheet">'''
    
    if 'css/papa-pages.css' not in content:
        content = content.replace('<!-- Main Stylesheet -->\n\t<link href="css/style.css" rel="stylesheet">', 
                                '<!-- Main Stylesheet -->\n\t<link href="css/style.css" rel="stylesheet">\n\t' + css_links)
    
    # Xóa style inline và sửa section title
    content = re.sub(r'<div class="section-title-area[^>]*" style="[^"]*">', 
                    r'<div class="section-title-area ltn__section-title-1 text-center">', 
                    content)
    
    # Xóa class papa-title nếu có
    content = content.replace('class="section-title papa-title"', 'class="section-title"')
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    # Danh sách các file cần cập nhật
    papa_files = [
        'papas-bakeria.html',
        'papas-burgeria.html', 
        'papas-cheeseria.html',
        'papas-cupcakeria.html',
        'papas-donuteria.html',
        'papas-freezeria.html',
        'papas-hot-doggeria.html',
        'papas-pancakeria.html',
        'papas-pastaria.html',
        'papas-pizzeria.html',
        'papas-scooperia.html',
        'papas-sushiria.html',
        'papas-taco-mia.html',
        'papas-wingeria.html',
        'papa-louie-when-pizzas-attack.html',
        'papa-louie-2-when-burgers-attack.html',
        'papa-louie-3-when-sundaes-attack.html',
        'jacksmith.html',
        'cactus-mccoy-1.html',
        'cactus-mccoy-2.html'
    ]

    # Thư mục gốc của project
    root_dir = os.path.dirname(os.path.abspath(__file__))

    # Cập nhật từng file
    for file_name in papa_files:
        file_path = os.path.join(root_dir, file_name)
        if os.path.exists(file_path):
            print(f'Đang cập nhật {file_name}...')
            modify_html_file(file_path)
            print(f'Đã cập nhật xong {file_name}')
        else:
            print(f'Không tìm thấy file {file_name}')

if __name__ == '__main__':
    main() 
import os
import re

def modify_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Thêm link CSS
    css_links = '''<!-- Game Pages Stylesheet -->
    <link href="/css/game-pages.css" rel="stylesheet">
    <!-- Papa Pages Stylesheet -->
    <link href="/css/papa-pages.css" rel="stylesheet">'''
    
    if 'css/papa-pages.css' not in content:
        content = content.replace('<!-- Main Stylesheet -->\n\t<link href="/css/style.css" rel="stylesheet">', 
                                '<!-- Main Stylesheet -->\n\t<link href="/css/style.css" rel="stylesheet">\n\t' + css_links)
    
    # Xóa style inline và sửa section title
    content = re.sub(r'<div class="section-title-area[^>]*" style="[^"]*">', 
                    r'<div class="section-title-area ltn__section-title-1 text-center">', 
                    content)
    
    # Xóa class papa-title nếu có
    content = content.replace('class="section-title papa-title"', 'class="section-title"')
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    # Thư mục gốc của project
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Cập nhật các file trong thư mục go
    go_dir = os.path.join(root_dir, 'go')
    if os.path.exists(go_dir):
        go_files = [f for f in os.listdir(go_dir) if f.endswith('.html')]
        for file_name in go_files:
            file_path = os.path.join(go_dir, file_name)
            print(f'Đang cập nhật go/{file_name}...')
            modify_html_file(file_path)
            print(f'Đã cập nhật xong go/{file_name}')

if __name__ == '__main__':
    main() 
import os
import re

def add_layout_css(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Tìm vị trí để chèn layout.css
    css_insert_pattern = r'(.*<link href="/css/responsive.css" rel="stylesheet">)'
    new_css = r'\1\n\t<link href="/css/layout.css" rel="stylesheet">'
    
    new_content = re.sub(css_insert_pattern, new_css, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def main():
    # Thư mục gốc của project
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Cập nhật các file trong thư mục gốc
    html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]
    
    for file_name in html_files:
        file_path = os.path.join(root_dir, file_name)
        if os.path.exists(file_path):
            print(f'Đang cập nhật {file_name}...')
            add_layout_css(file_path)
            print(f'Đã cập nhật xong {file_name}')
    
    # Cập nhật các file trong thư mục go và category
    for subdir in ['go', 'category']:
        subdir_path = os.path.join(root_dir, subdir)
        if os.path.exists(subdir_path):
            subdir_files = [f for f in os.listdir(subdir_path) if f.endswith('.html')]
            for file_name in subdir_files:
                file_path = os.path.join(subdir_path, file_name)
                print(f'Đang cập nhật {subdir}/{file_name}...')
                add_layout_css(file_path)
                print(f'Đã cập nhật xong {subdir}/{file_name}')

if __name__ == '__main__':
    main() 
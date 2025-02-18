import os
import re

def get_menu_from_index():
    with open('index.html', 'r', encoding='utf-8') as file:
        content = file.read()
        # Tìm toàn bộ phần menu từ trang chủ, bao gồm cả container
        menu_match = re.search(
            r'<div class="col-xl-8 col-lg-8">\s*'
            r'<div class="header-menu header-menu-style-1">\s*'
            r'<nav>\s*'
            r'<div class="ltn__main-menu">\s*'
            r'<ul>(.*?)</ul>\s*'
            r'</div>\s*'
            r'</nav>\s*'
            r'</div>\s*'
            r'</div>',
            content, 
            re.DOTALL
        )
        if menu_match:
            return menu_match.group(0)
    return None

def update_html_file(file_path, menu_content):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Tìm và thay thế toàn bộ phần menu
    new_content = re.sub(
        r'<div class="col-xl-8 col-lg-8">\s*'
        r'<div class="header-menu header-menu-style-1">\s*'
        r'<nav>\s*'
        r'<div class="ltn__main-menu">\s*'
        r'<ul>.*?</ul>\s*'
        r'</div>\s*'
        r'</nav>\s*'
        r'</div>\s*'
        r'</div>',
        menu_content,
        content,
        flags=re.DOTALL
    )
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def main():
    # Lấy menu từ trang chủ
    menu_content = get_menu_from_index()
    if not menu_content:
        print("Không tìm thấy menu trong trang chủ!")
        return
    
    print("Đã tìm thấy menu từ trang chủ.")
    
    # Thư mục gốc của project
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Cập nhật các file trong thư mục gốc
    html_files = [f for f in os.listdir(root_dir) if f.endswith('.html') 
                 and f not in ['index.html', 'privacy-policy.html', 'terms.html', 'contact.html']]
    
    for file_name in html_files:
        file_path = os.path.join(root_dir, file_name)
        if os.path.exists(file_path):
            print(f'Đang cập nhật {file_name}...')
            update_html_file(file_path, menu_content)
            print(f'Đã cập nhật xong {file_name}')
    
    # Cập nhật các file trong thư mục go
    go_dir = os.path.join(root_dir, 'go')
    if os.path.exists(go_dir):
        go_files = [f for f in os.listdir(go_dir) if f.endswith('.html')]
        for file_name in go_files:
            file_path = os.path.join(go_dir, file_name)
            print(f'Đang cập nhật go/{file_name}...')
            update_html_file(file_path, menu_content)
            print(f'Đã cập nhật xong go/{file_name}')

if __name__ == '__main__':
    main() 
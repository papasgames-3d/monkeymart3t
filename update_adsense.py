import os
import re

def add_adsense_code(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Kiểm tra xem mã AdSense đã tồn tại chưa
    if 'adsbygoogle.js?client=ca-pub-4151519079019358' in content:
        print(f'Mã AdSense đã tồn tại trong {file_path}')
        return
        
    # Tìm vị trí để chèn mã AdSense (trước thẻ </head>)
    adsense_code = '\t<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4151519079019358" crossorigin="anonymous"></script>'
    
    # Thêm mã AdSense vào trước </head>
    head_pattern = r'(.*</head>)'
    new_content = re.sub(head_pattern, f'{adsense_code}\n\\1', content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    print(f'Đã thêm mã AdSense vào {file_path}')

def main():
    # Thư mục gốc của project
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Cập nhật các file trong thư mục gốc
    html_files = [f for f in os.listdir(root_dir) if f.endswith('.html')]
    
    for file_name in html_files:
        file_path = os.path.join(root_dir, file_name)
        if os.path.exists(file_path):
            print(f'Đang cập nhật {file_name}...')
            add_adsense_code(file_path)
            print(f'Đã cập nhật xong {file_name}')
    
    # Cập nhật các file trong thư mục go và category
    for subdir in ['go', 'category']:
        subdir_path = os.path.join(root_dir, subdir)
        if os.path.exists(subdir_path):
            subdir_files = [f for f in os.listdir(subdir_path) if f.endswith('.html')]
            for file_name in subdir_files:
                file_path = os.path.join(subdir_path, file_name)
                print(f'Đang cập nhật {subdir}/{file_name}...')
                add_adsense_code(file_path)
                print(f'Đã cập nhật xong {subdir}/{file_name}')

if __name__ == '__main__':
    main() 
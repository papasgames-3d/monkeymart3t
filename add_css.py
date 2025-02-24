import os

def add_category_pages_css(directory):
    # Đường dẫn đến thư mục chứa các file HTML
    dir_path = directory
    
    # Lặp qua tất cả các file trong thư mục
    for filename in os.listdir(dir_path):
        if filename.endswith('.html'):
            file_path = os.path.join(dir_path, filename)
            
            # Đọc nội dung file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Tìm vị trí để chèn category-pages.css
            css_insert_point = content.find('<link href="/css/layout.css" rel="stylesheet">')
            if css_insert_point != -1:
                # Tìm vị trí kết thúc của dòng layout.css
                line_end = content.find('\n', css_insert_point)
                
                # Chèn category-pages.css sau layout.css
                new_content = (
                    content[:line_end] + 
                    '\n\t<link href="/css/category-pages.css" rel="stylesheet">' +
                    content[line_end:]
                )
                
                # Ghi nội dung mới vào file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                    
                print(f'Added category-pages.css to {filename}')

# Chạy script với thư mục go
add_category_pages_css('go')
def modify_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Thêm link đến game-pages.css và papa-pages.css
    css_links = '''<!-- Game Pages Stylesheet -->
    <link href="css/game-pages.css" rel="stylesheet">
    <!-- Papa Pages Stylesheet -->
    <link href="css/papa-pages.css" rel="stylesheet">'''
    
    content = content.replace('<!-- Main Stylesheet -->\n\t<link href="css/style.css" rel="stylesheet">', 
                            '<!-- Main Stylesheet -->\n\t<link href="css/style.css" rel="stylesheet">\n\t' + css_links)
    
    # ... phần code còn lại giữ nguyên ... 
# Multi-line string
print('''
hello
there
''')

# Multi-line f-string
title = 'Website'
content = 'This is a website.'

HTML = f'''
<html>
    <head>
        {title}
    </head>
    <body>
        {content}
    </body>
</html
'''
print(HTML)

# Can also use quotes
print("""
hello
there
""")

# Mix and match to block comment, otherwise it interferes
'''
print("""
hello
there
""")
'''

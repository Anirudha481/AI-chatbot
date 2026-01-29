import markdown
import os

# Read the markdown file
with open('Project Report.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Convert to HTML
html_content = markdown.markdown(text, extensions=['fenced_code', 'tables'])

# Add CSS for better printing
styled_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Project Report</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            color: #24292e;
        }}
        h1, h2, h3 {{ border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }}
        code {{ background-color: #f6f8fa; padding: 0.2em 0.4em; border-radius: 3px; }}
        pre {{ background-color: #f6f8fa; padding: 16px; overflow: auto; border-radius: 3px; }}
        blockquote {{ border-left: 0.25em solid #dfe2e5; color: #6a737d; padding: 0 1em; }}
        img {{ max-width: 100%; }}
        @media print {{
            body {{ max-width: 100%; padding: 0; }}
            a {{ text-decoration: none; color: black; }}
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

# Write to HTML file
with open('Project_Report_Printable.html', 'w', encoding='utf-8') as f:
    f.write(styled_html)

print("Created Project_Report_Printable.html")

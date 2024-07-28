import re

def convert_to_markdown(text):
    # Replace specific div elements with :::note info and :::
    text = re.sub(r'<div class="row">\s*<div class="col s12 light-blue lighten-5">\s*', ':::note info\n', text)
    text = re.sub(r'\s*</div>\s*</div>', '\n:::\n', text)
    
    # Remove remaining div tags
    text = re.sub(r'<div.*?>', '', text)
    text = re.sub(r'</div>', '', text)
    
    # Replace <br> tags with newlines
    text = text.replace('<br>', '\n')
    
    # Convert <ul> and <li> tags to Markdown list syntax
    text = re.sub(r'<ul>\s*', '', text)  # Remove opening <ul> tags
    text = re.sub(r'\s*</ul>', '', text)  # Remove closing </ul> tags
    text = re.sub(r'<li>\s*', '* ', text)  # Replace opening <li> tags with Markdown list items
    text = re.sub(r'\s*</li>', '', text)  # Remove closing </li> tags
    
    # Convert <strong> tags to Markdown bold syntax
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)
    
    # Replace specific HTML entities if any
    text = text.replace('&nbsp;', ' ')
    
    # Ensure newlines after blockquotes
    text = re.sub(r'(\n> [^\n]*)', r'\1\n', text)
    
    return text


# Read the original file
input_file = './text/【民法1】序論・行為能力と制限行為能力者制度・失踪宣告・法人・権利能力なき社団・権利の客体・法律行為'
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

# Convert the content to GitHub Markdown format
markdown_content = convert_to_markdown(content)

# Write the converted content to a new file
output_file = './text/【民法1】序論・行為能力と制限行為能力者制度・失踪宣告・法人・権利能力なき社団・権利の客体・法律行為.md'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(markdown_content)

output_file

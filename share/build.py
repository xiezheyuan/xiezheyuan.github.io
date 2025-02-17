import markdown
import jinja2
import os

files = []

for filename in os.listdir("./md"):
    if filename.endswith(".md"):
        files.append("md/" + filename)

def convert_markdown_to_html(file_path):
    with open(file_path, "r") as f:
        md_content = f.read()

    html_content = markdown.markdown(md_content, extensions=[
        "extra",
        "codehilite",
        "mdx_math"
    ], extension_configs={'mdx_math': {'enable_dollar_delimiter': True}})
    return html_content
# markdown.Markdown(extensions=['mdx_math'], extension_configs={'mdx_math': {'enable_dollar_delimiter': True}})

def generate_html_pages(files):
    template_loader = jinja2.FileSystemLoader(searchpath="./html")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("template.html")
    for file_path in files:
        html_content = convert_markdown_to_html(file_path)
        html_file_path = file_path.replace("md", "html")
        with open(html_file_path, "w") as f:
            f.write(template.render(content=html_content, name=html_file_path))
            print(f"HTML file generated: {html_file_path}")

for i in os.listdir("./html"):
    if i != "template.html" and i != "github.css":
        os.remove(f"./html/{i}")
generate_html_pages(files)

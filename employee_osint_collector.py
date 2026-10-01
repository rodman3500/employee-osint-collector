def load_html(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Could not find {filename}")
        return None


html = load_html("employee_directory.html")

if html is not None:
    print("HTML file loaded successfully.")
from bs4 import BeautifulSoup

def load_html(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: Could not find {filename}")
        return None

html = load_html("employee_results.html")

if html is not None:
    soup = BeautifulSoup(html, "html.parser")
    print(soup.title.get_text(strip=True))
    print("HTML file loaded successfully.")

    employees = soup.find_all("div", class_="employee-result")

    for employee in employees:
        name_tag = employee.find("h3", class_="emp-name-margin")
        title_tag = employee.find("p", class_="emp-title-margin")

        if name_tag and title_tag:
            name = name_tag.get_text(strip=True)
            title = title_tag.get_text(strip=True)

            print(name, "-", title)
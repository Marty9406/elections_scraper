import sys
import csv
import bs4
import requests


def get_file_name():
    file_name = sys.argv[2]
    if file_name and file_name.endswith(".csv"):
        return file_name
    else:
        print("Wrong file name. Terminating the program.")
        exit()


def get_main_page():
    main_page = requests.get(sys.argv[1])
    if sys.argv[1].startswith("https://volby.cz/pls/ps2017nss/") and main_page.status_code == 200:
        return bs4.BeautifulSoup(main_page.text, "html.parser")
    else:
        print("Something is wrong. Terminating the program.")
        exit()


def get_code_list(main_page):
    all_links = main_page.find_all("a")
    code_list = []
    link_list = []
    for link in all_links:
        if link.text.isnumeric():
            code_list.append(link.text)
            link_list.append("https://volby.cz/pls/ps2017nss/" + link["href"])
    return code_list, link_list


def get_header(preview_link):
    header = ["City code", "City name", "Eligible voters", "Issued envelopes", "Valid votes"]
    preview_page = requests.get(preview_link)
    preview_page_soup = bs4.BeautifulSoup(preview_page.text, "html.parser")
    for party in preview_page_soup.find_all("td")[10::5]:
        if party.text != "-":
            header.append(party.text)

    return header


def get_city_info(city_link, city_code):
    city_info = [city_code]
    city_page = requests.get(city_link)
    city_page_soup = bs4.BeautifulSoup(city_page.text, "html.parser")
    city_info.append(str(city_page_soup.find_all("h3")[len(city_page_soup.find_all("h3"))-3].text).split(":")[1].strip())  # add name of the city
    city_info.append("".join(str(city_page_soup.find_all("td")[3].text).split()))  # add number of eligible voters
    city_info.append("".join(str(city_page_soup.find_all("td")[4].text).split()))  # add number of issued envelopes
    city_info.append("".join(str(city_page_soup.find_all("td")[7].text).split()))  # add number of valid votes
    for parti in city_page_soup.find_all("td")[11::5]:
        if parti.text != "-":
            city_info.append(parti.text)

    return city_info


def main():
    main_page = get_main_page()
    print("Downloading data from URL:", sys.argv[1])
    code_list, link_list = get_code_list(main_page)
    header = get_header(link_list[0])
    with open(get_file_name(), "w", newline="") as file:
        print("Saving to file:", sys.argv[2])
        file_writer = csv.writer(file, delimiter=";")
        file_writer.writerow(header)
        for i in range(len(code_list)):
            file_writer.writerow(get_city_info(link_list[i], code_list[i]))
    print("Completed. Terminating the program.")


main()

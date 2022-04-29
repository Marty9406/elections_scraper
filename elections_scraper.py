"""
author:  Martin Rečka
email: martinrec@seznam.cz
discord: Martin Rečka#2020
"""

import sys
import csv
import bs4
import requests


def check_arguments():
    if len(sys.argv) < 3:
        print("Not enough arguments. Terminating the program.")
        exit()
    elif not sys.argv[1].startswith("https://volby.cz/pls/ps2017nss/ps3"):
        print("Wrong webpage. Terminating the program")
        exit()
    elif not sys.argv[2].endswith(".csv"):
        print("Wrong file suffix. Terminating the program.")
        exit()


def get_main_page():
    main_page = requests.get(sys.argv[1])
    if main_page.status_code == 200:
        return bs4.BeautifulSoup(main_page.text, "html.parser")
    else:
        print("Something is wrong. Terminating the program.")
        exit()


def get_code_list(main_page):
    continents = [
        "Evropa",
        "Asie",
        "Amerika",
        "Afrika",
        "Austrálie a Oceánie"
    ]
    code_list = []
    link_list = []
    all_links = main_page.find_all("a")
    for link in all_links:
        if link.text.isnumeric() and len(link.text) == 6 or link.text in continents:
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
    h3_number = len(city_page_soup.find_all("h3"))-3  # because of different number of h3 tags on Prague pages
    city_info.append(str(city_page_soup.find_all("h3")[h3_number].text).split(":")[1].strip())  # adds name of the city
    city_info.append("".join(str(city_page_soup.find_all("td")[3].text).split()))  # adds number of eligible voters
    city_info.append("".join(str(city_page_soup.find_all("td")[4].text).split()))  # adds number of issued envelopes
    city_info.append("".join(str(city_page_soup.find_all("td")[7].text).split()))  # adds number of valid votes
    for parti in city_page_soup.find_all("td")[11::5]:
        if parti.text != "-":  # because of empty lines in some tables
            city_info.append(parti.text)  # adds party results
    return city_info


def main():
    check_arguments()
    main_page = get_main_page()
    print("Downloading data from URL:", sys.argv[1])
    code_list, link_list = get_code_list(main_page)
    header = get_header(link_list[0])
    with open(sys.argv[2], "w", newline="") as file:
        print("Saving to file:", sys.argv[2])
        file_writer = csv.writer(file, delimiter=";")
        file_writer.writerow(header)
        for i in range(len(code_list)):
            file_writer.writerow(get_city_info(link_list[i], code_list[i]))
    print("Completed. Terminating the program.")


main()

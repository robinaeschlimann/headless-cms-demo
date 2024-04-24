import requests

BASE_URL = "http://localhost:8080"


def get_navigations():
    return requests.get(BASE_URL + "/api/de/v1/cms/navigations").json()


def get_navigation(navigation_id):
    return requests.get(BASE_URL + "/api/de/v1/cms/navigations/" + str(navigation_id)).json()


def get_pages(navigation_id):
    return requests.get(BASE_URL + "/api/de/v1/cms/navigations/" + str(navigation_id) + "/pages").json()


def get_layout_regions(navigation_id, page_id):
    return requests.get(BASE_URL + "/api/de/v1/cms/navigations/" + str(navigation_id) + "/pages/" +
                        str(page_id) + "/layoutregions").json()


def get_page_contents(navigation_id, page_id, layout_region_id):
    return requests.get(BASE_URL + "/api/de/v1/cms/navigations/" + str(navigation_id) + "/pages/" +
                            str(page_id) + "/layoutregions/" + str(layout_region_id) + "/content").json()


def get_navigation_contents(navigation_id, layout_region_id):
    return requests.get(BASE_URL + "/api/de/v1/cms/navigations/" + str(navigation_id) +"/layoutregions/" +
                        str(layout_region_id) + "/content").json()

import requests

""" Base url of the headless cms """
BASE_URL = "http://localhost:8080"


def get_navigations():
    """
    Get navigations from the headless cms
    :return: returns the response as json
    """
    return requests.get(f'{BASE_URL}/api/de/v1/cms/navigations').json()


def get_navigation(navigation_id):
    """
    Get a navigation by id
    :param navigation_id:
    :return: returns the response as a json
    """
    return requests.get(f'{BASE_URL}/api/de/v1/cms/navigations/{navigation_id}').json()


def get_pages(navigation_id):
    """
    Get pages of a navigation
    :param navigation_id: id of the navigation
    :return: returns the response as a json
    """
    return requests.get(f'{BASE_URL}/api/de/v1/cms/navigations/{navigation_id}/pages').json()


def get_layout_regions(navigation_id, page_id):
    """
    Get layout regions of a page
    :param navigation_id:
    :param page_id:
    :return: returns the response as a json
    """
    return requests.get(f'{BASE_URL}/api/de/v1/cms/navigations/{navigation_id}/pages/{page_id}/layoutregions').json()


def get_page_contents(navigation_id, page_id, layout_region_id):
    """
    Get contents of a page
    :param navigation_id:
    :param page_id:
    :param layout_region_id:
    :return: returns the response as a json
    """
    return requests.get(f'{BASE_URL}/api/de/v1/cms/navigations/{navigation_id}/pages/{page_id}/layoutregions/'
                        f'{layout_region_id}/content').json()


def get_navigation_contents(navigation_id, layout_region_id):
    """
    Get contents of a navigation
    :param navigation_id:
    :param layout_region_id:
    :return: returns the response as a json
    """
    return requests.get(f'{BASE_URL}/api/de/v1/cms/navigations/{navigation_id}/layoutregions/{layout_region_id}'
                        f'/content').json()

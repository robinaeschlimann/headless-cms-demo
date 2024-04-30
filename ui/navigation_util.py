from service import rest_client
import streamlit as st


def get_navigation_prefix(depth):
    """
    Returns a prefix for the navigation. The prefix is used to show the navigation in a structured way
    :param depth: the depth of the navigation
    :return:
    """
    prefix = ""
    for _ in range(depth):
        prefix += "\t__"

    return prefix


def get_navigation_select():
    """
    Get navigations from the headless cms and show them in a select box
    :return: returns the selected navigation
    """
    response = rest_client.get_navigations()

    navigation_dict = get_navigations(response, {})

    option = st.selectbox('Wähle eine Navigation aus', (list(navigation_dict.keys())))

    return navigation_dict[option]


def get_navigations(navigations, navigation_dict, depth=0):
    """
    Get all navigations and their subNavigations hierarchically
    :param navigations: list of navigations as json
    :param navigation_dict:
    :param depth: used to show the correct amount of prefixes
    :return: returns the complete navigation
    """

    if len(navigations) == 0:
        return navigation_dict

    for navigation in navigations:
        prefix = get_navigation_prefix(depth)
        navigation_dict[prefix + ' ' + navigation['title']] = navigation
        get_navigations(navigation['subNavigations'], navigation_dict, depth + 1)

    return navigation_dict


def show_navigation(navigation_id, show_navigation_horizontal):
    """
    shows the subNavigations of a navigation. Not hierarchically!
    :param navigation_id:
    :param show_navigation_horizontal: if true the navigation is shown horizontally otherwise vertically
    """
    navigation = rest_client.get_navigation(navigation_id)

    navigations = ""

    for sub_navigation in navigation['subNavigations']:

        html_link = '<a href="' + sub_navigation['url'] + '">' + sub_navigation['title'] + '</a> '

        if show_navigation_horizontal:
            navigations += html_link
        else:
            st.html(html_link)

    if show_navigation_horizontal:
        st.html(navigations)

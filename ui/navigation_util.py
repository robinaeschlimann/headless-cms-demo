from service import rest_client
import streamlit as st


def get_navigation_prefix(depth):
    prefix = ""
    for i in range(depth):
        prefix += "\t__"

    return prefix


def get_navigation_select():
    response = rest_client.get_navigations()

    navigation_dict = get_navigations(response, {})

    option = st.selectbox('Wähle eine Navigation aus', (list(navigation_dict.keys())))

    return navigation_dict[option]


def get_navigations(navigations, navigation_dict, depth=0):
    if len(navigations) == 0:
        return navigation_dict

    for navigation in navigations:
        prefix = get_navigation_prefix(depth)
        navigation_dict[prefix + ' ' + navigation['title']] = navigation
        get_navigations(navigation['subNavigations'], navigation_dict, depth + 1)

    return navigation_dict
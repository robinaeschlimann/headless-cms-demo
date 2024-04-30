from service import rest_client
import streamlit as st


def get_page_select(navigation_id):
    """
    Get pages of a navigation and show them in a select box
    :param navigation_id:
    :return: returns the selected page
    """
    response = rest_client.get_pages(navigation_id)

    page_dict = {}

    for page in response:
        page_dict[page['title']] = page

    selected_page = st.selectbox('Wähle eine Seite aus', (list(page_dict.keys())))

    if selected_page:
        return page_dict[selected_page]
    else:
        return None

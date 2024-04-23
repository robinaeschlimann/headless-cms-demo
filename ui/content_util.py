import streamlit as st

from ui import navigation_util
from ui import page_util

TEMPLATE_ID_TEXT = 24001
TEMPLATE_ID_BUTTON = 24002
TEMPLATE_ID_IMAGE = 24003
TEMPLATE_ID_VIDEO = 24004
TEMPLATE_ID_HERO = 24110

BASE_URL = "http://localhost:8080"


def show_title(title):
    st.title(title)


def show_sidebar():
    with st.sidebar:
        selected_navigation = navigation_util.get_navigation_select()

        navigation_id = selected_navigation['id']

        selected_page = page_util.get_page_select(navigation_id)

        show_navigation_layout_regions = st.checkbox("LayoutRegionen der Navigation anzeigen?", value=True)

    return {'selected_navigation': selected_navigation, 'selected_page': selected_page,
            'show_navigation_layout_regions': show_navigation_layout_regions}


def get_add_field(add_fields, id, default_value):
    for add_field in add_fields:
        if add_field['id'] == id:
            return add_field

    return {'id': id, 'value': default_value}


def show_images(content):
    images = content['images']

    for image in images:
        st.image(BASE_URL + image['url'])


def show_video(content):
    addfields = content['addfields']

    video_url = get_add_field(addfields, 0, None)['value']

    if not video_url:
        video_url = get_add_field(addfields, 1, None)['value']

    if video_url:
        loop = get_add_field(addfields, 4, False)['value']

        st.video('https://youtu.be/' + video_url, loop=bool(loop))


def show_button(content):
    addfields = content['addfields']
    button_text = get_add_field(addfields, 1, "Button")['value']
    button_link = get_add_field(addfields, 0, "/")['value']

    st.link_button(label=button_text, url=button_link)


def handle_contents(container):
    contents = container['contents']
    for content in contents:
        template_id = content['templateId']

        handle_content(content, template_id)


def show_text(content):
    text = content['text']

    if text:
        if content['images']:

            col1, col2 = st.columns(2)
            with col1:
                st.html(text)
            with col2:
                show_images(content)
        else:
            st.html(text)


def handle_content(content, template_id):
    if template_id == TEMPLATE_ID_TEXT:
        show_text(content)
    elif template_id == TEMPLATE_ID_BUTTON:
        show_button(content)
    elif template_id == TEMPLATE_ID_IMAGE:
        show_images(content)
    elif template_id == TEMPLATE_ID_VIDEO:
        show_video(content)
    elif template_id == TEMPLATE_ID_HERO:
        show_images(content)

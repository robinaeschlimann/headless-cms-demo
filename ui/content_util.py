import streamlit as st

from ui import navigation_util, layout_region_util
from ui import page_util

TEMPLATE_ID_TEXT = 24001
TEMPLATE_ID_BUTTON = 24002
TEMPLATE_ID_IMAGE = 24003
TEMPLATE_ID_VIDEO = 24004
TEMPLATE_ID_TEXT_MEDIA = 24100
TEMPLATE_ID_HERO = 24110
TEMPLATE_ID_CONTACT = 24150
TEMPLATE_ID_SOCIAL_MEDIA = 24151
TEMPLATE_ID_NAVIGATION = 24152

BASE_URL = "http://localhost:8080"


def show_title(title):
    st.title(title)


def show_sidebar():
    with st.sidebar:
        selected_navigation = navigation_util.get_navigation_select()

        navigation_id = selected_navigation['id']

        selected_page = page_util.get_page_select(navigation_id)

        show_structure = st.checkbox("Struktur anzeigen?", value=False)

        show_navigation_layout_regions = True

        if show_structure:
            show_navigation_layout_regions = st.checkbox("LayoutRegionen der Navigation anzeigen?", value=True)

    return {'selected_navigation': selected_navigation, 'selected_page': selected_page,
            'show_navigation_layout_regions': show_navigation_layout_regions, "show_structure": show_structure}


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


def show_social_media(content):
    addfields = content['addfields']
    social_media_links = [{'label': 'Facebook', 'link': get_add_field(addfields, 0, None)['value']},
                          {'label': 'Twitter', 'link': get_add_field(addfields, 1, None)['value']},
                          {'label': 'LinkedIn', 'link': get_add_field(addfields, 2, None)['value']},
                          {'label': 'Xing', 'link': get_add_field(addfields, 3, None)['value']},
                          {'label': 'Instagram', 'link': get_add_field(addfields, 4, None)['value']},
                          {'label': 'YouTube', 'link': get_add_field(addfields, 5, None)['value']}]

    for social_media_link in social_media_links:
        link = social_media_link['link']
        if link:
            st.page_link(page=link, label=social_media_link['label'])


def show_contact(content):
    addfields = content['addfields']
    title = get_add_field(addfields, 0, None)['value']

    contact_fields = [{'label': 'Firma', 'value': get_add_field(addfields, 1, None)['value']},
                     {'label': 'Adresse', 'value': get_add_field(addfields, 2, None)['value']},
                     {'label': 'Ort', 'value': get_add_field(addfields, 3, None)['value']},
                     {'label': 'Postfach', 'value': get_add_field(addfields, 4, None)['value']},
                     {'label': 'Email', 'value': get_add_field(addfields, 5, None)['value']},
                     {'label': 'Telefon', 'value': get_add_field(addfields, 6, None)['value']}]

    if title:
        st.markdown("<h3>" + title + "</h3>", unsafe_allow_html=True)

    contact = ""

    for contact_field in contact_fields:
        value = contact_field['value']
        if value:
            contact += value + "\n"

    st.text(contact)


def show_navigation(content):
    addfields = content['addfields']
    title = get_add_field(addfields, 0, None)['value']
    navigation_id = get_add_field(addfields, 1, None)['value']
    alignment = get_add_field(addfields, 2, 'vertical')['value']

    if navigation_id:
        if title:
            st.html('<h3>' + title + "<h3>")

        navigation_util.show_navigation(navigation_id, alignment=='horizontal')



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
    elif template_id == TEMPLATE_ID_SOCIAL_MEDIA:
        show_social_media(content)
    elif template_id == TEMPLATE_ID_CONTACT:
        show_contact(content)
    elif template_id == TEMPLATE_ID_NAVIGATION:
        show_navigation(content)
    elif template_id == TEMPLATE_ID_TEXT_MEDIA:
        show_text(content)


def show_page(navigation_id, page_id, page_title):
    layout_region_util.show_layout_region(navigation_id, page_id, 24920, False, False)
    show_title(page_title)
    layout_region_util.show_layout_region(navigation_id, page_id, 1, False, False)

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        layout_region_util.show_layout_region(navigation_id, page_id, 24900, False, True)
    with col2:
        layout_region_util.show_layout_region(navigation_id, page_id, 24901, False, True)
    with col3:
        layout_region_util.show_layout_region(navigation_id, page_id, 24902, False, True)

    st.divider()

    layout_region_util.show_layout_region(navigation_id, page_id, 24903, False, True)

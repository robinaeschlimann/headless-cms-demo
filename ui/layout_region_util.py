from service import rest_client
import streamlit as st

from ui import content_util


def show_layout_regions(navigation_id, page_id, show_navigation_layout_regions):
    for layout_region in rest_client.get_layout_regions(navigation_id, page_id):
        layout_region_id = layout_region['id']

        with st.expander(layout_region['title']):
            if show_navigation_layout_regions and layout_region['boundToNavigation']:
                containers = rest_client.get_navigation_contents(navigation_id, layout_region_id)
                handle_containers(containers)
            else:
                containers = rest_client.get_page_contents(navigation_id, page_id, layout_region_id)

                handle_containers(containers)


def handle_containers(containers):
    for container in containers:
        with st.container(border=True):
            content_util.handle_contents(container)

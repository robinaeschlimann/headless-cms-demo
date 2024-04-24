from service import rest_client
import streamlit as st

from ui import content_util


def show_layout_regions(navigation_id, page_id, show_navigation_layout_regions, show_container_border):
    for layout_region in rest_client.get_layout_regions(navigation_id, page_id):
        layout_region_id = layout_region['id']

        is_bound_to_navigation = layout_region['boundToNavigation']

        if not is_bound_to_navigation or show_navigation_layout_regions:
            with st.expander(layout_region['title']):

                show_layout_region(navigation_id, page_id, layout_region_id, show_container_border,
                                   is_bound_to_navigation)


def show_layout_region(navigation_id, page_id, layout_region_id, show_container_border, is_bound_to_navigation):

    if is_bound_to_navigation:
        containers = rest_client.get_navigation_contents(navigation_id, layout_region_id)
    else:
        containers = rest_client.get_page_contents(navigation_id, page_id, layout_region_id)

    handle_containers(containers, show_container_border)


def handle_containers(containers, show_container_border):
    for container in containers:
        with st.container(border=show_container_border):
            content_util.handle_contents(container)

from ui import content_util, layout_region_util

if __name__ == '__main__':

    sidebar_dict = content_util.show_sidebar()

    navigation_id = sidebar_dict['selected_navigation']['id']
    selected_page = sidebar_dict['selected_page']
    show_navigation_layout_regions = sidebar_dict['show_navigation_layout_regions']

    if selected_page:
        page_id = selected_page['id']
        content_util.show_title(selected_page['title'])
        layout_region_util.show_layout_regions(navigation_id, page_id, show_navigation_layout_regions)

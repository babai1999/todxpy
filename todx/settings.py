# -*- coding: utf-8 -*- 
status_aliases_dict = {
    'v': '☑',
    'x': '☒',
    ' ': '☐'
}

done_markers = ['v', '☑', 'x', '☒', 'o']

tag_marker = ''

version = '0.1.2'

modifiers = ['+', '#']

def status_aliases(status):
    if status in status_aliases_dict:
        return status_aliases_dict[status]
    return status

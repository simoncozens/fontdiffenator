

def cli_reporter(font_a, font_b, comp_data, output_lines=10):
    """Generate a report wip"""
    # TODO (m4rc1e): turn into decent report with good formatting.
    print '%s vs %s' % (font_a, font_b)
    for category in comp_data:
        for sub_category in comp_data[category]:
            if comp_data[category][sub_category]:
                print '\n***%s %s %s***' % (
                    category, len(comp_data[category][sub_category]), sub_category
                )
                if category == 'attribs' and sub_category == 'modified':
                    print dict_cli_table(
                        comp_data[category][sub_category][:output_lines],
                        ['table', 'attrib', 'value_a', 'value_b']
                    )
                elif category == 'metrics' and sub_category == 'modified':
                    print dict_cli_table(
                        comp_data[category][sub_category][:output_lines],
                        ['glyph', 'adv', 'lsb', 'rsb']
                    )
                elif category == 'kern':
                    print dict_cli_table(
                        comp_data[category][sub_category][:output_lines],
                        ['left', 'right', 'value']
                    )
                elif category == 'marks':
                    print dict_cli_table(
                        comp_data[category][sub_category][:output_lines],
                        ['base_glyph', 'base_x', 'base_y',
                         'mark_glyph', 'mark_x', 'mark_y']
                    )
                elif category == 'glyphs':
                    print dict_cli_table(
                        comp_data[category][sub_category][:output_lines],
                        ['glyph', 'value']
                    )
                elif category == 'input':
                    print dict_cli_table(
                        comp_data[category][sub_category][:output_lines],
                        ['glyph']
                    )
                else:
                    print dict_cli_table(comp_data[category][sub_category][:output_lines])
            else:
                print '\n***%s %s***' % (category, sub_category)
                print 'No differences'


def dict_cli_table(l, columns=None):
    """Output a cli friendly table from a list of dicts"""
    if not columns:
        columns = l[0].keys()
    t_format = "{:<20}" * len(columns)
    table = []
    table.append(t_format.format(*tuple(columns)))
    for row in l:
        assembled = []
        for h in columns:
            assembled.append(row[h])
        table.append(t_format.format(*tuple(assembled)))
    return '\n'.join(table)
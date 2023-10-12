def generate_rss_xml_sitemap(urls):
    xml_sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_sitemap += '<rss xmlns:dc="http://purl.org/dc/elements/1.1/" version="2.0" xml:base="https://pages.detective.io/">\n'
    xml_sitemap += '<channel>\n'
    xml_sitemap += '<title>pages detective</title>\n'
    xml_sitemap += '<link>https://pages.detective.io/</link>\n'
    xml_sitemap += '<description/>\n'
    xml_sitemap += '<language>en</language>\n'
    
    for url in urls:
        xml_sitemap += f'<item><title/><link>{url}</link><description/></item>\n'
    
    xml_sitemap += '</channel>\n'
    xml_sitemap += '</rss>\n'
    return xml_sitemap

def create_sitemaps(url_list, urls_per_sitemap):
    num_sitemaps = (len(url_list) + urls_per_sitemap - 1) // urls_per_sitemap
    for i in range(num_sitemaps):
        start_idx = i * urls_per_sitemap
        end_idx = min((i + 1) * urls_per_sitemap, len(url_list))
        sitemap_content = generate_rss_xml_sitemap(url_list[start_idx:end_idx])
        with open(f'amare{i + 1}.xml', 'w') as f:
            f.write(sitemap_content)

def main():
    with open('list.txt', 'r') as f:
        url_list = [line.strip() for line in f.readlines()]

    urls_per_sitemap = 60  # Set this to 60 for 60 URLs per sitemap
    create_sitemaps(url_list, urls_per_sitemap)
    print(f'{len(url_list)} URLs split into {len(url_list) // urls_per_sitemap + 1} sitemaps.')

if __name__ == '__main__':
    main()

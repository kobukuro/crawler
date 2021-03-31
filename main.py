from functions.web import web

if __name__ == '__main__':
    for i in range(19, 84):
        url = f'http://www.cngdwx.com/yiwenshangxi/sanguozhibaihuawen/190{i}.html'
        print(url)
        web_html = web.get_html(url)
        # print(web_html)
        soup = web.soup_analyze(web_html)
        div_items = soup.findAll('div', {'class': 'Layout no_bg no_bor'})
        # print(div_items)
        title = div_items[0].find('h1').text
        with open(f'result\\three_kingdoms\\{title}.txt', 'w', encoding='utf-8') as file:
            print(title)
            # print(div_items[0].text)
            all_text = div_items[0].text
            row_text = ''
            for i in range(len(all_text)):
                if i % 30 == 0:
                    file.write(row_text)
                    file.write('\n')
                    row_text = ''
                else:
                    row_text += all_text[i]
            if row_text != '':
                file.write(row_text)
            file.close()
            # print(all_text)

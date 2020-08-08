import scrapy

class TuoiTre(scrapy.Spider):
    name = 'TuoiTre'
    allowed_domains = ['tuoitre.vn']
    start_urls = ['https://tuoitre.vn/']
    count = 0
    def parse(self, response):
        if response.status == 200 and response.css('meta[property="og:type"]::attr("content")').get() == 'article':
            f = open('D:/PyCharm/CodePythyon/Tuoitre/TuoiTre.txt', 'a', encoding='utf8')

            Link = response.url
            f.write('[Bài viết] ' + Link.strip() + '\n')
            f.write('\n')

            for i in response.css('div.menu-category li.menu-li1'):
                category = i.css('a::text').get()
                f.write(str(category).strip() + ' || ')
            f.write('\n')
            f.write('\n')

            Time = response.css('div.date-time::text').get()
            f.write(str(Time).strip() + '\n')
            f.write('\n')

            Title = response.css('h1.article-title::text').get()
            f.write(str(Title).strip() + '\n')
            f.write('\n')

            SubTitle = response.css('h2.sapo::text').get()
            f.write(str(SubTitle).strip() + '\n')
            f.write('\n')

            for i in response.css('div.content.fck p'):
                content = ''.join(i.css('*::text').getall())
                f.write(content.strip() + '\n')

            f.write('\n')
            f.write('Tác giả:')
            Source = response.css('div.author::text').getall()
            f.write(str(Source).strip() + '\n')
            f.write('\n')

            f.write('Tags:')
            Tags = response.css('meta[property="article:tag"]::attr("content")').getall()
            f.write(str(Tags).strip() + '\n')
            f.write('\n')

            self.count += 1
            self.crawler.stats.set_value('CRAWL COUNT', self.count)

        yield from response.follow_all(css='a[href^="https://tuoitre.vn/"]::attr(href), a[href^="/"]::attr(href)', callback=self.parse)



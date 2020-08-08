# Mã nguồn : Python + Scrapy

##name :tên của spider và không được đặt các name giống nhau
##allowed_domains:vùng cho phép crawl dữ liệu
##start_urls:
##Hàm parse(self,response):hàm gọi để xử lý phản hồi được tải xuống và thực hiện các chức năng:
##Kiểm tra xem link đó có phải là link cần crawl không (tránh crawl các link rác)
Sau khi kiểm tra thì ghi lại :link, category, time, title, subtitle, content, source, tags ra file .tex
##yield from : cho phép chỉ tiến hành crawl trên các bài báo có dạng "https://tuoitre.vn/" hoặc "/" và callback lại parse

# Các công việc đã thực hiện được: lấy được link, category, thời gian, tiêu đề, tiêu đề con, nội dung, tác giả và tag của một bài viết.
# Kết quả : đã thu nhập được 13072 bài viết trừ trang https://tuoitre.vn/ và các bài viết được đặt trong file TuoiTre.txt nằm trong mục Tuoitre

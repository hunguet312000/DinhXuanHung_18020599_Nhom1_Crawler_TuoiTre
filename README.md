# Mã nguồn : Python + Scrapy
def parse(self, response) có 2 phần:
+) Phần đầu thực hiện kiểm tra xem link có phải là bài báo không. Nếu đúng thực hiện việc ghi : link, category, time, title, subtitle, content, source, tags ra file .text
+) Nếu không phải thì thực hiện việc gọi callback lại hàm parse. Và trong hàm yield chỉ chọn những link có dạng : "https://tuoitre.vn/" hoặc "/".
# Các công việc đã thực hiện được: lấy được link, category, thời gian, tiêu đề, tiêu đề con, nội dung, tác giả và tag của một bài viết.
# Kết quả : đã thu nhập được 13072 bài viết trừ trang https://tuoitre.vn/ và các bài viết được đặt trong file TuoiTre.txt nằm trong mục TuoiTre

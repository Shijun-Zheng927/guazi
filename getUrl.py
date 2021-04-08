# 京东 https://www.jd.com/
import time
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")

url="https://www.guazi.com/jn/buy/"
# driver = webdriver.PhantomJS(executable_path=r'D:\CodeData\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver = webdriver.Chrome()

goods_url_list=[]
driver.set_window_size(1920,1080)
# 进入主页
driver.get(url)
# print(driver.get(url))
# 在输入框输入搜索关键字并操作点击
# driver.find_element_by_id('key').send_keys(u'手机')
# driver.find_element_by_id("search").find_element_by_tag_name("button").click()
time.sleep(5)
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
# 获取搜索结果第1页商品详情页面的超链接
for good in driver.find_element_by_id("J_goodsList").find_elements_by_class_name("gl-item"):
    goods_url_list.append(good.find_element_by_class_name("p-img").find_element_by_tag_name("a").get_attribute("href"))
    print(good.find_element_by_class_name("p-img").find_element_by_tag_name("a").get_attribute("href"))
# 获取搜索结果第2-10页商品详情页面的超链接
for page_no in range(2,11):
    # 获取页面底部页面跳转相关元素
    bottom_pages = driver.find_element_by_id("J_bottomPage").find_elements_by_tag_name("a")
    # 判断页面跳转元素，获取各个分页商品详情页面的超链接
    for bottom_page in bottom_pages:
        if str(page_no)==bottom_page.text:
            bottom_page.click()
            time.sleep(5)
            for good in driver.find_element_by_id("J_goodsList").find_elements_by_class_name("gl-item"):
                goods_url_list.append(good.find_element_by_class_name("p-img").find_element_by_tag_name("a").get_attribute("href"))
                print(good.find_element_by_class_name("p-img").find_element_by_tag_name("a").get_attribute("href"))
            break
driver.quit()
goods_url_list=list(set(goods_url_list))

# 将商品详情超链接写入文件，方便后续获取商品详情数据
# jd_goods_urls=open("./jd_goods_urls.txt","w",encoding='utf-8')
jd_goods_urls = open("jd_urls.txt", "w", encoding='utf-8')
for good_url in goods_url_list:
    # jd_goods_urls.write(good_url + "\n")
    print(good_url, file=jd_goods_urls)
    print(good_url)
jd_goods_urls.close()


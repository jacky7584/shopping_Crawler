import requests
from bs4 import BeautifulSoup

url = "https://www.momoshop.com.tw/search/searchShop.jsp?keyword=%E5%AF%B5%E7%89%A9%E7%94%A8%E5%93%81&searchType=1&curPage=1&_isFuzzy=0&showType=chessboardType&serviceCode=MT01"

# 發送GET請求並獲取網頁內容
response = requests.get(url)

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(response.text, "html.parser")

# 在這裡根據網頁結構定位並提取所需資料
# 以下僅為示例程式碼，你可以根據實際需求進行修改

# 獲取商品列表
product_list = soup.find_all("div", class_="prdListArea")

# 逐一處理每個商品
for product in product_list:
    # 獲取商品名稱
    name = product.find("a", class_="prdName").text.strip()
    
    # 獲取商品價格
    price = product.find("span", class_="price").text.strip()
    
    # 印出商品資訊
    print("商品名稱:", name)
    print("商品價格:", price)
    print("-----------------------")

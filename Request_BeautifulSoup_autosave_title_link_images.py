import requests
from bs4 import BeautifulSoup

def create_request(page):
    if page ==1:
        url = "https://sc.chinaz.com/tupian/xiaomaotupian.html"
    else:
        url = "https://sc.chinaz.com/tupian/xiaomaotupian_%s.html"%page
    # print(url)

    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"}

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response

def download_content(response):

    soup = BeautifulSoup(response.text, "html.parser")
    pic_data = soup.find_all(name="div",class_ = "item")
    pic_list=[]
    for pic in pic_data:
        pic_info = {}
        pic_title = pic.find("div", class_="bot-div")
        if pic_title:
            pic_title = pic_title.a.text
        else:
            pic_title = "None"
        # print(pic_title)
        pic_info["pic_title"] = pic_title
        pic_url = "https:" + pic.img["data-original"]
        pic_info["pic_url"] = pic_url.strip()
        # print(f"pic Info: {pic_title}  {pic_url}")
        pic_list.append(pic_info)
    # print(pic_list)

        print(f"downloading image {pic_url}")
        response2 = requests.get(pic_url)
        with open("./catImg/" + pic_title + ".jpg","wb") as file: #save image (names)
            file.write(response2.content)
        print("***"*10)

if __name__ == "__main__":
    print("This is to download images from page to page")
    start_page = int(input("enter the start page #: "))
    end_page = int(input("enter the end page #: "))

    for page in range(start_page,end_page+1):
        # print(page)
        response = create_request(page) #step1
        download_content(response) #step2
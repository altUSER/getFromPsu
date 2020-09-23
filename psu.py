import requests
from bs4 import BeautifulSoup as bs
import re
from secret import id

def getTT(id):
    session = requests.Session()
    r = session.get("https://student.psu.ru/pls/stu_cus_et/stu.timetable", cookies={"session_id":id})
    content = r.text
    soup = bs(content, features="lxml")

    tt = []

    for day in soup.find_all("div", { "class" : "day" }):
        el_d = {"name": day.h3.text, "less": []}
        if "Пар нет!" in day.text:
            el_d = {"name": day.h3.text, "less": None}
        for less in day.find_all("tr"):
            dis = less.find("span", { "class" : "dis" })
            if dis == None:
                el_d["less"].append(None)
            else:
                el_d["less"].append(re.sub("^\s+|\n|\r|\s+$", '', dis.text))
        tt.append(el_d)

    return(tt)



print(getTT(id))

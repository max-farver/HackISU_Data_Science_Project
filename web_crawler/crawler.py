from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs
import time

url = 'http://catalog.iastate.edu/planofstudy/#collegeofliberalartsandsciencestext'

file = open("major_class.csv", "w")
headers = "College,Major,Class"
file.write(headers + "\n")

client = uReq(url)
page = client.read()
client.close()

soup = bs(page, "html.parser")

temp = soup.findAll("div", {"class", 'tab_content'})
colleges = temp[1:len(temp) - 1]
max = ""
print(len(colleges))
print(colleges[0])
count = 0
collegeCount = 1
templst = soup.findAll("ul", {"class","clearfix"})
templst = templst[0].findAll("a")

for college in colleges:
    collegeName = templst[collegeCount].text.strip().lower()
    if collegeName == "liberal arts and sciences":
        collegeName = "LAS"
    elif collegeName == "human sciences":
        collegeName = "H SCI"
    elif collegeName == "engineering":
        collegeName = "ENGR"
    elif collegeName == "design":
        collegeName = "DSGN"
    elif collegeName == "business":
        collegeName = "BUS"
    elif collegeName == "agriculture and life sciences":
        collegeName = "CALS"
    print(collegeName)
    majors = college.findAll("li")
    print(college['id'])
    print(len(majors))
    for majorli in majors:
        if count >= 20:
            time.sleep(3)
            count = 0
        major = majorli.findAll("a")
        print(major)
        majorName = major[0].text.strip().replace(",", "-")
        print("major name", majorName)
        print('http://catalog.iastate.edu' + str(major[0]['href']))
        client2 = uReq('http://catalog.iastate.edu' + str(major[0]['href']))
        page2 = client2.read()
        client2.close()

        soup2 = bs(page2, "html.parser")
        nonBreakSpace = u'\xa0'
        titles = soup2.findAll("title")
        print(titles[0].text.strip())
        lst = soup2.findAll("tr")
        print(len(lst))

        for temp in lst:

            classes = temp.findAll("td", {"class", "codecol"})
            print(len(classes))

            for cls in classes:
                className = cls.text.strip().replace(nonBreakSpace, " ")
                print(className)
                className = className.lower()
                className = className.replace("and lab", "")
                print(className)
                if not ("1" in className or "2" in className or "3" in className or "4" in className or "5" in className or "6" in className or "7" in className or "8" in className or "9" in className):
                    break
                if "3-6" in className:
                    index = className.find("3-6")
                    print("index of 3-6" + str(index))
                    className = className[:index]
                if "/" in className:
                    index = className.find("/")
                    print("index of /" + str(index))
                    className = className[:index]
                if "(" in className:
                    index = className.find("(")
                    print("index of (" + str(index))
                    className = className[:index]
                if "*" in className:
                    index = className.find("*")
                    print("index of *" + str(index))
                    className = className[:index]
                if "#" in className:
                    index = className.find("#")
                    print("index of #" + str(index))
                    className = className[:index]
                if className[len(className) - 1:] == 'l':
                    break
                if "&" in className:
                    index = className.find("&")
                    print("index of &" + str(index))
                    className = className[:index]
                    print(className)
                if "fall" in className:
                    index = className.find("fall")
                    print("index of fall" + str(index))
                    className = className[:index]
                    print(className)
                if "credits" in className:
                    index = className.find("credits")
                    print("index of credits" + str(index))
                    className = className[:index]
                    print(className)
                #SORRY FOR THIS IF STATEMENT
                if not("humanities" in className or "science" in className or "languages" in className or "elective" in className or "diversity" in className or "perspective" in className \
                        or "perspectives" in className or "additional" in className or "level" in className or "choice" in className or "or" in className or "," in className \
                        or "general" in className or "international" in className or "arts" in className or "humanites" in className or "select" in className or "course" in className \
                        or "advanced" in className or "culture" in className or "technical" in className or "humanity" in className or "chemistry" in className or "option" in className \
                        or "concentration" in className or "choose" in className or "speech" in className or "statistics" in className or "teacher" in className or "following" in className \
                        or "approved" in className or "sci" in className or "research" in className or "studio" in className or "approved" in className or "edu" in className or "and" in className \
                        or "communications" in className or "-" in className):
                    if len(className) > len(max):
                        max = className
                    file.write(collegeName + "," + majorName + "," + className.upper() + "\n" )


        count += 1
    collegeCount +=1

file.close()
print(max)
print("Done! XD")
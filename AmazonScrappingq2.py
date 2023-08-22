from time import  sleep  #IMPORTED TIME LIBERARY FOR SLEEP 
import csv               #HAVE TO COLLECT THE DATA IN CSV FILE


#THIS IS HOW OUR EXCEL SHEET WILL LOOK LIKE (PS:it would overwrite it)
headings=['TITLE','PRICE(INR)','RATING','RATING COUNTS','LINK']
with open("AmazonWebscarppeddata.csv","w",newline="",encoding="UTF8") as f:
    writer = csv.writer(f)    
    writer.writerow(headings)


from bs4 import BeautifulSoup as bs #To extract data from html 
import requests as re               #To request https\

#A SIMPLE FUNCTION TO GET RESPONSE AND DATA FROM THE HTTP SERVER USING REQUEST MODULE
def getdata(url):

    #header need to be useragent otherwise you cannot access amazon url
    headers1={'User-Agent': ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")}
    return re.get(url  , headers=headers1,timeout=35)    


def nextpage(data):
    temp=(data.find("div" ,class_="a-section a-text-center s-pagination-container")).find(class_="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator")
    try:    
        url ="https://www.amazon.in"+temp['href']  
        return url
    except: 
        pass

#url changes everytime for new page
url ="https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"

I=1
#We know we have to scrap this much page so a loop till that
while True:
    REALLYMAIN=[]

    print(f"Page number {I} IS BEING SCRAPPED.Please wait....... ")
    
    
    a=getdata(url)

    #prints respose if connected to the url
    print(a)
    data=a.text
    new_data=(bs(data , "html.parser"))


    # extract the major container we want:
    name=new_data.find_all("div",class_="sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col-12-of-24 s-list-col-right")

    #we loop through the container to get every information for each item
    for i in name:
        MAINDATA=[]

        #USED TRY AND EXCEPT J IN CASE IT THROWS ERROR IT WOULD BE FILLED WITH NA
        try:
            MAINDATA.append(i.find("span",class_="a-size-medium a-color-base a-text-normal").get_text()) #name of the element
        except:
            MAINDATA("NA")
        
        try:
            MAINDATA.append(i.find("span",class_="a-price-whole").get_text())  #price for the element
        except:
            MAINDATA("NA")
        

        redirectedlink="https://www.amazon.in"+(
            i.find("h2" ,
            class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2")
            ).find("a",
            class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" 
            )["href"]  #url link for the element


    # REVIEWS , COUNT REVIEWS : 
        try:
            review=i.find("div",class_="a-row a-size-small")
            
            for j in review:
                MAINDATA.append(j['aria-label'])      #GET US REVIEWS AND NUMBER OF REVIEWS
            MAINDATA.append(redirectedlink)           #NOTE WE APPENED every data in maindata firstly and then in reallymaind 
            
        except:
            pass

        REALLYMAIN.append(MAINDATA)

    #adding collected data to our csv file in UTF8 format so that it could be easily viewed in excel sheet
    with open("AmazonWebscarppeddata.csv","a",newline="",encoding="UTF8") as f: 
        writer = csv.writer(f)
        
        for i in REALLYMAIN: #writting data for each element one by one
            writer.writerow(i)
        
   
    print(I,"th page data added")
    if nextpage(new_data):
        url=nextpage(new_data)
    else:
        print("this was the last page")
        break
    I+=1   
    sleep(30) #used so that to get a time gap between request the html from the url again otherwise AMAZON COULD EVEN BLOCK OUR IP ADDRESS

print("EOF") #end of file

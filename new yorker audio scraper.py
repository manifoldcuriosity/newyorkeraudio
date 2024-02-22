from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException  
import time

DRIVER_PATH = 'C:/Users/Sean/Downloads/selenium-scraper/chromedriver_win32/'
driver = webdriver.Chrome()
##driver.set_window_size(1080,800);
driver.get('https://www.newyorker.com/magazine');

magazine = 0
CurrentArticle = 0
ArticleElementList = driver.find_elements_by_xpath("//a[.//h4]")
print(ArticleElementList)
print("Article Element List Made")
ArticleCount = len(ArticleElementList)
print("Article Element List Count is ", ArticleCount)
while magazine < 20:
    
    try:


        if CurrentArticle < ArticleCount:
            print("currently on magazine ", (magazine +1))
            time.sleep(2)
            ArticleElementList = driver.find_elements_by_xpath("//a[.//h4]")
            ArticleCount = len(ArticleElementList)
            print("Article Element List Count is ", ArticleCount)
            CurrentArticleElement = ArticleElementList[CurrentArticle]
            ArticleLinkString = CurrentArticleElement.get_attribute("href");
            print("navigating to article number ", (CurrentArticle + 1))
            print(ArticleLinkString)
            driver.get(ArticleLinkString);
            time.sleep(2);
            driver.execute_script("window.scrollTo(0, 450)") 
            time.sleep(2);
            driver.execute_script("document.body.style.zoom='.4'");
            time.sleep(2);

            

            try:
                player = driver.find_element_by_xpath('//iframe[@title="Embedded Frame"]');
                print("player found!");
                playerlink = player.get_attribute("src");
                print (playerlink);
                print ("navigating to player link");
                driver.get(playerlink);
                time.sleep(2);
            
                try:
                    driver.find_element_by_tag_name('button').click();
                    print("button found and clicked")
                    time.sleep(2);
                
                    try:
                        if "wync" in playerlink:
                            audiolink = (playerlink.replace('https://www.wnyc.org/widgets/ondemand_player/thenewyorker/#file=', ''))
                            
                        audioelement = driver.find_element_by_xpath("//video");
                        print("audio element found")
                        audiolink = audioelement.get_attribute("src");
                        print("audio link is ", audiolink);
                        ## if "wync" in playerlink:
                        ## grab poem audio from mp3? how?
                            
                        driver.get(audiolink);
                        
                        print("sound file downloaded! :) moving back to index")
                        time.sleep(2);
                        driver.back();
                        time.sleep(2);
                        driver.back();
                        CurrentArticle = CurrentArticle + 1
                        print("Current Article Count has changed to ", (CurrentArticle + 1))
                        
                    
                    except NoSuchElementException:
                        print("audio element could not be found :( moving back to index")
                        time.sleep(2);
                        driver.back();
                        time.sleep(2);
                        driver.back();
                        CurrentArticle = CurrentArticle + 1
                    
                except NoSuchElementException:
                    print("button could not be found :( moving back to index")
                    time.sleep(2);
                    driver.back();
                    time.sleep(2);
                    driver.back();
                    CurrentArticle = CurrentArticle + 1
                
                
            except NoSuchElementException:
                print("player link not found :( moving back to index")
                driver.back();
                CurrentArticle = CurrentArticle + 1
        else:
            magazine = magazine + 1
            print("navigating to next magazine")
            driver.find_element_by_xpath('//button[@class="Button__button___2vDCa Button__tertiary___1LRXQ  "]').click()
            CurrentArticle = 0
             
    except NoSuchElementException:
        print("could not acquire list of articles or maybe grab the right href link")

else:
    print("exited the loop")






                                                                                             

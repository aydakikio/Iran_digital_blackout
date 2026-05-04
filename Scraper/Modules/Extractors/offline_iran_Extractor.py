#Libararies
from bs4 import BeautifulSoup

#modules
from Scraper.Models.Experience_offline_iran import Experience_Data

class offline_iran_extractor:
    @staticmethod
    def extract_experiences(webpage_content:BeautifulSoup, scroll_numbers):

        experience_section = webpage_content.find("section", class_="space-y-10")
        if not experience_section:
            print("Error in finding the experience section!")
            return

        experiences = experience_section.find_all('div', class_='md:block', recursive=False)

        #Creating Filters the results
        start_index = scroll_numbers*20
        end_index = ((scroll_numbers+1)*20)

        #Iterate through the filtered list
        for I,experience in  enumerate(experiences[start_index:end_index]):
            print(f'Getting the {I}th experience')

            experience_text_wrapper = experience.find("p", class_="mb-2")
            if not experience_text_wrapper:
                return

            collapse_btn = experience_text_wrapper.find("button", attrs={"aria-label": "collapse"})
            if collapse_btn:
                collapse_btn.decompose()

            #Getting Sender name and date
            footer = experience.find("footer")
            if not footer:
                return

            #Creating data class
            experience_data:Experience_Data = Experience_Data()
            experience_data.experience_text = experience_text_wrapper.get_text()


            span_tags = footer.find_all('span')

            if len(span_tags) >= 2:
                name_spans = span_tags[:-1]
                experience_data.sender_name = ' '.join(span.get_text(strip=True) for span in name_spans)

                experience_data.published_date = span_tags[-1].get_text(strip=True).lstrip('، ')



            #attatchs the data class to an queue to f

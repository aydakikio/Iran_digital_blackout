#Modules
from Scraper.Offline_Iran.Models.Experience_offline_iran import Experience_Data

#Libararies
import jdatetime
import datetime

class database_manger:

    @staticmethod
    def parse_jalali_date(date_string: str) -> datetime:
        jalali_date = jdatetime.datetime.strptime(date_string, '%d %B %Y')
        return jalali_date.togregorian()

    @staticmethod
    def insert_experience(data:Experience_Data):
        date = database_manger.parse_jalali_date(data.published_date)

        print(date)
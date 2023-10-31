import config
import datetime
import re
import random
import string
from dateutil.parser import parse

class JJFPost:

    def __init__(self):
        self.name = ''
        self.post_date_str = ''
        self.post_date = ''
        self.post_id = ''
        self.desc = ''
        self.ext = ''
        self.full_text = ''
        self.title = ''
        self.type = ''
        self.photo_seq = -1

        self.url_vid = ''
        self.url_photo = []

        self.post_soup = {}

    def prepdata(self):
        match = re.search(r'([a-zA-Z]+\s\d+,\s\d+,\s\d+:\d+\s[apmAPM]+)', self.post_date_str)
        if match:
            clean_date_str = match.group(1)
            try:
                self.post_date = datetime.datetime.strptime(match.group(1), "%B %d, %Y, %I:%M %p").strftime("%Y-%m-%d")
            except Exception as e:
                print(f"Warning: Could not parse date for post {self.post_id}. Error: {e}. Using post ID as could not parse date.")
                self.post_date = self.post_id  # Using the whole post ID if the date cannot be parsed
        else:
            print(f"Warning: Could not parse date for post {self.post_id}. Using post ID as could not parse date.")
            self.post_date = self.post_id  # Using the whole post ID if the date cannot be parsed


        self.desc = self.full_text[0:50].strip() + ('...' if len(self.full_text) > 45 else '')
        self.desc = re.sub(r'["|/|\:|?|$|!|<|>|~|`|(|)|@|#|$|%|^|&|*|\n|\t|\r]', r'', self.desc)
        
        self.title = config.file_name_format \
            .replace('{name}', self.name) \
            .replace('{post_date}', self.post_date) \
            .replace('{post_id}', self.post_id) \
            .replace('{desc}', self.desc) \
            .replace('{ext}', self.ext)
        
        self.title = self.title.replace('{photo_seq}', '.' + str(self.photo_seq).zfill(2)) if self.photo_seq > -1 else self.title.replace('{photo_seq}', '')

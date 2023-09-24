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

        try:
            # Use regular expression to extract date and time
            date_match = re.search(r'(\w+ \d+, \d+, \d+:\d+ [APMapm]{2})', self.post_date_str)
            if date_match:
                clean_date_str = date_match.group(1)
                self.post_date = parse(clean_date_str).strftime("%Y-%m-%d")
            else:
                print(f"Could not parse date from string: {self.post_date_str}")
                self.post_date = 'unknown_date_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))  # Placeholder date with random characters
        except Exception as e:
            print(f"An error occurred while parsing the date: {e}")
            self.post_date = 'unknown_date_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))  # Placeholder date with random characters

        self.desc = self.full_text[0:50].strip() + ('...' if len(self.full_text) > 45 else '')
        self.desc = re.sub(r'["|/|\:|?|$|!|<|>|~|`|(|)|@|#|$|%|^|&|*|\n|\t|\r]', r'', self.desc)
        
        self.title = config.file_name_format \
            .replace('{name}', self.name) \
            .replace('{post_date}', self.post_date) \
            .replace('{post_id}', self.post_id[-5:]) \
            .replace('{desc}', self.desc) \
            .replace('{ext}', self.ext)
        
        self.title = self.title.replace('{photo_seq}', '.' + str(self.photo_seq).zfill(2)) if self.photo_seq > -1 else self.title.replace('{photo_seq}', '')

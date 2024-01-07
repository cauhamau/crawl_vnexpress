import argparse
import tqdm
from utils import get_urls_of_type, write_content
import json

article_type_dict = {
    0: "thoi-su",
    1: "the-gioi",
    2: "kinh-doanh",
    3: "bat-dong-san",
    4: "khoa-hoc",
    5: "giai-tri",
    6: "the-thao",
    7: "phap-luat",
    8: "giao-duc",
    9: "suc-khoe",
    10: "doi-song"
}

def crawl_urls(urls):
    index_len = len(str(len(urls)))
           
    contents = []
    with tqdm.tqdm(total=len(urls)) as pbar:
        for i, url in enumerate(urls):
            file_index = str(i+1).zfill(index_len)
            output_fpath = "".join(["/url_", file_index, ".txt"])
            content = write_content(url)
            if not content:
                print(url)
            else:
                contents.append(content)
            pbar.update(1)
    #contents = list({"title":title,"date":date,"description":description,"paragraphs":list(paragraphs)})
    return contents

def main(article_type=4, total_pages=1):

    return crawl_urls(get_urls_of_type(article_type, total_pages))
    

if __name__ == "__main__":
    for i in range(0,11):
        a = main(article_type=i, total_pages=100)
        with open(f'vnexpress\\vnexpress_{article_type_dict[i]}.jsonl', 'w', encoding='utf-8') as json_file:
            for i in a:
                json.dump(i, json_file, ensure_ascii=False)
                json_file.write('\n')
'''
article_type_dict = {
    0: "thoi-su",
    1: "the-gioi",
    2: "kinh-doanh",
    3: "bat-dong-san",
    4: "khoa-hoc",
    5: "giai-tri",
    6: "the-thao",
    7: "phap-luat",
    8: "giao-duc",
    9: "suc-khoe",
    10: "doi-song"
}
'''
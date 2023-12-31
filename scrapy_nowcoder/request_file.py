import random
import time
from datetime import datetime

import pandas
import requests

page_start = 0
page_size = 20

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
           "Cookie": "NOWCODERCLINETID=35920F903855AC538C6FDA13AE2BC230; NCOURSEFROM=202xuexi01; "
                     "NOWCODERQUERY=%E7%BB%8F%E7%BA%AC%E6%81%92%E6%B6%A6%3A%E5%90%AF%E6%98%8E%E6%98%9F%E8%BE%B0%3A%E5"
                     "%8D%8E%E4%B8%BAod%3A%E8%8B%8F%E5%AE%81Java%3A%E8%8B%8F%E5%AE%81; gray=0; hrId=329140; "
                     "node_gray=0; view_gray=0; gr_user_id=24e7a3a4-ddf0-4cb5-8efa-fc3132b49454; "
                     "c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=486941334; "
                     "NOWCODERUID=A9D62358FFC8AA6FD48F69013E7B82E5; "
                     "c196c3667d214851b11233f5c17f99d5_gr_session_id=4542d41c-90f4-4217-8295-fd3ca7e43387; "
                     "acw_tc=7d595fd6c8d0d5aafbb4018fb4e4b14c37eba9663d9be4373e90ddb615ada762; "
                     "isAgreementChecked=true; t=20978751EC9BCDF673E01B02D0C24D85; "
                     "c196c3667d214851b11233f5c17f99d5_gr_last_sent_sid_with_cs1=4542d41c-90f4-4217-8295-fd3ca7e43387"
                     "; c196c3667d214851b11233f5c17f99d5_gr_session_id_4542d41c-90f4-4217-8295-fd3ca7e43387=true; "
                     "c196c3667d214851b11233f5c17f99d5_gr_cs1=486941334"}


def crawl_nowcoder_recommend(page: int, size: int, cuid: str) -> dict:
    timestamp = int(datetime.now().timestamp() * 1000)
    response = requests.get(url=f"https://gw-c.nowcoder.com/api/sparta/home/recommend?"
                                f"page={page}&size={size}&cuid={cuid}&_={timestamp}", headers=headers,
                            timeout=10)

    json_data = response.json()
    records = json_data["data"]["records"]
    return records


frame = None
for i in range(0, 5):
    records_data = crawl_nowcoder_recommend(i, page_size, "24e7a3a4-ddf0-4cb5-8efa-fc3132b49454")
    time.sleep(random.randint(5, 15))
    if frame is None:
        frame = pandas.DataFrame(records_data)
    else:
        pandas.concat([frame, pandas.DataFrame(records_data)])
    for index in range(0, len(records_data)):
        user_brief = records_data[index]["userBrief"]
        print(records_data[index]["userId"], "\t", user_brief["nickname"], "\t", user_brief["authDisplayInfo"])

frame.to_csv("data.csv", encoding="utf_8_sig", index=True)

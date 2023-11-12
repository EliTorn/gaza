import requests as r
import json


def get_data():
    with open("data.json", "r") as f:
        links_json = json.load(f)
    return links_json


def update_json(data):
    with open("data_image.json", "w") as f:
        json.dump(data, f)


def get_into_web(page):
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "IR_4202=1699797202017%7C0%7C1699797202017%7C%7C; _fbp=fb.1.1699796925449.456246746; _ga=GA1.2.2139293330.1699796925; _ga_DMJJ3WT1SM=GS1.1.1699796925.1.1.1699797202.60.0.0; _gat_UA-85194766-1=1; _gid=GA1.2.1574749365.1699796925; gtm_ppn=category_browse; _gcl_au=1.1.797589898.1699796925; sp=es=newest&rps=open&ei=; unisess=WGgrb0hhTEZpaUxrTmpTUno1bDBZckUvWXkvdUpYbmZmdGxDOXBwYTFIdE5BVXNJaHNPS3phNm5xYUhVZkM4d2J4OTFnUEV1R3grbXFPd01SL2FQSlE9PS0tcU5jY1k2WXdUOXQ5NlpJazBLbkNLZz09--d1bd760c8acb3f103e1a4d4b0a4243f9a7d19ef8; csrf=t=UZMIF%2F6pY3NBq3DRcqa5gFFM6%2FeXMqARi7h2eAmIVDk%3D; ELOQUA=GUID=FFF2CBADE05F4B158D2F8408990DC99B; IR_gbd=gettyimages.com; vis=vid=d29d80f7-f829-48c7-8409-75e1093ede7c; giu=nv=1&lv=2023-11-12T13%3A48%3A41Z; uac=t=ASGr3Ffb0FsX2YfqWF5j36hpxxvBrsVy7Lwt%2FCAjlBJMYeRXiBzHfsyc8QxiH7NaYGRFDiOcvjVYT5KDSruFOzSXqWcNDgZWka3HEW7WaDrXyopMfaS9gblVn6tOyj68wqBL0LL046z0maMtqCdnSOVltPytaymj2HObNI5hBfo%3D%7C77u%2FTW5rOEI3RFB3ZDFNZE96MWVocFcKMTAwCgpPV2t5R0E9PQpRWEF5R0E9PQowCgoKMAoxMDAKCjEwMAowCmQyOWQ4MGY3LWY4MjktNDhjNy04NDA5LTc1ZTEwOTNlZGU3YwoK%7C3%7C1%7C1&d",
        "Host": "www.gettyimages.com",
        "Referer": f"https://www.gettyimages.com/photos/gaza?assettype=image&family=editorial&{page}=3&phrase=gaza&recency=last30days&sort=newest",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    }
    data = r.get(
        f"https://www.gettyimages.com/photos/gaza?assettype=image&family=editorial&page={page}&phrase=gaza&recency=last30days&sort=newest",
        headers=headers).json()
    return data


array = []


def get_all_data():
    for i in range(1, 101):
        data = get_into_web(i)
        array.append(data)
        print(i)

    with open("gaza.json", "w") as f:
        json.dump(array, f)


def get_all_image():
    for page in range(1, 1001):
        data = get_into_web(page)
        i = 0
        while True:
            if i < len(data["gallery"]["assets"]):
                # Get the thumbUrl of the asset at index i
                thumb_url = data["gallery"]["assets"][i]["thumbUrl"]
                print(i)
                array.append(thumb_url)
                i += 1
            else:
                # Handle the case where the list index is out of range
                print("The list index is out of range.")
                break

    update_json(array)

# // gallery.assets[0].thumbUrl
# // gallery.assets[1].thumbUrl
# gallery.assets[2].thumbUrl
# gallery.assets[59].thumbUrl

# get_all_image()

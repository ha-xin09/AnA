items = {
    "아오리사과": {
        "type": "과일",
        "description": "사과는 달콤하고 아삭한 과일입니다.",
        "price": 200000,
    },
    "블랙사파이어포도": {
        "type": "과일",
        "description": "퀸만먹을 수 있는 보석같은 과일.",
        "price": 900000,
    },
    "망고스틴": {
        "type": "과일",
        "description": "음~마싯다!",
        "price": 1000000,
    },
    "제주도에서 온 체리": {
        "type": "과일",
        "description": "제주도에서 구할 수 있는 멋진 과일 체리!",
        "price": 50000000,
    }
}
#for k in items.keys():
#   print(k)
#for k in items.values():
#    print(k)

#for k in items.keys():
#   print(k,":",items[k],"원")

for k in items.keys():
    item = items[k]
    print(f"{k}({item["type"]}): {item["price"]}원")
    print(f"ㄴ {item["description"]}")
 

#? Đệ quy
lstDemo = [
    {"id": 1,
     "value": [{"id": 2,
               "value": [{"id": 3,
                          "value": [{"id": 4,
                                     "value": []
                                     }]
                          }]
                }]
    },
    {
        "id": 5,
        "value": []
    }
]

def print_ds(dict):
    for item in dict:
        print(item["id"])
        if item["value"]:
            print_ds(item["value"])
            
print_ds(lstDemo)
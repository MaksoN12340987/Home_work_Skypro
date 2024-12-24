import src.widget, src.processing

if __name__ == "__main__":
    # print(src.widget.mask_account_card())
    # print(src.widget.mask_account_card())

    # print(src.processing.filter_by_state())
    print(src.processing.sort_by_date([
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-13T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-13T08:20:00.419441"}
    ], False))

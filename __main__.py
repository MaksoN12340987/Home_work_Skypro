import src.widget, src.processing

if __name__ == "__main__":
    test_1 = "Visa Platinum 7000792289606361"
    test_2 = "Счет 73654108430135874305"
    
    print(src.widget.mask_account_card(test_1))
    print(src.widget.mask_account_card(test_2))

    test_3 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-13T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-13T08:20:00.419441"}
    ]

    print(src.processing.filter_by_state(test_3, "CANCELED"))
    print(src.processing.sort_by_date(test_3, False))

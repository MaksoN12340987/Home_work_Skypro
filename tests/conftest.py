import pytest


@pytest.fixture
def card_number() -> str:
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def account_number() -> str:
    return "Счет 73654108430135874305"


# Test processind module
@pytest.fixture()
def input_list_to_filter() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Test fixture generators
@pytest.fixture
def log_operations():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def result_log_operations_usd():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


@pytest.fixture
def result_log_operations_rub():
    return [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def result_generator_card_number_1_4():
    return ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"]


@pytest.fixture
def result_discription():
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.fixture
def return_api():
    return {
        "date": "2025-01-14",
        "info": {"rate": 103.374534, "timestamp": 1736890683},
        "query": {"amount": 10, "from": "USD", "to": "RUB"},
        "result": 1033.74534,
        "success": "true",
    }


@pytest.fixture
def return_api_error():
    return "error"


@pytest.fixture
def operations_json():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 214024827,
            "state": "EXECUTED",
            "date": "2018-12-20T16:43:26.929246",
            "operationAmount": {"amount": "70946.18", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 10848359769870775355",
            "to": "Счет 21969751544412966366",
        },
        {
            "id": 522357576,
            "state": "EXECUTED",
            "date": "2019-07-12T20:41:47.882230",
            "operationAmount": {"amount": "51463.70", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 48894435694657014368",
            "to": "Счет 38976430693692818358",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215",
        },
        {
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472",
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
            "operationAmount": {"amount": "77751.04", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "Maestro 3928549031574026",
            "to": "Счет 84163357546688983493",
        },
        {
            "id": 147815167,
            "state": "EXECUTED",
            "date": "2018-01-26T15:40:13.413061",
            "operationAmount": {"amount": "50870.71", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "Maestro 4598300720424501",
            "to": "Счет 43597928997568165086",
        },
        {
            "id": 518707726,
            "state": "EXECUTED",
            "date": "2018-11-29T07:18:23.941293",
            "operationAmount": {"amount": "3348.98", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "MasterCard 3152479541115065",
            "to": "Visa Gold 9447344650495960",
        },
        {
            "id": 649467725,
            "state": "EXECUTED",
            "date": "2018-04-14T19:35:28.978265",
            "operationAmount": {"amount": "96995.73", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 27248529432547658655",
            "to": "Счет 97584898735659638967",
        },
        {
            "id": 782295999,
            "state": "EXECUTED",
            "date": "2019-09-11T17:30:34.445824",
            "operationAmount": {"amount": "54280.01", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 24763316288121894080",
            "to": "Счет 96291777776753236930",
        },
        {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {"amount": "90582.51", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319",
        },
        {
            "id": 558167602,
            "state": "EXECUTED",
            "date": "2019-04-12T17:27:27.896421",
            "operationAmount": {"amount": "43861.89", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 73654108430135874305",
            "to": "Счет 89685546118890842412",
        },
        {
            "id": 407169720,
            "state": "EXECUTED",
            "date": "2018-02-03T14:52:08.093722",
            "operationAmount": {"amount": "67011.26", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "MasterCard 4047671689373225",
            "to": "Maestro 3806652527413662",
        },
        {
            "id": 361044570,
            "state": "EXECUTED",
            "date": "2018-03-02T02:03:11.563721",
            "operationAmount": {"amount": "7484.91", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 96008924215040031147",
            "to": "Счет 30377212495530283001",
        },
        {
            "id": 536723678,
            "state": "EXECUTED",
            "date": "2018-06-12T07:17:01.311610",
            "operationAmount": {"amount": "26334.08", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Classic 4195191172583802",
            "to": "Счет 17066032701791012883",
        },
        {
            "id": 172864002,
            "state": "EXECUTED",
            "date": "2018-12-28T23:10:35.459698",
            "operationAmount": {"amount": "49192.52", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 96231448929365202391",
        },
        {
            "id": 476991061,
            "state": "CANCELED",
            "date": "2018-11-23T17:47:33.127140",
            "operationAmount": {"amount": "26971.25", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 7305799447374042",
            "to": "Maestro 3364923093037194",
        },
        {
            "id": 633268359,
            "state": "EXECUTED",
            "date": "2019-07-12T08:11:47.735774",
            "operationAmount": {"amount": "2631.44", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Gold 3589276410671603",
            "to": "Счет 96292138399386853355",
        },
        {
            "id": 988276204,
            "state": "EXECUTED",
            "date": "2018-02-22T00:40:19.984219",
            "operationAmount": {"amount": "71771.90", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 4956649687637418",
            "to": "Счет 90562872508279542248",
        },
        {
            "id": 888407131,
            "state": "EXECUTED",
            "date": "2019-09-29T14:25:28.588059",
            "operationAmount": {"amount": "45849.53", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 35421428450077339637",
            "to": "Счет 46723050671868944961",
        },
        {
            "id": 634356296,
            "state": "EXECUTED",
            "date": "2018-01-21T01:10:28.317704",
            "operationAmount": {"amount": "96900.90", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 33407225454123927865",
            "to": "Счет 79619011266276091215",
        },
        {
            "id": 34148726,
            "state": "EXECUTED",
            "date": "2018-11-23T23:52:36.999661",
            "operationAmount": {"amount": "79428.73", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 5355133159258236",
            "to": "Maestro 8045769817179061",
        },
        {
            "id": 970724427,
            "state": "CANCELED",
            "date": "2019-01-15T17:58:27.064377",
            "operationAmount": {"amount": "90688.44", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 2241653116508487",
            "to": "Счет 26494285169417058486",
        },
        {
            "id": 104807525,
            "state": "EXECUTED",
            "date": "2019-06-01T06:46:16.803326",
            "operationAmount": {"amount": "60888.63", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "МИР 8201420097886664",
            "to": "Счет 35116633516390079956",
        },
        {
            "id": 550607912,
            "state": "EXECUTED",
            "date": "2018-07-31T12:25:32.579413",
            "operationAmount": {"amount": "34380.08", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 8532498887072395",
            "to": "Счет 44238164562083919420",
        },
        {
            "id": 608117766,
            "state": "CANCELED",
            "date": "2018-10-08T09:05:05.282282",
            "operationAmount": {"amount": "77302.31", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 6527183396477720",
            "to": "Счет 38573816654581789611",
        },
        {
            "id": 484201274,
            "state": "EXECUTED",
            "date": "2019-04-11T23:10:21.514616",
            "operationAmount": {"amount": "62621.51", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "МИР 8193813157568899",
            "to": "МИР 9425591958944146",
        },
        {
            "id": 547682597,
            "state": "EXECUTED",
            "date": "2018-12-29T21:45:18.495053",
            "operationAmount": {"amount": "66263.93", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 77977573135347241529",
            "to": "Счет 33062909508148771891",
        },
        {
            "id": 811920303,
            "state": "EXECUTED",
            "date": "2019-06-14T19:37:49.044089",
            "operationAmount": {"amount": "63150.74", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 73222753239048295679",
            "to": "Счет 78544755774551298747",
        },
        {
            "id": 509645757,
            "state": "EXECUTED",
            "date": "2019-10-30T01:49:52.939296",
            "operationAmount": {"amount": "23036.03", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 7756673469642839",
            "to": "Счет 48943806953649539453",
        },
        {
            "id": 801684332,
            "state": "EXECUTED",
            "date": "2019-11-05T12:04:13.781725",
            "operationAmount": {"amount": "21344.35", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 77613226829885488381",
        },
        {
            "id": 122284694,
            "state": "EXECUTED",
            "date": "2019-08-08T21:58:06.688541",
            "operationAmount": {"amount": "98657.83", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 99668626339273709694",
            "to": "Счет 27219929444683698245",
        },
        {
            "id": 154927927,
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614",
            "operationAmount": {"amount": "30153.72", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 7810846596785568",
            "to": "Счет 43241152692663622869",
        },
        {
            "id": 743628025,
            "state": "EXECUTED",
            "date": "2018-06-04T06:59:55.424356",
            "operationAmount": {"amount": "978.31", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 54883981902864782073",
            "to": "Счет 61834060137088759145",
        },
        {
            "id": 743278119,
            "state": "EXECUTED",
            "date": "2018-10-15T08:05:34.061711",
            "operationAmount": {"amount": "51203.12", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "MasterCard 1435442169918409",
            "to": "Maestro 7452400219469235",
        },
        {
            "id": 871921546,
            "state": "EXECUTED",
            "date": "2019-02-14T03:09:23.006652",
            "operationAmount": {"amount": "47022.09", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Classic 6216537926639975",
            "to": "Счет 67667879435628279708",
        },
        {
            "id": 373912477,
            "state": "EXECUTED",
            "date": "2018-03-09T02:11:01.339352",
            "operationAmount": {"amount": "33249.01", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 7022985698476865",
            "to": "Счет 60979028617970883410",
        },
        {
            "id": 720751477,
            "state": "EXECUTED",
            "date": "2018-11-08T08:21:45.902633",
            "operationAmount": {"amount": "16872.46", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75743795418434298755",
            "to": "Счет 80785963509390811744",
        },
        {
            "id": 949194534,
            "state": "EXECUTED",
            "date": "2019-08-15T01:48:10.042554",
            "operationAmount": {"amount": "31222.43", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 65298957349197687907",
            "to": "Счет 38784565940893479418",
        },
        {
            "id": 260972664,
            "state": "EXECUTED",
            "date": "2018-01-23T01:48:30.477053",
            "operationAmount": {"amount": "2974.30", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 3414396880443483",
            "to": "Visa Gold 2684274847577419",
        },
        {
            "id": 317987878,
            "state": "EXECUTED",
            "date": "2018-01-13T13:00:58.458625",
            "operationAmount": {"amount": "55985.82", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 8906171742833215",
            "to": "Visa Platinum 6086997013848217",
        },
        {
            "id": 72122709,
            "state": "EXECUTED",
            "date": "2018-12-18T17:07:09.800800",
            "operationAmount": {"amount": "19683.25", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 86675623828180311969",
            "to": "Счет 15351391408911677994",
        },
        {
            "id": 242885401,
            "state": "EXECUTED",
            "date": "2019-07-08T00:08:32.986663",
            "operationAmount": {"amount": "10083.68", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 38427597486442637521",
            "to": "Счет 83889757415570699323",
        },
        {
            "id": 286706711,
            "state": "EXECUTED",
            "date": "2018-02-06T06:42:02.219233",
            "operationAmount": {"amount": "621.37", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "MasterCard 9175985085449563",
            "to": "Счет 82781399328834147668",
        },
        {
            "id": 108066781,
            "state": "EXECUTED",
            "date": "2019-06-21T12:34:06.351022",
            "operationAmount": {"amount": "25762.92", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 90817634362091276762",
        },
        {
            "id": 100392079,
            "state": "EXECUTED",
            "date": "2019-03-03T03:13:18.622393",
            "operationAmount": {"amount": "44493.45", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 6319351940209800",
            "to": "Счет 14073196441261107791",
        },
        {
            "id": 51314762,
            "state": "EXECUTED",
            "date": "2018-08-25T02:58:18.764678",
            "operationAmount": {"amount": "52245.30", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 4040551273087672",
            "to": "Visa Platinum 7825450883088021",
        },
        {
            "id": 464419177,
            "state": "CANCELED",
            "date": "2018-07-15T18:44:13.346362",
            "operationAmount": {"amount": "71024.64", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 9657499677062945",
            "to": "Счет 19213886662094884261",
        },
        {
            "id": 560813069,
            "state": "CANCELED",
            "date": "2019-12-03T04:27:03.427014",
            "operationAmount": {"amount": "17628.50", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "MasterCard 1796816785869527",
            "to": "Visa Classic 7699855375169288",
        },
        {
            "id": 894961746,
            "state": "EXECUTED",
            "date": "2019-08-04T20:17:25.443322",
            "operationAmount": {"amount": "2523.44", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 33721541831646393763",
            "to": "Счет 68774571780974952778",
        },
        {
            "id": 360577236,
            "state": "EXECUTED",
            "date": "2019-09-07T07:20:13.889610",
            "operationAmount": {"amount": "18536.73", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Maestro 4284341727554246",
            "to": "МИР 1582474475547301",
        },
        {
            "id": 285353808,
            "state": "EXECUTED",
            "date": "2018-08-06T16:22:54.643491",
            "operationAmount": {"amount": "82946.19", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 12189246980267075758",
        },
        {
            "id": 416017997,
            "state": "EXECUTED",
            "date": "2019-05-07T01:32:37.142797",
            "operationAmount": {"amount": "29033.65", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "МИР 4878656375033856",
            "to": "Maestro 6890749237669619",
        },
        {
            "id": 556488059,
            "state": "CANCELED",
            "date": "2019-05-17T01:50:00.166954",
            "operationAmount": {"amount": "74604.56", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "МИР 8021883699486544",
            "to": "Visa Gold 8702717057933248",
        },
        {
            "id": 74897425,
            "state": "EXECUTED",
            "date": "2019-02-08T09:09:35.038506",
            "operationAmount": {"amount": "62654.30", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 28429442875257789335",
            "to": "Счет 95473010446151855633",
        },
        {
            "id": 636137913,
            "state": "EXECUTED",
            "date": "2019-06-16T22:17:01.825020",
            "operationAmount": {"amount": "24260.78", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на счет",
            "from": "Visa Platinum 8990850370884895",
            "to": "Счет 15574304810835774010",
        },
        {
            "id": 813238385,
            "state": "EXECUTED",
            "date": "2018-05-04T03:29:30.253483",
            "operationAmount": {"amount": "22007.02", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на счет",
            "from": "MasterCard 3595832182277400",
            "to": "Счет 79697233246085035210",
        },
        {
            "id": 854048120,
            "state": "EXECUTED",
            "date": "2019-03-29T10:57:20.635567",
            "operationAmount": {"amount": "30234.99", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 1203921041964079",
            "to": "Счет 34616199494072692721",
        },
        {
            "id": 269462132,
            "state": "EXECUTED",
            "date": "2018-08-14T05:42:30.104666",
            "operationAmount": {"amount": "19010.50", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 18125798580985711166",
            "to": "Счет 98841213648056852372",
        },
        {
            "id": 692008409,
            "state": "CANCELED",
            "date": "2019-02-14T17:38:09.910336",
            "operationAmount": {"amount": "37044.95", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Classic 4610247282706784",
            "to": "Счет 63229171188548882700",
        },
        {
            "id": 431131847,
            "state": "EXECUTED",
            "date": "2018-05-05T01:38:56.538074",
            "operationAmount": {"amount": "56071.02", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "MasterCard 9454780748494532",
            "to": "Счет 51958934737718181351",
        },
        {
            "id": 15948212,
            "state": "EXECUTED",
            "date": "2018-12-23T11:47:52.403285",
            "operationAmount": {"amount": "47408.20", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "МИР 8665240839126074",
            "to": "Maestro 3000704277834087",
        },
        {
            "id": 114832369,
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890",
            "operationAmount": {"amount": "48150.39", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Classic 2842878893689012",
            "to": "Счет 35158586384610753655",
        },
        {
            "id": 176798279,
            "state": "CANCELED",
            "date": "2019-04-18T11:22:18.800453",
            "operationAmount": {"amount": "73778.48", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 90417871337969064865",
        },
        {
            "id": 482520625,
            "state": "EXECUTED",
            "date": "2019-11-13T17:38:04.800051",
            "operationAmount": {"amount": "62814.53", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 38611439522855669794",
            "to": "Счет 46765464282437878125",
        },
        {
            "id": 414894334,
            "state": "EXECUTED",
            "date": "2019-06-30T15:11:53.136004",
            "operationAmount": {"amount": "95860.47", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 59956820797131895975",
            "to": "Счет 43475624104328495820",
        },
        {},
        {
            "id": 509552992,
            "state": "EXECUTED",
            "date": "2019-04-19T12:02:30.129240",
            "operationAmount": {"amount": "81513.74", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Maestro 9171987821259925",
            "to": "МИР 2052809263194182",
        },
        {
            "id": 596914981,
            "state": "EXECUTED",
            "date": "2018-04-16T17:34:19.241289",
            "operationAmount": {"amount": "65169.27", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1813166339376336",
            "to": "Счет 97848259954268659635",
        },
        {
            "id": 200634844,
            "state": "CANCELED",
            "date": "2018-02-13T04:43:11.374324",
            "operationAmount": {"amount": "42210.20", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 33355011456314142963",
            "to": "Счет 45735917297559088682",
        },
        {
            "id": 879660146,
            "state": "EXECUTED",
            "date": "2018-07-22T07:42:32.953324",
            "operationAmount": {"amount": "92130.50", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 19628854383215954147",
            "to": "Счет 90887717138446397473",
        },
        {
            "id": 893507143,
            "state": "EXECUTED",
            "date": "2018-02-03T07:16:28.366141",
            "operationAmount": {"amount": "90297.21", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 37653295304860108767",
        },
        {
            "id": 710136990,
            "state": "CANCELED",
            "date": "2018-08-17T03:57:28.607101",
            "operationAmount": {"amount": "66906.45", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Maestro 1913883747791351",
            "to": "Счет 11492155674319392427",
        },
        {
            "id": 390558607,
            "state": "EXECUTED",
            "date": "2019-02-12T00:08:07.524972",
            "operationAmount": {"amount": "16796.95", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 72645194281643232984",
            "to": "Счет 95782287258966264115",
        },
        {
            "id": 902831954,
            "state": "EXECUTED",
            "date": "2018-04-22T17:01:46.885252",
            "operationAmount": {"amount": "84732.61", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 3530191547567121",
            "to": "Счет 46878338893256147528",
        },
        {
            "id": 86608620,
            "state": "EXECUTED",
            "date": "2019-08-16T04:23:41.621065",
            "operationAmount": {"amount": "6004.00", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "MasterCard 8826230888662405",
            "to": "Счет 96119739109420349721",
        },
        {
            "id": 232222017,
            "state": "EXECUTED",
            "date": "2018-07-06T22:32:10.495465",
            "operationAmount": {"amount": "37160.27", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 4062745111784804",
            "to": "Maestro 8602249654751155",
        },
        {
            "id": 280743947,
            "state": "EXECUTED",
            "date": "2018-09-27T14:26:24.629306",
            "operationAmount": {"amount": "45653.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 23177857685058835559",
            "to": "Счет 56363465303962313778",
        },
        {
            "id": 185048835,
            "state": "EXECUTED",
            "date": "2019-05-06T00:17:42.736209",
            "operationAmount": {"amount": "74895.83", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 27921306202254867520",
            "to": "Счет 49884962711830774470",
        },
        {
            "id": 422035015,
            "state": "EXECUTED",
            "date": "2019-02-27T03:59:25.921176",
            "operationAmount": {"amount": "69311.35", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "MasterCard 8847384717023026",
            "to": "Счет 85458008326755993377",
        },
        {
            "id": 917824439,
            "state": "EXECUTED",
            "date": "2019-07-18T12:27:13.355343",
            "operationAmount": {"amount": "82139.20", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 6942697754917688",
            "to": "МИР 2956603572573342",
        },
        {
            "id": 121646999,
            "state": "CANCELED",
            "date": "2018-06-08T16:14:59.936274",
            "operationAmount": {"amount": "91121.62", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 7552745726849311",
            "to": "Счет 34799481846914116850",
        },
        {
            "id": 816266176,
            "state": "CANCELED",
            "date": "2018-06-24T00:46:32.422648",
            "operationAmount": {"amount": "60030.73", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "МИР 6381702861749111",
            "to": "Счет 27804394774631586026",
        },
        {
            "id": 736942989,
            "state": "EXECUTED",
            "date": "2019-09-06T00:48:01.081967",
            "operationAmount": {"amount": "6357.56", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Visa Gold 3654412434951162",
            "to": "Счет 59986621134048778289",
        },
        {
            "id": 580054042,
            "state": "EXECUTED",
            "date": "2018-06-20T03:59:34.851630",
            "operationAmount": {"amount": "96350.51", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на счет",
            "from": "МИР 3766446452238784",
            "to": "Счет 86655182730188443980",
        },
        {
            "id": 619287771,
            "state": "EXECUTED",
            "date": "2019-08-19T16:30:41.967497",
            "operationAmount": {"amount": "81150.87", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 17691325653939384901",
            "to": "Счет 49304996510329747621",
        },
        {
            "id": 490100847,
            "state": "EXECUTED",
            "date": "2018-12-22T02:02:49.564873",
            "operationAmount": {"amount": "56516.63", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 8326537236216459",
            "to": "MasterCard 6783917276771847",
        },
        {
            "id": 179194306,
            "state": "EXECUTED",
            "date": "2019-05-19T12:51:49.023880",
            "operationAmount": {"amount": "6381.58", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "МИР 5211277418228469",
            "to": "Счет 58518872592028002662",
        },
        {
            "id": 27192367,
            "state": "CANCELED",
            "date": "2018-12-24T20:16:18.819037",
            "operationAmount": {"amount": "991.49", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 71687416928274675290",
            "to": "Счет 87448526688763159781",
        },
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412",
            "operationAmount": {"amount": "25780.71", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 26406253703545413262",
            "to": "Счет 20735820461482021315",
        },
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
            "operationAmount": {"amount": "92688.46", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265",
        },
        {
            "id": 957763565,
            "state": "EXECUTED",
            "date": "2019-01-05T00:52:30.108534",
            "operationAmount": {"amount": "87941.37", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 46363668439560358409",
            "to": "Счет 18889008294666828266",
        },
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {"amount": "97853.86", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612",
        },
    ]


@pytest.fixture
def output_execudet_json():
    return """
2019.08.26 Перевод организации
Maestro 1596 83** **** 5199 -> Счет **9589
Сумма: 31957.58 RUB

2019.07.03 Перевод организации
MasterCard 7158 30** **** 6758 -> Счет **5560
Сумма: 8221.37 USD

2018.06.30 Перевод организации
Счет **6952 -> Счет **6702
Сумма: 9824.07 USD

2018.03.23 Открытие вклада
 -> Счет **2431
Сумма: 48223.05 RUB

2019.04.04 Перевод со счета на счет
Счет **8542 -> Счет **4188
Сумма: 79114.93 USD

2019.03.23 Перевод со счета на счет
Счет **4719 -> Счет **1160
Сумма: 43318.34 RUB

2018.12.20 Перевод организации
Счет **5355 -> Счет **6366
Сумма: 70946.18 USD

2019.07.12 Перевод организации
Счет **4368 -> Счет **8358
Сумма: 51463.70 USD

2018.08.19 Перевод с карты на карту
Visa Classic 6831 98** **** 7658 -> Visa Platinum 8990 92** **** 5229
Сумма: 56883.54 USD

2018.07.11 Открытие вклада
 -> Счет **6215
Сумма: 79931.03 RUB

2018.04.04 Перевод организации
Visa Gold 5999 41** **** 6353 -> Счет **4472
Сумма: 40701.91 USD

2019.12.08 Открытие вклада
 -> Счет **5907
Сумма: 41096.24 USD

2018.01.26 Перевод с карты на счет
Maestro 4598 30** **** 4501 -> Счет **5086
Сумма: 50870.71 RUB

2018.11.29 Перевод с карты на карту
MasterCard 3152 47** **** 5065 -> Visa Gold 9447 34** **** 5960
Сумма: 3348.98 USD

2018.04.14 Перевод организации
Счет **8655 -> Счет **8967
Сумма: 96995.73 RUB

2019.09.11 Перевод организации
Счет **4080 -> Счет **6930
Сумма: 54280.01 USD

2018.10.14 Перевод организации
Visa Platinum 2256 48** **** 2539 -> Счет **9319
Сумма: 90582.51 USD

2019.04.12 Перевод со счета на счет
Счет **4305 -> Счет **2412
Сумма: 43861.89 USD

2018.02.03 Перевод с карты на карту
MasterCard 4047 67** **** 3225 -> Maestro 3806 65** **** 3662
Сумма: 67011.26 RUB

2018.03.02 Перевод организации
Счет **1147 -> Счет **3001
Сумма: 7484.91 USD

2018.06.12 Перевод организации
Visa Classic 4195 19** **** 3802 -> Счет **2883
Сумма: 26334.08 USD

2018.12.28 Открытие вклада
 -> Счет **2391
Сумма: 49192.52 USD

2019.07.12 Перевод организации
Visa Gold 3589 27** **** 1603 -> Счет **3355
Сумма: 2631.44 RUB

2018.02.22 Перевод организации
MasterCard 4956 64** **** 7418 -> Счет **2248
Сумма: 71771.90 USD

2019.09.29 Перевод со счета на счет
Счет **9637 -> Счет **4961
Сумма: 45849.53 USD

2018.01.21 Перевод со счета на счет
Счет **7865 -> Счет **1215
Сумма: 96900.90 RUB

2018.11.23 Перевод с карты на карту
Visa Platinum 5355 13** **** 8236 -> Maestro 8045 76** **** 9061
Сумма: 79428.73 USD

2019.06.01 Перевод с карты на счет
МИР 8201 42** **** 6664 -> Счет **9956
Сумма: 60888.63 RUB

2018.07.31 Перевод организации
MasterCard 8532 49** **** 2395 -> Счет **9420
Сумма: 34380.08 USD

2019.04.11 Перевод с карты на карту
МИР 8193 81** **** 8899 -> МИР 9425 59** **** 4146
Сумма: 62621.51 RUB

2018.12.29 Перевод организации
Счет **1529 -> Счет **1891
Сумма: 66263.93 RUB

2019.06.14 Перевод со счета на счет
Счет **5679 -> Счет **8747
Сумма: 63150.74 USD

2019.10.30 Перевод с карты на счет
Visa Gold 7756 67** **** 2839 -> Счет **9453
Сумма: 23036.03 RUB

2019.11.05 Открытие вклада
 -> Счет **8381
Сумма: 21344.35 RUB

2019.08.08 Перевод организации
Счет **9694 -> Счет **8245
Сумма: 98657.83 RUB

2019.11.19 Перевод организации
Maestro 7810 84** **** 5568 -> Счет **2869
Сумма: 30153.72 RUB

2018.06.04 Перевод организации
Счет **2073 -> Счет **9145
Сумма: 978.31 USD

2018.10.15 Перевод с карты на карту
MasterCard 1435 44** **** 8409 -> Maestro 7452 40** **** 9235
Сумма: 51203.12 USD

2019.02.14 Перевод организации
Visa Classic 6216 53** **** 9975 -> Счет **9708
Сумма: 47022.09 RUB

2018.03.09 Перевод с карты на счет
Visa Classic 7022 98** **** 6865 -> Счет **3410
Сумма: 33249.01 RUB

2018.11.08 Перевод организации
Счет **8755 -> Счет **1744
Сумма: 16872.46 USD

2019.08.15 Перевод организации
Счет **7907 -> Счет **9418
Сумма: 31222.43 RUB

2018.01.23 Перевод с карты на карту
Visa Classic 3414 39** **** 3483 -> Visa Gold 2684 27** **** 7419
Сумма: 2974.30 USD

2018.01.13 Перевод с карты на карту
Visa Classic 8906 17** **** 3215 -> Visa Platinum 6086 99** **** 8217
Сумма: 55985.82 USD

2018.12.18 Перевод со счета на счет
Счет **1969 -> Счет **7994
Сумма: 19683.25 USD

2019.07.08 Перевод со счета на счет
Счет **7521 -> Счет **9323
Сумма: 10083.68 USD

2018.02.06 Перевод организации
MasterCard 9175 98** **** 9563 -> Счет **7668
Сумма: 621.37 RUB

2019.06.21 Открытие вклада
 -> Счет **6762
Сумма: 25762.92 RUB

2019.03.03 Перевод с карты на счет
Visa Classic 6319 35** **** 9800 -> Счет **7791
Сумма: 44493.45 USD

2018.08.25 Перевод с карты на карту
Visa Classic 4040 55** **** 7672 -> Visa Platinum 7825 45** **** 8021
Сумма: 52245.30 USD

2019.08.04 Перевод со счета на счет
Счет **3763 -> Счет **2778
Сумма: 2523.44 RUB

2019.09.07 Перевод с карты на карту
Maestro 4284 34** **** 4246 -> МИР 1582 47** **** 7301
Сумма: 18536.73 RUB

2018.08.06 Открытие вклада
 -> Счет **5758
Сумма: 82946.19 RUB

2019.05.07 Перевод с карты на карту
МИР 4878 65** **** 3856 -> Maestro 6890 74** **** 9619
Сумма: 29033.65 USD

2019.02.08 Перевод организации
Счет **9335 -> Счет **5633
Сумма: 62654.30 USD

2019.06.16 Перевод с карты на счет
Visa Platinum 8990 85** **** 4895 -> Счет **4010
Сумма: 24260.78 USD

2018.05.04 Перевод с карты на счет
MasterCard 3595 83** **** 7400 -> Счет **5210
Сумма: 22007.02 USD

2019.03.29 Перевод с карты на счет
Visa Classic 1203 92** **** 4079 -> Счет **2721
Сумма: 30234.99 USD

2018.08.14 Перевод со счета на счет
Счет **1166 -> Счет **2372
Сумма: 19010.50 RUB

2018.05.05 Перевод с карты на счет
MasterCard 9454 78** **** 4532 -> Счет **1351
Сумма: 56071.02 RUB

2018.12.23 Перевод с карты на карту
МИР 8665 24** **** 6074 -> Maestro 3000 70** **** 4087
Сумма: 47408.20 USD

2019.12.07 Перевод организации
Visa Classic 2842 87** **** 9012 -> Счет **3655
Сумма: 48150.39 USD

2019.11.13 Перевод со счета на счет
Счет **9794 -> Счет **8125
Сумма: 62814.53 RUB

2019.06.30 Перевод со счета на счет
Счет **5975 -> Счет **5820
Сумма: 95860.47 RUB

2019.04.19 Перевод с карты на карту
Maestro 9171 98** **** 9925 -> МИР 2052 80** **** 4182
Сумма: 81513.74 RUB

2018.04.16 Перевод организации
Visa Platinum 1813 16** **** 6336 -> Счет **9635
Сумма: 65169.27 USD

2018.07.22 Перевод организации
Счет **4147 -> Счет **7473
Сумма: 92130.50 USD

2018.02.03 Открытие вклада
 -> Счет **8767
Сумма: 90297.21 RUB

2019.02.12 Перевод организации
Счет **2984 -> Счет **4115
Сумма: 16796.95 USD

2018.04.22 Перевод организации
Visa Platinum 3530 19** **** 7121 -> Счет **7528
Сумма: 84732.61 RUB

2019.08.16 Перевод с карты на счет
MasterCard 8826 23** **** 2405 -> Счет **9721
Сумма: 6004.00 RUB

2018.07.06 Перевод с карты на карту
Visa Classic 4062 74** **** 4804 -> Maestro 8602 24** **** 1155
Сумма: 37160.27 RUB

2018.09.27 Перевод организации
Счет **5559 -> Счет **3778
Сумма: 45653.70 RUB

2019.05.06 Перевод со счета на счет
Счет **7520 -> Счет **4470
Сумма: 74895.83 RUB

2019.02.27 Перевод с карты на счет
MasterCard 8847 38** **** 3026 -> Счет **3377
Сумма: 69311.35 RUB

2019.07.18 Перевод с карты на карту
Visa Platinum 6942 69** **** 7688 -> МИР 2956 60** **** 3342
Сумма: 82139.20 RUB

2019.09.06 Перевод организации
Visa Gold 3654 41** **** 1162 -> Счет **8289
Сумма: 6357.56 USD

2018.06.20 Перевод с карты на счет
МИР 3766 44** **** 8784 -> Счет **3980
Сумма: 96350.51 USD

2019.08.19 Перевод организации
Счет **4901 -> Счет **7621
Сумма: 81150.87 USD

2018.12.22 Перевод с карты на карту
Visa Gold 8326 53** **** 6459 -> MasterCard 6783 91** **** 1847
Сумма: 56516.63 USD

2019.05.19 Перевод организации
МИР 5211 27** **** 8469 -> Счет **2662
Сумма: 6381.58 USD

2018.03.09 Перевод организации
Счет **3262 -> Счет **1315
Сумма: 25780.71 RUB

2019.07.15 Открытие вклада
 -> Счет **2265
Сумма: 92688.46 USD

2019.01.05 Перевод со счета на счет
Счет **8409 -> Счет **8266
Сумма: 87941.37 RUB

2019.07.13 Перевод с карты на счет
Maestro 1308 79** **** 7170 -> Счет **8612
Сумма: 97853.86 RUB
"""


@pytest.fixture
def output_execudet_csv_filt_rub():
    return """
2021.07.08 Перевод с карты на карту
Visa 0773 09** **** 2450 -> Discover 8602 78** **** 0491
Сумма: 23182.0 RUB

2023.08.30 Перевод с карты на карту
Mastercard 3093 12** **** 8405 -> American Express 6950 00** **** 0411
Сумма: 18420.0 RUB

2021.12.03 Перевод со счета на счет
Счет **9601 -> Счет **6527
Сумма: 21574.0 RUB

2023.10.20 Перевод с карты на карту
American Express 5313 94** **** 6164 -> Discover 0329 77** **** 1288
Сумма: 31741.0 RUB

2022.03.25 Перевод организации
American Express 5289 34** **** 4249 -> Счет **7273
Сумма: 22818.0 RUB

2023.07.31 Перевод с карты на карту
American Express 6902 83** **** 4644 -> American Express 1368 44** **** 5273
Сумма: 11562.0 RUB

2022.05.31 Перевод организации
Visa 9698 31** **** 8820 -> Счет **1508
Сумма: 29532.0 RUB

2021.03.14 Перевод организации
Discover 8455 44** **** 7314 -> Счет **3739
Сумма: 12576.0 RUB

2022.04.24 Перевод с карты на карту
Mastercard 8817 38** **** 2795 -> Discover 3942 17** **** 6690
Сумма: 18125.0 RUB

2022.09.09 Перевод со счета на счет
Счет **3319 -> Счет **2541
Сумма: 20083.0 RUB

2022.08.07 Перевод с карты на карту
Discover 6574 69** **** 9422 -> Discover 4659 40** **** 8758
Сумма: 15333.0 RUB

2021.10.25 Перевод с карты на карту
Mastercard 7725 50** **** 1579 -> Discover 8189 48** **** 3162
Сумма: 18106.0 RUB

2023.08.25 Перевод со счета на счет
Счет **1423 -> Счет **2934
Сумма: 22833.0 RUB

2020.05.10 Перевод с карты на карту
Visa 7657 17** **** 6531 -> Mastercard 5442 62** **** 8510
Сумма: 29722.0 RUB

2020.03.10 Открытие вклада
nan -> Счет **4628
Сумма: 22131.0 RUB

2023.03.25 Перевод с карты на карту
Visa 3723 52** **** 9611 -> American Express 4201 11** **** 1655
Сумма: 16225.0 RUB

2023.01.26 Перевод со счета на счет
Счет **7605 -> Счет **0525
Сумма: 26980.0 RUB

2023.10.12 Перевод с карты на карту
Mastercard 4205 96** **** 8141 -> Mastercard 3182 66** **** 6884
Сумма: 29511.0 RUB

2023.05.13 Перевод с карты на карту
Discover 2343 95** **** 3158 -> American Express 8400 86** **** 3599
Сумма: 23989.0 RUB

2022.12.20 Перевод организации
Visa 1399 15** **** 6740 -> Счет **3905
Сумма: 21833.0 RUB

2023.02.08 Перевод с карты на карту
Visa 1563 07** **** 8104 -> Visa 6133 88** **** 8564
Сумма: 17867.0 RUB

2022.08.12 Перевод организации
Mastercard 0560 25** **** 3874 -> Счет **3522
Сумма: 26278.0 RUB

2023.08.28 Перевод со счета на счет
Счет **2472 -> Счет **4845
Сумма: 27895.0 RUB

2021.09.06 Перевод с карты на карту
Visa 7986 44** **** 2194 -> Visa 8862 36** **** 2151
Сумма: 33345.0 RUB

2023.06.17 Перевод с карты на карту
Mastercard 8924 43** **** 7202 -> Visa 5653 66** **** 2651
Сумма: 16143.0 RUB

2023.05.09 Перевод с карты на карту
American Express 0134 02** **** 7734 -> Mastercard 7974 41** **** 2242
Сумма: 15292.0 RUB

2021.06.26 Перевод с карты на карту
Visa 3057 94** **** 8198 -> Discover 4035 89** **** 9221
Сумма: 12545.0 RUB

2021.03.25 Перевод со счета на счет
Счет **1151 -> Счет **7279
Сумма: 34455.0 RUB

2021.09.15 Перевод со счета на счет
Счет **6580 -> Счет **8517
Сумма: 32900.0 RUB

2023.01.08 Перевод с карты на карту
American Express 9171 90** **** 6946 -> Visa 1486 89** **** 2527
Сумма: 34114.0 RUB

2021.07.10 Открытие вклада
nan -> Счет **5996
Сумма: 27596.0 RUB

2021.11.21 Перевод с карты на карту
Mastercard 4061 23** **** 3434 -> Visa 7539 82** **** 7635
Сумма: 12868.0 RUB

2020.06.12 Перевод с карты на карту
Discover 8926 69** **** 3176 -> Discover 9331 95** **** 1046
Сумма: 32753.0 RUB

2023.08.05 Перевод с карты на карту
Mastercard 9458 11** **** 2215 -> Visa 6335 85** **** 6628
Сумма: 30065.0 RUB
"""


@pytest.fixture
def output_execudet_xlsx_filt_rub():
    return """
2021.07.08 Перевод с карты на карту
Visa 0773 09** **** 2450 -> Discover 8602 78** **** 0491
Сумма: 23182.0 RUB

2023.08.30 Перевод с карты на карту
Mastercard 3093 12** **** 8405 -> American Express 6950 00** **** 0411
Сумма: 18420.0 RUB

2021.12.03 Перевод со счета на счет
Счет **9601 -> Счет **6527
Сумма: 21574.0 RUB

2023.10.20 Перевод с карты на карту
American Express 5313 94** **** 6164 -> Discover 0329 77** **** 1288
Сумма: 31741.0 RUB

2022.03.25 Перевод организации
American Express 5289 34** **** 4249 -> Счет **7273
Сумма: 22818.0 RUB

2023.07.31 Перевод с карты на карту
American Express 6902 83** **** 4644 -> American Express 1368 44** **** 5273
Сумма: 11562.0 RUB

2022.05.31 Перевод организации
Visa 9698 31** **** 8820 -> Счет **1508
Сумма: 29532.0 RUB

2021.03.14 Перевод организации
Discover 8455 44** **** 7314 -> Счет **3739
Сумма: 12576.0 RUB

2022.04.24 Перевод с карты на карту
Mastercard 8817 38** **** 2795 -> Discover 3942 17** **** 6690
Сумма: 18125.0 RUB

2022.09.09 Перевод со счета на счет
Счет **3319 -> Счет **2541
Сумма: 20083.0 RUB

2022.08.07 Перевод с карты на карту
Discover 6574 69** **** 9422 -> Discover 4659 40** **** 8758
Сумма: 15333.0 RUB

2021.10.25 Перевод с карты на карту
Mastercard 7725 50** **** 1579 -> Discover 8189 48** **** 3162
Сумма: 18106.0 RUB

2023.08.25 Перевод со счета на счет
Счет **1423 -> Счет **2934
Сумма: 22833.0 RUB

2020.05.10 Перевод с карты на карту
Visa 7657 17** **** 6531 -> Mastercard 5442 62** **** 8510
Сумма: 29722.0 RUB

2020.03.10 Открытие вклада
nan -> Счет **4628
Сумма: 22131.0 RUB

2023.03.25 Перевод с карты на карту
Visa 3723 52** **** 9611 -> American Express 4201 11** **** 1655
Сумма: 16225.0 RUB

2023.01.26 Перевод со счета на счет
Счет **7605 -> Счет **0525
Сумма: 26980.0 RUB

2023.10.12 Перевод с карты на карту
Mastercard 4205 96** **** 8141 -> Mastercard 3182 66** **** 6884
Сумма: 29511.0 RUB

2023.05.13 Перевод с карты на карту
Discover 2343 95** **** 3158 -> American Express 8400 86** **** 3599
Сумма: 23989.0 RUB

2022.12.20 Перевод организации
Visa 1399 15** **** 6740 -> Счет **3905
Сумма: 21833.0 RUB

2023.02.08 Перевод с карты на карту
Visa 1563 07** **** 8104 -> Visa 6133 88** **** 8564
Сумма: 17867.0 RUB

2022.08.12 Перевод организации
Mastercard 0560 25** **** 3874 -> Счет **3522
Сумма: 26278.0 RUB

2023.08.28 Перевод со счета на счет
Счет **2472 -> Счет **4845
Сумма: 27895.0 RUB

2021.09.06 Перевод с карты на карту
Visa 7986 44** **** 2194 -> Visa 8862 36** **** 2151
Сумма: 33345.0 RUB

2023.06.17 Перевод с карты на карту
Mastercard 8924 43** **** 7202 -> Visa 5653 66** **** 2651
Сумма: 16143.0 RUB

2023.05.09 Перевод с карты на карту
American Express 0134 02** **** 7734 -> Mastercard 7974 41** **** 2242
Сумма: 15292.0 RUB

2021.06.26 Перевод с карты на карту
Visa 3057 94** **** 8198 -> Discover 4035 89** **** 9221
Сумма: 12545.0 RUB

2021.03.25 Перевод со счета на счет
Счет **1151 -> Счет **7279
Сумма: 34455.0 RUB

2021.09.15 Перевод со счета на счет
Счет **6580 -> Счет **8517
Сумма: 32900.0 RUB

2023.01.08 Перевод с карты на карту
American Express 9171 90** **** 6946 -> Visa 1486 89** **** 2527
Сумма: 34114.0 RUB

2021.07.10 Открытие вклада
nan -> Счет **5996
Сумма: 27596.0 RUB

2021.11.21 Перевод с карты на карту
Mastercard 4061 23** **** 3434 -> Visa 7539 82** **** 7635
Сумма: 12868.0 RUB

2020.06.12 Перевод с карты на карту
Discover 8926 69** **** 3176 -> Discover 9331 95** **** 1046
Сумма: 32753.0 RUB

2023.08.05 Перевод с карты на карту
Mastercard 9458 11** **** 2215 -> Visa 6335 85** **** 6628
Сумма: 30065.0 RUB
"""

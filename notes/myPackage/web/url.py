def get_movie(itemPerPage=10, **kwargs):
    if itemPerPage not in range(1, 11):
        return 'Enter a number between 1 ~ 10.'

    if 'key' not in kwargs or 'targetDt' not in kwargs:
        return 'Input essential keywords.'

    URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    URL += f'itemPerPage={itemPerPage}&'
    for key, value in kwargs.items():
        URL += f'{key}={value}&'

    return URL

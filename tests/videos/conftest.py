import pytest


@pytest.fixture
def theme_data():
    '''
    Return valid theme data
    '''
    return {
        'name': 'Science',
    }


@pytest.fixture
def video_data():
    '''
    Return valid video data
    '''
    return {
        'title': 'Is Your Red The Same as My Red?',
        'url': 'https://www.youtube.com/watch?v=evQsOFQju08',
        'date_uploaded': '2017-07-01',
        'views': '100',
    }

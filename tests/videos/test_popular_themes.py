from datetime import datetime, timedelta

import pytest
from model_mommy import mommy


@pytest.mark.django_db
class TestTheme:
    '''
    Suite of tests for popular themes listing feature
    '''

    def test_popular_themes_list_by_metrics(self, client):
        '''
        Check if view returns themes correctly according metrics
        '''
        date_uploaded = datetime.now().date()

        # Create a great video
        good_theme = mommy.make('videos.Theme', name='Good theme')
        good_video = mommy.make(
            'videos.Video', date_uploaded=date_uploaded, views=1000,
            themes=[good_theme])

        mommy.make(
            'videos.Thumb', video=good_video, is_positive=True,
            _quantity=2)
        mommy.make(
            'videos.Comment', video=good_video, is_positive=True,
            _quantity=2)

        # Create a medium video
        medium_theme = mommy.make('videos.Theme', name='Medium theme')
        medium_video = mommy.make(
            'videos.Video', date_uploaded=date_uploaded, views=1000,
            themes=[medium_theme])

        mommy.make('videos.Thumb', video=medium_video, is_positive=True)
        mommy.make('videos.Thumb', video=medium_video, is_positive=False)
        mommy.make('videos.Comment', video=medium_video, is_positive=True)
        mommy.make('videos.Comment', video=medium_video, is_positive=False)

        # Create a bad video
        bad_theme = mommy.make('videos.Theme', name='Bad theme')
        bad_video = mommy.make(
            'videos.Video', date_uploaded=date_uploaded, views=1000,
            themes=[bad_theme])
        mommy.make(
            'videos.Thumb', video=bad_video, is_positive=False, _quantity=2)
        mommy.make(
            'videos.Comment', video=bad_video, is_positive=False, _quantity=2)

        resp = client.get('/videos/get_popular_themes/')

        # Assert order
        object_list = resp.context['object_list']

        assert object_list[0] == good_theme
        assert object_list[1] == medium_theme
        assert object_list[2] == bad_theme

    def test_popular_themes_list_by_views(self, client):
        '''
        Check if view returns themes correctly according views quantity
        '''
        date_uploaded = datetime.now().date()

        # Create a great video
        good_theme = mommy.make('videos.Theme', name='Good theme')
        good_video = mommy.make(
            'videos.Video', date_uploaded=date_uploaded, views=1000,
            themes=[good_theme])

        mommy.make('videos.Thumb', video=good_video, is_positive=True)
        mommy.make('videos.Comment', video=good_video, is_positive=True)

        # Create a medium video
        medium_theme = mommy.make('videos.Theme', name='Medium theme')
        medium_video = mommy.make(
            'videos.Video', date_uploaded=date_uploaded, views=900,
            themes=[medium_theme])

        mommy.make('videos.Thumb', video=medium_video, is_positive=True)
        mommy.make('videos.Comment', video=medium_video, is_positive=True)

        # Create a bad video
        bad_theme = mommy.make('videos.Theme', name='Bad theme')
        bad_video = mommy.make(
            'videos.Video', date_uploaded=date_uploaded, views=800,
            themes=[bad_theme])

        mommy.make('videos.Thumb', video=bad_video, is_positive=True)
        mommy.make('videos.Comment', video=bad_video, is_positive=True)

        resp = client.get('/videos/get_popular_themes/')

        # Assert order
        object_list = resp.context['object_list']

        assert object_list[0] == good_theme
        assert object_list[1] == medium_theme
        assert object_list[2] == bad_theme

    def test_popular_themes_list_by_date(self, client):
        '''
        Check if view returns themes correctly according uploaded date order
        '''
        today = datetime.now().date()
        thirty_days_ago = datetime.now().date() - timedelta(days=60)
        one_hundred_days_ago = datetime.now().date() - timedelta(days=100)

        # Create a great video
        good_theme = mommy.make('videos.Theme', name='Good theme')
        good_video = mommy.make(
            'videos.Video', date_uploaded=today, views=1000,
            themes=[good_theme])

        mommy.make('videos.Thumb', video=good_video, is_positive=True)
        mommy.make('videos.Comment', video=good_video, is_positive=True)

        # Create a medium video
        medium_theme = mommy.make('videos.Theme', name='Medium theme')
        medium_video = mommy.make(
            'videos.Video', date_uploaded=thirty_days_ago, views=1000,
            themes=[medium_theme])

        mommy.make('videos.Thumb', video=medium_video, is_positive=True)
        mommy.make('videos.Comment', video=medium_video, is_positive=True)

        # Create a bad video
        bad_theme = mommy.make('videos.Theme', name='Bad theme')
        bad_video = mommy.make(
            'videos.Video', date_uploaded=one_hundred_days_ago, views=1000,
            themes=[bad_theme])

        mommy.make('videos.Thumb', video=bad_video, is_positive=True)
        mommy.make('videos.Comment', video=bad_video, is_positive=True)

        resp = client.get('/videos/get_popular_themes/')

        # Assert order
        object_list = resp.context['object_list']

        assert object_list[0] == good_theme
        assert object_list[1] == medium_theme
        assert object_list[2] == bad_theme

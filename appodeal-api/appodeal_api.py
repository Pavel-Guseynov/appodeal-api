import requests
from http_build_query import http_build_query


ROOT_URL = 'https://www.appodeal.com'


class Error(Exception):
    pass


class AppodealClient(object):

    def __init__(self, api_key, user_id):
        self.api_key = api_key
        self.user_id = user_id

    def call(self, action, params=None):
        _params = {
            'api_key': self.api_key,
            'user_id': self.user_id
        }
        if params:
            _params.update(params)
        query_string = http_build_query(_params)

        url = '{root_url}/api/v3/{action}?{qs}'.format(root_url=ROOT_URL, action=action, qs=query_string)

        r = requests.get(url)

        return r.json()

    def stats_api(self, date_from, date_to, detalisation=None, app=None, country=None, network=None,
                  include_shared_apps=False):
        """
        Args:
            date_from: the first date to include statistics for. This parameter is mandatory and should be in format 'YYYY-mm-dd'

            date_to: the last date to include statistics for. This parameter is mandatory and should be in format 'YYYY-mm-dd'. It cannot be less then date_from

            detalisation:
                date - Split the statistics by dates.
                app - Split the statistics by applications. You'll have application keys in the output.
                country - Split the statistics by countries. You'll have country code in the output.
                network - Split the statistics by networks. You'll have network names in the output (the same as for network parameter).
                banner_type - Split the statistics by ad types. (interstitial, video, baner, native, mrec, rewarded video).
                segment - Split the statistics by segments.
                placement - Split the statistics by placements.

            app: the application key to get statistics for or ALL. If omitted - statistics for all your and shared for you applications is calculated. You may use one per request

            country: the country ISO 2-characters code or ALL. The default is ALL - includes the statistics for all countries. You may use one per request

            network:  the network you want to get statistics for. Possible values are (you may use several per request)
                adcolony - include only AdColony data into the resulting statistics
                admob - include only AdMob data into the resulting statistics
                amazon_ads - include only Amazon Ads data into the resulting statistics
                applovin - include only Applovin data into the resulting statistics
                appodeal - include only Appodeal data into the resulting statistics
                chartboost - include only Chartboost data into the resulting statistics
                heyzap - include only HeyZap data into the resulting statistics
                smaato - include only Smaato data into the resulting statistics
                unity - include only Unity Ads data into the resulting statistics
                vungle - include only Vungle data into the resulting statistics
                mailru - include only Mail.ru data into the resulting statistics
                facebook - include only Facebook data into the resulting statistics
                inmobi - include only Inmobi data into the resulting statistics
                yandex - include only Yandex data into the resulting statistics
                startapp - include only StartApp data into the resulting statistics
                liverail - include only Liverail data into the resulting statistics
                flurry - include only Flurry data into the resulting statistics
                avocarrot - include only Avocarrot data into the resulting statistics
                pubnative - include only PubNative data into the resulting statistics
                millenium - include only Millenial Media data into the resulting statistics
                spotx - include only SpotX data into the resulting statistics
                mopub - include only MoPub data into the resulting statistics
                tapsense - include only TapSense data into the resulting statistics
                openx - include only OpenX data into the resulting statistics
                inneractive - include only Inneractive data into the resulting statistics
                rubicon - include only Rubicon data into the resulting statistics
                ani_view - include only AnyView data into the resulting statistics
                directoffer - include only your Direct Campaigns data into the resulting statistics

            include_shared_apps:  if passed with non-zero value the output will include the apps shared to you by other users

        Returns:

        """

        params = {
            'date_from': date_from,
            'date_to': date_to,
        }
        if app:
            params.update({'app': [app]})
        if country:
            params.update({'country': [country]})
        if network:
            params.update({'network': network})
        if detalisation:
            if type(detalisation) is list:
                params.update({'detalisation': detalisation})
            else:
                params.update({'detalisation': [detalisation]})

        return self.call('stats_api', params)

    def check_status(self, task_id):
        return self.call('check_status', {'task_id': task_id})

    def output_result(self, task_id):
        return self.call('output_result', {'task_id': task_id})

    def untarget_apps(self, creative_id, app_ids):
        """
        Удаление одной или несколько ап из таргетинга по id креатива и перечню id приложений.
        Несколько приложений передаются через запятую.
        https://www.appodeal.com/api/v3/untarget_apps/<creative_id>/<apps_coma_separated_ids_list>?api_key=<your_api_key>&user_id=<your_user_id>

        Args:
            creative_id: integer
            app_ids: integer or list of integers

        Returns:
            {"status":0,"message":"Success"}
        """
        if type(app_ids) is not list:
            app_ids = [app_ids]
        apps_ids_comma_str = ','.join(map(str, app_ids))
        action = 'untarget_apps/{creative_id}/{app_ids}'.format(creative_id=creative_id, app_ids=apps_ids_comma_str)
        return self.call(action)

    def target_apps(self, creative_id, app_ids):
        """
        Добавление одной или несколько ап в таргетинг по id креатива и перечню id приложений.
        Несколько приложений передаются через запятую
        https://www.appodeal.com/api/v3/target_apps/<creative_id>/<apps_coma_separated_ids_list>?api_key=<your_api_key>&user_id=<your_user_id>


        Args:
            creative_id: integer
            app_ids: integer or list of integers

        Returns:
            {"status":0,"message":"Success"}
        """
        if type(app_ids) is not list:
            app_ids = [app_ids]
        apps_ids_comma_str = ','.join(map(str, app_ids))
        action = 'target_apps/{creative_id}/{app_ids}'.format(creative_id=creative_id, app_ids=apps_ids_comma_str)
        return self.call(action)

    def list_campaigns(self):
        """
        Перечень кампаний
        https://www.appodeal.com/api/v3/list_campaigns?api_key=<your_api_key>&user_id=<your_user_id>

        Returns:
            {"status":0,"message":"Success","data":[
                {"id":1551,"name":"название_кампании","package_name":"package.name","is_network":false,"active":false,"deleted":false},
                {"id":1550,"name":"test","package_name":"test","is_network":false,"active":false,"deleted":false}
            ]}
        """
        return self.call('list_campaigns')

    def list_apps(self, creative_id):
        """
        Перечень приложений, по которым осуществляется таргетинг креатива

        Args:
            creative_id: int

        Returns:

            {
                "status": 0,
                "message": "Success",
                "data": [
                    {"id": 4, "name": "Piano Tiles Google Play", "package_name": "com.sabzira.PianoTiles",
                     "app_key": "1d0a9c7f68990cbfbdcafdaff3b5cf175e435c434391c090"},
                    {"id": 1, "name": "1 Test App", "package_name": "com.appodeal.test",
                     "app_key": "fee50c333ff3825fd6ad6d38cff78154de3025546d47a84f"}
                ]
            }
        """
        action = 'list_apps/{creative_id}'.format(creative_id=creative_id)
        return self.call(action)


включение одной или несколько кампаний по ID кампаний, несколько кампаний передаются через запятую
http://www.appodeal.com/api/v3/enable_campaigns/<campaigns_coma_separated_ids_list>?api_key=<your_api_key>&user_id=<your_user_id>
респонз:

```
{"status":0,"updated":2,"message":"Only available campaigns from given list were updated"}
```

выключение одной или несколько кампаний по ID кампаний, несколько кампаний передаются через запятую
http://www.appodeal.com/api/v3/disable_campaigns/<campaigns_coma_separated_ids_list>?api_key=<your_api_key>&user_id=<your_user_id>
респонз:
```
{"status":0,"updated":2,"message":"Only available campaigns from given list were updated"}
```
инфо про креатив и его кампанию по id креатива
http://www.appodeal.com/api/v3/campaign_image_info/<creative_id>?api_key=<your_api_key>&user_id=<your_user_id>
респонз:
```
{
    "status":0,
    "message":"Success",
    "data":{
        "campaign_image":{"id":2832,"bid_floor":100.0,"platform":1,"type":2,"width":640,"height":360,"deleted":false},
        "campaign":{"id":1551,"name":"test","package_name":"test","is_network":false,"active":false,"deleted":false}
    }
}
```
​перечень приложений, по которым осуществляется таргетинг креатива
http://www.appodeal.com/api/v3/list_apps/<creative_id>?api_key=<your_api_key>&user_id=<your_user_id>
респонз:
```
{"status":0,"message":"Success","data":[
    {"id":4,"name":"Piano Tiles Google Play","package_name":"com.sabzira.PianoTiles","app_key":"1d0a9c7f68990cbfbdcafdaff3b5cf175e435c434391c090"},
    {"id":1,"name":"1 Test App","package_name":"com.appodeal.test","app_key":"fee50c333ff3825fd6ad6d38cff78154de3025546d47a84f"}
]}
```
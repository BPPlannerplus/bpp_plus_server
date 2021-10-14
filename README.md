### 서비스설명.


### Tools 

  ##### 기술스택 
    - Python
    - Django
    - Django REST Framework
    - Crontab
    - JWT
    - AWS EC2
    - AWS RDS (MySQL)
   ##### 협업
    - Git 
    - Gitkraken
    - Notion


### REST API
   ##### login
1. kakao access_token으로 자체 access, refresh token 발급  


   - url  

        ~~~ http
        POST /login/new-token/ 
        ~~~
   - request
     
        ~~~ json
        {
           "access_token": "sBpMzzmjm7rKz3vY1Bs_lIFHuZu5Xt6iiTcjaAopb1UAAAF69oCtMw"
        }
        ~~~

     
     
   - response
        ~~~json
          {
             "refresh": "kpx3rJBWG7GdAGjm9LXlAvYLxB6TaP5HP5kWpT8AbjseEkqODJuIvGLLZJG6pu303TjXlJZjKejY4e6cKNrmU0nLzL84YD57mMXXS5Fpcb2ayLBYedTm6DK03TzxZyAHgYexojcPLZWuSz1T9yuh3xSffvSUPfufInNxuATn9SvdPx9AAopg4m3etJGKkjnZQbnCjyPE",
             "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI4MjM4NTMwLCJqdGkiOiI5YmU0NWUzNWVlN2U0NTIzYWEyOGNmZDJiOGJjMGUzZSIsInVzZXJfaWQiOjMsInVzZXJuYW1lIjoiXHVjNzc0XHVjMjE4XHVjNWYwIiwidWlkIjoxODIzOTM3MzE3fQ.Y4wd-yKfm6z6YLijZX1e9twfQ3kt8nm0rL-LM81cJOQ"
          }
        ~~~
     
2. refresh token으로 access token 재발급


   - url  

        ~~~ http
        POST /login/token/refresh/
        ~~~
   - request
     
     ~~~ json
        {
           "user_id" : 1,
           "refresh_token" : "Ku88jzG2ZUR9UANJpVwtuGydhhYQsvs9k31Yd4h9FLSQ4NVzai3vaITbWQxXnbFzRc9GFRJDbCJ5IMwNWrdVmQP4pTTtc7nZoqewCD8rGjKgxWXZIQxy2ny1rxDCMJgzypDF2B2ZeMviVsphFONcrO5NzZgjq8OwpDDYZnm7vORbpQwTXbjKQifdgZNgwEkFMJuDbAI2"
        }
       ~~~
     
     
   - response
        ~~~json
          {
            "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI3NDY4NDg0LCJqdGkiOiI3NzQ1ZDdmZjkwZDc0YzZlOTI2NDBjMmY2ODRjZDc4NSIsInVzZXJfaWQiOjEsInVzZXJuYW1lIjoiXHVjNzc0XHVjMjE4XHVjNWYwIiwidWlkIjoxODIzOTM3MzE3fQ.LG9Zhe7ICf8O8FgocI75tAY1J77eOR244RMaTUOu8Ks"
          }
        ~~~
     



3. 회원탈퇴


   - url  

        ~~~ http
        DELETE /login/withdrawal/
        ~~~
   - request


     
   - response
        ~~~json
         {
            "detail": "Successful withdrawal of members"
         }
        ~~~
   
#### shops

1. studio 전체목록 조회(찜순)


   - url  

        ~~~ http
        GET /shops/studios/?page=1&address=&like=
        ~~~
   - request

         
        | Parameter | Type | Description |
        | :--- | :--- | :--- |
        | `page` | `integer` | **Required**. pagination|
        | `address` | `string` | **Required**. 스튜디오 위치하는 구 필터링|
        | `like` | `boolean` | **Required**. 찜한 studio concept만 볼지(true,false) |
     
     
   - response
        ~~~json
     {
              "count": 3,
              "next": null,
              "previous": null,
              "results": [
                  {
                      "id": 3,
                      "name": "studio2",
                      "address": "gangdong",
                      "minprice": 600000,
                      "profile": "http://3.35.146.251:8000/media/KakaoTalk_20210802_202926771_02_eJFAEkq.png",
                      "like": true
                  },
                  {
                      "id": 5,
                      "name": "studio3",
                      "address": "gwangjin",
                      "minprice": 400000,
                      "profile": "http://3.35.146.251:8000/media/KakaoTalk_20210802_202947501_01_Os3pVhB.png",
                      "like": false
                  },
                  {
                      "id": 1,
                      "name": "studio1",
                      "address": "gangnam",
                      "minprice": 20000,
                      "profile": "http://3.35.146.251:8000/media/KakaoTalk_20210802_202947501.png",
                      "like": true
                  }
              ]
     }
        ~~~

2. beautyshop 전체목록 조회(찜순)


   - url  

        ~~~ http
        GET /shops/beautyshops/?page=1&address=&like=
        ~~~
   - request

         
        | Parameter | Type | Description |
        | :--- | :--- | :--- |
        | `page` | `integer` | **Required**. pagination| 
        | `address` | `string` | **Required**. 뷰티샵아 위치하는 구 필터링|
        | `like` | `boolean` | **Required**. 찜한 studio concept만 볼지(true,false) |
     
     
   - response
        ~~~json
     {
              "count": 3,
              "next": null,
              "previous": null,
              "results": [
                  {
                      "id": 6,
                      "name": "beautyshop3",
                      "address": "mapo",
                      "minprice": 700000,
                      "profile": "http://3.35.146.251:8000/media/KakaoTalk_20210802_202939803_01_9qKsgcL.png",
                      "like": false
                  },
                  {
                      "id": 4,
                      "name": "beautyshop2",
                      "address": "gangdong",
                      "minprice": 300000,
                      "profile": "http://3.35.146.251:8000/media/KakaoTalk_20210802_202947501_01_TIPlUXz.png",
                      "like": false
                  },
                  {
                      "id": 2,
                      "name": "beautyshop1",
                      "address": "gangnam",
                      "minprice": 300000,
                      "profile": "http://3.35.146.251:8000/media/KakaoTalk_20210802_202926771_02.png",
                      "like": true
                  }
              ]
       }
        ~~~


3. 특정 studio,beautyshop 조회(concept제외)


   - url  

        ~~~ http
        GET /shops/1
        ~~~
   - request

     
     
   - response
        ~~~json
     {
              "id": 1,
              "name": "studio1",
              "address_detail": "서울시 강남구 머시기 머시기",
              "minprice": 20000,
              "logo": "http://3.35.146.251:8000/media/bpp_U0iusS2.png",
              "profiles": [
                  "http://3.35.146.251:8000/media/KakaoTalk_20210802_202947501.png",
                  "http://3.35.146.251:8000/media/KakaoTalk_20210802_202947501_01.png",
                  "http://3.35.146.251:8000/media/KakaoTalk_20210802_202939803.png"
              ],
              "like": true,
              "map": "http://3.35.146.251:8000/media/KakaoTalk_20210802_202926771_01.png",
              "kakaourl": "https://pf.kakao.com/_xgCxjfj",
              "affiliates": [
                  {
                      "id": 4,
                      "name": "beautyshop2",
                      "profile": "http://3.35.146.251:8000/media/KakaoTalk_20210802_202947501_01_TIPlUXz.png"
                  },
                  {
                      "id": 6,
                      "name": "beautyshop3",
                      "profile": "http://3.35.146.251:8000/media/KakaoTalk_20210802_202939803_01_9qKsgcL.png"
                  }
              ]
      }
        ~~~     
   
4. 특정 studio,beautyshop의 concept 조회(등록순)


   - url  

        ~~~ http
        GET /shops/1/concepts
        ~~~
   - request

     
   - response
        ~~~json
          {
              "count": 2,
              "next": null,
              "previous": null,
              "results": [
                  {
                      "id": 1,
                      "profile": "http://3.35.146.251:8000/media/KakaoTalk_20210802_202926771_02_5800kq5.png"
                  },
                  {
                      "id": 2,
                      "profile": "http://3.35.146.251:8000/media/KakaoTalk_20210802_202947501_uzHPVja.png"
                  }
              ]
     }
        ~~~
     
 
5. 특정 studio,beautyshop 찜 토글


   - url  

        ~~~ http
        PUT /shops/1/like
        ~~~
   - request
     ~~~json
        {
           "change_to_like": false
        }
        ~~~

     
     
   - response
        ~~~json
          {
              "result": "shop like create"
          }
        ~~~     
     
##### concept
1. studio concept 전체 조회(찜순) : 컨셉북


   - url  

        ~~~ http
        GET /concepts/studios/?head_count=&gender=&background=&prop=&dress=&page=&like= 
        ~~~
   - request

         
        | Parameter | Type | Description |
        | :--- | :--- | :--- |
        | `head_count` | `integer` | **Required**. 1,2,3 | 
        | `gender` | `string` | **Required**. man,woman | 
        | `background` | `string` | **Required**. white,black,chromatic,etc,outside | 
        | `prop` | `string` | **Required**. health,mini,etc |
        | `dress` | `string` | **Required**. athleisure,swimsuit,underwear,etc| 
        | `page` | `string` | **Required**. 조회할 페이지(1,2,3...) |
        | `like` | `boolean` | **Required**. 찜한 studio concept만 볼지(true,false) |

     
     
   - response
        ~~~json
     {
              "count": 3,
              "next": null,
              "previous": null,
              "results": [
                  {
                      "id": 2,
                      "profile": "http://3.35.146.251:8000/media/KakaoTalk_20210802_202947501_uzHPVja.png",
                      "shop": {
                          "id": 1,
                          "name": "studio1"
                      },
                      "like": false
                  },
                  {
                      "id": 1,
                      "profile": "http://3.35.146.251:8000/media/KakaoTalk_20210802_202926771_02_5800kq5.png",
                      "shop": {
                          "id": 1,
                          "name": "studio1"
                      },
                      "like": true
                  },
                  {
                      "id": 3,
                      "profile": "http://3.35.146.251:8000/media/KakaoTalk_20210802_202926771.png",
                      "shop": {
                          "id": 3,
                          "name": "studio2"
                      },
                      "like": false
                  }
              ]
      }
        ~~~
     
2. 특정 studio concept 찜 토글


   - url  

        ~~~ http
        PUT /concepts/studios/1/like
        ~~~
   - request
     ~~~json
          {
            "change_to_like": true
          }
        ~~~

     
     
   - response
        ~~~json
          {
              "result": "shop like create"
          }
        ~~~   



##### reservation
1. 샵 문의중/확정 전체조회


   - url  

        ~~~ http
        GET /reservations?inquiry=
        ~~~
   - request

         
        | Parameter | Type | Description |
        | :--- | :--- | :--- |
        | `inquiry` | `boolean` | **Required**. 문의중 조회면 true, 확정&만료 조회면 false |

     
     
   - response
        ~~~json
        {
            "remaining_days": 16,
            "results": [
                {
                    "id": 3,
                    "state": 0,
                    "reserved_date": null,
                    "shop": {
                        "id": 2,
                        "shop_type": 1,
                        "name": "beautyshop1",
                        "logo": "http://3.35.146.251:8000/media/bpp_r5ZQYqs.png"
                    }
                }
            ]
        }
        ~~~

2. 샵 문의중 추가


   - url  

        ~~~ http
        POST /reservations/shops/:shop_id
        ~~~
   - request
     
   - response
        ~~~json
        {
            "result": "reservation create"
        }
        ~~~

3. 샵 예약확정 날짜받기


   - url  

        ~~~ http
        PATCH /reservations/:reservation_id
        ~~~
   - request
        ~~~json
        {
            "reserved_date": "2021-05-15"
        }
        ~~~

     
     
   - response
        ~~~json
        {
            "detail": "reserved_date input success"
        }
        ~~~

4. 샵 문의중 취소


   - url  

        ~~~ http
        DELETE /reservations/:reservation_id
        ~~~
   - request
     
   - response
        ~~~json
        {
            "detail": "reservation delete success"
        }
        ~~~

### 디렉토리 구조
~~~ bash
.
├── Dockerfile
├── README.md
├── concept
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── login
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
├── reservation
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── cron.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── secrets.json
└── shop
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
~~~
![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/668ae036-213c-4dcd-8e29-c0c672a865d3/KakaoTalk_Photo_2021-09-22-00-36-26.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220502%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220502T052159Z&X-Amz-Expires=86400&X-Amz-Signature=de6e01b29ec4de4115fadd37f4d348cd4c9388f2184835d0e5d0e2cba8bebe7c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22KakaoTalk_Photo_2021-09-22-00-36-26.png%22&x-id=GetObject)

### 서비스설명
바디프로필 정보를 일일이 찾아보기 힘들었던 소비자들에게 본인이 원하는 취향을 반영하여 스튜디오,메이크업샵,왁싱,태닝샵을 한 번에 찾아보고 여러 예약을 관리할 수 있게 해주는 서비스 

### 타켓층

![](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F69d187bf-4c96-40f3-bf69-4d536049b982%2FTarget.png?table=block&id=424fa6f3-5511-478a-b501-ca42c55781af&spaceId=a7e5d55f-58c1-4194-b564-431208c578b7&width=2000&userId=f780b332-6c42-48fa-a9a1-d8836ed7aec7&cache=v2)

### Tools 

  ##### 기술스택 
    - Python
    - Django
    - Django REST Framework
    - JWT
    - AWS EC2
    - AWS RDS (Postgresql)
    - AWS ROUTE53
    - AWS ELB
    - AWS ACM
    - Docker
   
   ##### 협업
    - Git 
    - Gitkraken
    - Notion


### REST API
https://documenter.getpostman.com/view/15198716/Tzm8GFjs


### 디렉토리 구조
~~~ bash
bpp-plus-server
  ├── __init__.py
  ├── __pycache__  
  ├── asgi.py
  ├── settings
  │   ├── __init__.py
  │   ├── __pycache__
  │   │   ├── __init__.cpython-39.pyc
  │   │   ├── base.cpython-39.pyc
  │   │   └── dev.cpython-39.pyc
  │   ├── base.py
  │   ├── dev.py
  │   └── prod.py
  ├── urls.py
  └── wsgi.py

config  
  ├── __init__.py
  ├── __pycache__
  │   └── __init__.cpython-39.pyc
  ├── docker
  │   └── entrypoint.prod.sh
  ├── nginx
  │   ├── Dockerfile
  │   └── nginx.conf
  └── scripts
      └── deploy.sh

.github
  └── workflows
      └── deploy.yml


login
  ├── __init__.py
  ├── __pycache__
  ├── admin.py
  ├── apps.py
  ├── migrations
  ├── models.py
  ├── serializers.py
  ├── tests.py
  ├── urls.py
  └── views.py

shop
  ├── __init__.py
  ├── __pycache__
  ├── admin.py
  ├── apps.py
  ├── migrations
  ├── models.py
  ├── serializers.py
  ├── tests.py
  ├── urls.py


concept
  ├── __init__.py
  ├── __pycache__
  ├── admin.py
  ├── apps.py
  ├── migrations
  ├── models.py
  ├── serializers.py
  ├── tests.py
  ├── urls.py
  ├── validators.py
  └── views.py

reservation
  ├── __init__.py
  ├── __pycache__
  ├── admin.py
  ├── apps.py
  ├── migrations
  ├── models.py
  ├── serializers.py
  ├── tasks.py
  ├── tests.py
  ├── urls.py
  └── views.py


cs
├── __init__.py
├── __pycache__
├── admin.py
├── apps.py
├── migrations
├── models.py
├── serializers.py
├── tests.py
├── urls.py
└── views.py

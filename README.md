# project_insta
[ 백엔드 공부 ] Part .2 두번째 개인 프로젝트 "SNS 서비스"  
  
프론트엔드를 배우기전에 서버에 흐름과 어떻게 데이터들이 통신하고 주고받는지 이해하기위해  
백엔드를 기초적으로 얕게라도 공부해보았습니다.  
그래서 아직 프론트엔트를 공부를 안해봐서  
HTML / CSS / JS 는 백엔드 개발 포커스에 맞게 최대한 간단하게 구현 했습니다.  

구현된 기능

- 이미지 업로드 
- 게시글 CRUD
- 댓글 CRUD
- 로그인 / 로그아웃 / 회원탈퇴 / 회원정보 수정 / 내정보
- 팔로워 / 해쉬테그 
- 좋아요 / 싫어요 기능

<img src="https://user-images.githubusercontent.com/76981768/106841705-f215f000-66e5-11eb-8f32-8c9bcf957d31.png" width="500" height="300">
<img src="https://user-images.githubusercontent.com/76981768/106841697-ef1aff80-66e5-11eb-80c1-b0d5ec23faeb.png" width="500" height="300">
<img src="https://user-images.githubusercontent.com/76981768/106841711-f3471d00-66e5-11eb-9b9a-e6bd9972385b.png" width="500" height="300">


해당 프로젝트는 python / Django 로 개발하였습니다.  
DB는 postgresql을 사용하였습니다.  
클론시 데이터베이스 portgresql 필요합니다.  

가상환경 설치방법 pip install virtualenv  
virtualenv venv  
call venv/scripts/activate  

해당 프로젝트에 쓰인 라이브러리 requirements.txt 설치방법  
pip install -r requirements.txt  

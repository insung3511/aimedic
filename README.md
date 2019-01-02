# Ai-Medic
약쟁이 프로젝트를 그대로 커밋하기에는 아닌거 같다고 한 아토 쌤의 말에 정로가 Ai-Medic 이라는 세련된 이름을 주어줬다. ~~역시 젊은 머리가 좋은가보다~~ </br>

인공지능이 알약을 찍은 사진을 보고 약의 이름을 타탄~ 하면서 알려주는 프로젝트이다. 사실 알약의 정보 (제약사, 효능, 부작용, 주의사항 등등...) 까지 나오게 하는 것이 목표였으나 아쉽게도 역시 한국은 약에 대한 API가 없기 덕분에 거기 까지 개발을 하지는 않았다. 
이에 대한 탐구 보고서는 <a href="https://docs.google.com/document/d/14yG68THHNvSeLGnVcI02y36Z87__uRbU0qtobdZ4hVQ/edit?usp=sharing"> 여기에 </a> 있다. </br>

# How it Works?
약들이 필요하다. </br>

![img_0183](https://user-images.githubusercontent.com/17959335/48658420-b3ec7180-ea84-11e8-88c5-01a351b4525a.JPG) </br>
약은 많으면 많을수록 인공지능이 공부할수 있는 양은 많아진다. 이런 약들을 공부를 시키기 위해서는 사진을 찍을수 있는 장소가 있으면 좋다. 이때 사진을 찍을때에는 카메라의 초점, 주변광, 밝기, 배경이 좋으면 좋다. 또한 약을 돌려가면서 찍어야지 인공지능에게 공부를 시키고 나중에 더 좋은 결과를 볼수가 있을것이다. 

![img_0185](https://user-images.githubusercontent.com/17959335/48658432-e1d1b600-ea84-11e8-9176-63a9ddae4492.JPG) </br>
여러 장소를 거치고 거쳐서 최종적으로 위에 사진 처럼 나왔다. 라즈베리파이가 약의 사진을 찍는동안 상자 안에 있는 EV3는 약을 계속 돌리면서 약을 여러면에서 찍도록 도와준다. 핸드폰에 조명 기능을 키고 약 사진을 찍었다. </br>

![kakaotalk_photo_2018-11-17-14-44-57](https://user-images.githubusercontent.com/17959335/48658433-eeeea500-ea84-11e8-9faa-8a3f4ed4d604.jpeg) </br>
이렇게 했다. 약의 적힌 숫자, 그림, 단어 들이 명확하게 보여야 인공지능이 공부를 하기에 가장 좋다. 이 약의 사진이 가장 중요하기 때문에 꼭 사진을 찍을때 잘 찍어줘야 한다. 만일 색, 모양이 비슷한 약 2개를 양옆에 두고 비교를 하기 위해서는 약에 적혀 있는 그림, 숫자, 단어를 기준으로 구별을 하기 때문이다. 어차피 돈 많이 받고 구별 하는 인간이나 돈 안 받고 사진 받은 인공지능이나 구별하는 방식은 다를뿐 보상이 뭐냐에 따라서 다른 것이다.

![kakaotalk_photo_2018-11-17-14-44-51](https://user-images.githubusercontent.com/17959335/48658434-eeeea500-ea84-11e8-8f2a-7ea66170aae5.jpeg) </br>
사진상으로 보이진 않지만 실제로는 돌아가고 있다. 사진 처럼 주변광이 실제로는 많이 어둡진 않다. 카메라가 초점을 약을 중점으로 찍어서 더 어두워 보이는 것이다. 이렇게 약 한개당 20장을 찍게 된다. 다만 캡슐약은 뒷면, 앞면 차이가 없어서 아무면 이나 20장을 찍는다. 내복용 알약은 숫자면, 그림 혹은 글자로 적힌 면이 따로 있기 때문에 숫자면 20장, 그림면 20장으로 찍어서 올린다. </br>

![img_0186](https://user-images.githubusercontent.com/17959335/48658449-3aa14e80-ea85-11e8-8342-5783b69c9aac.JPG) </br>
이렇게 많은 약들의 사진들을 라즈베리파이에서 찍는다. 라즈베리파이에서 사진을 찍을때에는 파이썬 코드로 picamera 라이브러리를 이용해서 사진을 찍는다. 이 사진들은 찍어서 맥으로 옮길때에는 SFTP로 옮긴다. 옮긴 후 맥에서 Azure Custom Vision으로 업로드를 한다. 

## Contact me
----------------------------------------
If you have problem about this code, then contect me. </br>
Email : insung.park123@gmail.com </br>
Facebook : https://www.facebook.com/insung.bahk </br>
</br>
If you want to give me some money... Please money send here! </br>
Bitcoin : 17qKUu57aUBcvx9T1ea8Ga87EPnDdmwAEP </br>
Ether : 0xdFE8D1536deE8F839Ede7c1f3A0c44116287D931  
Bitcoin Cash : qp90gf09r3y3h06czmtnsfhz9w7s90se4s72vd9pam </br> 
</br>
🙇‍♀️👾🤩Thank you! 🤩👾🙇‍♂️ 
----------------------------------------

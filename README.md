# 3줄 요약좀 해주세요

#### 🧑‍💻멤버 구성

18101210 김효근

18101270 정석영

#### 🔥 프로젝트 설명

```
1. 세상엔 긴 글이 참 많다.
2. 하지만 다 읽기엔 시간이 없다.
3. 그래서 글들을 3줄 요약을 하려고 한다.
```

 세상엔 참 많은 글들이 있다. 그 많은 글들을 읽기 위해서는 시간이 많이 걸리고, 글이 길어지면 집중력을 잃기 쉽기 때문에 핵심을 파악하지 못하는 경우가 종종 있다.~~(귀찮아서 읽지 않는 것은 아니다.)~~

그래서 3줄 요약이라는 밈이 생기게 되었고, 뉴스나 자신이 원하는 텍스트를 3줄 요약을 해주는 프로그램을 만드려고 한다.

#### ⁉️ 사용된 알고리즘

1. TextRank
2. Seq2Seq + Attention ( 추후 개선, 추가 예정 )

#### 🧾 Requirements

```
konlpy
requests
BeautifulSoup4
networkx
numpy
pandas
```

#### ㏈ 사용된 데이터

[AIHub 문서요약 텍스트](https://aihub.or.kr/aidata/8054)

#### 🦻How To Use

```
python summarizer.py
```

위의 코드를 실행하면 다음과 같은 안내가 나온다.

**Select Mode - 1 : News, 2 : Custom Text**

1이나 2를 입력하면 각각의 모드로 넘어간다.



Mode 1 : News Mode

- Mode 1을 선택하면 Url을 입력하라는 글이 나온다.

- 뒤에 요약을 원하는 뉴스의 URL을 입력해준다.

- 예시

  ```
  ❯ python summarizer.py
  Select Mode - 1 : News, 2 : Custom Text
  1
  Input Url : https://www.yna.co.kr/view/AKR20220528021400007?input=1195m
  ```

- output :  손흥민은 프리미어리그가 27일(현지시간) 발표한 2021-2022시즌 리그 올해의 팀 한자리를 꿰찼다. 2021-2022시즌 프리미어리그 올해의 팀.  올해의 팀에 선정된 토트넘 선수는 손흥민이 유일하다.

Mode 2 : Custom Text Mode

- 내가 원하는 텍스트를 복사해서 붙여 넣으면 요약을 해주는 모드이다.

- Mode 2를 선택하면 아래와 같은 문구가 나온다.

  **Input Text all and input 'end' :**

- 이 뒤에 자신이 원하는 텍스트를 붙여넣고, 엔터를 친 뒤, end를 써준다.

- 예시

  ``` 
  ❯ python summarizer.py                                                                                       
  Select Mode - 1 : News, 2 : Custom Text
  2
  Input Text all and input 'end' : ~~~~~~
  end
  ```

#### 🙇Reference

[TextRank 기법을 이용한 핵심 어구 추출 및 텍스트 요약](https://bab2min.tistory.com/552)

[Sequence-to-Sequence 모델로 뉴스 제목 추출하기](https://ratsgo.github.io/natural%20language%20processing/2017/03/12/s2s/)




# Git

> 분산버전관리시스템(DVCS)



## 0. 폴더, 파일

`mkdir` 폴더 생성

`cd` 폴더 이동

`ls` 목록

`touch` 파일 생성

`rm` 삭제

`pwd` 현재 디렉토리 출력



## 1. git 저장소 만들기

> Create an empty Git repository or reinitialize an existing one

```bash
$ git init
Initialized empty Git repository in C:/Users/takhe/Desktop/first/.git/
(master) $
```

- `.git`폴더가 생성 ==> 버전이 기록되는 저장소
  - 해당 폴더를 지우게 되면 모든 버전이 삭제되니 주의
- `(master)`



## 2. 버전 기록하기

![git 구조](Git%EC%82%AC%EC%9A%A9%EB%B2%95.assets/git%20%EA%B5%AC%EC%A1%B0.jpg)

### add

> Add file contents to the index

```bash
$ git add 파일명
$ git add a.txt
$ git add a.txt b.txt
```

### commit

> record changes to the repository

```bash
$ git commit -m '커밋메시지'
```

- 커밋 메시지는 항상 버전의 내용(변경 사항)에 대해서 나타낼 수 있도록 기록한다.



### status

>Show the working tree status

```bash
$ git status
```

상태가 어떤지 파악

staring area에만 저장되고 commit되지 않은경우 알려줌

```bash
#커밋할 변경사항들
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    b.txt
        
#커밋을 위해 준비되지 않은 변경사항(staging area X => working directory)
#있었다가 변경된 애
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt
        
#트래킹되지 않은 파일들(Working directory)
#새로 만들어진 애
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        c.txt
```

- 파일을 조작하는 방법은 총 4가지
  - 생성 Create
  - ~~읽기 Read~~
  - 수정 Update
  - 삭제 Delete



### log

```bash
$ git log
```

버전마다 뭐가 달라졌는지 체크 가능



## git 파일의 라이프 사이클

[관련 문서 - Git 기초](https://git-scm.com/book/ko/v2/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EA%B8%B0%EC%B4%88)

[관련 문서 - Git 수정하고 저장소에 저장하기](https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EA%B8%B0%EC%B4%88-%EC%88%98%EC%A0%95%ED%95%98%EA%B3%A0-%EC%A0%80%EC%9E%A5%EC%86%8C%EC%97%90-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0)

![image-20220113101851253-16420396855881](Git%EC%82%AC%EC%9A%A9%EB%B2%95.assets/image-20220113101851253-16420396855881.png)

![image-20220113101938077](Git%EC%82%AC%EC%9A%A9%EB%B2%95.assets/image-20220113101938077.png)



### git에서 관리하는 파일 변경사항 상태

- untracked
- tracked
  - modified : 커밋에 비해 수정된 경우
  - staged : 커밋 되기전 staging area에 목록
  - commited : 커밋된 상태



```bash
quiz/
	.git
	a.txt
	my_folder/
	
project/
	.git
	a.py
	b.py
	
내 폴더/
	마케팅/
	..
```

- quiz 폴더 이름을 변경해도 되는가? O

- quiz 폴더 이름 변경에 대한 기록이 남는가? X

- quiz 폴더 위치를 변경해도 되는가? △

  - project에는 이동X
    - git 프로젝트 저장소에 옮기는 경우 : 내부에서 동작이 복잡하게 진행
      - git 관리되는 리포지토리가 하나의 폴더 안에 두개가 존재

  - 내 폴더로는 이동은 언제든지 O

- my_folder는 지우면 복원 가능? △

  - 커밋된 변경사항은 복원 가능
  - 커밋되지 않은 경우는 절대 불가능

- 만약 .git 폴더가 있는 저장소 내부에서 새롭게 .git 만들어도 될까? X

  - `git init` 하려고 하는데 `master` 가 있으면 하지말자


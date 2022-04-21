# Collaboration

## 개발 전

1. GitHub Repository 생성

2. Repository - settings - Collaborators에서 초대, 승인, 권한 부여

3. 팀원들은 해당 Repository를 clone으로 받고 각자 개발 시작

4. 기능 개발 시작 전 브랜치 생성 및 이동

   ```bash
   # 브랜치 만들면서 이동
   $ git switch -c feature/login
   ```



## 개발

1. 특정 기능 개발(예시 : feature/login 기능) 진행

2. 기능 개발 완료 후 commit, push

   ```bash
   # 커밋
   $ git commit -m "커밋 메세지"
   
   # 푸쉬
   $ git push origin feature/login
   ```




## 개발 후

1. GitHub에서 본인이 푸쉬한 내용 `merge request` 하기
2. 다른 팀원들이 `pull request` 확인 후 `merge`
3. GitHub에 반영 된 상태



## 반영 후

1. 개발한 팀원은 로컬로 돌아와서 브랜치 `master`로 변경 후 GitHub에서 `pull` 하기 => 프로젝트 변경사항 반영

   ```bash
   # 브랜치 변경
   $ git switch master
   
   # GitHub에서 프로젝트 변경사항 반영하기
   $ git pull origin master
   ```

2. 기존에 개발 완료했던 브랜치 삭제

   ```bash
   $ git branch -d feature/login
   
   # master와 관계 없이 강제로 삭제하려면 
   $ git branch -D feature/login
   ```
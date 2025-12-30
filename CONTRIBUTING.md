# 🤝 Contributing Guide

이 프로젝트에 기여해주셔서 감사합니다!

아래 가이드는 프로젝트에 기여할 때 따라야 할 규칙과 절차를 설명합니다.
모든 협업자는 아래의 브랜치 규칙, 커밋 규칙, PR 프로세스를 따라주세요.

---

## 🌳 브랜치 전략

본 프로젝트는 **Git Flow 전략**을 따릅니다.  
아래 표는 브랜치 구조와 용도를 정리한 것입니다.

| 🌿 브랜치            | 🛠️ 용도                    | 📌 비고                                             |
| -------------------- | -------------------------- | --------------------------------------------------- |
| `main`               | 🚀 배포용 (항상 안정 상태) | 직접 push 금지 (보호 브랜치)                        |
| `develop`            | 🧩 기본 개발 브랜치        | feature 브랜치 병합 대상                            |
| `feature/*`          | ✏️ 기능 개발용             | feature/#이슈번호-작업내용. 예: `feature/#24-login` |
| `fix/*` / `hotfix/*` | 🐞 버그 수정용             | 긴급 수정은 `hotfix`로 생성                         |

### 🍃 브랜치 기본 규칙

1. **기본 브랜치**는 `develop`입니다. 새로 클론하면 자동으로 `develop`이 활성화됩니다.
2. 모든 개발은 `feature/*` 브랜치에서 진행하세요.
3. `main` 브랜치에는 직접 push하지 마세요. `develop → main` PR만 허용됩니다.
4. PR은 반드시 **리뷰 승인 + CI 통과 후 병합(Squash merge)** 해야 합니다.

---

## 🏷️ 이슈 라벨 규칙

| 라벨             | 의미                               | 비고                      |
| ---------------- | ---------------------------------- | ------------------------- |
| ✨ `feat`        | 새로운 기능 개발                   | enhancement와 병행 가능   |
| 🐛 `fix`         | 버그 수정                          | bug와 병행 가능           |
| 📚 `docs`        | 문서 수정                          | documentation과 병행 가능 |
| 🎨 `style`       | 코드 스타일 변경                   | 기능 변화 없음            |
| ♻️ `refactor`    | 코드 리팩토링                      | 성능 개선, 구조 변경      |
| ✅ `test`        | 테스트 코드 추가/수정              | 단위/통합 테스트          |
| 🔧 `chore`       | 빌드/환경 설정/기타 작업           | 의존성 업데이트 등        |
| 🙋 `help wanted` | 도움이 필요한 작업                 |                           |
| ❌ `invalid`     | 잘못된 이슈 (재현 불가, 불필요 등) |                           |
| ❓ `question`    | 질문/논의용 이슈                   |                           |
| 🚫 `wontfix`     | 수정하지 않을 예정인 이슈          |                           |

---

## 📝 커밋 메시지 규칙

1. 커밋 메시지는 Conventional Commits 스타일을 권장합니다. 타입은 소문자 접두사(`feat`, `fix`, `docs`, `chore` 등)를 사용하세요.
2. 제목(헤더)과 본문은 한 줄 띄워 구분합니다.
3. 제목은 50자 이내, 명령형으로 작성하세요. 예: `feat: 로그인 페이지 추가`.
4. 본문은 72자 이내로 적절히 줄바꿈하고, 변경의 이유(Why)와 요약(What)을 적습니다.
5. 필요 시 제목 또는 본문에 이슈 번호를 참조하세요. 예: `feat: 로그인 구현 (#12)`

### ✏️ 예시

```
fix: Safari에서 모달 스크롤 이슈 수정

모바일 Safari 환경에서 모달을 띄웠을 때
배경 스크롤이 움직이는 문제를 수정함.
```

### 🏷️ 커밋 타입

| 타입       | 설명                                 |
| ---------- | ------------------------------------ |
| `feat`     | ✨ 새로운 기능 추가                  |
| `fix`      | 🐛 버그 수정                         |
| `docs`     | 📚 문서 수정                         |
| `style`    | 🎨 코드 스타일 변경 (기능 변화 없음) |
| `rebase`   | 🔄 브랜치 정리(rebase 수행)          |
| `test`     | ✅ 테스트 코드 추가/수정             |
| `refactor` | ♻️ 코드 리팩토링                     |
| `chore`    | 🔧 환경 설정/기타 작업               |
| `build`    | 🏗️ 빌드 관련 작업                    |

---

## 🛠️ 작업 흐름 (Workflow)

1. 📥 최신 `develop` 브랜치 가져오기

```bash
git checkout develop
git pull origin develop
```

2. 🌱 기능 브랜치 생성

```bash
git checkout -b feature/기능명
```

3. 💾 기능 개발 후 커밋

```bash
git add .
git commit -m "feat: 기능 설명"
```

4. 🚀 GitHub에 푸시

```bash
git push -u origin feature/기능명
```

5. 🔀 GitHub에서 PR(Pull Request) 생성 (feature → develop)

- PR 제목 예시: `feat: 로그인 페이지 구현 (#12)` / `fix: 회원가입 유효성 검사 추가 (#17)`
- 최신 develop과 동일한 파일을 수정한 경우 rebase 진행

6. 📦 배포 준비

- develop → release → main 순으로 머지
- Replit에서 Pull from GitHub 실행하여 배포

---

## 🎨 코드 스타일

### 🐍 Python (백엔드)

- PEP8 스타일 가이드 준수
- 환경 변수는 `.env` + `python-dotenv` 사용 (API키 등 민감 정보는 커밋 금지)
- Replit 배포 시 서비스의 Secrets 기능 사용

### ⚛️ React-Vite / JavaScript (프론트엔드)

- ES6+ 문법 사용
- 기능 단위로 컴포넌트 분리
- API 호출은 `/src/api/` 디렉토리에서 관리

---

## 📦 로컬 빌드 및 테스트

- Backend (Windows 예시)

```powershell
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt
pytest
```

- Frontend

```bash
cd aiChat_front
npm install
npm run dev
npm run build
```

---

## 🔁 Pull Request 프로세스

1. Issue 생성 → 담당자 지정
2. feature 브랜치 생성 후 작업
3. Commit & Push
4. Pull Request 생성 → 리뷰 요청
5. 리뷰 후 승인 및 Merge (Squash)

### ⚔️ PR 전 Conflict 미리 해결하기 (Rebase 권장)

PR 생성 전에 `develop` 브랜치와의 충돌을 미리 해결해주세요.  
이 과정을 거치면 리뷰어가 바로 머지할 수 있고, 불필요한 Conflict를 줄일 수 있습니다.

```bash
# 1️⃣ develop 최신화
git fetch origin

# 2️⃣ feature 브랜치로 이동
git checkout feature/기능명

# 3️⃣ develop 최신 커밋 위로 재배치 (rebase)
git rebase origin/develop

💥 충돌(conflict)이 발생하면:

git status  # 충돌 파일 확인 & 수정
git add <파일명>
git rebase --continue

모두 해결되면:

git push -f origin feature/기능명
```

✅ 이 과정을 거치면 PR 시 Able to merge 상태가 유지되어
리뷰어가 추가 조치 없이 바로 Merge할 수 있습니다.

---

## 🧩 긴급 수정 (Hotfix)

```bash
# 1️⃣ main에서 분기
git checkout main
git pull
git checkout -b hotfix/<이슈명>

# 2️⃣ 수정 및 푸시
git add .
git commit -m "hotfix: 긴급 수정 내용"
git push -u origin hotfix/<이슈명>

# 3️⃣ PR 생성 (hotfix → main)
# 4️⃣ main에 병합 후 develop에도 반영 (PR: main → develop)
```

---

## 🧪 릴리스 (Release)

1. `develop`에서 테스트 완료 후 `main`으로 PR 생성 (base: `main`, compare: `develop`)
2. 리뷰 & CI 통과 후 **Squash Merge**
3. 버전 태그 추가

```bash
git checkout main
git pull
git tag -a vX.Y.Z -m "Release vX.Y.Z"
git push origin vX.Y.Z
```

---

## 🚀 배포

- `main` 브랜치에 머지되면 배포 준비 완료
- Replit에서 `Pull from GitHub` 실행
- 배포 후 기능 테스트 진행

---

## ⚠️ 협업 원칙

- 🚫 `main` 브랜치에 직접 커밋 금지
- ✅ 모든 변경은 PR(Pull Request)로 진행
- 🧩 기능 단위로 feature 브랜치 생성
- 🧹 커밋은 의미 단위로 작게 분리
- 🧾 커밋 메시지는 통일된 규칙 유지
- 🗂️ 코드 리뷰는 최소 1명 이상 승인 필수
  - ☑️ 리뷰어의 요청 사항은 가능한 한 반영합니다
  - 🗨️ 논의가 필요한 경우 PR 코멘트에서 대화합니다

---

## 💬 문의

기여 과정에서 궁금한 점이 있다면
이슈를 생성하거나 프로젝트 관리자에게 문의해주세요.

감사합니다 🙌

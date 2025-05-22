# syntax=docker/dockerfile:1
# 1. 빌더 스테이지: 개발 환경을 구축하고 종속성을 설치합니다[2][7].
FROM python:3.12-slim-buster AS builder

# 2. 작업 디렉토리 설정[7].
WORKDIR .

# 3. Poetry 설치 (또는 pip 사용 가능)[3].
RUN apt-get update && apt-get install -y --no-install-recommends curl
RUN curl -sSL https://install.python-poetry.org | python3 -

# 4. 프로젝트 파일 복사[3].
COPY poetry.lock pyproject.toml ./

# 5. Poetry를 사용하여 종속성 설치 (dev 종속성 제외)[3].
RUN poetry config virtualenvs.create false && poetry install --no-interaction --disable-plugins --without dev

# 6. 애플리케이션 코드 복사[3].
COPY . ./app

# 7. 최종 스테이지: 최소한의 런타임 환경을 구성합니다[2][7].
FROM python:3.12-slim-buster AS release

# 8. 작업 디렉토리 설정[7].
WORKDIR /app

# 9. 빌더 스테이지에서 종속성 복사[7].
COPY --from=builder . /app
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages

# 10. 애플리케이션 시작 명령 설정[4].
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

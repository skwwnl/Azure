FROM python:3.12-alpine

# 빌드 도구 및 uv 설치
RUN apk add --no-cache curl git build-base

# uv 설치
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# uv가 설치된 경로를 PATH에 추가
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# 의존성 파일 복사
COPY pyproject.toml ./

# requirements.txt 생성 (bash 대신 직접 파일로)
RUN uv pip compile pyproject.toml > requirements.txt

# uv로 시스템에 패키지 설치
RUN uv pip install --system --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

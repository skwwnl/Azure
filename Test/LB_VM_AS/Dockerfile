# syntax=docker/dockerfile:1

FROM python:3.12-alpine AS builder

# 필수 패키지 설치 및 uv 설치
RUN apk add --no-cache build-base curl

# uv 설치
RUN curl -LsSf -o /tmp/install_uv.sh https://astral.sh/uv/install.sh && \
    sh /tmp/install_uv.sh && \
    rm /tmp/install_uv.sh

# # uv 실행 경로 환경변수 추가
# ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# pyproject.toml만 복사 (poetry.lock 불필요)
COPY pyproject.toml ./

# uv로 의존성 설치 (가상환경 없이)
RUN uv pip install --system --no-cache-dir -r <(uv pip compile pyproject.toml)

# 소스 코드 복사
COPY . .

# 최종 이미지 (멀티스테이지)
FROM python:3.12-alpine

WORKDIR /app

# uv 실행파일 복사 (필요시)
COPY --from=builder /root/.cargo/bin/uv /usr/local/bin/uv

# 빌더에서 설치된 패키지 복사
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

# 소스 코드 복사
COPY --from=builder /app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

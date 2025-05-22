FROM python:3.13.3

# 2. 작업 디렉토리 설정: 컨테이너 내에서 명령이 실행될 기본 디렉토리를 설정합니다.
WORKDIR /code

# 3. 종속성 파일 복사: requirements.txt 파일을 컨테이너의 작업 디렉토리로 복사합니다.
#    이 파일을 먼저 복사하고 패키지를 설치하면, 코드 변경 시 Docker 빌드 캐시를 활용하여 빌드 시간을 단축할 수 있습니다.
COPY ./requirements.txt /code/requirements.txt

# 4. 종속성 설치: pip를 사용하여 requirements.txt에 명시된 패키지들을 설치합니다.
#    --no-cache-dir: pip가 캐시를 저장하지 않도록 하여 이미지 크기를 줄입니다.
#    --upgrade: 명시된 패키지들을 최신 버전으로 업그레이드합니다.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 5. 애플리케이션 코드 복사: FastAPI 애플리케이션 코드가 있는 디렉토리(예: ./app)를
#    컨테이너의 작업 디렉토리 내의 app 디렉토리로 복사합니다.
COPY . /code

# 6. 컨테이너 실행 명령: 컨테이너가 시작될 때 실행될 명령을 지정합니다.
#    fastapi run 명령어를 사용하여 app/main.py 파일 내의 FastAPI 애플리케이션을 실행합니다.
#    --host 0.0.0.0: 컨테이너 외부에서 애플리케이션에 접근할 수 있도록 합니다.
#    --port 80: 애플리케이션이 컨테이너의 80번 포트에서 실행되도록 합니다.
CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
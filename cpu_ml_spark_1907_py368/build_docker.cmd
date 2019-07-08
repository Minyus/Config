docker build -t minyus86/cpu_ml_spark_1907_py368:v0.0.4 .
docker run -v /home:/home -p 22:22 -p 5000:5000 --name ml minyus86/cpu_ml_spark_1907_py368:v0.0.4
pause

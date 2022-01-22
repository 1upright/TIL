## json



```python
import json
# 파일 열기 (경로)
f = open('data/movie.json', encoding='utf-8')
# 해당 파일 load 
data = json.load(f)
# 알아보기
print(data, type(data))
```


# practice_card

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="card.css">
  <title>Layout</title>
</head>
<body>
  <div class="container">
    <div class="card">
      <div class="card-nav">
        <h2>오늘의 명소</h2>
      </div>
      <div class="card-header">
        <img src="images/image.png" alt="card image" class="card-img">
        <div class="card-img-description">
          <h4>제주도</h4>
          <h4>성산 일출봉</h4>
        </div>
      </div>
      <div class="card-body">
        <div class="card-body-title">
          <h4>제주도 서귀포시 성산읍</h4>
          <p>2020.03.23</p>
        </div>
        <hr />
        <div class="card-body-content">
          <p>
            <span style="color: red">성산일출봉</span>은 제주도의 다른 오름들과는 달리 마그마가 물속에서 분출하면서 만들어진 수성화산체다.
            화산활동시 분출된 뜨거운 마그마가 차가운 바닷물과 만나면서 화산재가 습기를 많이 머금어 끈끈한 성질을 띄게 되었고,
            이것이 층을 이루면서 쌓인 것이 성산일출봉이다.
          </p>
        </div>
      </div>
      <div class="card-footer">
        <div>&copy; COMPANY</div>
      </div>
    </div>
  </div>
</body>
</html>
```



```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.container {
  width: 1200px;
  margin: 200px auto;
}

.card {
  width: 700px;
  margin: 0 auto;
  border: 2px dashed black;
}

h4 {
  font-family: Arial;
  font-weight: bold;
  font-size: 20px;
}

p {
  font-family: Arial;
}

.card-header {
  padding: 18px;
  /* line-height: 0; */
}

.card-body {
  padding: 18px;
}

.card-img {
  width: 100%;
  height: 330px;
  display: block; /* 여백을 없애기 위함 - header에 font-size: 0 or line-height: 0; 도 가능 */
}

.card-nav {
  background-color: mediumseagreen;
  text-align: center;
}

.card-img-description {
  background-color: mediumseagreen;
  text-align: center;
  height: 70px;
  color: white;
  line-height: 35px; /* 수직 가운데 정렬 */
}

.card-body-title {
  position: relative;
}

.card-body-title > h4 {
  display: inline;
}

.card-body-title > p {
  display: inline;
  position: absolute;
  right: 0;
}

.card-body-content {
  margin-top: 10px;
  padding: 10px;
  background-color: bisque;
}

.card-footer {
  /* height: 30px;
  line-height: 30px; */
  padding: 10px;
  text-align: end;
  background-color: green;
  color: white;
}
```


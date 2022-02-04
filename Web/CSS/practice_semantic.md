# practice_sementic

![sem](practice_semantic.assets/sem.PNG)



```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="semantic.css">
  <title>Layout Practice</title>
</head>
<body>
  <header class="bg-lightgrey m-4 p-4 border br-4">
    <h1>
      <h1 class="text-center">
        header
      </h1>
    </h1>
  </header>
  <nav class="bg-lightgrey m-4 p-4 border br-4">
    <h2>nav</h2>
  </nav>
  <div class="clearfix">
    <section class="bg-lightgrey section-width-height border br-4 padding-4">
      <h2>section</h2>
      <article class="bg-white border br-4 margin-4 padding-4">
        <h3>article1</h3>
      </article>
      <article class="bg-white border br-4 margin-4 padding-4">
        <h3>article2</h3>
      </article>
    </section>
    <aside class="bg-lightgrey aside-width-height border br-4 padding-4">
      <h2>aside</h2>
    </aside>
  </div>  
  <footer class="bg-lightgrey m-4 p-4 border br-4">
    <h2>footer</h2>
  </footer>
</body>
</html>
```



```css
/* 아래 코드는 수정하지 마세요. */
body {
  font-family: Arial;
  width: 800px;
}

section {
  float: left;
  margin-left: 4px;
}

aside { 
  float: right;
  margin-right: 4px;
}

.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

/* 여기서부터 작성하세요. */
/* 모든 스타일 요소를 ***클래스***로 만들어 작성 후 사용합니다. */

/* 1. article 태그는 white로 나머지 시멘틱 태그는 lightgrey로 배경색을 바꿔주세요. */
.bg-lightgrey {
  background-color: lightgrey;
}

.bg-white {
  background-color: white;
}
/* 2. header, nav, footer 태그의 margin을 4px로 만들어주세요. */
.m-4 {
  margin: 4px;
}
/* 3. header, nav, footer 태그의 padding을 4px로 만들어주세요. */
.p-4 {
  padding: 4px;
}
/* 4. h1 태그를 수평 중앙 정렬 시켜주세요. */
.text-center {
  text-align: center;
}
/* 5. section 태그는 width 490px height 300px, 
   aside 태그는 width 280px height 300px로 만들어주세요.*/
.section-width-height {
  width: 490px;
  height: 300px;
}
.aside-width-height {
  width: 280px;
  height: 300px;
}
/* 6. 모든 semantic 태그의 border 두께를 1px, 실선, 검은색으로 만들어주세요. */
.border {
  border: 1px solid black;
}
/* 7. 모든 semantic 태그의 border 모서리 반경을 4px로 만들어주세요. */
.br-4 {
  border-radius: 4px;
}
/* 주석의 조건에 맞추기 위해 그냥 내가 새로 만들어 버린 class 두개 */
.padding-4 {
  padding: 4px;
}

.margin-4 {
  margin: 4px;
}
```


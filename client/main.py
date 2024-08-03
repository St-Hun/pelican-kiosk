<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Pelican Kiosk</title>
    <link
      rel="stylesheet"
      href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css"
      integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="./dist/css/style.css" />
  </head>

  <body>
    <header class="header">
      <div class="start-window">Pelican</div>
      <div class="header-container">
        <button class="btn-home trans">
          <i class="fas fa-home"></i>
        </button>
        <h1 class="home"><span>Pelican's</span> <span>KIOSK</span></h1>
        <button class="btn-dev trans">
          <i class="fas fa-plus-square"></i>
        </button>
      </div>
      <nav class="main-nav">
        <ul class="menu-tab list">
          <li id="seasonmenu" class="tab-list trans btn-active">시즌 메뉴</li>
          <li id="icemenu" class="tab-list trans">커피(ICE)</li>
          <li id="hotmenu" class="tab-list trans">커피(HOT)</li>
        </ul>
      </nav>
      <div class="dev-modal-container">
        <div class="dev-modal">
          <h3 class="dev-modal-heading">신규 메뉴 추가</h3>
          <p class="dev-modal-text">새로운 상품을 추가해 주세요</p>
          <div class="dev-modal-input">
            <form>
              <section>
                <div>
                  <label>메뉴명</label
                  ><input
                    class="dev-name input-text"
                    type="text"
                    placeholder="상품명 입력"
                    autofocus
                    required
                  />
                </div>
                <span>* 한글로 2자이상 입력해주세요</span>
              </section>
              <section>
                <div>
                  <label>이미지</label
                  ><input
                    class="dev-image-url input-text"
                    type="text"
                    placeholder="이미지 주소 입력"
                    required
                  />
                </div>
                <span>* url을 넣어주세요</span>
              </section>
              <section>
                <div>
                  <label>상품 가격</label
                  ><input
                    class="dev-price input-price"
                    type="text"
                    placeholder="가격 입력"
                    required
                  />
                </div>
                <span>* 숫자를 입력해주세요</span>
              </section>
              <section>
                <div>
                  <label>사이즈 업 가격</label
                  ><input
                    class="dev-size-price input-price"
                    type="text"
                    placeholder="가격 입력"
                    required
                  />
                </div>
                <span>* 숫자를 입력해주세요</span>
              </section>
              <section>
                <div>
                  <label>샷 추가 가격</label
                  ><input
                    class="dev-shot-price input-price"
                    type="text"
                    placeholder="가격 입력"
                    required
                  />
                </div>
                <span>* 숫자를 입력해주세요</span>
              </section>
              <div>
                <label>샷 추가 여부</label
                ><input class="dev-shot input-check" type="checkbox" />
              </div>
            </form>
            <div class="dev-modal-btn">
              <button class="modal-storage" disabled>저장</button>
              <button class="modal-exit">닫기</button>
            </div>
          </div>
        </div>
      </div>
    </header>
    <main>
      <div class="main__container">
        <ul class="menu-list"></ul>
        <div class="btn-group"></div>
        <div class="menu-modal-container">
          <ul class="modal">
            <!-- <li class="modal-item">
            <figure>
              <img class="modal-img"
                src="https://cdn.shopify.com/s/files/1/0273/4535/4826/products/coldbrew_69e25680-9a16-41ed-ad47-e42d7b201b6a.jpg?v=1587042356">
              <div>
                <figcaption class="modal-title">아이스 아메리카노</figcaption>
                <span class="modal-price">2000원</span>
              </div>
            </figure>
          </li>
          <li class="modal-item">
            <button class="btn btn-size-up"><i class="fa fa-coffee" aria-hidden="true"></i> 사이즈 업</button>
            <span class="size-up-price">1000원</span>
            <button class="btn btn-addshot"><i class="fa fa-coffee" aria-hidden="true"></i> 샷 추가</button>
            <span class="size-up-price">1000원</span>
          </li>
          <li class="modal-item">
            <button class="btn-order">주문 담기</button>
            <button class="btn-close">취소</button>
          </li> -->
          </ul>
        </div>
      </div>
    </main>
    <!-- footer 주문 내역 영역 -->
    <footer class="footer">
      <div class="remaining-time-container">
        남은시간 <span class="remaining-time"></span>초
      </div>
      <ul class="order-list">
        <!-- `<li id="${id}" class="order-item">
        <i class="remove-item far fa-times-circle"></i>
        <span class="item-name">${menuName}</span>
        <span class="item-price">${price}원</span>
        </li>` -->
      </ul>
      <div class="selected-item-container">
        선택한 상품 <span class="selected-item-num"></span>
      </div>
      <button class="order-btn order-btn-invalid">
        <span class="total-price"></span> 결제하기
      </button>
      <button class="delete-all-items">전체삭제</button>

      <!-- 결제 내역 모달 영역 -->
      <div class="pay-modal-container modal-invisible">
        <div class="pay-modal">
          <h3 class="pay-modal-heading">주문리스트</h3>
          <p class="pay-modal-text"><span>주문리스트</span>를 확인해 주세요.</p>

          <div class="pay-list-container">
            <div class="pay-list-head">
              <span>메뉴</span>
              <span>가격</span>
            </div>

            <ul class="pay-list">
              <!-- `<li id="${id}" class="pay-item">
            <span class="item-name">${item}</span>
            <span><span class="item-price">${price}</span>원</span>
          </li>` -->
            </ul>
          </div>

          <div class="pay-result">
            <span>총 수량 <span class="total-item-num"></span></span>
            <span>총 결제금액 <span class="total-item-price"></span></span>
          </div>
          <div>
            <button class="pay-result-check">확 인</button>
            <button class="pay-result-cancel">취 소</button>
          </div>
        </div>
      </div>
    </footer>

    <!-- RASA Chat Widget -->
    <div id="rasa-chat-widget"></div>
    
    <!-- Load Rasa WebChat script -->
    <script>
      !(function () {
        let e = document.createElement("script"),
          t = document.head || document.getElementsByTagName("head")[0];
        (e.src =
          "https://cdn.jsdelivr.net/npm/rasa-webchat@1.0.0/lib/index.js"), // 최신 버전으로 변경
          (e.async = !0),
          (e.onload = () => {
            window.WebChat.default(
              {
                customData: { language: "en" },
                socketUrl: "https://19fe-221-146-62-69.ngrok-free.app", // 정확한 ngrok URL 사용
                socketPath: "/socket.io/",
                title: "Rasa bot",
                subtitle: "Get It, Make It.",
                showMessageDate: true,
                inputTextFieldHint: "Type Hi",
              },
              null
            );
          }),
          t.insertBefore(e, t.firstChild);
      })();
    </script>
    
    <!-- Ensure JavaScript bundle is loaded last -->
    <script defer src="dist/js/bundle.js"></script>
  </body>
</html>

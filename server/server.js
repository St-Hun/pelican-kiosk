const express = require("express");
const path = require("path");
const axios = require("axios");

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware to parse JSON requests
app.use(express.json());

// Serve static files for the client
app.use(express.static(path.join(__dirname, "../client")));

// Serve images from the 'add_img' directory
app.use("/add_img", express.static(path.join(__dirname, "add_img")));

// Menu data
let data = {
  iceMenu: [
    {
      id: 1,
      menuName: "아이스 아메리카노",
      imgUrl: "/add_img/ice_americano.jpg",
      price: 2500,
      active: true,
      shot: true,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 2,
      menuName: "아이스 라떼",
      imgUrl: "/add_img/ice_latte.jpg",
      price: 3500,
      active: false,
      shot: true,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 3,
      menuName: "아이스 카페모카",
      imgUrl: "/add_img/iced_cafemocha.jpg",
      price: 4500,
      active: false,
      shot: true,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 4,
      menuName: "아이스 초코",
      imgUrl: "/add_img/iced_chocolate.jpg",
      price: 3000,
      active: false,
      shot: false,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 5,
      menuName: "아이스 프라프치노",
      imgUrl: "/add_img/iced_frappuccino.jpg",
      price: 5500,
      active: false,
      shot: true,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 6,
      menuName: "아이스 그린티 라떼",
      imgUrl: "/add_img/iced_greentea_latte.jpg",
      price: 4500,
      active: false,
      shot: false,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 7,
      menuName: "아이스 바닐라 라떼",
      imgUrl: "/add_img/ice_vanlia_latte.jpg",
      price: 6500,
      active: false,
      shot: true,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
  ],
  hotMenu: [
    {
      id: 1,
      menuName: "아메리카노",
      imgUrl: "/add_img/americano.jpg",
      price: 2000,
      active: false,
      shot: true,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 2,
      menuName: "라떼",
      imgUrl: "/add_img/latte.jpg",
      price: 3000,
      active: true,
      shot: true,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 3,
      menuName: "캐모마일 티",
      imgUrl: "/add_img/chamomile_tea.jpg",
      price: 4000,
      active: true,
      shot: false,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 4,
      menuName: "유자차",
      imgUrl: "/add_img/yuza_tea.jpg",
      price: 5000,
      active: true,
      shot: false,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
  ],
  seasonMenu: [
    {
      id: 1,
      menuName: "골드망고 스무디",
      imgUrl: "/add_img/mango.jpg",
      price: 4000,
      active: true,
      shot: false,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 2,
      menuName: "코코넛 커피 스무디",
      imgUrl: "/add_img/coconet_coffee.jpg",
      price: 4800,
      active: false,
      shot: true,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 3,
      menuName: "망고 코코넛 주스",
      imgUrl: "/add_img/mango_coconut_juice.jpg",
      price: 3800,
      active: false,
      shot: false,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 4,
      menuName: "망고 히비스 커스티",
      imgUrl: "/add_img/mango_hibiscus_tea.jpg",
      price: 5800,
      active: false,
      shot: false,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 5,
      menuName: "딸기 쿠키 프라페",
      imgUrl: "/add_img/strawberry_cookie_frappe.jpg",
      price: 4900,
      active: false,
      shot: false,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 6,
      menuName: "흑당 버블 라떼",
      imgUrl: "/add_img/brownsugar_bubble_latte.jpg",
      price: 4800,
      active: false,
      shot: true,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
    {
      id: 7,
      menuName: "흑당 라떼",
      imgUrl: "/add_img/brownsugar_latte.jpg",
      price: 5000,
      active: false,
      shot: true,
      shotPrice: 1000,
      sizeUpPrice: 1000,
    },
  ],
};

// Endpoints to get the entire menu
app.get("/data", (req, res) => {
  res.send(data);
});

app.get("/icemenu", (req, res) => {
  res.send(data.iceMenu);
});

app.get("/hotmenu", (req, res) => {
  res.send(data.hotMenu);
});

app.get("/seasonmenu", (req, res) => {
  res.send(data.seasonMenu);
});

// Endpoints to get menu items by ID
app.get("/icemenu/:id", (req, res) => {
  const id = +req.params.id;
  const menu = data.iceMenu.find((menu) => menu.id === id);
  res.send(menu);
});

app.get("/hotmenu/:id", (req, res) => {
  const id = +req.params.id;
  const menu = data.hotMenu.find((menu) => menu.id === id);
  res.send(menu);
});

app.get("/seasonmenu/:id", (req, res) => {
  const id = +req.params.id;
  const menu = data.seasonMenu.find((menu) => menu.id === id);
  res.send(menu);
});

// Endpoints to add new menu items
app.post("/icemenu", (req, res) => {
  data.iceMenu = [...data.iceMenu, req.body];
  res.send(data.iceMenu);
});

app.post("/hotmenu", (req, res) => {
  data.hotMenu = [...data.hotMenu, req.body];
  res.send(data.hotMenu);
});

app.post("/seasonMenu", (req, res) => {
  data.seasonMenu = [...data.seasonMenu, req.body];
  res.send(data.seasonMenu);
});

// Chatbot endpoint to interact with Rasa
app.post("/chat", async (req, res) => {
  const { message, sender } = req.body;

  try {
    const response = await axios.post(
      "http://localhost:5005/webhooks/rest/webhook",
      {
        sender: sender,
        message: message,
      }
    );
    res.json(response.data);
  } catch (error) {
    res.status(500).send(error);
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

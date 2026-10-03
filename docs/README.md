# Kyrgyz4x4rentals

Одностраничный сайт (landing page) для компании по аренде подготовленных экспедиционных внедорожников 4x4 в Кыргызстане.

## О проекте

Сайт представляет автопарк из 5 внедорожников (Toyota Land Cruiser 100 ×2, Lexus LX 470 ×2, Lexus GX 470), оснащённых палатками на крыше и полным туристическим снаряжением.

## Технологии

- **HTML5** — семантическая разметка
- **CSS3** — переменные, Grid, Flexbox, анимации
- **Vanilla JavaScript** — без фреймворков
- **Font Awesome 6.4** — иконки
- **Google Fonts** — Plus Jakarta Sans, Space Grotesk

## Структура проекта

```
Kyrgyz4x4rentals/
├── index.html          # Единственный файл сайта (HTML + CSS + JS)
├── img/                # Фотографии автомобилей
│   ├── lc100 n1.jfif   # Toyota LC 100 #1
│   ├── lc100 n2.jfif   # Toyota LC 100 #2
│   ├── lx470 n1.jfif   # Lexus LX 470 #1
│   ├── lx470 n2.jfif   # Lexus LX 470 #2
│   └── gx460.jfif      # Lexus GX 470
└── docs/               # Документация
    ├── README.md
    ├── ARCHITECTURE.md
    ├── IMPLEMENTATION_PLAN.md
    ├── DEVELOPMENT_GUIDE.md
    └── DEPLOYMENT.md
```

## Быстрый старт

1. Откройте `index.html` в любом современном браузере
2. Или запустите локальный сервер:
   ```bash
   npx serve .
   # или
   python -m http.server 8000
   ```

## Разделы документации

- [Архитектура](./ARCHITECTURE.md) — структура и устройство сайта
- [План реализации](./IMPLEMENTATION_PLAN.md) — текущий статус и дорожная карта
- [Руководство по разработке](./DEVELOPMENT_GUIDE.md) — как вносить изменения
- [Деплой](./DEPLOYMENT.md) — как опубликовать сайт

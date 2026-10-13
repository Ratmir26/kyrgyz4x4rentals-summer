# Деплой

## Локальный просмотр

```bash
# Python
python -m http.server 8000

# Node.js
npx serve .
```

## Перед публикацией (обязательно)

```bash
python build.py
# должен вывести: OK: N keys per language, M data-lang usages covered
# без FAIL — иначе в деплой уйдёт index.html со старым словарём
```

После деплоя GitHub Pages и браузер кэшируют страницу ~10 минут. Проверяй свежую версию через инкогнито или параметр `?v=число`, иначе увидишь старый текст переводов.

## Публикация

### GitHub Pages
1. Загрузите файлы в репозиторий
2. Settings → Pages → выбрать ветку
3. Сайт доступен по адресу `https://username.github.io/repo/`

### Netlify
1. Перетащите папку в [Netlify Drop](https://app.netlify.com/drop)
2. Сайт опубликован мгновенно

### Vercel
1. Импортируйте репозиторий в [Vercel](https://vercel.com)
2. Деплой произойдёт автоматически

## Оптимизация перед запуском

- [ ] Сжать фотографии (рекомендуемый формат: WebP)
- [ ] Проверить отображение на мобильных устройствах
- [ ] Проверить ссылки на мессенджеры
- [x] Добавить favicon
- [ ] Протестировать калькулятор

## Домен kyrgyz4x4rentals.com + SEO

SEO-пакет в коде: title/description/keywords, canonical, hreflang ru/en/x-default (`?lang=` ссылки рабочие), OG + Twitter Card (картинка `img/lx470-n1.jfif`), `robots.txt` (admin закрыт), `sitemap.xml`. Мета title/description/og переключаются со словарём; twitter-теги статичны (краулеры JS не выполняют).

Шаги запуска:
1. Купить домен (платит владелец по команде Ratmir).
2. Привязать: GitHub Pages → Settings → Pages → Custom domain (или Vercel → Domains — решение о переезде за владельцем). Включить HTTPS.
3. Проверить: `https://kyrgyz4x4rentals.com/` открывается с замком, `.../robots.txt` и `.../sitemap.xml` отдаются.
4. Google Search Console: подтвердить владение, загрузить sitemap, запросить обход. OG-картинка заработает только после привязки домена (до этого 404 — ожидаемо).

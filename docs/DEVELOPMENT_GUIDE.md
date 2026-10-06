# Руководство по разработке

## Добавление нового автомобиля

1. Скопируйте блок карточки в секции `#cars`
2. Замените путь к изображению в `src="img/ваше-фото.jfif"`
3. Обновите `alt`, `car-badge`, `car-title`
4. При необходимости измените характеристики в `.car-specs-list`

```html
<div class="car-card">
    <div class="car-image-container">
        <span class="car-badge">Название</span>
        <img class="car-photo" src="img/photo.jfif" alt="Название">
    </div>
    <div class="car-info">
        <h3 class="car-title">Название</h3>
        <div class="car-specs-list">
            <div class="spec-item"><i class="fa-solid fa-gauge-high"></i> <span>4.7L</span></div>
            <div class="spec-item"><i class="fa-solid fa-gas-pump"></i> <span>Бензин</span></div>
            <div class="spec-item"><i class="fa-solid fa-calendar"></i> <span>2020</span></div>
            <div class="spec-item"><i class="fa-solid fa-campground"></i> <span>Палатка</span></div>
        </div>
        <a href="#pricing" class="btn btn-primary">Забронировать</a>
    </div>
</div>
```

5. Добавьте автомобиль в `<select id="carSelect">` в калькуляторе

## Замена фотографии

Поместите файл в папку `img/` и обновите `src` у соответствующего `<img class="car-photo">`.

**Важно:** Фото будет автоматически масштабироваться через `object-fit: cover`. Рекомендуемое соотношение сторон — как у контейнера (примерно 320×240px или шире).

## Изменение текстов (i18n)

Переводы живут в JSON-файлах — это источник правды:
- `locales/ru.json` — русские строки
- `locales/en.json` — английские строки

Элементы для локализации имеют атрибут `data-lang="ключ"`. Договор аренды всегда на английском (требование владельца) и ключей не имеет.

После любых правок JSON обязательно пересобери словарь в `index.html`:
```bash
python build.py
```
Скрипт проверит паритет ключей ru/en и покрытие всех `data-lang`, затем впишет словарь в `index.html`. Без этого сайт будет использовать старый текст.

Вайтлист (не переводится, багом не считается): имена Toyota/Lexus/Kyrgyz4x4rentals, домен Kyrgyz4x4rentals.com, единицы 4.7L/4WD/€/USD, мессенджеры WhatsApp/Telegram/Instagram/Email, топонимы запретных зон, модалка договора (всегда EN по требованию владельца).

## Изменение стилей

CSS-переменные находятся в блоке `:root` (цвета, отступы, тени). Стили карточек — в блоке `.car-card`.

## Переключение темы

Добавьте в `<html>` атрибут `data-theme="light"` или `data-theme="dark"`. Кнопка в шапке переключает автоматически.

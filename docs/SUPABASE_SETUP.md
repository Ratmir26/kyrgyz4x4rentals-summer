# Supabase Setup (отзывы + регистрация)

Пошаговая инструкция для владельца репозитория. Выполняется один раз.

## 1. Создать проект

1. Зарегистрироваться на https://supabase.com (бесплатный тариф).
2. New project → имя `kyrgyz4x4rentals` → придумать пароль БД → регион ближе к Центральной Азии (например, Singapore / Frankfurt).
3. Дождаться запуска проекта (~2 минуты).

## 2. Таблица отзывов (SQL Editor → New query → Run)

```sql
create table public.reviews (
  id bigint generated always as identity primary key,
  user_id uuid references auth.users(id) on delete set null,
  name text not null,
  text text not null,
  rating int not null check (rating between 1 and 5),
  photo_url text check (photo_url is null or photo_url like '%/storage/v1/object/public/review-photos/%'),
  approved boolean not null default false,
  created_at timestamptz not null default now()
);
alter table public.reviews enable row level security;

-- читать всем только одобренные
create policy "read approved reviews"
on public.reviews for select using (approved = true);

-- вставлять только вошедшим, за себя, самомодерация запрещена
create policy "insert own review"
on public.reviews for insert
with check (auth.uid() = user_id and approved = false);
```

Одобрение отзывов: Table Editor → таблица `reviews` → колонка `approved` → поставить `true`.
Удаление чужих/неприличных — там же (Delete row). Отдельной админки на сайте в MVP нет.

## 3. Хранилище фото

Storage → New bucket → имя `review-photos`, Public: **ON**. Затем SQL Editor:

```sql
create policy "public read review-photos"
on storage.objects for select using (bucket_id = 'review-photos');

create policy "upload own review photo"
on storage.objects for insert
with check (bucket_id = 'review-photos' and auth.uid()::text = split_part(name, '/', 1));
```

## 4. Вход без подтверждения email

Authentication → Providers → Email → **Confirm email: OFF**.
(От спама защищает ручное одобрение отзывов.)

## 5. Вставить ключи в сайт

Project Settings → API: скопировать `Project URL` и `anon public` ключ.
В `index.html` заменить плейсхолдеры:
- `PASTE_SUPABASE_URL_HERE` → Project URL
- `PASTE_SUPABASE_ANON_KEY_HERE` → anon public ключ

`service_role` ключ НИКОГДА не вписывать в код сайта. Затем `python build.py`, проверка, push.

Без заменённых ключей секция отзывов показывает заглушку, остальной сайт работает.

# Supabase для админки (машины + тексты)

Одноразовая настройка владельцем репозитория. Выполняется один раз.

## 1. Проект

1. https://supabase.com → New project → имя `kyrgyz4x4rentals` (бесплатный тариф).
2. Дождаться запуска (~2 минуты).

## 2. Схема + права (SQL Editor → New query → Run целиком)

```sql
create extension if not exists "pgcrypto";

create table if not exists public.cars (
  id uuid primary key default gen_random_uuid(),
  title text,
  badge text,
  photo_url text,
  color_ru text,
  color_en text,
  sort_order int,
  is_visible boolean default true,
  created_at timestamptz default now()
);

create table if not exists public.site_content (
  key text primary key,
  value_ru text,
  value_en text,
  updated_at timestamptz default now()
);

insert into public.site_content (key, value_ru, value_en) values
  ('price_rate1', 'Для 2 путешественников (палатка на крыше + весь комплект снаряжения)', 'For 2 travelers (Rooftop tent + full equipment)'),
  ('price_rate2', 'Если более 2-х путешественников (в комплект добавляется обычная палатка)', 'For >2 travelers (Additional ground tent included)'),
  ('price_min_days', 'Минимальный срок аренды: <b>5 дней</b>', 'Minimum rental period: <b>5 days</b>'),
  ('price_deposit', 'Залог / страховая франшиза: <b>800€</b>', 'Deductible / Security Deposit: <b>800€</b>'),
  ('terms_i1', '<b>Франшиза (депозит):</b> 800€.', '<b>Deductible:</b> 800 euro.'),
  ('terms_i2', '<b>Условие возврата депозита:</b> Если при возврате машины не выявится нарушений ПДД, штрафов и повреждений кузова/интерьера, залог возвращается клиенту в полном объёме (800€) при завершении поездки! Если выявляются нарушения, царапины или штрафы — соответствующая сумма вычитается (минусуется) из депозита.', '<b>Deposit return condition:</b> If no traffic violations, fines, or body/interior damage are found upon return, the deposit is returned to the client in full (800€) upon completion of the trip! If violations, scratches, or fines are found, the corresponding amount is deducted from the deposit.'),
  ('terms_g10', '<b>Регионы приема/сдачи:</b> Приём и возврат машины в других регионах помимо Бишкека обсуждаются индивидуально с клиентом при обращении по контактам.', '<b>Pick-up / Return regions:</b> Pick-up and return of the vehicle in regions other than Bishkek is discussed individually with the client upon contact.'),
  ('price_region_note', 'Прием/сдача авто в других регионах обговаривается индивидуально (свяжитесь с нами).', 'Pick-up / Return in other regions is discussed individually.')
on conflict (key) do nothing;

insert into public.cars (title, badge, photo_url, color_ru, color_en, sort_order, is_visible) values
  ('Toyota Land Cruiser 100 #1', 'Toyota TLC 100', 'img/lc100 n1.jfif', 'Черный', 'Black', 10, true),
  ('Toyota Land Cruiser 100 #2', 'Toyota TLC 100', 'img/lc100 n2.jfif', 'Серый', 'Gray', 20, true),
  ('Lexus LX 470 #1', 'Lexus LX 470', 'img/lx470 n1.jfif', 'Белый', 'White', 30, true),
  ('Lexus LX 470 #2', 'Lexus LX 470', 'img/lx470 n2.jfif', 'Черный', 'Black', 40, true),
  ('Lexus GX 470', 'Lexus GX 470', 'img/gx460.jfif', 'Серый', 'Gray', 50, true);

alter table public.cars enable row level security;
alter table public.site_content enable row level security;

drop policy if exists "cars public visible" on public.cars;
create policy "cars public visible" on public.cars
  for select to anon, authenticated using (is_visible = true);
drop policy if exists "cars auth all" on public.cars;
create policy "cars auth all" on public.cars
  for select to authenticated using (true);
drop policy if exists "cars auth insert" on public.cars;
create policy "cars auth insert" on public.cars
  for insert to authenticated with check (true);
drop policy if exists "cars auth update" on public.cars;
create policy "cars auth update" on public.cars
  for update to authenticated using (true) with check (true);
drop policy if exists "cars auth delete" on public.cars;
create policy "cars auth delete" on public.cars
  for delete to authenticated using (true);

drop policy if exists "content public" on public.site_content;
create policy "content public" on public.site_content
  for select to anon, authenticated using (true);
drop policy if exists "content auth insert" on public.site_content;
create policy "content auth insert" on public.site_content
  for insert to authenticated with check (true);
drop policy if exists "content auth update" on public.site_content;
create policy "content auth update" on public.site_content
  for update to authenticated using (true) with check (true);
drop policy if exists "content auth delete" on public.site_content;
create policy "content auth delete" on public.site_content
  for delete to authenticated using (true);
```

## 3. Хранилище фото

Storage → New bucket → `car-photos`, Public: **ON**. Политики `storage.objects`:
- SELECT: `bucket_id = 'car-photos'` (все)
- INSERT/UPDATE/DELETE: `authenticated`, путь `{user_id}/{timestamp}.{ext}`

## 4. Вход только для своих

1. Authentication → Providers → Email → **Allow new signups: OFF** (регистрация закрыта).
2. Users → Add user → email + сложный пароль админа. Данные для входа передать другу лично (не в чат сайта).

## 5. Ключи в сайт

Project Settings → API: `Project URL` + `anon public` ключ → вписать вместо
`PASTE_SUPABASE_URL_HERE` / `PASTE_SUPABASE_ANON_KEY_HERE` в `index.html` и `admin.html`.
`service_role` НИКОГДА не вписывать. Затем `python build.py`, проверка, push.

## 6. Как пользуется друг

Открывает `.../admin.html` на телефоне → входит → вкладки «Машины» (добавить/изменить/удалить, фото, видимость) и «Тексты» (тарифы, залог, сроки, часть условий) → «Проверить на сайте». Если на сайте старый текст — hard-refresh (обновить дважды).

Для проектування CRM-системи, подібної до Jira або TestRail, важливо орієнтуватися не стільки на фізичну діагональ монітора, скільки на **роздільну здатність екрана** та **viewport** (реальну робочу область браузера).

Ось актуальні дані на 2026 рік для вашого дизайн-проекту:

## 1. Десктопна версія (Основна робоча область)

Для систем з великою кількістю таблиць, графіків та бокових панелей (як у Jira), найпоширенішим стандартом залишається **Full HD**, але бізнес-сегмент активно переходить на вищу чіткість.

* **Найвживаніша роздільна здатність:** **1920 × 1080 (Full HD)**. Це база, на яку припадає понад 60-70% корпоративних користувачів.
* **Трендова роздільна здатність:** **2560 × 1440 (QHD)**. Користувачі CRM часто використовують 27-дюймові монітори, де ця роздільна здатність є «золотою серединою» для багатозадачності.
* **Діагоналі моніторів:** * **24"** (зазвичай 1080p) — офісний стандарт.
    * **27"** (1440p) — стандарт для розробників та менеджерів.

**Порада для дизайну:** Використовуйте **гумову верстку (Fluid Layout)**. Мінімальна ширина, при якій інтерфейс має виглядати ідеально без горизонтального скролу — **1280px**.

---

## 2. Мобільна версія (Для перегляду звітів)

Оскільки ви плануєте лише перегляд звітів, фокусуйтеся на вертикальному скролі та компактних картках замість широких таблиць.

* **Найпоширеніші роздільні здатності (Viewport):**
    * **390 × 844 / 430 × 932** (iPhone 13-16 Pro/Max).
    * **360 × 800** (популярні моделі Android).
* **На які цифри орієнтуватись:**
    * **360px — 390px**: Ширина для проектування «вузького» мобільного екрана.
    * **414px — 430px**: Ширина для великих смартфонів (Max/Plus/Ultra).

---

## Шпаргалка по Breakpoints (Точки перелому)

При проектуванні в Figma або аналогічних інструментах, орієнтуйтеся на ці ключові точки:

| Тип пристрою | Ширина (px) | Цільове використання |
| :--- | :--- | :--- |
| **Mobile** | **360 – 480** | Перегляд звітів, сповіщення. |
| **Tablet / Small Laptop** | **768 – 1024** | Базова робота з документами (iPad). |
| **Desktop (Base)** | **1280 – 1440** | Стандартний ноутбук (MacBook Air/Pro 13"). |
| **Desktop (Large)** | **1920+** | Повноцінна робота з CRM, дешборди. |

**Важливий нюанс для CRM:** Враховуйте **"sidebar"** (бокову панель). У системах типу Jira вона займає 240–280px. Ваша робоча область для документів на 13-дюймовому ноутбуці (1280px) залишиться в межах ~1000px. Це критично для проектування таблиць.


ЗАПИТ ДО АІ
Ось запит, спеціально структурований для Figma AI або Figma дизайнера, щоб згенерувати порожні фрейми (макети) з потрібними налаштуваннями:

---

### Запит (Prompt) для Figma AI / Дизайнера

**Subject:** Create a multi-device UI starter project structure for a Document CRM system.

**Objective:** Generate a clean Figma canvas with named Frames for three key pages, across four standard screen resolutions (Breakpoints), optimized for a Jira-like professional interface.

**Required Deliverables:**
A single Figma canvas containing 12 organized, empty Frames (3 pages × 4 resolutions). Each Frame must be labeled with the Page Name and Resolution.

**Technical Specifications (Resolutions & Device Types):**

1.  **Mobile (Portrait)**:
    * **Resolution:** 390 × 844 px
    * **Use Case:** Report viewing.
2.  **Tablet (Portrait/Small Laptop)**:
    * **Resolution:** 834 × 1194 px
    * **Use Case:** Basic interaction (e.g., iPad Pro 11").
3.  **Desktop (Standard/Compact)**:
    * **Resolution:** 1440 × 900 px
    * **Use Case:** Base design, MacBook standard.
4.  **Desktop (Professional/Large)**:
    * **Resolution:** 1920 × 1080 px
    * **Use Case:** Full-HD CRM workspace (Primary Target).

**Pages to Create (Names for Frames):**

1.  **Page 1: Login** (e.g., "1. Login - Desktop Large", "1. Login - Mobile")
2.  **Page 2: Dashboard (Home)** (e.g., "2. Dashboard - Desktop Standard")
3.  **Page 3: Document Workspace** (e.g., "3. Doc Workspace - Tablet")

**Constraints (Crucial):**
* **DO NOT GENERATE ANY UI ELEMENTS:** No buttons, no forms, no text fields, no placeholders, no images. The frames must be completely empty.
* **DO NOT DEFINE STYLES:** Do not apply any colors, backgrounds, or specific fonts to the frames. Leave them white/transparent with default gray borders.
* **ORGANIZATION:** Arrange frames logically on the canvas: group by Page Name vertically, and by Resolution horizontally (e.g., Column 1 = all Login resolutions).

**Purpose of this Request:** To establish a purely structured layout based on real-world usage data, allowing me to define typography, color palette, and background images later without pre-existing content.
**Purpose of this Request:** To establish a purely structured layout based on real-world usage data, allowing me to define typography, color palette, and background images later without pre-existing content.
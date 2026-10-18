# Навыки и плагины для Claude — на русском

Готовые навыки для Claude с описаниями на русском: соцсети и Instagram, монтаж видео по ссылке, маркетинг, дизайн, данные, разработка, финансы, генерация видео и картинок. Каждый навык скачивается отдельным zip-файлом и ставится в Claude за минуту.

**Главная фишка — навык [`montazh-po-ssylke`](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/montazh-po-ssylke.zip):** присылаете ссылку на видео или файл, а Claude сам расшифровывает речь, находит сильные моменты и собирает готовые Reels/Shorts 9:16 в вашем стиле: без пауз, с субтитрами, хуком на экране, логотипом, музыкой и обложкой.

## Как установить навык (claude.ai и приложение Claude)

1. Скачайте zip нужного навыка из таблицы ниже (или со страницы [Releases](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest)). Распаковывать не нужно.
2. В Claude откройте **Настройки → Возможности** и включите выполнение кода и создание файлов — без этого навыки не работают.
3. Там же в разделе **Навыки** нажмите «Загрузить навык» и выберите zip. Каждый навык загружается отдельно.
4. Проверьте, что навык включён, и просто попросите Claude о задаче — он сам подхватит нужный навык.

Названия разделов могут немного отличаться в зависимости от версии и тарифа Claude.

## Как установить всё сразу (Claude Code)

```
/plugin marketplace add pohnah000-byte/skill-claude-inst
/plugin install moi-navyki@ru-plugins
```

Вместо `moi-navyki` можно поставить любой плагин из папки `plugins/`.

## Список навыков

### Мои навыки: соцсети, Instagram и монтаж

Мои навыки на русском: разбор блогеров и конкурентов, комментарии, тренды, «залётные» посты, спрос на продукт (набор ScrapeCreators), Instagram-контент (рилс, карусели, подписи, профиль, план, переупаковка), режим «учусь, пока строю» VibeWise и монтаж видео по ссылке в моём стиле.

| Навык | Что делает | Скачать |
|---|---|---|
| `ad-library-teardown` | Разбор рекламы конкурентов из библиотек объявлений Meta/Facebook, Google и LinkedIn: сообщения, хуки, офферы, призывы к действию, расшифровки видеорекламы, о… | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/ad-library-teardown.zip) |
| `audience-research` | Оценка аудитории блогера, инфлюенсера или бренда по открытым данным: сигналы профиля, демография аудитории TikTok, подписчики и подписки, комментарии, геогра… | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/audience-research.zip) |
| `comment-mining` | Анализ комментариев и ответов под публичными постами и видео: реакции аудитории, живой язык клиентов, вопросы, возражения, жалобы, идеи продуктов, готовность… | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/comment-mining.zip) |
| `competitor-social-research` | Исследование соцсетей конкурентов: сравнение брендов и блогеров, что работает в нише, пробелы в контенте и практичный бриф со стратегией по открытым данным. | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/competitor-social-research.zip) |
| `content-repurposing` | Переработка контента: превращает публичные видео, расшифровки, посты или разбор блогеров в новые материалы — посты для LinkedIn, треды для X, сценарии коротк… | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/content-repurposing.zip) |
| `creator-profile-teardown` | Разбор аккаунта блогера, инфлюенсера, основателя или бренда: позиционирование, рубрики, «залётные» посты, хуки, форматы, реакция аудитории и что можно взять … | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creator-profile-teardown.zip) |
| `ig-caption` | Подпись к посту Instagram на русском: первая строка, которая переживает обрезку «… ещё», текст, один призыв, поисковые слова и до 5 хэштегов, с проверкой скр… | [zip, 12 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/ig-caption.zip) |
| `ig-carousel` | Карусель для Instagram на русском: обложка, ради которой листают, текст по слайдам и файлы 1080×1350. | [zip, 6 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/ig-carousel.zip) |
| `ig-plan` | План недели в Instagram на русском: что публиковать, в каком формате, когда и с кем взаимодействовать. | [zip, 6 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/ig-plan.zip) |
| `ig-profile` | Оценка профиля Instagram по 12 пунктам из 100 и переписывание того, что теряет баллы: поле имени, шапка, ссылка, актуальное, закреплённые посты, сетка. | [zip, 7 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/ig-profile.zip) |
| `ig-reel` | Сценарий рилс для Instagram из сырой идеи на русском: три хука по 26 формулам с оценкой, текст для речи, текст на экран и тайминг по битам. | [zip, 32 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/ig-reel.zip) |
| `ig-repurpose` | Превращает один длинный материал (видео, эфир, подкаст, пост Boosty, статью, расшифровку) в неделю рилс и каруселей на русском. | [zip, 6 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/ig-repurpose.zip) |
| `ig-viral` | Поиск рилс, которые сейчас реально работают в нише автора: рейтинг по тому, во сколько раз ролик обогнал свой же аккаунт, формула хука каждого и банк хуков, … | [zip, 29 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/ig-viral.zip) |
| `influencer-prospecting` | Поиск блогеров, инфлюенсеров, партнёров и аккаунтов в нише для коллабораций, рекламы, UGC, рассылки продукта или исследования конкурентов. | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/influencer-prospecting.zip) |
| `montazh-po-ssylke` | Монтаж видео «под меня» по ссылке или файлу: скачивает ролик, расшифровывает речь, находит сильные моменты, режет паузы и собирает готовые Reels/Shorts/TikTo… | [zip, 15 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/montazh-po-ssylke.zip) |
| `outlier-post-finder` | Поиск «залётных» постов, видео, рилс, шортс и твитов, которые сработали лучше обычного для автора, бренда или конкурента: объясняет, почему они сработали, вы… | [zip, 3 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/outlier-post-finder.zip) |
| `product-demand-research` | Проверка идеи продукта по открытым данным: боли аудитории, сигналы спроса, возражения и живой язык клиентов из Reddit, постов, расшифровок видео и комментариев. | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/product-demand-research.zip) |
| `scrapecreators-api` | Сбор открытых данных с 27+ соцсетей через REST API ScrapeCreators (нужен платный ключ SCRAPECREATORS_API_KEY): TikTok, Instagram, YouTube, LinkedIn, Facebook… | [zip, 5 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/scrapecreators-api.zip) |
| `social-listening-brief` | Мониторинг соцсетей: что люди говорят о бренде, человеке, продукте, теме или нише на открытых площадках. | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/social-listening-brief.zip) |
| `transcript-intelligence` | Расшифровки видео из TikTok, Instagram, YouTube, Facebook, X/Twitter, LinkedIn, Rumble и Reddit: краткое содержание, разбор и переработка. | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/transcript-intelligence.zip) |
| `trend-discovery` | Поиск трендов в нише: темы, хэштеги, звуки, посты, рилс, шортс, блогеры и форматы. | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/trend-discovery.zip) |
| `vibe-wise-learn` | Learning-first development mode (VibeWise). | [zip, 9 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/vibe-wise-learn.zip) |

### adobe-for-creativity

Инструменты Adobe Creative Cloud для фото, векторов, дизайна и видео: пакетное редактирование, адаптация под разные площадки, многошаговые творческие задачи с аккуратным результатом.

| Навык | Что делает | Скачать |
|---|---|---|
| `adobe` | Экскурсия по коннектору Adobe: какие возможности есть, пример задачи для каждой и какой продукт Adobe за ней стоит. | [zip, 4 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe.zip) |
| `adobe-anydocx` | ОБЯЗАТЕЛЬНО, если для задачи с Word/DOCX исходник — загруженный PDF (даже если текст PDF уже виден в разговоре). | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe-anydocx.zip) |
| `adobe-anyexcel` | ОБЯЗАТЕЛЬНО, если для задачи с Excel/XLSX исходник — загруженный PDF (даже если текст или таблицы PDF уже видны в разговоре). | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe-anyexcel.zip) |
| `adobe-anypdf` | ОБЯЗАТЕЛЬНО для любой задачи с PDF (файл .pdf, «PDF», сжать/уменьшить размер, объединить, разделить, извлечь/повернуть/переставить/удалить страницы, распозна… | [zip, 4 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe-anypdf.zip) |
| `adobe-anypptx` | ОБЯЗАТЕЛЬНО, если для задачи с PowerPoint/PPTX исходник — загруженный PDF (даже если текст PDF уже виден в разговоре). | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe-anypptx.zip) |
| `adobe-batch-edit-photos` | Единая обработка серии фото, чтобы они выглядели как отредактированные вместе. | [zip, 13 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe-batch-edit-photos.zip) |
| `adobe-create-pdfs-from-data` | Слияние данных в InDesign: таблица CSV/TSV + шаблон .indd (или PDF, который автоматически переводится в .indd). | [zip, 5 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe-create-pdfs-from-data.zip) |
| `adobe-create-social-variations` | Подгоняет фото или видео под соцсети инструментами Adobe Creative Cloud: меняет размер, кадрирует, экспортирует для Instagram, TikTok, LinkedIn, Facebook, Yo… | [zip, 8 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe-create-social-variations.zip) |
| `adobe-design-from-template` | Любой дизайн по шаблонам Adobe Express: флаеры, постеры, посты для соцсетей (Instagram, Facebook, LinkedIn), визитки, приглашения, открытки, резюме, сопровод… | [zip, 6 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe-design-from-template.zip) |
| `adobe-design-to-pdf` | Находит шаблон Adobe Express, меняет текст или цвет фона и превращает в PDF для печати, подборку или ссылку для отправки. | [zip, 6 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe-design-to-pdf.zip) |
| `adobe-document-review` | Умный маркер для любого PDF: договоры, счета, медкарты, инструкции, резюме, отчёты, тексты. | [zip, 9 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe-document-review.zip) |
| `adobe-edit-quick-cut` | Динамичная нарезка лучших моментов из видео через Adobe Quick Cut — на запросы «сделай хайлайты», «нарезка лучшего», «быстрый монтаж», «вырежи лучшие моменты… | [zip, 6 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe-edit-quick-cut.zip) |
| `adobe-fonts` | Поиск и просмотр настоящих лицензируемых шрифтов Adobe Fonts: рекомендации под задачу, поиск по названию или признакам (словолитня, дизайнер, стиль), сведени… | [zip, 6 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe-fonts.zip) |
| `adobe-resize-photos-and-videos` | Меняет размер фото и видео до точных пикселей или соотношения сторон инструментами Adobe. | [zip, 10 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe-resize-photos-and-videos.zip) |
| `adobe-retouch-portraits` | Пакетная ретушь папки портретов инструментами Adobe — для свадебных и событийных фотографов, которым нужна быстрая обработка без участия. | [zip, 13 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/adobe-retouch-portraits.zip) |

### animation-studio

Рисованные анимационные мультфильмы: каждый кадр рисуется кодом, музыка синтезируется кодом и идеально совпадает с картинкой. На выходе готовый MP4 1080p — горизонтальный 16:9 или вертикальный 9:16 для Reels, TikTok и Shorts.

| Навык | Что делает | Скачать |
|---|---|---|
| `animation-studio` | Рисованный 2D-мультфильм с нуля: каждый кадр рисуется кодом, а музыка синтезируется кодом (или берётся ваша песня с анализом ритма) и синхронизируется по еди… | [zip, 2.6 МБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/animation-studio.zip) |

### appstore-screenshots

Автоматические скриншоты для App Store и Google Play (приложения на Expo/React Native): съёмка экранов через Maestro, рамки телефонов через fastlane, рекламные надписи через Pillow.

| Навык | Что делает | Скачать |
|---|---|---|
| `appstore-screenshots` | Автоматически делает скриншоты для App Store и Google Play (приложения на Expo/React Native, на Mac). | [zip, 10 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/appstore-screenshots.zip) |

### archgram — схемы архитектуры

Рисует архитектуру программного проекта в виде анимированной SVG-схемы по коду и документации — для README на GitHub.

| Навык | Что делает | Скачать |
|---|---|---|
| `archgram` | Рисует архитектуру программного проекта анимированной SVG-схемой с помощью archgram — для README и документации, по коду и докам. | [zip, 19 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/archgram.zip) |

### cowork-plugin-management

Создание и настройка собственных плагинов под ваши инструменты и процессы: подключение MCP-серверов, изменение поведения плагинов, адаптация шаблонов под то, как работает ваша команда.

| Навык | Что делает | Скачать |
|---|---|---|
| `cowork-plugin-customizer` | Настройка плагина Claude под инструменты и процессы конкретной команды или компании. | [zip, 11 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/cowork-plugin-customizer.zip) |
| `create-cowork-plugin` | Пошагово помогает создать новый плагин с нуля. | [zip, 17 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/create-cowork-plugin.zip) |

### creative-claw

Превращает фото товаров в рекламные видео и их варианты для TikTok, Instagram Reels и YouTube Shorts. Генерация картинок и видео (Nano Banana, Seedance, Gemini Omni), озвучка и синтез речи (ElevenLabs), музыка (Mureka). Видео из фото и из текста, клонирование голоса, звуковые эффекты, UGC-реклама, предметные фотосессии, постоянные персонажи и многосценовые ролики. После установки откройте вкладку «Коннекторы» плагина и войдите в Creative Claw.

| Навык | Что делает | Скачать |
|---|---|---|
| `creativeclaw` | Общий вход в Creative Claw для смешанных, неясных и многоформатных запросов и управления пространством. | [zip, 175 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw.zip) |
| `creativeclaw-build-film` | Полноценный многосценовый фильм в Creative Claw — от планирования до собранного первого монтажа. | [zip, 90 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-build-film.zip) |
| `creativeclaw-clone-voice` | Помогает записать, приватно загрузить, клонировать, проверить и использовать свой голос (с согласия владельца) через Cartesia или ElevenLabs. | [zip, 60 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-clone-voice.zip) |
| `creativeclaw-create-avatar` | Создаёт постоянный аватар человека или вымышленного персонажа по фото или описанию: генерирует и согласует лист персонажа в едином стиле, сохраняет его в «Пе… | [zip, 87 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-create-avatar.zip) |
| `creativeclaw-create-character` | Сохраняет, показывает или обновляет уже созданного постоянного персонажа Creative Claw и его внешний образ. | [zip, 43 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-create-character.zip) |
| `creativeclaw-create-reels` | Нарезает готовое длинное видео на цельные клипы для соцсетей в нужном формате, по желанию с субтитрами. | [zip, 22 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-create-reels.zip) |
| `creativeclaw-create-ugc-ad` | UGC-реклама товара по сценарию в стиле блогера через Creative Claw. | [zip, 90 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-create-ugc-ad.zip) |
| `creativeclaw-edit-media` | Монтаж готового видео или аудио в Creative Claw без перегенерации: обрезать, вырезать и переставить моменты, сменить размер или кадрирование, добавить субтит… | [zip, 23 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-edit-media.zip) |
| `creativeclaw-generate-image` | Создаёт или редактирует одно изображение в Creative Claw и выбирает подходящую модель. | [zip, 36 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-generate-image.zip) |
| `creativeclaw-generate-music` | Пишет музыку в Creative Claw: саундтреки, фоновые подложки, джинглы, короткие заставки, темы, инструменталы и песни с вокалом (Lyria 3.5, ElevenLabs Music, M… | [zip, 25 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-generate-music.zip) |
| `creativeclaw-generate-sound-effects` | Генерирует звуковые эффекты, шумы, атмосферу, петли, звуки интерфейса, переходы, удары и звуковые текстуры через ElevenLabs Sound Effects v2 в Creative Claw. | [zip, 21 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-generate-sound-effects.zip) |
| `creativeclaw-generate-video` | Создаёт, оживляет, продлевает, перекадрирует или преобразует один видеоклип в Creative Claw. | [zip, 92 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-generate-video.zip) |
| `creativeclaw-generate-voiceover` | Озвучка в Creative Claw: закадровый текст, диалоги, выразительная речь или новый синтетический голос по описанию. | [zip, 67 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-generate-voiceover.zip) |
| `creativeclaw-plan-video` | Планирует видео: согласованный сценарий, список кадров и раскадровка с чистыми референсами для генерации. | [zip, 89 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-plan-video.zip) |
| `creativeclaw-product-photoshoot` | Серия рекламных фото товара в едином стиле через Creative Claw. | [zip, 35 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-product-photoshoot.zip) |
| `creativeclaw-render-html` | Рендерит точный HTML/CSS-макет в PNG или делает моушн-видео как композицию HyperFrames на HTML/CSS/JS в Creative Claw. | [zip, 37 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-render-html.zip) |
| `creativeclaw-setup` | Первый запуск Creative Claw с подсказками: рассказывает, что умеет, спрашивает, что вы хотите сделать, собирает фото, логотип и референсы бренда и ведёт к пе… | [zip, 96 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-setup.zip) |
| `creativeclaw-submit-feedback` | Отправляет команде Creative Claw конкретный отзыв о продукте и качестве, когда пользователь даёт обратную связь или возникла конкретная проблема; не для запр… | [zip, 17 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/creativeclaw-submit-feedback.zip) |

### crypto-spot-futures-analyzer

Разбор сделок с криптовалютой на споте и фьючерсах: скриншоты TradingView, сетапы BTC/ETH/альткоинов, точки входа, стопы, цели, плечо, риск ликвидации, теханализ, риск/прибыль, размер позиции, фандинг, открытый интерес, усреднение (DCA) и риски портфеля.

| Навык | Что делает | Скачать |
|---|---|---|
| `crypto-spot-futures-analysis` | Разбор сделок с криптовалютой на споте и фьючерсах: скриншоты TradingView и бирж, сетапы BTC/ETH/альткоинов, точки входа, стоп-лоссы, тейк-профиты, плечо, ри… | [zip, 14 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/crypto-spot-futures-analysis.zip) |

### CutPro — нарезка клипов

Нарезает длинные видео и стримы на короткие клипы с помощью ИИ, рендерит их и публикует в TikTok, Instagram и YouTube. Также расшифровывает аудио и видео в текст.

| Навык | Что делает | Скачать |
|---|---|---|
| `cutpro` | Нарезает длинные видео и стримы на короткие клипы через CutPro, рендерит и публикует их. | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/cutpro.zip) |

### data

Работа с данными: SQL-запросы, исследование таблиц, поиск выводов, графики и дашборды, понятные истории из сырых цифр для руководства и команды.

| Навык | Что делает | Скачать |
|---|---|---|
| `build-dashboard` | Интерактивный HTML-дашборд с графиками, фильтрами и таблицами. | [zip, 12 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/build-dashboard.zip) |
| `create-viz` | Графики публикационного качества на Python. | [zip, 6 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/create-viz.zip) |
| `data-analyze` | Отвечает на вопросы по данным — от быстрой справки до полного анализа. | [zip, 6 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/data-analyze.zip) |
| `data-context-extractor` | Создаёт или улучшает навык анализа данных под конкретную компанию, собирая неписаные знания аналитиков. | [zip, 17 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/data-context-extractor.zip) |
| `data-visualization` | Эффективная визуализация данных на Python (matplotlib, seaborn, plotly). | [zip, 8 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/data-visualization.zip) |
| `explore-data` | Профилирует и исследует набор данных: форма, качество, закономерности. | [zip, 9 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/explore-data.zip) |
| `sql-queries` | Правильный и быстрый SQL для всех основных хранилищ данных (Snowflake, BigQuery, Databricks, PostgreSQL и др.). | [zip, 8 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/sql-queries.zip) |
| `statistical-analysis` | Статистические методы: описательная статистика, анализ трендов, поиск выбросов, проверка гипотез. | [zip, 8 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/statistical-analysis.zip) |
| `validate-data` | Проверка анализа перед тем, как им делиться: методология, точность, искажения. | [zip, 10 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/validate-data.zip) |
| `write-query` | Оптимизированный SQL под ваш диалект по лучшим практикам. | [zip, 6 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/write-query.zip) |

### design

Для дизайнеров: критика макетов, управление дизайн-системой, тексты интерфейса, проверка доступности, сводка исследований и передача макетов в разработку — от идеи до точных спецификаций.

| Навык | Что делает | Скачать |
|---|---|---|
| `accessibility-review` | Проверка доступности дизайна или страницы по WCAG 2.1 AA. | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/accessibility-review.zip) |
| `design-critique-brief` | Структурная обратная связь по дизайну: удобство, иерархия, единообразие. | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/design-critique-brief.zip) |
| `design-handoff` | Спецификации для передачи макета разработчикам. | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/design-handoff.zip) |
| `design-system` | Аудит, документация и развитие дизайн-системы. | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/design-system.zip) |
| `research-synthesis` | Сводит результаты исследований пользователей в темы, выводы и рекомендации. | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/research-synthesis.zip) |
| `user-research` | Планирование, проведение и обобщение исследований пользователей. | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/user-research.zip) |
| `ux-copy` | Пишет и проверяет тексты интерфейса — микрокопирайтинг, сообщения об ошибках, пустые состояния, призывы к действию. | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/ux-copy.zip) |

### design-skills

10 навыков по UX и дизайну на основе признанных методик: исследования, критика дизайна, доступность, карта пути пользователя, дизайн-системы, стратегия, дизайн взаимодействия, организация дизайн-процессов, тексты интерфейса и улучшение визуала.

| Навык | Что делает | Скачать |
|---|---|---|
| `accessibility-audit` | Аудит доступности по WCAG 2.2: проверяет страницы, компоненты и сценарии на соответствие уровням A, AA и AAA, находит проблемы, оценивает серьёзность, даёт и… | [zip, 35 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/accessibility-audit.zip) |
| `design-critique` | Оценивает интерфейсы по эвристикам юзабилити, законам UX, паттернам и принципам дизайна взаимодействия, информационной архитектуре и качеству контента. | [zip, 52 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/design-critique.zip) |
| `design-elevation` | Система «прокачки» дизайна: автоматически превращает рабочий визуал в аккуратный профессиональный дизайн. | [zip, 80 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/design-elevation.zip) |
| `design-ops` | Организация дизайн-процессов: дизайн-спринты, передача макетов в разработку, командные ритуалы, стандарты документации и контроль качества дизайна. | [zip, 48 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/design-ops.zip) |
| `design-systems` | Создание, документирование и поддержка дизайн-систем: дизайн-токены, спецификации компонентов, библиотеки паттернов, правила именования и процессы управления. | [zip, 41 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/design-systems.zip) |
| `interaction-design` | Проектирование взаимодействий: микровзаимодействия, анимации, состояния, жесты, предотвращение ошибок и поведение продукта. | [zip, 41 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/interaction-design.zip) |
| `journey-mapping` | Карты пути клиента, сервисные блюпринты, карты опыта, карты эмпатии и другие схемы для согласования команды. | [zip, 52 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/journey-mapping.zip) |
| `ux-research` | Планирование, проведение и анализ UX-исследований по проверенным методикам. | [zip, 63 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/ux-research.zip) |
| `ux-strategy` | Связывает дизайн-решения с бизнес-результатами: конкурентный анализ, карта возможностей, Jobs to Be Done, поиск решений от результата, проектирование ценност… | [zip, 50 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/ux-strategy.zip) |
| `ux-writing` | Тексты интерфейса (микрокопирайтинг), понятные и доступные: кнопки, подписи, сообщения об ошибках, уведомления, формы, онбординг, пустые состояния, сообщения… | [zip, 36 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/ux-writing.zip) |

### engineering

Для разработчиков: стендапы, ревью кода, архитектурные решения, разбор инцидентов и техническая документация. Работает с вашими инструментами или самостоятельно.

| Навык | Что делает | Скачать |
|---|---|---|
| `architecture` | Создаёт или оценивает запись архитектурного решения (ADR). | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/architecture.zip) |
| `code-review` | Ревью изменений кода: безопасность, производительность, корректность. | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/code-review.zip) |
| `debug` | Структурная отладка: воспроизвести, изолировать, найти причину, исправить. | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/debug.zip) |
| `deploy-checklist` | Чек-лист проверки перед выкаткой. | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/deploy-checklist.zip) |
| `documentation` | Пишет и поддерживает техническую документацию. | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/documentation.zip) |
| `incident-response` | Реагирование на инцидент: разбор, коммуникация, постмортем. | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/incident-response.zip) |
| `standup` | Апдейт для стендапа по недавней активности. | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/standup.zip) |
| `system-design` | Проектирование систем, сервисов и архитектур. | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/system-design.zip) |
| `tech-debt` | Находит, классифицирует и приоритизирует технический долг. | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/tech-debt.zip) |
| `testing-strategy` | Стратегии и планы тестирования. | [zip, 1 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/testing-strategy.zip) |

### extract-alpha

Убирает фон с картинок, сгенерированных ИИ, с идеальной прозрачностью: одна и та же картинка генерируется на белом и на чёрном фоне, а плагин сравнивает их и вычисляет прозрачность по пикселям.

| Навык | Что делает | Скачать |
|---|---|---|
| `extract-alpha` | Убирает фон с картинок, сгенерированных ИИ (например, Gemini), методом сравнения двух версий. | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/extract-alpha.zip) |
| `extract-alpha-prompt` | Пишет пару промптов для генерации картинки (на белом и на чёрном фоне), готовую для вырезания прозрачности. | [zip, 2 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/extract-alpha-prompt.zip) |

### figma-suite

Продвинутый набор для Figma (для Claude Code): двусторонняя синхронизация токенов и компонентов между кодом и Figma (с проверкой через Zod и мостом Code Connect), создание библиотек компонентов, дизайн экранов и аудит дизайн-систем через официальный MCP-сервер Figma.

| Навык | Что делает | Скачать |
|---|---|---|
| `figma-suite` | Двусторонняя синхронизация дизайн-системы между кодом и Figma — токены и переменные, компоненты и проверенная через Zod связка компонентов кода и Figma, — а … | [zip, 98 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/figma-suite.zip) |

### finance

Бухгалтерия и финансы: проводки, сверки, финансовая отчётность и анализ отклонений. Ускоряет подготовку к аудиту, закрытие месяца и поддержание учёта в порядке.

| Навык | Что делает | Скачать |
|---|---|---|
| `audit-support` | Поддержка соответствия SOX 404: методика тестирования контролей, отбор выборок, стандарты документирования. | [zip, 10 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/audit-support.zip) |
| `close-management` | Управление закрытием месяца: последовательность задач, зависимости, статусы. | [zip, 7 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/close-management.zip) |
| `financial-statements` | Финансовая отчётность (отчёт о прибылях и убытках, баланс, движение денежных средств) со сравнением периодов и анализом отклонений. | [zip, 9 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/financial-statements.zip) |
| `journal-entry` | Готовит бухгалтерские проводки с правильным дебетом, кредитом и расшифровкой. | [zip, 6 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/journal-entry.zip) |
| `journal-entry-prep` | Готовит бухгалтерские проводки с правильным дебетом, кредитом и подтверждающими документами для закрытия месяца. | [zip, 7 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/journal-entry-prep.zip) |
| `reconciliation` | Сверка счетов: сравнение остатков главной книги с аналитическим учётом, банковскими выписками или данными контрагентов. | [zip, 7 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/reconciliation.zip) |
| `sox-testing` | Выборки, рабочие документы тестирования и оценки контролей по SOX. | [zip, 7 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/sox-testing.zip) |
| `variance-analysis` | Раскладывает финансовые отклонения на факторы с пояснениями и каскадным анализом. | [zip, 8 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/variance-analysis.zip) |

### marketing

Маркетинг: создание контента, планирование кампаний, анализ результатов по каналам, единый голос бренда, отслеживание конкурентов и отчёты о том, что работает.

| Навык | Что делает | Скачать |
|---|---|---|
| `brand-review` | Проверяет контент на соответствие голосу бренда, гайду по стилю и ключевым сообщениям: отмечает отклонения по серьёзности и даёт правки «было — стало». | [zip, 9 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/brand-review.zip) |
| `campaign-plan` | Полный бриф кампании: цели, аудитория, сообщения, стратегия по каналам, контент-календарь и метрики успеха. | [zip, 9 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/campaign-plan.zip) |
| `competitive-brief` | Исследует конкурентов и сравнивает позиционирование и сообщения: пробелы в контенте, возможности и угрозы. | [zip, 9 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/competitive-brief.zip) |
| `content-creation` | Маркетинговый контент для разных каналов: статьи для блога, посты для соцсетей, email-рассылки, лендинги, пресс-релизы и кейсы. | [zip, 8 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/content-creation.zip) |
| `draft-content` | Черновики статей, постов для соцсетей, email-рассылок, лендингов, пресс-релизов и кейсов с оформлением под канал и SEO-рекомендациями. | [zip, 6 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/draft-content.zip) |
| `email-sequence` | Цепочки писем: полный текст, тайминг, ветвления, условия выхода и ориентиры по результатам. | [zip, 8 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/email-sequence.zip) |
| `performance-report` | Отчёт об эффективности маркетинга: ключевые метрики, тренды, успехи и провалы, приоритетные рекомендации. | [zip, 11 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/performance-report.zip) |
| `seo-audit` | Полный SEO-аудит: подбор ключевых слов, анализ страниц, пробелы в контенте, технические проверки и сравнение с конкурентами. | [zip, 8 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/seo-audit.zip) |

### productivity

Личная продуктивность: задачи, план на день и память о важном контексте по работе. Синхронизируется с календарём, почтой и чатами, чтобы всё было под контролем.

| Навык | Что делает | Скачать |
|---|---|---|
| `memory-management` | Двухуровневая память, которая делает Claude полноценным коллегой: расшифровывает сокращения, аббревиатуры, прозвища и внутренний жаргон, чтобы понимать прось… | [zip, 7 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/memory-management.zip) |
| `productivity-update` | Синхронизирует задачи и обновляет память по вашей текущей активности. | [zip, 6 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/productivity-update.zip) |
| `start` | Запускает систему продуктивности и открывает дашборд. | [zip, 6 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/start.zip) |
| `task-management` | Простое управление задачами через общий файл TASKS.md. | [zip, 5 КБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/task-management.zip) |

### video-shotcraft

Кинематографичные видео о продукте на Remotion (видео из кода): готовые рецепты кадров, превью движения, переиспользуемые компоненты, звуковые эффекты и шаблон для продакшена.

| Навык | Что делает | Скачать |
|---|---|---|
| `video-shotcraft` | Кинематографичные видео о продукте по карточкам-рецептам кадров, проверенному шаблону и ресурсам кода и звука (Remotion + настоящие скриншоты страниц + 2.5D-… | [zip, 42.3 МБ](https://github.com/pohnah000-byte/skill-claude-inst/releases/latest/download/video-shotcraft.zip) |

### Плагины-подключения (без навыков)

Эти плагины только подключают внешний сервис, навыков-файлов у них нет. Их ставят как плагин целиком (через Claude Code или каталог плагинов), а после установки входят в аккаунт сервиса.

| Плагин | Что делает |
|---|---|
| Abracadabrax — обложки для альбомов | Обложки для музыки: назовите Claude название, исполнителя, жанр и настроение, и Abracadabrax нарисует квадратную обложку для альбома, сингла, EP, микстейпа и… |
| Abracadabrax — фоновая музыка | Фоновая музыка с ИИ: опишите настроение и для чего нужен трек, и Claude подготовит инструментальную композицию для видео, подкаста, рекламы, игры, стрима или… |
| Abracadabrax — картинки и видео | Генерация картинок и видео с ИИ: превращает текстовое описание в изображение или ролик, с выбором модели, формата и длительности. |
| Abracadabrax — фото товаров | Фото товара с ИИ: опишите товар, и Claude подготовит снимок на белом фоне, сцену в интерьере, раскладку сверху (флэтлей), баннер или крупный план для магазин… |
| Аниме-истории: мультфильмы с ИИ | Превращает идею истории в короткий мультфильм: аниме, мультяшный стиль, чиби, сказочная книжка или 3D, с постоянными персонажами, диалогами и закадровым голо… |
| Видео на день рождения с ИИ | Поздравительное видео: превращает ваши воспоминания в ролик на день рождения, годовщину или юбилей — с закадровым голосом и пожеланием в конце. |

## Что важно знать

- **Навыки, которые работают через сервисы** (Creative Claw, CutPro, Adobe, Abracadabrax, ManyMotions, ScrapeCreators), требуют подключить и войти в соответствующий сервис; часть сервисов платная.
- **Монтаж по ссылке** скачивает видео с прямых ссылок и многих площадок. YouTube и другие сайты, требующие входа, из облака Claude видео не отдают — тогда навык предложит CutPro или попросит прислать файл.
- **Не ставьте один и тот же навык дважды** (например, и оригинал, и эту версию) — Claude будет путаться, какой выбрать.
- Навык `video-shotcraft` собран облегчённым (без демо-примеров) и всё равно весит ~42 МБ; если Claude не примет такой большой файл, ставьте его как плагин через Claude Code.

## Для разработчиков

- `plugins/` — исходники плагинов; каждый навык — папка с `SKILL.md`.
- `tools/build_skill_zips.py` — пересобрать zip всех навыков в `dist/`: `python3 tools/build_skill_zips.py`.
- Скрипты монтажа можно запускать и локально (Python 3 + ffmpeg):

```bash
pip install yt-dlp faster-whisper
python3 plugins/moi-navyki/skills/montazh-po-ssylke/scripts/transcribe.py видео.mp4
python3 plugins/moi-navyki/skills/montazh-po-ssylke/scripts/montage.py example > plan.json
python3 plugins/moi-navyki/skills/montazh-po-ssylke/scripts/montage.py render plan.json
```

## Авторство и лицензии

Плагины принадлежат их авторам и распространяются по их лицензиям (MIT, Apache-2.0, MPL-2.0 — указаны в каждом плагине и в каждом zip). В этом репозитории переведены описания на русский и добавлен навык монтажа `montazh-po-ssylke` (MIT). Официальный плагин Figma сюда не включён — ставьте его из каталога плагинов Claude.

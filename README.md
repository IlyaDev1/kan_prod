Здесь я добавил пакеты Backend и ML

В пакете ML - модель, ее загрузка, функции и тд
В пакете Backend - бэк и сервис модуль. Пока самого бэка нет

Это пока не конец ветки, но у меня есть вопросы:
1) Что за папка model создалась
2) Запусти этот пул, выводятся ворнинги и не 1 или 0, а дробное число, посмотри, пожалуйста, мб я кринж сделал
3) Как видишь, я использую ml_model как пакет, который генерит модель для переиспользования, которая создается один раз при запуске контейнера в будующем, норм ли это политика, мб это плохая практика

Просьбы и замечания:
1) from kan import * - плохая практика, засоряешь оперативку
2) Делай аннотации, пожалуйста

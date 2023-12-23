//Голосовой поиск
		function handleSpeech(event) {
            const transcript = event.results[0][0].transcript.toLowerCase();

            // Проверяем распознанные команды и выполняем переходы
            if (transcript.includes('перейти на дневник тренировок')) {
                window.location.href = 'Training_diary.html';
            } else if (transcript.includes('перейти на дневник питания')) {
                window.location.href = 'Food_diary.html'; 
            } else if (transcript.includes('перейти на дневник приёма таблеток')) {
                window.location.href = 'Pill_diary.html'; 
            } else if (transcript.includes('перейти на заметки')) {
                window.location.href = 'Notes.html'; 
            } else if (transcript.includes('перейти на календарь')) {
                window.location.href = 'Calendar.html'; 
            } else if (transcript.includes('перейти на личное расписание')) {
                window.location.href = 'Schedule.html'; 
            } else if (transcript.includes('перейти на расписание занятий')) {
                window.location.href = 'Schedule_of_classes_in_the_rehabilitation_center.html'; 
            } else if (transcript.includes('перейти на информацию о травме')) {
                window.location.href = 'Info.html'; 
            } else if (transcript.includes('о проекте')) {
                window.location.href = 'About.html';
            }
        }

        // Создаем объект распознавания речи
        const recognition = new webkitSpeechRecognition();
        recognition.onresult = handleSpeech;

        // Начинаем распознавание речи после загрузки страницы
        window.addEventListener('DOMContentLoaded', () => {
            if ('webkitSpeechRecognition' in window) {
                recognition.start();
            } else {
                alert('Web Speech API не поддерживается в вашем браузере.');
            }
        });

// Добавляем обработчик события загрузки страницы
window.addEventListener('load', () => {

  // Запрашиваем доступ к микрофону
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {

      const recognition = new webkitSpeechRecognition();
      recognition.lang = 'ru-RU';
      recognition.continuous = true;
      recognition.onresult = event => {
        // Вызываем функцию handleSpeech 
        // для обработки результатов распознавания
        handleSpeech(event); 
      };

      recognition.start();

    })
    .catch(error => {
      console.log('Нет доступа к микрофону');
    });

});

		//конец голосового поиска
    function handleSearch(event) {
      event.preventDefault();

      var searchQuery = document.getElementById("searchInput").value;

      // Получаем все элементы, которые нужно фильтровать
      var items = document.getElementsByClassName("searchable-item");

      // Проходимся по каждому элементу и скрываем/отображаем его в зависимости от поискового запроса
      for (var i = 0; i < items.length; i++) {
        var item = items[i];
        var itemText = item.textContent.toLowerCase(); // Получаем текст элемента в нижнем регистре

        if (itemText.includes(searchQuery.toLowerCase())) {
          item.style.display = "block"; // Отображаем элемент, если текст содержит поисковый запрос
        } else {
          item.style.display = "none"; // Скрываем элемент, если текст не содержит поисковый запрос
        }
      }
    }
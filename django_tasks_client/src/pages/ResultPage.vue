<template>
  <body class="bg-light">
  <main-header/>
  <div class="container justify-content-center pt-5 mt-2 text-secondary">
    <div class="container pt-2 card ">
      <div class="row pt-2 mx-3">
        <div class="col-12 col-sm-6 ">
          <h4>Название теста: {{ test.name }}</h4>
        </div>
        <div class="col-12 col-sm-6 ">
          <div class="container">
            <a class="btn btn-outline-primary w-25 float-lg-end " type="button" href="{% url 'main' %}"> Закрыть
            </a>
          </div>
        </div>
      </div>
      <div class="row mx-3">
        <div class="col-12">
          <h6>Название категории: {{ category.name }}</h6>
        </div>
      </div>
      <div class="row  mx-3">
        <div class="col-12 pt-1">
          <h4>Ваш результат</h4>
        </div>
      </div>
      <div class="row  mx-3">
        <div class="col-12">
          <h6>Количество вопросов в тесте: {{ countQuestions }}</h6>
        </div>
      </div>
      <div class="row  mx-3">
        <div class="col-12">
          <h6>Количество верных ответов: {{ countright }}</h6>
        </div>
      </div>
      <div class="row  mx-3">
        <div class="col-12">
          <h6>Время прохождения: {{ min }} мин. {{ sec }} сек.</h6>
        </div>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-12 pt-2 col-md-12 col-sm-12">
            <div class="accordion accordion-flush" id="accordionFlushExample">
              {% for test in resultForView %}
              <div class="accordion-item">
                <h2 class="accordion-header" id="flush-heading{{test.answerID}}">
                  <button class="accordion-button collapsed " type="button" data-bs-toggle="collapse"
                          data-bs-target="#flush-collapse{{test.answerID}}" aria-expanded="false"
                          aria-controls="flush-collapse{{test.answerID}}">
                    <div class="right mx-5">

                      {% if test.answerResult == test.answerRight %}
                      <svg width="19" height="19" viewBox="0 0 19 19" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M9.5 0C4.25334 0 0 4.25334 0 9.5C0 14.7467 4.25334 19 9.5 19C14.7467 19 19 14.7467 19 9.5C19 4.25334 14.7467 0 9.5 0ZM8.74 14.3097L3.86498 9.43464L6.01464 7.28536L8.74 10.0103L13.68 5.07034L15.8297 7.22L8.74 14.3097Z"
                            fill="#4DB664"/>
                      </svg>
                      {% else %}
                      <svg width="19" height="19" viewBox="0 0 19 19" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M9.5 0C4.25334 0 0 4.25334 0 9.5C0 14.7467 4.25334 19 9.5 19C14.7467 19 19 14.7467 19 9.5C19 4.25334 14.7467 0 9.5 0ZM14.755 12.6054L12.6054 14.7546L9.5 11.6497L6.39502 14.7546L4.24536 12.6054L7.35034 9.5L4.24498 6.39464L6.39464 4.24536L9.5 7.35034L12.605 4.24536L14.7546 6.39464L11.6497 9.5L14.755 12.6054Z"
                            fill="#D53131"/>
                      </svg>
                      {% endif %}
                    </div>
                    {{ test.question }}


                  </button>
                </h2>

                <div id="flush-collapse{{test.answerID}}" class="accordion-collapse collapse"
                     aria-labelledby="flush-heading{{test.answerID}}"
                     data-bs-parent="#accordionFlushExample">
                  <div class="accordion-body">
                    <!-- {{test.answerRight}} -->
                    {% if test.answerResult == "0!0" %}
                    Вы не отвечали на этот вопрос
                    {% else %}
                    Ваш ответ: {{ test.answerResult }}
                    {% endif %}

                  </div>

                </div>

              </div>
              {% endfor %}
            </div>

          </div>

        </div>

        <div class="row">
          <div class="col-12 pt-2 col-md-12 col-sm-12">
            <div class="container text-center mb-3">

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </body>
</template>

<script>
import MainHeader from "@/components/MainHeader";
export default {
  components: {MainHeader}
}
</script>
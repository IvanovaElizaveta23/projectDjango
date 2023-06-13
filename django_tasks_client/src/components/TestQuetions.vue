<template>
  <div>
    <div class="container justify-content-center  pt-3 mt-1 text-center">
      <div class="row justify-content-center text-secondary ">
        <h2 class="mb-1">
          <div id="timer"></div>
        </h2>
      </div>
    </div>

    <div class="container justify-content-center pt-2 mt-2 ">
      <div class="container  mt-5 card">
        <div class="row pt-2">
          <div class="col-12 col-md-6 col-sm-6 ">
          </div>
          <div class="col-12 col-md-6 col-sm-6 ">
            <div class="container pt-1">
<!--                 onclick="Finish('{{idTest}}')"> Завершить</a>-->
              <a class="btn btn-outline-danger w-25 float-lg-end " type="button">Завершить</a>
            </div>
          </div>
        </div>

        <div class="questions row pt-4">
          <div class="col-12 col-md-6 col-sm-6 ">
            <h4 class="text-secondary mx-4">Вопрос: {{ currentPage }}</h4>
            <div :id="question.id" class="question container pt-2 mx-3">
              <p>{{ question.content }}</p>
            </div>
          </div>
          <div class="col-12 col-md-6  ">
            <h4 class="text-secondary mx-2">Выберите варианты ответов:</h4>
            <div class="container pt-2">
              <div class="form-check"
                   v-for="answer in question.answers"
                   :key="answer.id"
              >
<!--                {%if test.answerSend == test.question.answer1 %}-->
<!--                <input class="form-check-input" onclick="SaveTest('{{idTest}}')"-->
                <input class="form-check-input" type="radio" value="" checked
                        name="flexCheckChecked" :id="answer.id">
<!--                {% else %}-->
<!--                <input class="answer1 form-check-input" onclick="SaveTest('{{idTest}}')" type="radio"-->
<!--                       value="" name="flexCheckChecked{{test.question.id}}">-->
<!--                {% endif %}-->

                <label class="form-check-label" for="flexCheckDefault" :id="answer.id">
                  {{ answer.content }}
                </label><br>
              </div>
            </div>
          </div>
        </div>

<!--        <div class="row pt-5 ">-->
<!--          <div class="col-12 col-md-6  ">-->
<!--            <nav aria-label="...">-->
<!--              <ul class="pagination pagination-sm">-->
<!--                {% for test in c %}-->
<!--                <li>-->
<!--                  &lt;!&ndash; <a class="btmPage page-link" id="{{test.id_question}}" tabindex="-1">1</a> &ndash;&gt;-->
<!--                  <button class="btmPage page-link" id="{{test.id_question}}" value="1">12</button>-->
<!--                </li>-->
<!--                {% endfor %}-->
<!--              </ul>-->
<!--            </nav>-->
<!--          </div>-->

<!--          <div class="col-12 col-md-6">-->
<!--            <div class="container">-->
<!--              <a class="btn btn-outline-primary w-25 float-lg-end " type="button" onclick="newPage()">-->
<!--                Следующий</a>-->
<!--            </div>-->
<!--            <div class="btn btn-outline w-10 float-lg-end">-->
<!--            </div>-->
<!--            <div class="container">-->
<!--              <a class="btn btn-outline-primary w-25 float-lg-end " type="button" onclick="backPage()">-->
<!--                Назад</a>-->
<!--            </div>-->
<!--          </div>-->
        </div>
      </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      question: '',
      pages: 0,
      currentPage: 1,
    }
  },
  methods: {
    getData(page){
      this.$load(async () => {
        if (page != '')
          page = '?page=' + page
        let question = (await this.$api.questions.get(this.$route.params.id, page)).data
        this.question = question.results[0]
        this.pages = question.count
        this.getAnswers(this.question.id)
      })
    },
    getAnswers(question) {
      this.$load(async () => {
        this.question.answers = (await this.$api.answers.getAll(question)).data.answers
      })
    },
  },
  created() {
    this.getData('')
  }
}
</script>

<style>
.wrap {

    height: 18.75rem;
    width: 16.5rem;
    perspective: 62.5rem;
}

.card {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.8s;
    transform-style: preserve-3d;
}

.wrap:hover .card {
    transform: rotateY(180deg);
}

.front, .back {
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden; /* Safari */
    backface-visibility: hidden;
}

.front {
    color: black;
}

.back {
    background-color: #fafafa;

    transform: rotateY(180deg);
}


@media only screen and (min-width: 450px) {
    .wrap {
        width: 100%;
    }
}

@media only screen and (min-width: 768px) {
    .wrap {
        width: 100%;
    }
}

@media only screen and (min-width: 1000px) {
    .wrap {
        width: 100%;
    }
}
</style>
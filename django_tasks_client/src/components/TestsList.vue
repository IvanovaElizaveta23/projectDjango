<template>
  <div>
    <br>
    <div style="background-color: rgb(192, 185, 227);"></div>

    <div class="container py-5">
          <test-modal
      v-if="isAuthModalOpen"
      @close="isAuthModalOpen = false"
    />
      <ul class="nav nav-tabs" id="myTab" role="tablist">
        <li class="nav-item" role="presentation">
          <button class="nav-link active fs-5" id="home-tab" data-bs-toggle="tab" data-bs-target="#home"
                  type="button" role="tab" aria-controls="home" aria-selected="true">Все тесты
          </button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link fs-5" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile"
                  type="button" role="tab" aria-controls="profile" aria-selected="false">Пройденные тесты
          </button>
        </li>
      </ul>

      <!--Фильтр(не работает)-->
      <div class="row float-lg-end">
        <div class="container">
          <div class="dropdown">
            <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown"
                    aria-expanded="false">Фильтр
            </button>
            <ul class="dropdown-menu">
              <!--            <input id="NameSearch" class="form-control mr-sm-2 " type="search" value="{{name}}"-->
              <!--                   placeholder="Поиск" aria-label="Search">-->
              <!--            {% for test in categories %}-->
              <!--            <li>-->
              <!--              {%if test.id|slugify in categoriesSelect %}-->
              <!--              <input class="category form-check-input mx-2" checked type="checkbox" value="">-->
              <!--              {% else %}-->
              <!--              <input class="category form-check-input mx-2" type="checkbox" value="">-->
              <!--              {% endif %}-->
              <!--              <label id="{{test.id}}" class="category form-check-label" for="flexCheckChecked3">-->
              <!--                {{ test.name }}-->
              <!--              </label>-->

              <!--            </li>-->

              <!--            {% endfor %}-->
              <button class="btn btn-primary" onclick="Search()">Найти</button>
              <button class="btn btn-primary text-left" style="width: 80px;" @click="$router.push({ name: 'main' })">
                Сбросить
              </button>
            </ul>
          </div>
        </div>
      </div>


      <div class="tab-content" id="myTabContent">
        <!--Вывод всех тестов-->
        <div class="tab-pane fade show active" id="home" role="tabpanel" aria-labelledby="home-tab">
          <div class="row mt-4 ">
            <div class="col-12 col-sm-4 col-md-3 col-lg-3 mb-3 text-center"
                 v-if="tests.length == 0">
              По данному запросу нет нужных тестов
            </div>
            <div class="col-12 col-sm-4 col-md-3 col-lg-3 mb-3 text-center"
                 v-else
                 v-for="test in tests"
                 :key="test.id"
            >
              <div class="wrap">
                <!--                             :to="{ name: 'testing', params: { id: test.id } }"-->
                <a class="card-link text-muted text-decoration-none" type="button"
                   @click="isAuthModalOpen=true"
                >
                  <div class="card shadow-lg h-100">
                    <div class="front ">
                      <div class="card-body">
                        <div class="card img">
                          <img src="../assets/django.jpg">
                        </div>
                        <h5 class="pt-2">{{ test.name }}</h5>
                      </div>
                    </div>
                    <div class="back ">
                      <h3>Описание</h3>
                      <div class="text text-start mx-3">
                        <h6 class="mb-1">Название теста: {{ test.name }}</h6>
<!--           Названия вместо id             -->
                        <h6 class="mb-1">Категория теста: {{ test.cat }}</h6>
                        <h6 class="mb-1">Сложность теста: {{ test.dif }}</h6>
                        <h6></h6>
                        <h6 class="mb-1"
                            v-if="test.quantity_attempts == null"
                        >
                          У данного теста нет ограничения по количеству прохождений
                        </h6>
                        <h6 class="mb-1"
                            v-else
                        >
                          Прохождений теста: {{ sessionFilter(test.id).length }} из {{ test.quantity_attempts }}
                        </h6>
<!--                        <h6 class="mb-1 ">-->
<!--                          Вы сейчас проходите тест-->
<!--                        </h6>-->
                      </div>
                    </div>
                  </div>
                </a>
              </div>
            </div>
          </div>
        </div>

        <!--Вывод пройденных тестов-->
        <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
          <div class="row mt-4 ">
            <div class="col-12 col-sm-4 col-md-3 col-lg-3 mb-3 text-center"
                 v-if="sessions.length == 0">
              По данному запросу нет нужных тестов
            </div>
            <div class="col-12 col-sm-4 col-md-3 col-lg-3 mb-3 text-center"
                 v-else
                 v-for="test in tests"
                 :key="test.id"
            >
              <div class="card shadow-lg h-100"
                   v-if="sessionFilter(test.id).length != 0"
              >
                <div class="card-body">
                  <h5 class="card-title text-muted mb-5">{{ test.name }}</h5>
                  <div class=" h-50" style="overflow-y: scroll;">
<!--        href="/resultUser/{{test.idRes}}"      -->
                    <a style="text-decoration:none"
                       v-for="(session, index) in sessionFilter(test.id)"
                       :key="index"
                    >
                      <h5 class="card-subtitle mb-2 text-muted mb-5 pt-5">Попытка {{ index + 1 }}</h5>
                      <h5 class="text-muted">Результат: {{ session.result }}</h5>
                    </a>
                  </div>
                  <h5 class="card-subtitle mb-2 text-muted pt-5">Уровень сложности</h5>
<!--       Название вместо id           -->
                  <h5 class="card-subtitle mb-2 text-muted"> {{ test.dif }}</h5>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TestModal from "@/components/TestModal";

export default {
  components: {TestModal},
  data() {
    return {
      isAuthModalOpen: false
    }
  },
  props: {
    tests: {
      type: Array,
      default: () => []
    },
    sessions: {
      type: Array,
      default: () => []
    }
  },
  methods: {
    sessionFilter(id) {
      return this.sessions.filter(x => x.test == id)
    }
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
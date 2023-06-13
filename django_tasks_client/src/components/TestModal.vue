<template>
  <div class="container justify-content-center  pt-5 mt-3 text-center"
       @before-close="close"
  >
    <div class="container pt-5 mt-5 align-items-center ">
      <div class="row align-items-center justify-content-center mt-3">
        <div class="col-12 col-md-6 ">
          <div class="card  shadow p-3 mb-5 bg-white rounded ">
            <div class="card-body ">
              <form>
                <div class="row justify-content-center text-secondary ">
                  <h2 class="mb-3">{{ name }}</h2>
                  <div class="mb-5 w-75 pt-3">
                    <h5>Вопросов: 20</h5>
                    <h5>Время: 40 мин</h5>
                  </div>
                </div>
                <router-link class="btn btn-outline-primary w-50 mt-3" type="button"
                             :to="{ name: 'testing', params: { id: 1 } }">Начать тестирование
                </router-link>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "test-modal",
  data() {
    return {
      name: 'Тест',
    }
  },
  methods: {
    close() {
      this.$emit('close')
    },
  }
}
</script>

<template>
  <body class="bg-light">
  <main-header/>
  <div class="container justify-content-center  pt-5 mt-3 text-center">
    <div class="container pt-5 mt-5 align-items-center ">

      <div class="row align-items-center justify-content-center mt-3">
        <div class="col-12 col-md-6 ">
          <div class="card  shadow p-3 mb-5 bg-white rounded ">
            <div class="card-body ">
              <form>
                <div class="row justify-content-center">

                  <h2 class="text-secondary mb-3">Авторизация</h2>
                  <div class="mb-3 w-75 mt-3">
                    <input type="login" class="form-control border-secondary" id="exampleInputLogin"
                           aria-describedby="loginHelp" placeholder="Логин">
                  </div>

                </div>

                <div class="row justify-content-center">
                  <div class="mb-3 w-75 mt-3">
                    <input type="password" class="form-control border-secondary" id="exampleInputPass"
                           aria-describedby="passHelp" placeholder="Пароль">
                  </div>
                </div>
                <a class="btn btn-outline-primary w-25 mt-3" type="button"
                   onclick="LoginUser()"> Войти</a>
                <!-- href="alltests(user).html" -->
              </form>
              <label><a href="tel:+7 (924) 999 99 99">Служба подержки: +7(924)-999-99-99</a></label><br>
              <label><a href="mailto:support123@mail.com">Почта: support123@mail.com</a></label>
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

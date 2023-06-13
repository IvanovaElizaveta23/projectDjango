<template>
   <nav class="navbar navbar-expand-lg navbar-light bg-primary">
        <div class="container-fluid">
            <router-link class="navbar-brand text-light" :to="{ name: 'main' }">Лого</router-link>
<!--Реализация кнопки-->
            <a class="btn btn-outline-primary bg-white text-primary " type="button">Выйти</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Переключатель навигации">
                <span class="navbar-toggler-icon"></span>
            </button>
        </div>
    </nav>
</template>

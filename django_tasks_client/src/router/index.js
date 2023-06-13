import VueRouter from 'vue-router'

import MainPage from '../pages/MainPage'
import TestingProcess from '../pages/TestingProcess'

export default new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'main',
            component: MainPage
        },
        {
            path: '/testing/:id',
            name: 'testing',
            component: TestingProcess
        },
    ]
})
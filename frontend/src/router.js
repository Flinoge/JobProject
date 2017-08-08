import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

function load (component) {
  return () => System.import(`components/${component}.vue`)
}

export default new VueRouter({
  routes: [
    {
      path: '/dashboard',
      name: 'Index',
      component: load('containers/Index'),
      children: [
        {
          path: '/game',
          name: 'Game',
          component: load('views/Game')
        }
      ]
    },
    {
      path: '/',
      name: 'Login',
      component: load('containers/Login'),
      children: [
        {
          path: '/',
          name: 'Login',
          component: load('views/Login')
        },
        {
          path: '/signup',
          name: 'Signup',
          component: load('views/Signup')
        }
      ]
    },
    { path: '*', component: load('Error404') }
  ]
})

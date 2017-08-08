<template>
  <div class="container mb-3 mt-3">
    <div class="row">
      <q-field class="col-8" :error="loginError" error-label="Invalid Username/Password"
      >
        <q-input float-label="Username" v-model="username" />
      </q-field>
      <div class="col-4">
        About Button Lottery
      </div>
    </div>
    <div class="row">
      <q-field class="col-8"
      >
        <q-input float-label="Password" v-model="password" type="password"/>
      </q-field>
      <div class="col-4">
        Click the button to increase your chance to win the ending lottery.
      </div>
    </div>
    <div class="row">
      <div class="col-8">
        <q-btn push @click="login">Login</q-btn>
      </div>
      <div class="col-4">
        Once we reach 1000 clicks, we will pick a winner!
      </div>
    </div>
    <div class="row pb-3">
      <router-link to="signup">Need a account?</router-link>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import { QInput, QField, QBtn } from 'quasar'

  export default {
    data () {
      return {
        username: '',
        password: '',
        loginError: false
      }
    },
    components: {
      QInput,
      QField,
      QBtn
    },
    computed: {
    },
    methods: {
      login () {
        this.loginError = false
        axios({
          method: 'POST',
          url: 'http://localhost:8000/login',
          data: {
            username: this.username,
            password: this.password
          }
        }).then(response => {
          if (response.status === 200) {
            localStorage.setItem('player', response.data)
            this.$router.push('game')
          } else {
            this.loginError = true
          }
          console.log(response)
        }).catch(error => {
          console.log(error)
        })
      }
    },
    mounted () {
    }
  }
</script>

<style>
</style>

<template>
  <div class="container mb-3 mt-3">
    <div class="row">
      <q-field class="col-6" :error="firstnameError" :error-label="error"
      >
        <q-input float-label="First Name" v-model="firstname" />
      </q-field>
      <q-field class="col-6" :error="lastnameError" :error-label="error"
      >
        <q-input float-label="Last Name" v-model="lastname" />
      </q-field>
    </div>
    <div class="row">
      <q-field class="col-6" :error="usernameError" :error-label="error"
      >
        <q-input float-label="Username" v-model="username" />
      </q-field>
      <q-field class="col-6"
      >
        <q-input float-label="Password" v-model="password" type="password"/>
      </q-field>
    </div>
    <div class="row pb-3">
      <div class="col-3"></div>
      <q-field class="col-6" :error="!/[^@]+@[^@]+\.[a-zA-Z]{2,6}/.test(email) && emailTouched" error-label="Please enter a valid email."
      >
        <q-input float-label="Email Address" v-model="email" @focus="emailTouched = true"/>
      </q-field>
      <div class="col-3"></div>
    </div>
    <div class="row pb-3">
      <div class="col-3"></div>
      <q-btn push class="col-6" @click="signup" :disabled="disableButton">Submit</q-btn>
      <div class="col-3"></div>
    </div>
    <div class="row pb-3">
      <router-link to="/">Already have an account?</router-link>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import { QInput, QField, QBtn } from 'quasar'

  export default {
    data () {
      return {
        firstname: '',
        lastname: '',
        email: '',
        username: '',
        password: '',
        error: '',
        emailTouched: false,
        usernameError: false,
        firstnameError: false,
        lastnameError: false,
        emailError: false,
        passwordError: false
      }
    },
    components: {
      QInput,
      QField,
      QBtn
    },
    computed: {
      disableButton () {
        let goodToSubmit = true
        this.firstnameError = false
        this.lastnameError = false
        this.usernameError = false
        this.passwordError = false
        this.emailError = false
        if (this.firstname.length > 0) {
          if (this.lastname.length > 0) {
            if (this.username.length > 0) {
              if (this.password.length > 7) {
                if (/[^@]+@[^@]+\.[a-zA-Z]{2,6}/.test(this.email)) {
                  goodToSubmit = false
                } else {
                  this.error = 'Please user a valid email address.'
                  this.emailError = true
                }
              } else {
                this.error = 'Password needs to be at least 8 characters.'
                this.passwordError = true
              }
            } else {
              this.error = 'Please fill in your Username.'
              this.usernameError = true
            }
          } else {
            this.error = 'Please fill in your Last Name.'
            this.lastnameError = true
          }
        } else {
          this.error = 'Please fill in your First Name.'
          this.firstnameError = true
        }
        return goodToSubmit
      }
    },
    methods: {
      signup () {
        this.error = ''
        this.usernameError = false
        axios({
          method: 'post',
          url: 'http://localhost:8000/signup',
          data: {
            username: this.username,
            password: this.password,
            email: this.email,
            firstname: this.firstname,
            lastname: this.lastname
          }
        }).then(response => {
          if (response.status === 200) {
            this.$router.push('/')
          } else if (response.status === 250) {
            this.error = 'User Already Exists'
            this.usernameError = true
          } else {
            this.error = 'Something Weird Happened'
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

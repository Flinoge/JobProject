<template>
  <div class="fullscreen">
    <div class="img"></div>
    <div class="loginScreen">
      <q-card class="ml-auto mr-auto">
        <q-card-title>Button Lottery</q-card-title>
        <q-card-separator/>
        <router-view>
        </router-view>
      </q-card>
    </div>
  </div>
</template>

<script>
//  import axios from 'axios'
  import { QCard, QCardTitle, QCardSeparator } from 'quasar'

  export default {
    data () {
      return {
      }
    },
    components: {
      QCard,
      QCardTitle,
      QCardSeparator
    },
    computed: {
    },
    methods: {
    },
    mounted () {
    }
  }
</script>

<style scoped>
  .loginScreen {
    height: 100%;
    text-align: center;
    padding-top: 10%;
  }
  .img {
    background-image: url('../../statics/LoginBackground.jpeg');
    background-repeat: no-repeat;
    background-size: cover;
    position: absolute;
    height: 100%;
    width: 100%;
    z-index: -1;
  }
  .q-card {
    width: 40%;
    background-color: white;
  }
</style>

<template>
  <div class="gameBoard fullscreen">
    <q-card class="row gameCard m-5 p-5">
      <div class="col-4">
        <q-slider
          v-model="myClicks"
          :min="0"
          :max="1000"
          :disable="true"
          label-always
          :label-value="'You\'ve clicked ' + myClicks + ' times.'"
        />
      </div>
      <div class="col-4 row">
        <q-btn push @click="buttonClick" class="col-12 lotteryButton"></q-btn>
      </div>
      <div class="col-4">
        <q-slider
          v-model="totalClicks"
          :min="0"
          :max="1000"
          :disable="true"
          label-always
          :label-value="'Total Clicks: ' + totalClicks"
        />
      </div>
    </q-card>
    <q-collapsible>
      <q-list>
        <q-list-header>The Game Winners</q-list-header>
        <q-item v-for="(winner, index) in gamewinners" key="index">
          {{ winner.fields.username }}
        </q-item>
      </q-list>
    </q-collapsible>
  </div>
</template>

<script>
  import axios from 'axios'
  import { QBtn, QCard, QSlider, QCollapsible, QList, QItem, QListHeader } from 'quasar'

  export default {
    data () {
      return {
        myClicks: 0,
        totalClicks: 0,
        gamewinners: []
      }
    },
    components: {
      QBtn,
      QCard,
      QSlider,
      QCollapsible,
      QList,
      QItem,
      QListHeader
    },
    computed: {
    },
    methods: {
      buttonClick () {
        axios({
          method: 'POST',
          url: 'http://localhost:8000/click',
          data: {
            username: localStorage.getItem('player')
          }
        }).then(response => {
          this.updateClicks()
          this.updateTotalClicks()
          this.checkWinner()
        }).catch(error => {
          console.log(error)
        })
      },
      updateClicks () {
        axios({
          method: 'POST',
          url: 'http://localhost:8000/myclicks',
          data: {
            username: localStorage.getItem('player')
          }
        }).then(response => {
          this.myClicks = response.data
        }).catch(error => {
          console.log(error)
        })
      },
      updateTotalClicks () {
        axios({
          method: 'POST',
          url: 'http://localhost:8000/totalclicks'
        }).then(response => {
          this.totalClicks = response.data
        }).catch(error => {
          console.log(error)
        })
      },
      updateWinners () {
        axios({
          method: 'POST',
          url: 'http://localhost:8000/gamewinners'
        }).then(response => {
          this.gamewinners = response.data
        }).catch(error => {
          console.log(error)
        })
      },
      checkWinner () {
        axios({
          method: 'POST',
          url: 'http://localhost:8000/checkwinner'
        }).then(response => {
        }).catch(error => {
          console.log(error)
        })
      }
    },
    mounted () {
      this.updateClicks()
      this.updateTotalClicks()
      this.updateWinners()
    }
  }
</script>

<style scoped>
  .q-card {
    background-color: white;
  }
  .gameBoard {
    padding-top: 10%;
  }
  .gameCard {
    height: 40%
  }
  .lotteryButton {
    background-image: url('../../statics/TeasureChest.png');
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
  }
</style>

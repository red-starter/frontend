<template>
  <div class="Chicago">
    <h1>
      <img v-bind:class="{ spinner: isLoading }" alt="knife logo" height="100px" src="../assets/knife.svg">
      <v-btn @click="calculate" depressed large color="error">{{buttonText}}</v-btn>  
      <img v-bind:class="{ spinner: isLoading }" alt="knife logo" height="100px" src="../assets/cleaver-knife.svg">
    </h1>
    <v-container fluid>
    <v-layout>
      <v-flex xs4>
      <v-date-picker :disabledDates="disabledDates" v-model="datePicker" :landscape="landscape" :reactive="reactive"></v-date-picker>
      </v-flex>
      <v-flex xs4>
      <v-time-picker v-model="timePicker" :landscape="landscape"></v-time-picker>
      </v-flex>
      <v-flex xs4>
         <v-subheader>Select a district</v-subheader>
         <v-select
           v-model="select"
           :hint="`${select.name}, ${select.number} District`"
           :items="items"
           item-text="name"
           item-value="number"
           label="Select"
           persistent-hint
           return-object
           single-line
         ></v-select>
      </v-flex>
    </v-layout>
    </v-container>
    <router-link to="/">Home</router-link>
    <v-dialog
      v-model="dialog"
      width="500"
      height="500"
    >

      <v-card>
      <div v-if="agreed">
        <v-card-title class="headline">Are you sure you want to know your survival odds?</v-card-title>
        <v-card-text style="font-size:25px;"> date : {{this.datePicker}} </v-card-text>
        <v-card-text style="font-size:25px;"> time : {{this.timePicker}} </v-card-text>
        <v-card-text style="font-size:25px;"> district : {{this.select.name}} </v-card-text>
      
        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            flat="flat"
            @click="handleDisagree"
          >
            Disagree
          </v-btn>

          <v-btn
            color="green darken-1"
            flat="flat"
            @click="dialog = false"
          >
            <router-link to="/results">agree</router-link>
          </v-btn>
        </v-card-actions>
        </div>
        <div v-else>
          <h2>Too bad, you need to know the truth!</h2>
        </div>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
name: 'Chicago',
// props: {
//   msg: String
// }
data () {
return {
  dialog: false,
  isLoading: false,
  agreed: true,
  select: null,
  landscape: false,
  datePicker: new Date().toISOString().substr(0, 10),
  timePicker: null,
  reactive: false,
  select: {name: 'Central' , number: '1st'}, 
  items: [
    {name: 'Central' , number: '1st'}, 
    {name: 'Wentworth' , number: '2nd'}, 
    {name: 'Grand Crossing' , number: '3rd'}, 
    {name: 'South Chicago' , number: '4th'}, 
    {name: 'Calumet' , number: '5th'}, 
    {name: 'Gresham' , number: '6th'}, 
    {name: 'Englewood' , number: '7th'}, 
    {name: 'Chicago Lawn' , number: '8th'}, 
    {name: 'Deering' , number: '9th'}, 
    {name: 'Ogden' , number: '10th'}, 
    {name: 'Harrison' , number: '11th'}, 
    {name: 'Near West' , number: '12th'}, 
    {name: 'Shakespeare' , number: '14th'}, 
    {name: 'Austin' , number: '15th'}, 
    {name: 'Jefferson Park' , number: '16th'}, 
    {name: 'Albany Park' , number: '17th'}, 
    {name: 'Near North' , number: '18th'}, 
    {name: 'Town Hall' , number: '19th'}, 
    {name: 'Lincoln' , number: '20th'}, 
    {name: 'Morgan Park' , number: '22nd'}, 
    {name: 'Rogers Park' , number: '24th'}, 
    {name: 'Grand Central' , number: '25th'}, 
  ]
}
},
methods: {
  calculate(){
    this.isLoading = true
    this.dialog = true
  },
  handleDisagree(){
    this.agreed=false
    setTimeout(() => this.$router.push('results'), 2000)
  }

},
computed: {
  buttonText(){
    return this.isLoading ? 'loading ... ' : "Get Survival Odds"
  },

},
}

</script>

<style scoped>
  @keyframes spin {
      0% { transform: rotate(0deg); }
      100% {  transform: rotate(359deg); }
  }
  .spinner {
      animation: spin 2s linear infinite;

  }
</style>


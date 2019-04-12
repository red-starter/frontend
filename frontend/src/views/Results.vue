<template>
  <div>
    <h1>
      <knifeline/>
        <h4>Predicted crimes for {{district.name}} ({{district.number}} district) </h4>
        <h4>starting date: {{date}} and starting time: {{time}}</h4>
      <knifeline/>     
    </h1>
    <v-container>
      <GChart
        type="LineChart"
        :data="chartData"
        :options="chartOptions"
      />
    <!-- <v-data-table
      :headers="headers"
      :items="data"
      class="elevation-1"
    >
      <template v-slot:items="props">
        <td>{{ props.item.name }}</td>
        <td>{{ props.item.number }}</td>
      </template>
    </v-data-table> -->
    </v-container>
    <router-link to="/">Home</router-link>
  </div>
</template>

<script>
  import knifeline from '../components/knifeline.vue' 
  import { GChart } from 'vue-google-charts'

  export default {
    name: "Results",
    components: {knifeline,GChart
},
    props: ['time','date','district','data'],
    data () {
      return {
        headers: [
          {
            text: 'Type of crimes',
            align: 'center',
            // sortable: false,
            value: 'name'
          },
          {
            text: 'Number of predicted crimes',
            align: 'center',
            // sortable: true,
            value: 'number'
          },

        ],
      }
    },
    computed: {
      chartData(){
        const agg_day = JSON.parse(this.data.grouped_day)
        console.log(agg_day)
        const result = [['Number of','Assault','Battery','Burglary']]
        const dates = this.next7Days()
        agg_day.forEach((value, index) => {
          result.push([dates[index], value['Assault'],value['Battery'],value['Burglary']])
        })
        console.log(result)
        return result
      },
      chartOptions() {
        return { 
         title: 'Number of predicted crimes per day for '+ this.district.name, subtitle: 'Number of crimes each day' ,
         height: 330
        }
      },
    },
    methods:{
      formatDate(date) {
        let dd = date.getDate();
        let mm = date.getMonth() + 1;
        const yy = date.getFullYear().toString().substr(-2);
        // pull the last two digits of the year
        if (dd < 10) { dd = `0${dd}` }
        if (mm < 10) { mm = `0${mm}` }
        date = `${mm}/${dd}/${yy}`;
        return date
      },
      next7Days() {
        const result = []
        for (let i = 1; i < 8; i++) {
          const d = new Date(this.date);
          d.setDate(d.getDate() + i);
          result.push(this.formatDate(d))
        }
        return result
      }
    }
  }
</script>

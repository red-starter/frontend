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
        type="ColumnChart"
        :data="aggChartData"
        :options="aggChartOptions"
      />
      <GChart
        type="LineChart"
        :data="chartData"
        :options="chartOptions"
      />
      <GChart
        type="ColumnChart"
        :data="aggChartDataHour"
        :options="aggChartOptionsHour"
      />
      <GChart
        type="LineChart"
        :data="chartDataHour"
        :options="chartOptionsHour"
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
        const result = [['Date','Assault','Battery','Burglary',"Robbery", "Sex offense", "Stalking", "Weapons violation",]]
        const dates = this.next7Days()
        agg_day.forEach((value, index) => {
          result.push([dates[index], value['Assault'],value['Battery'],value['Burglary'], value["Robbery"], value["Sex offense"], value["Stalking"], value["Weapons violation"],
          ])
        })
        return result
      },
      chartOptions() {
        return { 
         title: 'Number of predicted crimes per type for each day in '+ this.district.name + ' district', subtitle: 'Number of crimes each day' ,
         height: 430
        }
      },
      aggChartData(){
        const agg_day = JSON.parse(this.data.grouped_day)
        const result = [['Date','total']]
        const dates = this.next7Days()
        agg_day.forEach((value, index) => {
          const sum = value['Assault']+ value['Battery']+ value['Burglary']+  value["Robbery"]+  value["Sex offense"]+  value["Stalking"]+  value["Weapons violation"]
          result.push([dates[index], sum])
        })
        return result
      },
      aggChartOptions() {
        return { 
         title: 'Number of all predicted crimes per day in '+ this.district.name + ' district', subtitle: 'Total Number of crimes each day' ,
         height: 430
        }
      },
      aggChartDataHour(){
        let agg_day = JSON.parse(this.data.grouped_hour)
        agg_day = agg_day.slice(0,25)
        const result = [['Date','total']]
        const dates = this.next24hours()
        agg_day.forEach((value, index) => {
          const sum = value['Assault']+ value['Battery']+ value['Burglary']+  value["Robbery"]+  value["Sex offense"]+  value["Stalking"]+  value["Weapons violation"]
          result.push([dates[index], sum])
        })
        return result
      },
      aggChartOptionsHour() {
        return { 
         title: 'Number of all predicted crimes per hour in '+ this.district.name + ' district', subtitle: 'Total Number of crimes each hour' ,
         height: 430
        }
      },
      chartDataHour(){
        let agg_day = JSON.parse(this.data.grouped_hour)
        agg_day = agg_day.slice(0,25)
        const result = [['Date','Assault','Battery','Burglary',"Robbery", "Sex offense", "Stalking", "Weapons violation",]]
        const dates = this.next24hours()
        agg_day.forEach((value, index) => {
          result.push([dates[index], value['Assault'],value['Battery'],value['Burglary'], value["Robbery"], value["Sex offense"], value["Stalking"], value["Weapons violation"],
          ])
        })
        return result
      },
      chartOptionsHour() {
        return { 
         title: 'Number of predicted crimes per type for each hour in '+ this.district.name + ' district', subtitle: 'Number of crimes each hour' ,
         height: 430
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
      formatHourDate(d) {
        var amOrPm = (d.getHours() < 12) ? "AM" : "PM";
        var hour = (d.getHours() < 12) ? d.getHours() : d.getHours() - 12;
        return   d.getDate() + ' / ' + d.getMonth() + ' / ' + ' ' + hour + amOrPm;
      },
      next24hours() {
        const result = []
        for (let i = 1  ; i <= 25; i++) {
          const hours = this.time.split(':')[0]
          const d = new Date(this.date);
          d.setHours(d.getHours() + hours);
          d.setHours(d.getHours() + i);
          result.push(this.formatHourDate(d))
        }
        return result
      },
      next7Days() {
        const result = []
        for (let i = 1  ; i < 9; i++) {
          const d = new Date(this.date);
          d.setDate(d.getDate() + i);
          result.push(this.formatDate(d))
        }
        return result
      }
    }
  }
</script>

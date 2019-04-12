<template>
  <div>
    <h1>
      <img alt="knife logo" height="100px" src="../assets/knife.svg">
        <h4>Predicted crimes for {{district.number}} {{district.name}} District </h4>
        <h4>on date: {{date}} at time: {{time}}</h4>
      <img alt="knife logo" height="100px" src="../assets/cleaver-knife.svg">
    </h1>
    <v-container>
    <v-data-table
      :headers="headers"
      :items="data"
      class="elevation-1"
    >
      <template v-slot:items="props">
        <td>{{ props.item.name }}</td>
        <td>{{ props.item.number }}</td>
      </template>
    </v-data-table>
    </v-container>
    <router-link to="/">Home</router-link>
  </div>
</template>

<script>
  export default {
    name: "Results",
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
    }
  }
</script>

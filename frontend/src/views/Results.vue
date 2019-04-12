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
      :items="crimes"
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
    props: ['time','date','district'],
    data () {
      return {
        headers: [
          {
            text: 'Type of crimes',
            align: 'center',
            sortable: false,
            value: 'name'
          },
          {
            text: 'Number of predicted crimes',
            align: 'center',
            sortable: true,
            value: 'number'
          },

        ],
        crimes: [{name: 'Theft', number: 1},
        {name: 'Battery', number: 1},
        {name: 'Criminal damage', number: 1},
        {name: 'Assault', number: 1},
        {name: 'Deceptive practice', number: 1},
        {name: 'Other offense', number: 1},
        {name: 'Narcotics', number: 1},
        {name: 'Burglary', number: 1},
        {name: 'Motor vehicle theft', number: 1},
        {name: 'Robbery', number: 1},
        {name: 'Criminal trespass', number: 1},
        {name: 'Weapons violation', number: 1},
        {name: 'Offense involving children', number: 1},
        {name: 'Crim sexual assault', number: 1},
        {name: 'Public peace violation', number: 1},
        {name: 'Interference with public officer', number: 1},
        {name: 'Sex offense', number: 1},
        {name: 'Prostitution', number: 1},
        {name: 'Homicide', number: 1},
        {name: 'Arson', number: 1},
        {name: 'Liquor law violation', number: 1},
        {name: 'Stalking', number: 1},
        {name: 'Gambling', number: 1},
        {name: 'Kidnapping', number: 1},
        {name: 'Intimidation', number: 1},
        {name: 'Concealed carry license violation', number: 1},
        {name: 'Obscenity', number: 1},
        {name: 'Non-criminal', number: 1},
        {name: 'Human trafficking', number: 1},
        {name: 'Public indecency', number: 1},
        {name: 'Other narcotic violation', number: 1},]
      }
    }
  }
</script>

<template>
  <div class="hello">
    
    <h1>
      <img alt="knife logo" height="100px" src="../assets/knife.svg">
      <span>Murder Not</span>
      <img alt="knife logo" height="100px" src="../assets/cleaver-knife.svg">
    </h1>
    
    <p>
      Your personal guide to avoid crime in dangerous cities<br>
      <!-- this will be link to github -->
      <!-- <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>. -->
    </p>
    <h2>Description</h2>
      <v-container>
      <div>I applied machine learning techniques to explore crime in Chicago. Chicago is a leading cities in homicides, having more than quadruple the amount of crimes than NYC. Can I get insight into what are the causes of crimes? What are the indicators of future crimes. One of the great thing about this project is that the data is constantly updated and well structured.</div>
      </v-container>
    <h2>Data Source</h2>
      <a href="https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2" target="_blank">The data come for crimes in chicago 2001 - 2018 </a>
    <h2>Supported Cities</h2>
    <ul>
      <li> <router-link to="/chicago">Chicago</router-link></li>
      <div>more coming soon ... </div> 
      <!-- <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank" rel="noopener">eslint</a></li> -->
    </ul>
    <h2> <img alt="octo cat logo" height="50px" src="../assets/GitHub_Logo.png"><img alt="octo cat logo" height="50px" src="../assets/Octocat.png"></h2>
    <ul>
      <li><a href="https://github.com/red-starter/frontend" target="_blank" rel="noopener">Front end repo</a></li>
      <li><a href="https://github.com/red-starter/capstone2" target="_blank" rel="noopener">Data sciencing repo</a></li>
    </ul>
    <h2>Libraries used</h2>
    <ul>
      <li><a href="https://pandas.pydata.org/" target="_blank" rel="noopener"> <img alt="knife logo" height="50px" src="../assets/pandas.png"></a></li>
      <li><a href="https://scikit-learn.org/stable/" target="_blank" rel="noopener"> <img alt="knife logo" height="50px" src="../assets/sklearn.svg"></a></li>
      <li><a href="http://flask.pocoo.org/" target="_blank" rel="noopener"> <img alt="knife logo" height="50px" src="../assets/flask.svg"></a></li>
      <li><a href="https://vuejs.org" target="_blank" rel="noopener"><img alt="knife logo" height="50px" src="../assets/logo.svg"></a></li>
      <li><a href="https://matplotlib.org/" target="_blank" rel="noopener"><img alt="knife logo" height="50px" src="../assets/matplotlib.png"></a></li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'HelloWorld',
  props: {
    // msg: String
  },
    data() {
      return {
        msg: '',
      };
    },
    methods: {
      getMessage() {
        const path = 'http://localhost:5000/ping';
        axios.get(path)
          .then((res) => {
            this.msg = res.data;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      },
    },
    created() {
      this.getMessage();
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h2 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

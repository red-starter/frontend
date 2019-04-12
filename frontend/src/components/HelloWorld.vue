<template>
  <div class="hello">
    
    <h1>
      <img alt="knife logo" height="100px" src="../assets/knife.svg">
      <span>Murder Not</span>
      <img alt="knife logo" height="100px" src="../assets/cleaver-knife.svg">
    </h1>
    
    <p>
      Your personal guide to traveling dangerous cities<br>
      <!-- this will be link to github -->
      <!-- <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>. -->
    </p>
    <h1>Supported Cities</h1>
    <ul>
      <li> <router-link to="/chicago">Chicago</router-link></li>
      <div>more coming soon ... </div> 
      <!-- <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank" rel="noopener">eslint</a></li> -->
    </ul>
    <h1> <img alt="octo cat logo" height="50px" src="../assets/GitHub_Logo.png"><img alt="octo cat logo" height="50px" src="../assets/Octocat.png"></h1>
    <ul>
      <li><a href="https://github.com/red-starter/frontend" target="_blank" rel="noopener">Front end repo</a></li>
      <li><a href="https://github.com/red-starter/capstone2" target="_blank" rel="noopener">Data sciencing repo</a></li>
    </ul>
    <h1>Libraries used</h1>
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
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
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

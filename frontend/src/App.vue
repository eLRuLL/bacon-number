<template>
  <div id="app">
    <ActorPath />
  </div>
</template>

<script>
import ActorPath from './components/ActorPath.vue'

export default {
  name: 'App',
  components: {
    ActorPath
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

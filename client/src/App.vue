<template lang="html">
  <v-app>
    <Header/>
    <Navbar/>
    <v-content>
      <router-view></router-view>
    </v-content>
    <Footer/>
  </v-app>
</template>

<script>
 import Header from './components/Header';
 import Navbar from './components/Navbar';
 import Footer from './components/Footer';

export default {
  name: 'App',
  components: {
    Header,
    Navbar,
    Footer
  }
};
</script>

<style media="screen"></style>

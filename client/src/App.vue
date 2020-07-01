<template lang="html">
  <v-app>
    <Header/>
    <Navbar/>
    <!-- <v-container id="header">
      <v-layout wrap row>
        <v-flex xs3>
        </v-flex>
        <v-flex id="header__title" xs6>
          <h1>시종사</h1>
        </v-flex>
        <v-flex id="header__menu" xs3>
          <a href="#"><small>로그인</small></a>
          |
          <a href="#"><small>장바구니</small></a>
          |
          <a href="#"><small>마이페이지</small></a>
          |
          <a href="#"><small>공지사항</small></a>
        </v-flex>
      </v-layout>
    </v-container>
    <v-toolbar app dark height="100px" floating>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat>반지</v-btn>
        <v-btn flat>목걸이</v-btn>
        <v-btn flat>팔찌</v-btn>
        <v-btn flat>귀걸이</v-btn>
        <v-btn flat>시계</v-btn>
      </v-toolbar-items>
    </v-toolbar> -->
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

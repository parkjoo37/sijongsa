<template lang="html">
  <v-container id="header">
    <v-layout wrap row>
      <v-flex xs3>
      </v-flex>
      <v-flex id="header__title" xs6>
        <h1><a href="/">시종사</a></h1>
      </v-flex>
      <v-flex id="header__menu" xs3>
        <a :href="item.path" v-for="item in items" :key="item">{{ item.title }}</a>
        <!-- <a href="#"><small>로그인</small></a>
        |
        <a href="#"><small>장바구니</small></a>
        |
        <a href="#"><small>마이페이지</small></a>
        |
        <a href="#"><small>공지사항</small></a> -->
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { title: '로그인', path: '/login' },
        { title: '장바구니', path: '/shopping-basket' },
        { title: '마이페이지', path: '/mypage' },
        { title: '공지사항', path: '/notice' }
      ]
    };
  }
}
</script>

<style lang="css" src="../assets/css/header.css" scoped>
</style>

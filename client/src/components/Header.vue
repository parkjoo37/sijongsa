<template lang="html">
  <v-container id="header">
    <v-layout wrap row>
      <v-flex lg3 xs3>
      </v-flex>
      <v-flex id="header__title" lg6 xs6>
        <h1><a href="/">SiJong.</a></h1>
      </v-flex>
      <v-flex id="header__menu" lg3 xs3>
        <!-- <a id="menu__bar"><i class="fas fa-bars"></i></a> -->
        <ul id="header__nav">
          <!-- <a :href="item.path" v-for="item in items" :key="item">{{ item.title }}</a> -->
          <li v-if="isLogin"><a @click="logout()"><small>로그아웃</small></a></li>
          <li v-else><a href="/login"><small>로그인</small></a></li>
          |
          <li><a href="#"><small>장바구니</small></a></li>
          |
          <li><a href="#"><small>마이페이지</small></a></li>
          |
          <li><a href="#"><small>공지사항</small></a></li>
        </ul>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  // data() {
  //   return {
  //     items: [
  //       { title: '로그인', path: '/login' },
  //       { title: '장바구니', path: '/shopping-basket' },
  //       { title: '마이페이지', path: '/mypage' },
  //       { title: '공지사항', path: '/notice' }
  //     ]
  //   };
  // }
  data() {
    return {
      // isLogin: this.$store.state.isLogin
    }
  },
  computed: {
    ...mapState(['isLogin', 'isLoginError'])
  },
  methods: {
    ...mapActions(['logout'])
  }
};
</script>

<style lang="css" src="../assets/css/header.css" scoped>
</style>

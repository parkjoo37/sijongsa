<template lang="html">
  <v-layout wrap row id="navbar">
    <v-flex id="navbar__menu" xs12>
      <a href="/ring">반지</a>
      |
      <a href="/necklace">목걸이</a>
      |
      <a href="/bracelet">팔찌</a>
      |
      <a href="/earring">귀걸이</a>
      |
      <a href="/clock">시계</a>
      <!-- <a :href="item.path" v-for="item in items" :key="item">
        {{ item.title }}
      </a> -->
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  // data() {
  //   return {
  //     items: [
  //       { title: '반지', path: '/ring' },
  //       { title: '목걸이', path: '/necklace' },
  //       { title: '팔찌', path: '/bracelet' },
  //       { title: '귀걸이', path: '/earring' },
  //       { title: '시계', path: '/clock' }
  //     ]
  //   };
  // }
}
</script>

<style lang="css" src="../assets/css/navbar.css" scoped>
</style>

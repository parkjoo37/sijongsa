<template lang="html">
  <v-container id="login">
    <v-layout row wrap justify-center>
        <h1 id="red__title">전상품 무료배송</h1>
    </v-layout>
    <v-layout row wrap justify-center>
      <h1 style="font-weight: lighter;">예쁜 상품 GET하러 로그인</h1>
    </v-layout>
    <v-layout row wrap justify-center id="input__info">
      <v-flex xs6>
        <v-text-field v-model="email" :rules="[rules.required, rules.email]" label="Email"></v-text-field>
        <v-text-field v-model="password" :rules="[rules.required]" label="password" counter max="15"></v-text-field>
        <v-btn id="login__btn" block>로그인</v-btn>
        <v-btn id="signup__btn" block>회원가입</v-btn>
        <div id="find__id__password">
          <a href="#" id="find__id">아이디 찾기</a>
          |
          <a href="#" id="find__password">비밀번호 찾기</a>
        </div>
        <div id="sns__login">
          <h4>간편로그인 / 가입</h4>
          <v-layout id="sns__btn" row wrap>
            <v-flex xs6>
              <v-btn id="facebook__btn" large>
                <i class="fab fa-facebook-square"></i>
                <strong>Facebook</strong>으로 계속하기
              </v-btn>
            </v-flex>
            <v-flex xs6>
              <v-btn id="google__btn" large>
                <i class="fab fa-google"></i>
                <strong>Google</strong> 계정으로 계속하기
              </v-btn>
            </v-flex>
          </v-layout>
          <v-btn id="kakao__btn" large>
            <i class="fab fa-kickstarter"></i>
            <strong>Kakao</strong> 계정으로 계속하기
          </v-btn>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
      rules: {
        required: (value) => !!value || '입력해주세요.',
        email: (value) => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(value) || '이메일을 입력해주세요.'
        }
      }
    }
  }
}
</script>

<style lang="css" src="../assets/css/login.css" scoped>
</style>

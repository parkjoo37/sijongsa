<template lang="html">
  <v-container id="signup">
    <v-layout row wrap justify-center>
      <h1 id="signup__title">회원가입</h1>
    </v-layout>
    <v-stepper v-model="e1" id="signup__stepper">
      <v-stepper-header>
        <v-stepper-step :complete="e1 > 1" step="1" color="black">본인인증</v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step :complete="e1 > 2" step="2" color="black">정보수집동의</v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step :complete="e1 > 3" step="3" color="black">정보입력</v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step step="4" color="black">가입완료</v-stepper-step>
      </v-stepper-header>
      <v-stepper-items>
        <v-stepper-content step="1">
          <v-layout column wrap align-center id="signup__verification">
            <h4>시종사 본인 인증</h4>
            <br><br>
            <v-img src="../assets/phone.png" width="75" height="120" max-width="75" max-height="120"></v-img>
            <br>
            <small>* 14세 미만 회원은 가입이 불가합니다.</small>
            <small>* 법인폰 사용자는 휴대폰 인증이 불가합니다.</small>
          </v-layout>
          <v-layout row wrap justify-center>
            <v-flex xs4></v-flex>
            <v-flex xs4 id="phone__verification">
              <v-btn dark @click.native="e1 = 2" large block>휴대폰 인증</v-btn>
            </v-flex>
            <v-flex xs4></v-flex>
          </v-layout>
        </v-stepper-content>
        <v-stepper-content step="2">
          <v-btn color="black" @click.native="e1 = 3">다음</v-btn>
        </v-stepper-content>
        <v-stepper-content step="3">
          <v-btn color="black" @click.native="e1 = 4">가입하기</v-btn>
        </v-stepper-content>
        <v-stepper-content step="4">
          <v-btn color="black" @click.native="e1 = 1">처음으로</v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      e1: 1
    }
  }
}
</script>

<style lang="css" src="../assets/css/signup.css" scoped>
</style>

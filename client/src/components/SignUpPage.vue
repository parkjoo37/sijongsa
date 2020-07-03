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
          <v-layout row wrap id="signup__agree">
            <v-flex xs3></v-flex>
            <v-flex xs6>
              <strong><v-checkbox v-model="agree1" label="시종사 약관 동의 (필수)" color="black" value="termx"></v-checkbox></strong>
              <v-card height="250px" width= "580px" max-height="250px" max-width="580px">
                <v-card-text>
                  <pre>
서비스 이용약관

본 서비스 이용약관(이하 “본 약관”)은 ㈜브랜디(이하 “회사”)가 제공하는
서비스 이용에 대한 조건을 정하고 있으며, 서비스 이용자와 회사 간의 계약을 구성
합니다.
회사의 서비스를 이용하고자 하는 자는 서비스를 등록 및 사용함에 있어서 본 약관에
따라 본 약관, 서비스 약관, 이용정책 등에 구속되며 본 약관을 준수할 것에
동의합니다.

제1장 총칙
                  </pre>
                </v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
          <v-layout row wrap id="signup__personal__information">
            <v-flex xs3></v-flex>
            <v-flex xs6>
              <strong><v-checkbox v-model="agree2" label="개인정보수집 및 이용에 대한 안내 (필수)" color="black" value="termx"></v-checkbox></strong>
              <v-card height="250px" width= "580px" max-height="250px" max-width="580px">
                <v-card-text>
                  <pre>
서비스 이용약관

본 서비스 이용약관(이하 “본 약관”)은 ㈜브랜디(이하 “회사”)가 제공하는
서비스 이용에 대한 조건을 정하고 있으며, 서비스 이용자와 회사 간의 계약을 구성
합니다.
회사의 서비스를 이용하고자 하는 자는 서비스를 등록 및 사용함에 있어서 본 약관에
따라 본 약관, 서비스 약관, 이용정책 등에 구속되며 본 약관을 준수할 것에
동의합니다.

제1장 총칙
                  </pre>
                </v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
          <v-layout row wrap justify-center>
            <v-flex xs4></v-flex>
            <v-flex xs4 id="agree__next__btn">
              <v-btn dark @click.native="e1 = 3" large block>다음</v-btn>
            </v-flex>
            <v-flex xs4></v-flex>
          </v-layout>
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

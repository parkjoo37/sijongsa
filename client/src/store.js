import Vue from "vue";
import Vuex from "vuex";
import router from './router';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userInfo: null,
    isLogin: false,
    isLoginError: false
  },
  mutations: {
    loginSuccess(state, payload) {
      state.isLogin = true;
      state.isLoginError = false;
      state.userInfo = payload;
    },
    loginError(state) {
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    },
    logout(state) {
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    }
  },
  actions: {
    login(dispatch, loginObj) {
      axios.post('http://127.0.0.1:8000/rest-auth/login/', loginObj)
        .then(res => {
          let token = res.data.token;
          localStorage.setItem('access_token', token);
          this.dispatch('getMemberInfo');
          router.push({name: 'home'})
          console.log(res.data.token);
        })
        .catch(() => {
          alert('이메일과 비밀번호를 확인하세요.');
        });
    },
    logout({commit}) {
      commit('logout');
      router.push({name: 'home'});
    },
    signup(dispatch, signupObj) {
      axios.post('http://127.0.0.1:8000/rest-auth/registration/', signupObj)
        .then(res => {
          alert('회원가입이 성공적으로 이뤄졌습니다.');
          router.push({name: 'login'});
          console.log(res);
        })
        .catch(() => {
          alert('이메일과 비밀번호를 확인하세요.');
        });
    },
    getMemberInfo({commit}) {
      let token = localStorage.getItem('access_token');
      let config = {
        // headers: {
        //   'access-token': token,
        // }
        headers: {
          'Authorization': 'JWT ' + token,
        }
      };
      axios.get('http://127.0.0.1:8000/rest-auth/user/', config)
        .then(response => {
          let userInfo = {
            url: response.data.data.url,
            email: response.data.data.email,
            username: response.data.data.username,
            age: response.data.data.age,
            gender: response.data.data.gender,
            address: response.data.data.address
          };
          commit('loginSuccess', userInfo);
        })
        .catch(() => {
          // alert('dd이메일과 비밀번호를 확인하세요.');
        });
    }
  },
  getters: {}
});

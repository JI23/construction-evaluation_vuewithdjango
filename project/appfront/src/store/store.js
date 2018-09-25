import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    // 设置属性
    currentUser: null,
    isLogin: false
  },
  getters: {
    // 获取属性的状态
    currentUser: state => state.currentUser,
    isLogin: state => state.isLogin
  },
  mutations: {
    // 更改用户的状态信息
    userStatus(state, user) {
      if (user) {
        state.currentUser = user
        state.isLogin = true
      } else {
        state.currentUser = null
        state.isLogin = false
      }
    }
  },
  actions: {
    // 应用mutations
    setUser({
      commit
    }, user) {
      commit("userStatus", user)
    }
  }
})
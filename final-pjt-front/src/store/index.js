import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    detailnum: 0,
    updateReview: null,
    user: null,
    movieList: [],
    searchResult: [],
    movieKey: "",
    notitle: 0,
    URL: "http://127.0.0.1:8000/movies/",
    token: localStorage.getItem("jwt"),
  },
  getters: {
    config: function (state) {
      return {
        Authorization: `JWT ${state.token}`,
      };
    },
    searchResults: function (state) {
      return state.searchResult;
    },
  },

  mutations: {
    TODETAIL: function (state, movie) {
      state.detailnum = movie;
    },
    LOGIN: function (state) {
      state.token = localStorage.getItem("jwt");
    },
    LOGOUT: function (state) {
      state.token = null;
    },
    LOAD_MOVIE_LIST: function (state, results) {
      state.movieList = results;
    },
    SEARCH_MOVIE: function (state, results) {
      state.searchResult = results;
    },
    GET_ID: function (state, data) {
      state.movieKey = data.id;
    },
    TOUPDATEREVIEW: function (state, data) {
      state.updateReview = data;
    },
    NOTITLE: function (state) {
      state.notitle = 1;
    },
    YESTITLE: function (state) {
      state.notitle = 0;
    },
  },
  actions: {
    toDetail: function ({ commit }, movie) {
      commit("TODETAIL", movie);
    },
    login: function ({ commit }) {
      commit("LOGIN");
    },
    logout: function ({ commit }) {
      commit("LOGOUT");
    },
    LoadMovieList: function ({ commit, getters }) {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/movies/",
        headers: getters.config,
      }).then((res) => {
        commit("LOAD_MOVIE_LIST", res.data);
      });
    },
    searchMovie: function (context, data) {
      context.commit("SEARCH_MOVIE", data);
    },
    GetId: function (context, data) {
      context.commit("GET_ID", data);
    },
    toUpdateReview: function ({ commit }, data) {
      commit("TOUPDATEREVIEW", data);
    },
    noTitle: function ({ commit }) {
      commit("NOTITLE");
    },
    yesTitle: function ({ commit }) {
      commit("YESTITLE");
    },
  },
});

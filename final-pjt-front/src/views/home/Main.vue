<template>
  <b-container>
    <!-- 서치바 -->
    <movie-searchbar @search-movie="searchMovie"> </movie-searchbar>
    <!-- 영화목록 -->
    <div class="d-flex flex-row flex-wrap justify-content-left">
      <movie-list
        class="py-3 px-2"
        v-for="movieCard in movieList"
        :key="movieCard.id"
        :movie="movieCard"
      >
      </movie-list>
    </div>
  </b-container>
</template>

<script>
import axios from "axios";
import MovieList from "@/components/MovieList.vue";
import MovieSearchbar from "@/components/MovieSearchbar.vue";
import { mapState } from "vuex";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Main",
  components: {
    MovieList,
    MovieSearchbar,
  },
  data: function () {
    return {
      movies: [],
      result: [],
    };
  },
  methods: {
    searchMovie: function (inputdata) {
      axios
        .get(`${SERVER_URL}/movies/find/${inputdata}`)
        .then((res) => {
          this.movies = res.data;
          this.$store.dispatch("searchMovie", this.movies);
          this.$router.push({ name: "MovieSearchResult" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created: function () {
    this.$store.dispatch("LoadMovieList");
  },
  computed: {
    ...mapState(["movieList"]),
  },
};
</script>

<style></style>

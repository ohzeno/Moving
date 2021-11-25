<template>
  <b-container>
    <div>
      <br />
      <h1 class="fs-2 text-start py-2">What's Popular</h1>
      <!-- 장르 클릭하면 해당 장르 영화 랜덤으로 가져옴 -->
      <div class="flex-container">
        <h2 v-for="genre in genres" :key="genre.id" class="p-1">
          <b-button
            @click="getRecommend_bygenre(genre.id)"
            class="p-2"
            variant="secondary"
          >
            {{ genre.name }}
          </b-button>
        </h2>
      </div>

      <br />
      <div class="d-flex flex-wrap justify-content-left">
        <div v-for="movie in movies" :key="movie.id" class="py-3 px-2">
          <div style="width: 305px; height: 550px">
            <div class="px-2 py-2 fs-3 con" style="height: 100px">
              <div v-if="movie.title.length > 24" class="overflow">
                {{ movie.title }}
              </div>
              <div v-else>
                {{ movie.title }}
              </div>
            </div>
            <div>
              <img
                :src="`https://image.tmdb.org/t/p/w300${movie.poster_path}`"
                @click="moveToDetail(movie)"
                alt="test"
                style="width: 300; height: 450px; object-fit: contain"
                class="scale"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </b-container>
</template>

<script>
import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Recommend",
  data: function () {
    return {
      movies: [],
      genres: [],
    };
  },
  methods: {
    getRecommended: function () {
      axios({
        method: "get",
        url: `${SERVER_URL}/movies/recommend/`,
        headers: this.$store.getters.config,
      })
        .then((res) => {
          this.movies = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    moveToDetail: function (data) {
      this.$store.dispatch("GetId", data);
      this.$router.push({ name: "MovieDetail" });
    },
    getGenres: function () {
      axios({
        method: "get",
        url: `${SERVER_URL}/movies/genres/`,
        headers: this.$store.getters.config,
      })
        .then((res) => {
          this.genres = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getRecommend_bygenre: function (genre_id) {
      axios({
        method: "get",
        url: `${SERVER_URL}/movies/recommend/genre/${genre_id}`,
        headers: this.$store.getters.config,
      })
        .then((res) => {
          this.movies = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created: function () {
    if (this.$store.state.token) {
      this.getRecommended();
      this.getGenres();
      // 로그인하지 않은 유저는 로그인페이지로
    } else {
      this.$router.push({ name: "Login" });
    }
  },
};
</script>

<style scoped>
.flex-container {
  display: flex;
  flex-wrap: wrap;
}
.con {
  display: flex;
  justify-content: center;
  align-items: center;
}
.overflow {
  height: 85px;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  align-items: center;
}
.scale {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.3s ease-in-out;
}
.scale:hover {
  transform: scale(1.1);
  -webkit-transform: scale(1.1);
  -moz-transform: scale(1.1);
  -ms-transform: scale(1.1);
  -o-transform: scale(1.1);
}
.img {
  overflow: hidden;
}
</style>
